# PROMPT 5: Task Validation System — "Har jag gjort rätt?"

## KONTEXT

Användare behöver kunna verifiera att de gjort en uppgift korrekt.
Utan validering vet de inte om de lärt sig rätt eller gjort fel.

## UPPDRAG

Implementera ett valideringssystem för tasks.

## VALIDERING TYPER

### Typ 1: Self-Check (Enkel)
Användaren markerar själv att de klarat uppgiften.
Visar förväntade resultat så de kan jämföra.

### Typ 2: Quiz Validation
Automatiska frågor som testar förståelse.
3-5 frågor per task.

### Typ 3: Command Validation (Avancerad)
Användaren kör kommandon och klistrar in output.
Systemet verifierar mot förväntade mönster.

## IMPLEMENTATION

### Backend Schema

```python
# apps/backend/src/schemas/validation.py

from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import UUID

class ValidationType(str, Enum):
    SELF_CHECK = "self_check"
    QUIZ = "quiz"
    COMMAND = "command"

class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct_index: int
    explanation: str

class CommandCheck(BaseModel):
    id: str
    description: str
    command: str
    expected_patterns: List[str]  # Regex patterns to match
    error_hints: dict[str, str]   # Pattern -> hint mapping

class ValidationConfig(BaseModel):
    type: ValidationType
    
    # For SELF_CHECK
    expected_results: Optional[List[str]] = None
    
    # For QUIZ
    questions: Optional[List[QuizQuestion]] = None
    passing_score: Optional[int] = 80  # Percentage
    
    # For COMMAND
    checks: Optional[List[CommandCheck]] = None

class ValidationSubmission(BaseModel):
    task_id: UUID
    
    # For QUIZ
    answers: Optional[dict[str, int]] = None  # question_id -> selected_index
    
    # For COMMAND
    outputs: Optional[dict[str, str]] = None  # check_id -> user output

class ValidationResult(BaseModel):
    task_id: UUID
    passed: bool
    score: Optional[int] = None
    
    # Detailed feedback
    feedback: List[dict]  # [{question_id, correct, explanation}]
    
    # For failed command checks
    hints: Optional[List[str]] = None
```

### Task Schema Update

```python
# Update apps/backend/src/schemas/task.py

class TaskContent(BaseModel):
    # ... existing fields ...
    
    # NEW: Validation configuration
    validation: Optional[ValidationConfig] = None
```

### Backend Routes

```python
# apps/backend/src/api/routes/validation.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import re

from src.core.deps import get_current_user, get_db
from src.schemas.validation import (
    ValidationSubmission, 
    ValidationResult,
    ValidationType
)
from src.db.models.task import Task
from src.db.models.progress import Progress

router = APIRouter(prefix="/api/validation", tags=["validation"])

@router.get("/task/{task_id}")
async def get_task_validation(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Get validation config for a task"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    content = task.content or {}
    validation = content.get("validation")
    
    if not validation:
        return {"type": "self_check", "expected_results": []}
    
    # Don't expose correct answers for quiz
    if validation.get("type") == "quiz":
        questions = validation.get("questions", [])
        safe_questions = [
            {
                "id": q["id"],
                "question": q["question"],
                "options": q["options"]
                # Exclude correct_index and explanation
            }
            for q in questions
        ]
        return {
            "type": "quiz",
            "questions": safe_questions,
            "passing_score": validation.get("passing_score", 80)
        }
    
    return validation

@router.post("/submit", response_model=ValidationResult)
async def submit_validation(
    submission: ValidationSubmission,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """Submit validation for a task"""
    task = db.query(Task).filter(Task.id == submission.task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    content = task.content or {}
    validation = content.get("validation", {})
    val_type = validation.get("type", "self_check")
    
    if val_type == "self_check":
        # Self-check always passes
        return ValidationResult(
            task_id=submission.task_id,
            passed=True,
            feedback=[{"message": "Self-check completed"}]
        )
    
    elif val_type == "quiz":
        return _validate_quiz(submission, validation)
    
    elif val_type == "command":
        return _validate_commands(submission, validation)
    
    raise HTTPException(status_code=400, detail="Unknown validation type")


def _validate_quiz(submission: ValidationSubmission, validation: dict) -> ValidationResult:
    """Validate quiz answers"""
    questions = validation.get("questions", [])
    answers = submission.answers or {}
    
    correct_count = 0
    feedback = []
    
    for q in questions:
        q_id = q["id"]
        user_answer = answers.get(q_id)
        is_correct = user_answer == q["correct_index"]
        
        if is_correct:
            correct_count += 1
        
        feedback.append({
            "question_id": q_id,
            "correct": is_correct,
            "correct_answer": q["correct_index"],
            "user_answer": user_answer,
            "explanation": q["explanation"]
        })
    
    score = int((correct_count / len(questions)) * 100) if questions else 0
    passing_score = validation.get("passing_score", 80)
    
    return ValidationResult(
        task_id=submission.task_id,
        passed=score >= passing_score,
        score=score,
        feedback=feedback
    )


def _validate_commands(submission: ValidationSubmission, validation: dict) -> ValidationResult:
    """Validate command outputs"""
    checks = validation.get("checks", [])
    outputs = submission.outputs or {}
    
    all_passed = True
    feedback = []
    hints = []
    
    for check in checks:
        check_id = check["id"]
        user_output = outputs.get(check_id, "")
        patterns = check.get("expected_patterns", [])
        error_hints = check.get("error_hints", {})
        
        # Check if any pattern matches
        matched = any(
            re.search(pattern, user_output, re.IGNORECASE | re.MULTILINE)
            for pattern in patterns
        )
        
        if not matched:
            all_passed = False
            # Find relevant hint
            for pattern, hint in error_hints.items():
                if re.search(pattern, user_output, re.IGNORECASE):
                    hints.append(hint)
                    break
            else:
                hints.append(f"Output för '{check['description']}' matchar inte förväntat resultat")
        
        feedback.append({
            "check_id": check_id,
            "description": check["description"],
            "passed": matched
        })
    
    return ValidationResult(
        task_id=submission.task_id,
        passed=all_passed,
        feedback=feedback,
        hints=hints if not all_passed else None
    )
```

