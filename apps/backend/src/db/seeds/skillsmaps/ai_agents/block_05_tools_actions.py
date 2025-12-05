"""
AI Agents SkillsMap - Block 05: Tools & Actions
Nodes 9-10: Advanced Tool Design, Action Patterns
"""

BLOCK_05_NODES = [
    {
        "id": "ai-agents-09",
        "slug": "advanced-tool-design",
        "title": "Advanced Tool Design Patterns",
        "order_index": 9,
        "estimated_minutes": 45,
        "xp_reward": 120,
        "difficulty": "hard",
        "node_type": "practice",
        "prerequisites": ["ai-agents-08"],
        "content": """# Advanced Tool Design Patterns

## Varför detta är viktigt

Verktyg är agentens händer — de bestämmer vad agenten faktiskt kan göra i världen.
Dåligt designade verktyg leder till:

- **Felaktiga anrop** — LLM missförstår vad verktyget gör
- **Säkerhetshål** — Verktyg utan validering är farliga
- **Dålig UX** — Användare ser konstiga fel
- **Höga kostnader** — Verktyg som returnerar för mycket data

De bästa agenterna har noggrant designade, välvaliderade verktyg med tydliga
kontrakt. Denna modul lär dig hur proffsen bygger dem.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Designa verktyg med optimala scheman för LLM-användning
- ✅ Implementera robust validering och felhantering
- ✅ Bygga komposita verktyg från enklare byggstenar
- ✅ Hantera async och long-running operations
- ✅ Implementera tool approval för farliga operationer

## Kärnkoncept

### Tool Design Principles

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      TOOL DESIGN PRINCIPLES                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. SINGLE RESPONSIBILITY                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  BAD:  general_action(type, target, params)                          │   │
│  │  GOOD: search_products(query)                                        │   │
│  │        get_product_details(product_id)                               │   │
│  │        update_product_price(product_id, new_price)                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  LLM förstår specifika verktyg bättre än generiska                         │
│                                                                              │
│  2. DESCRIPTIVE NAMING                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  BAD:  do_thing, process, handle                                     │   │
│  │  GOOD: search_customer_orders, calculate_shipping_cost               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  Namen ska avslöja vad verktyget gör utan att läsa description             │
│                                                                              │
│  3. SAFE BY DEFAULT                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Read-only operations ska inte kunna mutera                        │   │
│  │  • Destructive actions kräver bekräftelse                           │   │
│  │  • Validera ALL input                                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  4. PREDICTABLE OUTPUT                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Konsistent format (alltid JSON, alltid samma struktur)           │   │
│  │  • Explicit success/error status                                    │   │
│  │  • Begränsad output-storlek                                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  5. IDEMPOTENT WHEN POSSIBLE                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  • Samma anrop ska ge samma resultat                                │   │
│  │  • Undvik side effects i read-operations                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Tool Schema Best Practices

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    SCHEMA BEST PRACTICES                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PARAMETER DESCRIPTIONS - Be Specific!                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  BAD:  "query": {"description": "The search query"}                  │  │
│  │                                                                      │  │
│  │  GOOD: "query": {                                                    │  │
│  │           "description": "Search term for products. Use specific    │  │
│  │                          product names or categories. Max 100 chars. │  │
│  │                          Examples: 'iPhone 15', 'wireless headphones'│  │
│  │         }                                                            │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  USE ENUMS FOR LIMITED OPTIONS                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "category": {                                                       │  │
│  │    "type": "string",                                                 │  │
│  │    "enum": ["electronics", "clothing", "home", "sports"],            │  │
│  │    "description": "Product category to filter by"                    │  │
│  │  }                                                                   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  PROVIDE DEFAULTS                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "limit": {                                                          │  │
│  │    "type": "integer",                                                │  │
│  │    "default": 10,                                                    │  │
│  │    "minimum": 1,                                                     │  │
│  │    "maximum": 100,                                                   │  │
│  │    "description": "Max results to return (default: 10)"             │  │
│  │  }                                                                   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  USE NESTED OBJECTS FOR COMPLEX INPUTS                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  "filter": {                                                         │  │
│  │    "type": "object",                                                 │  │
│  │    "properties": {                                                   │  │
│  │      "min_price": {"type": "number"},                                │  │
│  │      "max_price": {"type": "number"},                                │  │
│  │      "in_stock": {"type": "boolean", "default": true}                │  │
│  │    }                                                                 │  │
│  │  }                                                                   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Production-Grade Tools

### 1. Robust Tool Base Class

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Optional, TypeVar, Generic
from enum import Enum
from pydantic import BaseModel, ValidationError
import time
import logging

logger = logging.getLogger(__name__)

class ToolRiskLevel(Enum):
    LOW = "low"           # Read-only
    MEDIUM = "medium"     # Creates data
    HIGH = "high"         # Modifies/deletes data
    CRITICAL = "critical" # System-level operations

@dataclass
class ToolResult:
    success: bool
    data: Any
    error: Optional[str] = None
    execution_time_ms: float = 0
    metadata: dict = field(default_factory=dict)

    def to_llm_string(self, max_length: int = 2000) -> str:
        \"\"\"Format result for LLM consumption.\"\"\"
        if self.success:
            data_str = str(self.data)
            if len(data_str) > max_length:
                data_str = data_str[:max_length] + "... [truncated]"
            return data_str
        else:
            return f"Error: {self.error}"

T = TypeVar('T', bound=BaseModel)

class ProductionTool(ABC, Generic[T]):
    \"\"\"Production-ready tool base class.\"\"\"

    # Subclasses must define these
    name: str
    description: str
    risk_level: ToolRiskLevel
    params_model: type[T]  # Pydantic model for validation

    def __init__(self):
        self._call_count = 0
        self._total_time_ms = 0
        self._error_count = 0

    @property
    def schema(self) -> dict:
        \"\"\"Generate OpenAI-compatible schema from Pydantic model.\"\"\"
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self._build_description(),
                "parameters": self.params_model.model_json_schema()
            }
        }

    def _build_description(self) -> str:
        \"\"\"Build comprehensive description.\"\"\"
        risk_warning = ""
        if self.risk_level in [ToolRiskLevel.HIGH, ToolRiskLevel.CRITICAL]:
            risk_warning = f"\\n⚠️ CAUTION: This is a {self.risk_level.value}-risk operation."

        return f\"{self.description}{risk_warning}\"

    def __call__(self, **kwargs) -> ToolResult:
        \"\"\"Execute tool with full validation and logging.\"\"\"
        start_time = time.perf_counter()
        self._call_count += 1

        try:
            # Validate input with Pydantic
            params = self.params_model(**kwargs)

            # Pre-execution hook (for approval, etc.)
            approval = self._pre_execute(params)
            if not approval.approved:
                return ToolResult(
                    success=False,
                    data=None,
                    error=f"Operation not approved: {approval.reason}"
                )

            # Execute
            result = self._execute(params)

            # Post-execution hook
            self._post_execute(params, result)

            execution_time = (time.perf_counter() - start_time) * 1000
            self._total_time_ms += execution_time

            result.execution_time_ms = execution_time
            return result

        except ValidationError as e:
            self._error_count += 1
            logger.error(f"Tool {self.name} validation error: {e}")
            return ToolResult(
                success=False,
                data=None,
                error=f"Invalid parameters: {e.errors()}"
            )
        except Exception as e:
            self._error_count += 1
            logger.exception(f"Tool {self.name} execution error")
            return ToolResult(
                success=False,
                data=None,
                error=str(e)
            )

    @abstractmethod
    def _execute(self, params: T) -> ToolResult:
        \"\"\"Implement actual tool logic.\"\"\"
        pass

    def _pre_execute(self, params: T) -> 'ApprovalResult':
        \"\"\"Hook for approval/validation before execution.\"\"\"
        return ApprovalResult(approved=True)

    def _post_execute(self, params: T, result: ToolResult) -> None:
        \"\"\"Hook for logging/cleanup after execution.\"\"\"
        logger.info(f"Tool {self.name} executed: success={result.success}")

    @property
    def stats(self) -> dict:
        \"\"\"Get tool usage statistics.\"\"\"
        return {
            "name": self.name,
            "call_count": self._call_count,
            "error_count": self._error_count,
            "avg_execution_ms": self._total_time_ms / max(self._call_count, 1),
            "error_rate": self._error_count / max(self._call_count, 1)
        }

@dataclass
class ApprovalResult:
    approved: bool
    reason: str = ""
```

### 2. Implementera konkret verktyg

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal

# Define parameter models with Pydantic
class SearchProductsParams(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Search term for products"
    )
    category: Optional[Literal["electronics", "clothing", "home", "sports"]] = Field(
        default=None,
        description="Filter by category"
    )
    min_price: Optional[float] = Field(default=None, ge=0)
    max_price: Optional[float] = Field(default=None, ge=0)
    limit: int = Field(default=10, ge=1, le=100)

    class Config:
        json_schema_extra = {
            "examples": [
                {"query": "wireless headphones", "category": "electronics", "limit": 5}
            ]
        }

class SearchProductsTool(ProductionTool[SearchProductsParams]):
    name = "search_products"
    description = \"\"\"
    Search the product catalog.

    Use this to find products matching a search term.
    Returns product name, price, and availability.

    Example queries:
    - "iPhone 15 Pro"
    - "running shoes size 42"
    - "4K monitor under 5000"
    \"\"\"
    risk_level = ToolRiskLevel.LOW
    params_model = SearchProductsParams

    def __init__(self, product_db):
        super().__init__()
        self.db = product_db

    def _execute(self, params: SearchProductsParams) -> ToolResult:
        # Build query
        filters = {}
        if params.category:
            filters["category"] = params.category
        if params.min_price is not None:
            filters["price_gte"] = params.min_price
        if params.max_price is not None:
            filters["price_lte"] = params.max_price

        # Execute search (mock)
        results = self.db.search(
            query=params.query,
            filters=filters,
            limit=params.limit
        )

        return ToolResult(
            success=True,
            data={
                "query": params.query,
                "count": len(results),
                "products": results
            },
            metadata={"filters_applied": filters}
        )


class DeleteProductParams(BaseModel):
    product_id: str = Field(..., description="ID of product to delete")
    reason: str = Field(..., min_length=10, description="Reason for deletion")
    confirm: bool = Field(..., description="Must be true to confirm deletion")

class DeleteProductTool(ProductionTool[DeleteProductParams]):
    name = "delete_product"
    description = \"\"\"
    Permanently delete a product from the catalog.

    ⚠️ This action cannot be undone!
    Requires confirmation and a reason.
    \"\"\"
    risk_level = ToolRiskLevel.HIGH
    params_model = DeleteProductParams

    def __init__(self, product_db, approval_callback=None):
        super().__init__()
        self.db = product_db
        self.approval_callback = approval_callback

    def _pre_execute(self, params: DeleteProductParams) -> ApprovalResult:
        # Check confirmation flag
        if not params.confirm:
            return ApprovalResult(
                approved=False,
                reason="Deletion not confirmed. Set confirm=true to proceed."
            )

        # External approval for high-risk operations
        if self.approval_callback:
            approved = self.approval_callback(
                f"Delete product {params.product_id}? Reason: {params.reason}"
            )
            if not approved:
                return ApprovalResult(
                    approved=False,
                    reason="User declined the operation"
                )

        return ApprovalResult(approved=True)

    def _execute(self, params: DeleteProductParams) -> ToolResult:
        deleted = self.db.delete(params.product_id)

        if deleted:
            return ToolResult(
                success=True,
                data={"deleted_id": params.product_id, "reason": params.reason}
            )
        else:
            return ToolResult(
                success=False,
                data=None,
                error=f"Product {params.product_id} not found"
            )
```

### 3. Composite Tools

```python
class CompositeToolResult(ToolResult):
    \"\"\"Result from a composite tool with sub-results.\"\"\"
    sub_results: list[ToolResult] = field(default_factory=list)

class CompositeTool(ProductionTool[T]):
    \"\"\"Tool that orchestrates multiple sub-tools.\"\"\"

    def __init__(self, sub_tools: list[ProductionTool]):
        super().__init__()
        self.sub_tools = {t.name: t for t in sub_tools}

    def _execute_sub_tool(self, tool_name: str, **kwargs) -> ToolResult:
        if tool_name not in self.sub_tools:
            return ToolResult(success=False, data=None, error=f"Unknown sub-tool: {tool_name}")
        return self.sub_tools[tool_name](**kwargs)


class ProductAnalysisParams(BaseModel):
    product_id: str
    include_reviews: bool = True
    include_competitors: bool = True

class ProductAnalysisTool(CompositeTool[ProductAnalysisParams]):
    \"\"\"Composite tool that analyzes a product comprehensively.\"\"\"

    name = "analyze_product"
    description = \"\"\"
    Get comprehensive analysis of a product.

    This combines:
    - Basic product details
    - Customer reviews summary
    - Competitor comparison

    Use when you need a full picture of a product.
    \"\"\"
    risk_level = ToolRiskLevel.LOW
    params_model = ProductAnalysisParams

    def _execute(self, params: ProductAnalysisParams) -> CompositeToolResult:
        sub_results = []

        # Get product details
        details = self._execute_sub_tool("get_product", product_id=params.product_id)
        sub_results.append(details)

        if not details.success:
            return CompositeToolResult(
                success=False,
                data=None,
                error=f"Could not find product: {params.product_id}",
                sub_results=sub_results
            )

        analysis = {"product": details.data}

        # Get reviews if requested
        if params.include_reviews:
            reviews = self._execute_sub_tool("get_reviews", product_id=params.product_id)
            sub_results.append(reviews)
            if reviews.success:
                analysis["reviews"] = reviews.data

        # Get competitors if requested
        if params.include_competitors:
            competitors = self._execute_sub_tool(
                "search_products",
                query=details.data.get("category", ""),
                limit=5
            )
            sub_results.append(competitors)
            if competitors.success:
                analysis["competitors"] = competitors.data

        return CompositeToolResult(
            success=True,
            data=analysis,
            sub_results=sub_results,
            metadata={"components_fetched": len(sub_results)}
        )
```

### 4. Async och Long-Running Tools

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

class AsyncToolResult(ToolResult):
    task_id: Optional[str] = None
    status: Literal["pending", "running", "completed", "failed"] = "completed"

class LongRunningTool(ProductionTool[T]):
    \"\"\"Base for tools that take time to complete.\"\"\"

    def __init__(self):
        super().__init__()
        self.executor = ThreadPoolExecutor(max_workers=4)
        self.tasks: dict[str, asyncio.Task] = {}

    async def execute_async(self, **kwargs) -> AsyncToolResult:
        \"\"\"Start async execution.\"\"\"
        task_id = f"{self.name}_{time.time_ns()}"

        # Validate params first
        try:
            params = self.params_model(**kwargs)
        except ValidationError as e:
            return AsyncToolResult(
                success=False,
                data=None,
                error=str(e),
                task_id=task_id,
                status="failed"
            )

        # Start background task
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(
            self.executor,
            lambda: self._execute(params)
        )

        self.tasks[task_id] = future

        return AsyncToolResult(
            success=True,
            data={"message": "Task started"},
            task_id=task_id,
            status="running"
        )

    async def check_status(self, task_id: str) -> AsyncToolResult:
        \"\"\"Check status of async task.\"\"\"
        if task_id not in self.tasks:
            return AsyncToolResult(
                success=False,
                data=None,
                error=f"Unknown task: {task_id}",
                task_id=task_id,
                status="failed"
            )

        future = self.tasks[task_id]

        if future.done():
            result = future.result()
            return AsyncToolResult(
                success=result.success,
                data=result.data,
                error=result.error,
                task_id=task_id,
                status="completed" if result.success else "failed"
            )
        else:
            return AsyncToolResult(
                success=True,
                data={"message": "Still processing"},
                task_id=task_id,
                status="running"
            )


class DataExportParams(BaseModel):
    format: Literal["csv", "json", "excel"]
    filters: Optional[dict] = None

class DataExportTool(LongRunningTool[DataExportParams]):
    \"\"\"Export large datasets (can take minutes).\"\"\"

    name = "export_data"
    description = \"\"\"
    Export data to a file. This is a long-running operation.

    Returns a task_id that can be used to check status.
    Use check_export_status with the task_id to see when it's done.
    \"\"\"
    risk_level = ToolRiskLevel.MEDIUM
    params_model = DataExportParams

    def _execute(self, params: DataExportParams) -> ToolResult:
        # Simulate long operation
        time.sleep(5)  # In reality: export logic here

        return ToolResult(
            success=True,
            data={
                "file_url": f"https://exports.example.com/{params.format}/export_123.{params.format}",
                "row_count": 10000,
                "file_size_mb": 25
            }
        )
```

## Vanliga problem

### Problem 1: "LLM anropar verktyg med fel format"

```python
# Lösning: Använd strict JSON schema validation
class StrictParams(BaseModel):
    class Config:
        extra = "forbid"  # Reject unknown fields
        str_strip_whitespace = True

# Och i tool schema:
def get_strict_schema(self) -> dict:
    schema = self.params_model.model_json_schema()
    schema["additionalProperties"] = False
    return schema
```

### Problem 2: "Verktyget returnerar för mycket data"

```python
class OutputLimiter:
    \"\"\"Limit tool output size.\"\"\"

    @staticmethod
    def truncate(data: Any, max_items: int = 10, max_str_len: int = 1000) -> Any:
        if isinstance(data, list):
            return data[:max_items]
        elif isinstance(data, str):
            return data[:max_str_len] + ("..." if len(data) > max_str_len else "")
        elif isinstance(data, dict):
            return {k: OutputLimiter.truncate(v, max_items, max_str_len)
                    for k, v in list(data.items())[:max_items]}
        return data

# I tool execute:
result = self._execute(params)
result.data = OutputLimiter.truncate(result.data)
```

## Praktisk övning

**Uppgift:** Bygg ett Tool Testing Framework

```python
class ToolTestFramework:
    \"\"\"
    TODO: Bygg ett framework för att testa tools.

    Funktioner:
    1. test_schema_validity(): Verifiera att schemat är korrekt
    2. test_with_examples(): Kör tool med example inputs
    3. test_edge_cases(): Testa gränsfall och felhantering
    4. test_performance(): Mät execution time
    5. generate_test_report(): Skapa rapport
    \"\"\"

    def __init__(self, tool: ProductionTool):
        self.tool = tool
        self.results = []

    def run_all_tests(self) -> dict:
        # Din kod här
        pass

# Användning
tool = SearchProductsTool(mock_db)
tester = ToolTestFramework(tool)
report = tester.run_all_tests()
print(report)
```

## Sammanfattning

- ✅ **Single responsibility** — ett verktyg gör en sak bra
- ✅ **Pydantic validation** garanterar korrekt input
- ✅ **Risk levels** kategoriserar verktyg för approval
- ✅ **Composite tools** kombinerar flera verktyg
- ✅ **Async patterns** hanterar long-running operations

## Nästa steg

- **Node 10:** Action Execution Patterns
- **Node 11:** Agent Frameworks — LangChain, CrewAI

---
*Pro tip: Test dina verktyg isolerat innan du integrerar med agenten!*
"""
    },
    {
        "id": "ai-agents-10",
        "slug": "action-execution-patterns",
        "title": "Action Execution Patterns",
        "order_index": 10,
        "estimated_minutes": 40,
        "xp_reward": 110,
        "difficulty": "medium",
        "node_type": "concept",
        "prerequisites": ["ai-agents-09"],
        "content": """# Action Execution Patterns

## Varför detta är viktigt

Hur agenten exekverar actions är minst lika viktigt som vilka actions den kan ta.
Dålig execution leder till:

- **Race conditions** när parallella actions kolliderar
- **Inkonsistent state** när actions misslyckas halvvägs
- **Dålig UX** när användare inte vet vad som händer
- **Säkerhetsproblem** när farliga actions körs utan kontroll

Denna modul handlar om patterns för säker, pålitlig och användarvänlig action execution.

## Vad du kommer lära dig

Efter denna modul kommer du kunna:
- ✅ Välja mellan sequential, parallel och conditional execution
- ✅ Implementera transaktionell execution med rollback
- ✅ Designa human-in-the-loop approval flows
- ✅ Hantera timeouts och retries gracefully
- ✅ Bygga execution pipelines med observability

## Kärnkoncept

### Execution Patterns Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    EXECUTION PATTERNS                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. SEQUENTIAL EXECUTION                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Action A ──► Action B ──► Action C ──► Done                        │   │
│  │                                                                      │   │
│  │  ✓ Simple to implement                                              │   │
│  │  ✓ Easy to debug                                                    │   │
│  │  ✗ Slow (waits for each action)                                     │   │
│  │                                                                      │   │
│  │  Use when: Actions depend on each other                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  2. PARALLEL EXECUTION                                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │       ┌─► Action A ──┐                                               │   │
│  │  Start├─► Action B ──┼─► Join ──► Done                              │   │
│  │       └─► Action C ──┘                                               │   │
│  │                                                                      │   │
│  │  ✓ Fast (parallel execution)                                        │   │
│  │  ✗ Complex error handling                                           │   │
│  │  ✗ Potential race conditions                                        │   │
│  │                                                                      │   │
│  │  Use when: Actions are independent                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  3. CONDITIONAL EXECUTION                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      ┌─► Action B                                    │   │
│  │  Action A ──► Check ─┼─► Action C                                    │   │
│  │                      └─► Action D                                    │   │
│  │                                                                      │   │
│  │  ✓ Adaptive behavior                                                │   │
│  │  ✗ More complex logic                                               │   │
│  │                                                                      │   │
│  │  Use when: Next action depends on result                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  4. TRANSACTIONAL EXECUTION                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Begin ──► A ──► B ──► C ──► Commit                                 │   │
│  │              │      │                                                │   │
│  │              └──────┴──► Rollback                                   │   │
│  │                                                                      │   │
│  │  ✓ All-or-nothing semantics                                         │   │
│  │  ✓ Consistent state                                                 │   │
│  │  ✗ More overhead                                                    │   │
│  │                                                                      │   │
│  │  Use when: Actions must succeed together                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Steg-för-steg: Implementera Execution Patterns

### 1. Sequential Executor

```python
from dataclasses import dataclass, field
from typing import Callable, Any, Optional
from enum import Enum
import time

class ExecutionStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass
class ActionResult:
    action_name: str
    status: ExecutionStatus
    result: Any = None
    error: Optional[str] = None
    duration_ms: float = 0

@dataclass
class ExecutionPlan:
    actions: list[tuple[str, Callable, dict]]  # (name, func, kwargs)
    results: list[ActionResult] = field(default_factory=list)
    status: ExecutionStatus = ExecutionStatus.PENDING

class SequentialExecutor:
    \"\"\"Execute actions one by one in sequence.\"\"\"

    def __init__(self, stop_on_error: bool = True):
        self.stop_on_error = stop_on_error

    def execute(self, plan: ExecutionPlan) -> ExecutionPlan:
        plan.status = ExecutionStatus.RUNNING

        for name, func, kwargs in plan.actions:
            start = time.perf_counter()

            try:
                result = func(**kwargs)
                duration = (time.perf_counter() - start) * 1000

                plan.results.append(ActionResult(
                    action_name=name,
                    status=ExecutionStatus.COMPLETED,
                    result=result,
                    duration_ms=duration
                ))

            except Exception as e:
                duration = (time.perf_counter() - start) * 1000

                plan.results.append(ActionResult(
                    action_name=name,
                    status=ExecutionStatus.FAILED,
                    error=str(e),
                    duration_ms=duration
                ))

                if self.stop_on_error:
                    plan.status = ExecutionStatus.FAILED
                    return plan

        plan.status = ExecutionStatus.COMPLETED
        return plan

# Usage
def get_user(user_id: str) -> dict:
    return {"id": user_id, "name": "Test User"}

def get_orders(user_id: str) -> list:
    return [{"order_id": "123", "total": 99.99}]

executor = SequentialExecutor()
plan = ExecutionPlan(actions=[
    ("get_user", get_user, {"user_id": "123"}),
    ("get_orders", get_orders, {"user_id": "123"}),
])
result = executor.execute(plan)
```

### 2. Parallel Executor

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed

class ParallelExecutor:
    \"\"\"Execute independent actions in parallel.\"\"\"

    def __init__(self, max_workers: int = 5, timeout: float = 30.0):
        self.max_workers = max_workers
        self.timeout = timeout

    def execute(self, plan: ExecutionPlan) -> ExecutionPlan:
        plan.status = ExecutionStatus.RUNNING

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all actions
            future_to_action = {
                executor.submit(self._execute_action, name, func, kwargs): name
                for name, func, kwargs in plan.actions
            }

            # Collect results
            for future in as_completed(future_to_action, timeout=self.timeout):
                action_name = future_to_action[future]
                try:
                    result = future.result()
                    plan.results.append(result)
                except Exception as e:
                    plan.results.append(ActionResult(
                        action_name=action_name,
                        status=ExecutionStatus.FAILED,
                        error=str(e)
                    ))

        # Set overall status
        if any(r.status == ExecutionStatus.FAILED for r in plan.results):
            plan.status = ExecutionStatus.FAILED
        else:
            plan.status = ExecutionStatus.COMPLETED

        return plan

    def _execute_action(self, name: str, func: Callable, kwargs: dict) -> ActionResult:
        start = time.perf_counter()
        try:
            result = func(**kwargs)
            return ActionResult(
                action_name=name,
                status=ExecutionStatus.COMPLETED,
                result=result,
                duration_ms=(time.perf_counter() - start) * 1000
            )
        except Exception as e:
            return ActionResult(
                action_name=name,
                status=ExecutionStatus.FAILED,
                error=str(e),
                duration_ms=(time.perf_counter() - start) * 1000
            )

# Usage - Independent actions run in parallel
parallel = ParallelExecutor(max_workers=3)
plan = ExecutionPlan(actions=[
    ("fetch_weather", fetch_weather, {"city": "Stockholm"}),
    ("fetch_news", fetch_news, {"topic": "tech"}),
    ("fetch_stocks", fetch_stocks, {"symbols": ["AAPL"]}),
])
result = parallel.execute(plan)
```

### 3. Transactional Executor with Rollback

```python
@dataclass
class RollbackAction:
    name: str
    func: Callable
    kwargs: dict

class TransactionalExecutor:
    \"\"\"Execute actions with rollback capability.\"\"\"

    def __init__(self):
        self.rollback_stack: list[RollbackAction] = []

    def execute(self, plan: ExecutionPlan) -> ExecutionPlan:
        plan.status = ExecutionStatus.RUNNING
        self.rollback_stack = []

        for name, func, kwargs in plan.actions:
            start = time.perf_counter()

            try:
                # Execute action
                result = func(**kwargs)
                duration = (time.perf_counter() - start) * 1000

                # Register rollback if available
                if hasattr(func, 'rollback'):
                    self.rollback_stack.append(RollbackAction(
                        name=f"rollback_{name}",
                        func=func.rollback,
                        kwargs={**kwargs, "result": result}
                    ))

                plan.results.append(ActionResult(
                    action_name=name,
                    status=ExecutionStatus.COMPLETED,
                    result=result,
                    duration_ms=duration
                ))

            except Exception as e:
                # Rollback all previous actions
                print(f"❌ Action {name} failed. Rolling back...")
                self._rollback()

                plan.results.append(ActionResult(
                    action_name=name,
                    status=ExecutionStatus.FAILED,
                    error=str(e),
                    duration_ms=(time.perf_counter() - start) * 1000
                ))
                plan.status = ExecutionStatus.FAILED
                return plan

        plan.status = ExecutionStatus.COMPLETED
        return plan

    def _rollback(self) -> None:
        \"\"\"Execute rollback actions in reverse order.\"\"\"
        while self.rollback_stack:
            rollback = self.rollback_stack.pop()
            try:
                print(f"  ↩️ Rolling back: {rollback.name}")
                rollback.func(**rollback.kwargs)
            except Exception as e:
                print(f"  ⚠️ Rollback failed: {e}")

# Example with rollback-enabled actions
def create_order(user_id: str, items: list) -> dict:
    order = {"id": "ord_123", "user_id": user_id, "items": items}
    # Save to database...
    return order

def create_order_rollback(user_id: str, items: list, result: dict):
    # Delete the order
    print(f"Deleting order {result['id']}")

# Attach rollback function
create_order.rollback = create_order_rollback
```

### 4. Human-in-the-Loop Approval

```python
from typing import Protocol

class ApprovalHandler(Protocol):
    def request_approval(self, action_name: str, details: dict) -> bool:
        ...

class ConsoleApprovalHandler:
    \"\"\"Simple console-based approval.\"\"\"

    def request_approval(self, action_name: str, details: dict) -> bool:
        print(f"\\n⚠️ APPROVAL REQUIRED")
        print(f"Action: {action_name}")
        print(f"Details: {details}")
        response = input("Approve? (y/n): ").lower()
        return response == 'y'

class SlackApprovalHandler:
    \"\"\"Slack-based approval with timeout.\"\"\"

    def __init__(self, slack_client, channel: str, timeout: int = 300):
        self.client = slack_client
        self.channel = channel
        self.timeout = timeout

    def request_approval(self, action_name: str, details: dict) -> bool:
        # Send Slack message with buttons
        message = self.client.chat_postMessage(
            channel=self.channel,
            text=f"🔐 Approval needed: {action_name}",
            blocks=[
                {"type": "section", "text": {"type": "mrkdwn", "text": f"*Action:* {action_name}"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"*Details:* {details}"}},
                {"type": "actions", "elements": [
                    {"type": "button", "text": {"type": "plain_text", "text": "✅ Approve"}, "action_id": "approve"},
                    {"type": "button", "text": {"type": "plain_text", "text": "❌ Deny"}, "action_id": "deny"}
                ]}
            ]
        )

        # Wait for response (simplified - real implementation needs webhook)
        # return self._wait_for_response(message['ts'], self.timeout)
        return True

class ApprovalGatedExecutor:
    \"\"\"Executor that requires approval for certain actions.\"\"\"

    def __init__(
        self,
        approval_handler: ApprovalHandler,
        require_approval_for: set[str] = None
    ):
        self.approval_handler = approval_handler
        self.require_approval_for = require_approval_for or set()

    def execute(self, plan: ExecutionPlan) -> ExecutionPlan:
        for name, func, kwargs in plan.actions:
            # Check if approval required
            if name in self.require_approval_for:
                approved = self.approval_handler.request_approval(name, kwargs)

                if not approved:
                    plan.results.append(ActionResult(
                        action_name=name,
                        status=ExecutionStatus.CANCELLED,
                        error="User denied approval"
                    ))
                    plan.status = ExecutionStatus.CANCELLED
                    return plan

            # Execute action
            try:
                result = func(**kwargs)
                plan.results.append(ActionResult(
                    action_name=name,
                    status=ExecutionStatus.COMPLETED,
                    result=result
                ))
            except Exception as e:
                plan.results.append(ActionResult(
                    action_name=name,
                    status=ExecutionStatus.FAILED,
                    error=str(e)
                ))
                plan.status = ExecutionStatus.FAILED
                return plan

        plan.status = ExecutionStatus.COMPLETED
        return plan

# Usage
executor = ApprovalGatedExecutor(
    approval_handler=ConsoleApprovalHandler(),
    require_approval_for={"delete_user", "send_mass_email", "deploy_to_prod"}
)
```

### 5. Retry with Backoff

```python
import random

class RetryConfig:
    max_retries: int = 3
    initial_delay: float = 1.0
    max_delay: float = 30.0
    exponential_base: float = 2.0
    jitter: bool = True
    retryable_exceptions: tuple = (ConnectionError, TimeoutError)

class RetryingExecutor:
    \"\"\"Executor with automatic retry and exponential backoff.\"\"\"

    def __init__(self, config: RetryConfig = None):
        self.config = config or RetryConfig()

    def execute_with_retry(
        self,
        name: str,
        func: Callable,
        kwargs: dict
    ) -> ActionResult:
        last_exception = None

        for attempt in range(self.config.max_retries + 1):
            try:
                start = time.perf_counter()
                result = func(**kwargs)

                return ActionResult(
                    action_name=name,
                    status=ExecutionStatus.COMPLETED,
                    result=result,
                    duration_ms=(time.perf_counter() - start) * 1000
                )

            except self.config.retryable_exceptions as e:
                last_exception = e

                if attempt < self.config.max_retries:
                    delay = self._calculate_delay(attempt)
                    print(f"⏳ Retry {attempt + 1}/{self.config.max_retries} "
                          f"for {name} in {delay:.2f}s")
                    time.sleep(delay)

            except Exception as e:
                # Non-retryable exception
                return ActionResult(
                    action_name=name,
                    status=ExecutionStatus.FAILED,
                    error=str(e)
                )

        return ActionResult(
            action_name=name,
            status=ExecutionStatus.FAILED,
            error=f"Max retries exceeded: {last_exception}"
        )

    def _calculate_delay(self, attempt: int) -> float:
        delay = min(
            self.config.initial_delay * (self.config.exponential_base ** attempt),
            self.config.max_delay
        )

        if self.config.jitter:
            delay *= (0.5 + random.random())  # 50-150% of delay

        return delay
```

## Praktisk övning

**Uppgift:** Bygg en Execution Pipeline

```python
class ExecutionPipeline:
    \"\"\"
    TODO: Bygg en konfigurerbar execution pipeline.

    Features:
    1. Stöd för sequential, parallel, och mixed execution
    2. Konfigurerbar error handling (stop, continue, retry)
    3. Pre- och post-hooks för logging/metrics
    4. Human approval gates
    5. Timeout handling

    Exempel på användning:

    pipeline = ExecutionPipeline()
    pipeline.add_stage("fetch_data", [action1, action2], parallel=True)
    pipeline.add_stage("process", [action3], requires_approval=True)
    pipeline.add_stage("save", [action4, action5], sequential=True)
    result = pipeline.execute()
    \"\"\"

    def __init__(self):
        self.stages = []

    def add_stage(
        self,
        name: str,
        actions: list,
        parallel: bool = False,
        requires_approval: bool = False,
        timeout: float = None
    ):
        # Din kod här
        pass

    def execute(self) -> ExecutionPlan:
        # Din kod här
        pass

# Test
pipeline = ExecutionPipeline()
# Konfigurera och kör din pipeline
```

## Sammanfattning

- ✅ **Sequential** för beroende actions
- ✅ **Parallel** för oberoende actions (snabbare)
- ✅ **Transactional** med rollback för kritiska operationer
- ✅ **Human-in-the-loop** för farliga actions
- ✅ **Retry med backoff** för flaky operations

## Nästa steg

- **Node 11:** Agent Frameworks — LangChain, CrewAI
- **Node 12:** Memory Systems — Hur agenter minns

---
*Pro tip: Välj rätt execution pattern baserat på action dependencies och risk level!*
"""
    }
]