### Frontend Components

#### `apps/frontend/src/components/validation/SelfCheckValidation.tsx`

```tsx
'use client';

import { CheckCircle, Circle } from 'lucide-react';
import { useState } from 'react';

interface SelfCheckValidationProps {
  expectedResults: string[];
  onComplete: () => void;
}

export function SelfCheckValidation({ expectedResults, onComplete }: SelfCheckValidationProps) {
  const [checked, setChecked] = useState<boolean[]>(
    new Array(expectedResults.length).fill(false)
  );
  
  const allChecked = checked.every(Boolean);

  const toggleCheck = (index: number) => {
    const newChecked = [...checked];
    newChecked[index] = !newChecked[index];
    setChecked(newChecked);
  };

  return (
    <div className="bg-gray-800/50 rounded-lg p-6 mt-8">
      <h3 className="text-lg font-semibold text-white mb-4">
        ✅ Verifiera att det fungerar
      </h3>
      
      <p className="text-gray-400 text-sm mb-4">
        Kryssa i varje punkt när du verifierat att det fungerar:
      </p>
      
      <ul className="space-y-3">
        {expectedResults.map((result, index) => (
          <li key={index}>
            <button
              onClick={() => toggleCheck(index)}
              className="flex items-start gap-3 text-left w-full group"
            >
              {checked[index] ? (
                <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
              ) : (
                <Circle className="w-5 h-5 text-gray-500 mt-0.5 flex-shrink-0 group-hover:text-gray-400" />
              )}
              <span className={`text-sm ${checked[index] ? 'text-green-400' : 'text-gray-300'}`}>
                {result}
              </span>
            </button>
          </li>
        ))}
      </ul>
      
      {allChecked && (
        <button
          onClick={onComplete}
          className="mt-6 w-full bg-green-600 hover:bg-green-700 text-white py-2 px-4 rounded-lg font-medium transition-colors"
        >
          Markera som klar ✓
        </button>
      )}
    </div>
  );
}
```

#### `apps/frontend/src/components/validation/QuizValidation.tsx`

```tsx
'use client';

import { useState } from 'react';
import { CheckCircle, XCircle, HelpCircle } from 'lucide-react';
import { api } from '@/lib/api';

interface Question {
  id: string;
  question: string;
  options: string[];
}

interface QuizValidationProps {
  taskId: string;
  questions: Question[];
  passingScore: number;
  onComplete: (passed: boolean) => void;
}

export function QuizValidation({ taskId, questions, passingScore, onComplete }: QuizValidationProps) {
  const [answers, setAnswers] = useState<Record<string, number>>({});
  const [result, setResult] = useState<any>(null);
  const [submitting, setSubmitting] = useState(false);

  const allAnswered = Object.keys(answers).length === questions.length;

  const handleSubmit = async () => {
    setSubmitting(true);
    try {
      const response = await api.post('/api/validation/submit', {
        task_id: taskId,
        answers
      });
      setResult(response.data);
      onComplete(response.data.passed);
    } catch (error) {
      console.error('Validation failed:', error);
    } finally {
      setSubmitting(false);
    }
  };

  if (result) {
    return (
      <div className="bg-gray-800/50 rounded-lg p-6 mt-8">
        <div className={`flex items-center gap-3 mb-4 ${result.passed ? 'text-green-400' : 'text-red-400'}`}>
          {result.passed ? (
            <CheckCircle className="w-6 h-6" />
          ) : (
            <XCircle className="w-6 h-6" />
          )}
          <h3 className="text-lg font-semibold">
            {result.passed ? 'Godkänt!' : 'Inte godkänt'} — {result.score}%
          </h3>
        </div>
        
        <div className="space-y-4">
          {result.feedback.map((fb: any, index: number) => (
            <div key={fb.question_id} className={`p-4 rounded-lg ${fb.correct ? 'bg-green-900/30' : 'bg-red-900/30'}`}>
              <p className="font-medium text-white mb-2">
                {questions[index].question}
              </p>
              <p className="text-sm text-gray-400">
                {fb.explanation}
              </p>
            </div>
          ))}
        </div>
        
        {!result.passed && (
          <button
            onClick={() => {
              setResult(null);
              setAnswers({});
            }}
            className="mt-4 text-blue-400 hover:text-blue-300 text-sm"
          >
            Försök igen
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="bg-gray-800/50 rounded-lg p-6 mt-8">
      <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
        <HelpCircle className="w-5 h-5" />
        Testa din förståelse
      </h3>
      
      <p className="text-gray-400 text-sm mb-6">
        Svara på frågorna nedan för att verifiera att du förstått koncepten.
        Du behöver {passingScore}% rätt för att bli godkänd.
      </p>
      
      <div className="space-y-6">
        {questions.map((q, qIndex) => (
          <div key={q.id} className="border-b border-gray-700 pb-6 last:border-0">
            <p className="font-medium text-white mb-3">
              {qIndex + 1}. {q.question}
            </p>
            <div className="space-y-2">
              {q.options.map((option, oIndex) => (
                <button
                  key={oIndex}
                  onClick={() => setAnswers(prev => ({ ...prev, [q.id]: oIndex }))}
                  className={`w-full text-left p-3 rounded-lg border transition-colors ${
                    answers[q.id] === oIndex
                      ? 'border-blue-500 bg-blue-900/30 text-white'
                      : 'border-gray-700 hover:border-gray-600 text-gray-300'
                  }`}
                >
                  {option}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>
      
      <button
        onClick={handleSubmit}
        disabled={!allAnswered || submitting}
        className="mt-6 w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 disabled:cursor-not-allowed text-white py-2 px-4 rounded-lg font-medium transition-colors"
      >
        {submitting ? 'Kontrollerar...' : 'Kontrollera svar'}
      </button>
    </div>
  );
}
```

#### `apps/frontend/src/components/validation/CommandValidation.tsx`

```tsx
'use client';

import { useState } from 'react';
import { Terminal, CheckCircle, XCircle } from 'lucide-react';
import { api } from '@/lib/api';

interface CommandCheck {
  id: string;
  description: string;
  command: string;
}

interface CommandValidationProps {
  taskId: string;
  checks: CommandCheck[];
  onComplete: (passed: boolean) => void;
}

export function CommandValidation({ taskId, checks, onComplete }: CommandValidationProps) {
  const [outputs, setOutputs] = useState<Record<string, string>>({});
  const [result, setResult] = useState<any>(null);
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = async () => {
    setSubmitting(true);
    try {
      const response = await api.post('/api/validation/submit', {
        task_id: taskId,
        outputs
      });
      setResult(response.data);
      onComplete(response.data.passed);
    } catch (error) {
      console.error('Validation failed:', error);
    } finally {
      setSubmitting(false);
    }
  };

  if (result) {
    return (
      <div className="bg-gray-800/50 rounded-lg p-6 mt-8">
        <div className={`flex items-center gap-3 mb-4 ${result.passed ? 'text-green-400' : 'text-red-400'}`}>
          {result.passed ? <CheckCircle className="w-6 h-6" /> : <XCircle className="w-6 h-6" />}
          <h3 className="text-lg font-semibold">
            {result.passed ? 'Alla kontroller godkända!' : 'Några kontroller misslyckades'}
          </h3>
        </div>
        
        {result.hints && result.hints.length > 0 && (
          <div className="bg-yellow-900/30 border border-yellow-700 rounded-lg p-4 mb-4">
            <h4 className="font-medium text-yellow-400 mb-2">Tips:</h4>
            <ul className="list-disc list-inside text-sm text-yellow-200 space-y-1">
              {result.hints.map((hint: string, i: number) => (
                <li key={i}>{hint}</li>
              ))}
            </ul>
          </div>
        )}
        
        {!result.passed && (
          <button
            onClick={() => setResult(null)}
            className="text-blue-400 hover:text-blue-300 text-sm"
          >
            Försök igen
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="bg-gray-800/50 rounded-lg p-6 mt-8">
      <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
        <Terminal className="w-5 h-5" />
        Verifiera med kommandon
      </h3>
      
      <p className="text-gray-400 text-sm mb-6">
        Kör kommandona nedan och klistra in resultatet för att verifiera att du gjort rätt.
      </p>
      
      <div className="space-y-6">
        {checks.map((check) => (
          <div key={check.id}>
            <label className="block text-sm font-medium text-gray-300 mb-2">
              {check.description}
            </label>
            <div className="bg-gray-900 rounded-lg p-3 mb-2 font-mono text-sm text-green-400">
              $ {check.command}
            </div>
            <textarea
              value={outputs[check.id] || ''}
              onChange={(e) => setOutputs(prev => ({ ...prev, [check.id]: e.target.value }))}
              placeholder="Klistra in output här..."
              className="w-full h-24 bg-gray-900 border border-gray-700 rounded-lg p-3 text-sm font-mono text-gray-300 placeholder-gray-600 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            />
          </div>
        ))}
      </div>
      
      <button
        onClick={handleSubmit}
        disabled={submitting || Object.keys(outputs).length !== checks.length}
        className="mt-6 w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 disabled:cursor-not-allowed text-white py-2 px-4 rounded-lg font-medium transition-colors"
      >
        {submitting ? 'Kontrollerar...' : 'Verifiera'}
      </button>
    </div>
  );
}
```

### Exempel: Task Content med Validation

```json
{
  "title": "Create personal dotfiles repository",
  "content": {
    "intro": "...",
    "steps": [...],
    
    "validation": {
      "type": "quiz",
      "passing_score": 80,
      "questions": [
        {
          "id": "q1",
          "question": "Varför använder vi symboliska länkar (symlinks) för dotfiles?",
          "options": [
            "För att spara diskutrymme",
            "För att ändringar i repot automatiskt påverkar konfigurationen",
            "För att filer ska vara dolda",
            "För att Git ska fungera"
          ],
          "correct_index": 1,
          "explanation": "Symboliska länkar gör att ~/.zshrc pekar på ~/dotfiles/shell/zshrc. När du ändrar filen i repot påverkar det direkt din konfiguration utan att du behöver kopiera filer."
        },
        {
          "id": "q2",
          "question": "Vad gör kommandot 'ln -sf'?",
          "options": [
            "Listar filer",
            "Skapar en symbolisk länk och tvingar överskrivning",
            "Tar bort en fil",
            "Kopierar en fil"
          ],
          "correct_index": 1,
          "explanation": "-s skapar en symbolisk länk (inte hard link), -f tvingar överskrivning om länken redan finns."
        }
      ]
    }
  }
}
```

## SUCCESS CRITERIA

- [ ] Validation API endpoints fungerar
- [ ] Self-check visas för enkla tasks
- [ ] Quiz fungerar med poängsystem
- [ ] Command validation matchar patterns
- [ ] Feedback visas tydligt
- [ ] Task markeras som klar vid godkänd validering

## COMMIT MESSAGE

```
feat(validation): add task validation system

Backend:
- Added ValidationConfig schema
- Created /api/validation endpoints
- Implemented quiz and command validation logic

Frontend:
- Created SelfCheckValidation component
- Created QuizValidation component
- Created CommandValidation component
- Integrated validation into task detail page

Validation types:
- self_check: Manual checklist verification
- quiz: Multiple choice questions with scoring
- command: Output pattern matching

Closes #XXX
```

## INTEGRATION

Efter validering är implementerad, uppdatera varje task i content rewrite (PROMPT_3) med lämplig validation-config.
