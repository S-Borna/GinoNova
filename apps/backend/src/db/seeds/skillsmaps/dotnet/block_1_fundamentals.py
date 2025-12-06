"""
C# & .NET SkillsMap - Block 1: C# Fundamentals
Nodes 1-4: Introduction, Variables & Types, Control Flow, Methods
"""

from typing import Any

# ============================================================================
# NODE 1: C# INTRODUCTION & SETUP
# ============================================================================

DOTNET_NODE_1_INTRO = {
    "node_id": 1,
    "title": "C# Introduction & Setup",
    "slug": "csharp-introduction",
    "description": "Introduktion till C# och .NET-ekosystemet",
    "difficulty": "beginner",
    "estimated_minutes": 45,
    "xp_reward": 100,
    "topics_covered": [
        "dotnet cli", "visual studio", "vs code", "hello world",
        "project structure", "compilation", "runtime"
    ],
    "content": """
# C# Introduction & Setup

> *"C# combines the power of C++ with the simplicity of Visual Basic."*
> — Anders Hejlsberg, Creator of C#

---

## 🎯 Why This Matters

C# är ett av världens mest använda programmeringsspråk:

- **#5 på TIOBE Index** - Miljarder rader kod i produktion
- **Microsoft ecosystem** - Azure, Windows, Xbox, Unity
- **Moderna features** - Async/await, LINQ, pattern matching
- **Cross-platform** - Kör på Windows, macOS, Linux

---

## 🧠 .NET Ecosystem

```
┌─────────────────────────────────────────────────────────────────┐
│                      .NET ECOSYSTEM                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    YOUR C# CODE                           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                            ▼                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              ROSLYN COMPILER (C# → IL)                    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                            ▼                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                .NET RUNTIME (CLR)                         │   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐            │   │
│  │  │    JIT     │ │   GC       │ │  Security  │            │   │
│  │  │ Compiler   │ │ Collector  │ │  Manager   │            │   │
│  │  └────────────┘ └────────────┘ └────────────┘            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                            ▼                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                 OPERATING SYSTEM                          │   │
│  │          Windows  │  macOS  │  Linux                      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### .NET Versions

| Version | Status | Användning |
|---------|--------|------------|
| **.NET 8** | LTS (2024-2026) | ⭐ Rekommenderat |
| .NET 9 | Current (2024) | Senaste features |
| .NET Framework | Legacy | Endast Windows |

---

## 💻 Installation

### Windows

```powershell
# Ladda ner .NET SDK från https://dotnet.microsoft.com
# Eller via winget:
winget install Microsoft.DotNet.SDK.8
```

### macOS

```bash
# Via Homebrew
brew install dotnet-sdk

# Verifiera
dotnet --version
```

### Linux (Ubuntu/Debian)

```bash
# Lägg till Microsoft repository
wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

# Installera SDK
sudo apt update
sudo apt install dotnet-sdk-8.0
```

---

## 💻 Your First C# Program

### Skapa projekt

```bash
# Skapa nytt console-projekt
dotnet new console -n HelloWorld
cd HelloWorld

# Projektstruktur
HelloWorld/
├── HelloWorld.csproj    # Projektfil (dependencies, settings)
├── Program.cs           # Din kod
└── obj/                 # Byggfiler
```

### Program.cs (Modern Top-Level Statements)

```csharp
// Program.cs - Minimal syntax sedan .NET 6
Console.WriteLine("Hello, World!");

// Läsa input
Console.Write("What's your name? ");
string name = Console.ReadLine() ?? "Anonymous";
Console.WriteLine($"Hello, {name}!");

// Variabler
int age = 25;
double salary = 50000.50;
bool isStudent = true;

Console.WriteLine($"Age: {age}, Salary: {salary:C}, Student: {isStudent}");
```

### Kör programmet

```bash
dotnet run

# Output:
# Hello, World!
# What's your name? Alice
# Hello, Alice!
# Age: 25, Salary: $50,000.50, Student: True
```

---

## 💻 Classic vs Modern Syntax

```csharp
// CLASSIC SYNTAX (före .NET 6)
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}

// MODERN SYNTAX (.NET 6+)
// Implicit using directives + top-level statements
Console.WriteLine("Hello, World!");
```

> 💡 **Pro Tip:** Modern syntax kompileras till samma IL-kod,
> men är mycket mer läsbar för enklare program.

---

## 🛠️ VS Code Setup

### Extensions att installera

1. **C# Dev Kit** (Microsoft) - IntelliSense, debugging
2. **NuGet Package Manager** - Hantera dependencies
3. **.NET Install Tool** - Installera .NET versioner

### launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "program": "${workspaceFolder}/bin/Debug/net8.0/HelloWorld.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal"
        }
    ]
}
```

---

## ⚠️ Vanliga Problem

### Problem 1: "dotnet: command not found"

```bash
# Lägg till i ~/.bashrc eller ~/.zshrc
export PATH="$PATH:$HOME/.dotnet"
export DOTNET_ROOT="$HOME/.dotnet"

source ~/.bashrc
```

### Problem 2: SDK version mismatch

```bash
# Kolla installerade versioner
dotnet --list-sdks

# Skapa global.json för att låsa version
dotnet new globaljson --sdk-version 8.0.100
```

---

## 🎮 Hands-on: Calculator

Skapa en enkel kalkylator:

```csharp
Console.WriteLine("=== Simple Calculator ===");
Console.Write("Enter first number: ");
double num1 = double.Parse(Console.ReadLine() ?? "0");

Console.Write("Enter operator (+, -, *, /): ");
string op = Console.ReadLine() ?? "+";

Console.Write("Enter second number: ");
double num2 = double.Parse(Console.ReadLine() ?? "0");

double result = op switch
{
    "+" => num1 + num2,
    "-" => num1 - num2,
    "*" => num1 * num2,
    "/" => num2 != 0 ? num1 / num2 : double.NaN,
    _ => throw new InvalidOperationException($"Unknown operator: {op}")
};

Console.WriteLine($"Result: {num1} {op} {num2} = {result}");
```

---

## ✅ Sammanfattning

- **.NET 8** är LTS - använd det för nya projekt
- **Top-level statements** förenklar koden
- **dotnet CLI** för allt: `new`, `run`, `build`, `publish`
- **Cross-platform** - samma kod körs överallt
""",
}


# ============================================================================
# NODE 2: VARIABLES & DATA TYPES
# ============================================================================

DOTNET_NODE_2_TYPES = {
    "node_id": 2,
    "title": "Variables & Data Types",
    "slug": "csharp-variables-types",
    "description": "Variabler, datatyper och typ-systemet i C#",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "value types", "reference types", "nullable", "var", "const",
        "strings", "arrays", "type conversion"
    ],
    "content": """
# Variables & Data Types

> *"C# has a unified type system. All types ultimately derive from object."*

---

## 🎯 Why This Matters

Att förstå C#:s typsystem är fundamentalt:
- **Type safety** - fångar fel vid kompilering
- **Performance** - value types vs reference types
- **Nullability** - undvik NullReferenceException

---

## 🧠 Type System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    C# TYPE SYSTEM                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                        object                                    │
│                          │                                       │
│            ┌─────────────┴─────────────┐                        │
│            │                           │                         │
│      Value Types               Reference Types                   │
│            │                           │                         │
│  ┌─────────┼─────────┐      ┌─────────┼─────────┐              │
│  │         │         │      │         │         │               │
│ struct   enum    primitives class  interface  array             │
│  │                   │                │                          │
│  │    int, bool,    │        string, object,                    │
│  │    double, etc   │        custom classes                      │
│                                                                  │
│  ══════════════════════════════════════════════════════════     │
│  VALUE TYPES        │  REFERENCE TYPES                          │
│  - Stored on stack  │  - Stored on heap                         │
│  - Copied by value  │  - Copied by reference                    │
│  - Cannot be null*  │  - Can be null                            │
│  ══════════════════════════════════════════════════════════     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Primitive Types

```csharp
// INTEGERS
byte b = 255;           // 0 to 255 (8 bit)
short s = 32767;        // -32,768 to 32,767 (16 bit)
int i = 2147483647;     // -2.1B to 2.1B (32 bit) ⭐ Default
long l = 9223372036854775807L;  // 64 bit

// UNSIGNED
uint ui = 4294967295;   // 0 to 4.2B
ulong ul = 18446744073709551615UL;

// FLOATING POINT
float f = 3.14f;        // 7 digits precision
double d = 3.14159265;  // 15-16 digits ⭐ Default
decimal m = 79228162514264337593543950335M;  // 28-29 digits (pengar!)

// BOOLEAN
bool isActive = true;

// CHARACTER
char c = 'A';           // Unicode (16 bit)

// STRING (reference type men beter sig som value type)
string name = "Alice";
```

### Implicit vs Explicit Typing

```csharp
// Explicit typing
int count = 10;
string message = "Hello";

// Implicit typing med var (typ inferred vid compile-time)
var count = 10;          // Kompilern vet att det är int
var message = "Hello";   // Kompilern vet att det är string
var user = GetUser();    // Typ baserad på return type

// ❌ Fungerar inte
var something;           // Error: måste ha initializer
```

---

## 💻 Strings

```csharp
// String literals
string name = "Alice";
string path = "C:\\Users\\Alice";  // Escape sequences
string rawPath = @"C:\Users\Alice"; // Verbatim string

// String interpolation ($ prefix)
int age = 25;
string message = $"Name: {name}, Age: {age}";

// Multi-line strings
string json = """
    {
        "name": "Alice",
        "age": 25
    }
    """;  // Raw string literals (.NET 7+)

// String methods
string text = "  Hello World  ";
Console.WriteLine(text.Trim());           // "Hello World"
Console.WriteLine(text.ToUpper());        // "  HELLO WORLD  "
Console.WriteLine(text.Contains("World")); // true
Console.WriteLine(text.Replace("World", "C#")); // "  Hello C#  "
Console.WriteLine(text.Split(' '));       // ["", "", "Hello", "World", "", ""]

// StringBuilder för många concatenations
var sb = new StringBuilder();
for (int i = 0; i < 1000; i++)
{
    sb.Append($"Item {i}, ");
}
string result = sb.ToString();
```

---

## 💻 Arrays & Collections

```csharp
// Arrays - fixed size
int[] numbers = new int[5];           // [0, 0, 0, 0, 0]
int[] primes = { 2, 3, 5, 7, 11 };    // Initializer
int[] squares = new int[] { 1, 4, 9, 16, 25 };

// Access
Console.WriteLine(primes[0]);          // 2
Console.WriteLine(primes.Length);      // 5

// Multi-dimensional
int[,] matrix = new int[3, 3];
matrix[0, 0] = 1;

// Jagged arrays (array of arrays)
int[][] jagged = new int[3][];
jagged[0] = new int[] { 1, 2 };
jagged[1] = new int[] { 3, 4, 5 };

// List<T> - dynamic size
List<string> names = new List<string> { "Alice", "Bob" };
names.Add("Charlie");
names.Remove("Bob");
Console.WriteLine(names.Count);        // 2

// Dictionary<K, V>
Dictionary<string, int> ages = new()
{
    ["Alice"] = 25,
    ["Bob"] = 30
};
ages["Charlie"] = 35;

if (ages.TryGetValue("Alice", out int age))
{
    Console.WriteLine($"Alice is {age}");
}
```

---

## 💻 Nullable Types

```csharp
// Value types can't be null by default
int count = null;  // ❌ Error

// Nullable value types (?)
int? nullableCount = null;  // ✅ OK
nullableCount = 10;

// Check if has value
if (nullableCount.HasValue)
{
    Console.WriteLine(nullableCount.Value);
}

// Null coalescing operator (??)
int actualCount = nullableCount ?? 0;  // 10 (or 0 if null)

// Null conditional operator (?.)
string? name = null;
int? length = name?.Length;  // null (doesn't throw)

// Null-forgiving operator (!)
string definitelyNotNull = name!;  // Trust me compiler, it's not null
```

---

## 💻 Type Conversion

```csharp
// Implicit conversion (safe, no data loss)
int i = 100;
long l = i;           // int → long OK
double d = i;         // int → double OK

// Explicit conversion (cast - potential data loss)
double pi = 3.14159;
int rounded = (int)pi;  // 3 (truncated)

// Parse strings
string numberStr = "42";
int number = int.Parse(numberStr);  // Throws if invalid

// TryParse (safe)
if (int.TryParse("42", out int result))
{
    Console.WriteLine($"Parsed: {result}");
}

// Convert class
int fromString = Convert.ToInt32("42");
string fromInt = Convert.ToString(42);
```

---

## ⚠️ Vanliga Problem

### Problem 1: NullReferenceException

```csharp
// ❌ Dåligt
string name = GetName();
Console.WriteLine(name.Length);  // Kraschar om null

// ✅ Bättre
string? name = GetName();
Console.WriteLine(name?.Length ?? 0);
```

### Problem 2: String concatenation i loopar

```csharp
// ❌ Långsamt (skapar ny string varje gång)
string result = "";
for (int i = 0; i < 10000; i++)
    result += i.ToString();

// ✅ Snabbt
var sb = new StringBuilder();
for (int i = 0; i < 10000; i++)
    sb.Append(i);
string result = sb.ToString();
```

---

## ✅ Sammanfattning

- **Value types** på stack, kopieras by value
- **Reference types** på heap, kopieras by reference
- **var** för implicit typing (fortfarande statiskt typat)
- **Nullable** (`?`) för null-säkra value types
- **StringBuilder** för många string-operationer
""",
}


# ============================================================================
# NODE 3: CONTROL FLOW
# ============================================================================

DOTNET_NODE_3_CONTROL_FLOW = {
    "node_id": 3,
    "title": "Control Flow & Loops",
    "slug": "csharp-control-flow",
    "description": "if/else, switch, loops och pattern matching",
    "difficulty": "beginner",
    "estimated_minutes": 50,
    "xp_reward": 100,
    "topics_covered": [
        "if else", "switch", "pattern matching", "for", "foreach",
        "while", "break", "continue"
    ],
    "content": """
# Control Flow & Loops

> *"Pattern matching in C# has evolved into one of its most powerful features."*

---

## 🎯 Why This Matters

Kontrollflöde är hjärtat i all programmering:
- **Beslut** - if/else, switch
- **Iteration** - for, foreach, while
- **Pattern Matching** - modern C# super power

---

## 💻 If/Else

```csharp
int score = 85;

// Basic if/else
if (score >= 90)
{
    Console.WriteLine("A");
}
else if (score >= 80)
{
    Console.WriteLine("B");
}
else if (score >= 70)
{
    Console.WriteLine("C");
}
else
{
    Console.WriteLine("F");
}

// Ternary operator
string grade = score >= 60 ? "Pass" : "Fail";

// Null check pattern
string? name = GetName();
if (name is not null)
{
    Console.WriteLine(name.ToUpper());
}

// Combined conditions
if (score >= 80 && score < 90)
{
    Console.WriteLine("B grade");
}
```

---

## 💻 Switch (Classic & Modern)

```csharp
// CLASSIC SWITCH
int day = 3;
switch (day)
{
    case 1:
        Console.WriteLine("Monday");
        break;
    case 2:
        Console.WriteLine("Tuesday");
        break;
    case 3:
    case 4:
    case 5:
        Console.WriteLine("Midweek");
        break;
    default:
        Console.WriteLine("Weekend");
        break;
}

// MODERN SWITCH EXPRESSION (.NET 6+)
string dayName = day switch
{
    1 => "Monday",
    2 => "Tuesday",
    3 or 4 or 5 => "Midweek",
    6 or 7 => "Weekend",
    _ => "Invalid"
};

// With conditions (when guards)
string category = score switch
{
    >= 90 => "Excellent",
    >= 80 => "Good",
    >= 70 => "Average",
    >= 60 => "Pass",
    _ => "Fail"
};
```

---

## 💻 Pattern Matching

```csharp
// Type patterns
object obj = "Hello";

if (obj is string s)
{
    Console.WriteLine($"It's a string: {s.ToUpper()}");
}

// Property patterns
var person = new { Name = "Alice", Age = 25 };

if (person is { Age: >= 18 })
{
    Console.WriteLine("Adult");
}

// Switch with type patterns
string Describe(object obj) => obj switch
{
    int i when i > 0 => $"Positive number: {i}",
    int i when i < 0 => $"Negative number: {i}",
    int => "Zero",
    string s => $"String of length {s.Length}",
    null => "Null value",
    _ => "Unknown type"
};

// List patterns (.NET 7+)
int[] numbers = { 1, 2, 3 };

if (numbers is [1, 2, 3])
{
    Console.WriteLine("Exact match");
}

if (numbers is [1, .., 3])  // First 1, last 3
{
    Console.WriteLine("Starts with 1, ends with 3");
}

if (numbers is [var first, .. var rest])
{
    Console.WriteLine($"First: {first}, Rest count: {rest.Length}");
}
```

---

## 💻 Loops

```csharp
// FOR LOOP
for (int i = 0; i < 5; i++)
{
    Console.WriteLine($"Iteration {i}");
}

// FOREACH (preferred for collections)
string[] names = { "Alice", "Bob", "Charlie" };
foreach (string name in names)
{
    Console.WriteLine(name);
}

// With index
foreach (var (name, index) in names.Select((n, i) => (n, i)))
{
    Console.WriteLine($"{index}: {name}");
}

// WHILE
int count = 0;
while (count < 5)
{
    Console.WriteLine(count);
    count++;
}

// DO-WHILE (runs at least once)
do
{
    Console.WriteLine("Enter password:");
} while (Console.ReadLine() != "secret");

// BREAK & CONTINUE
for (int i = 0; i < 10; i++)
{
    if (i == 3) continue;  // Skip 3
    if (i == 7) break;     // Stop at 7
    Console.WriteLine(i);  // 0, 1, 2, 4, 5, 6
}
```

---

## 💻 LINQ (Preview)

```csharp
int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

// Filter
var evens = numbers.Where(n => n % 2 == 0);

// Transform
var squares = numbers.Select(n => n * n);

// Aggregate
int sum = numbers.Sum();
int max = numbers.Max();
double avg = numbers.Average();

// Chain operations
var result = numbers
    .Where(n => n > 3)
    .Select(n => n * 2)
    .OrderByDescending(n => n)
    .Take(3)
    .ToList();
```

---

## ⚠️ Vanliga Problem

### Problem 1: Off-by-one errors

```csharp
// ❌ Common mistake
for (int i = 0; i <= array.Length; i++)  // IndexOutOfRange!
{
    Console.WriteLine(array[i]);
}

// ✅ Correct
for (int i = 0; i < array.Length; i++)
{
    Console.WriteLine(array[i]);
}

// ✅ Even better - use foreach
foreach (var item in array)
{
    Console.WriteLine(item);
}
```

### Problem 2: Missing break in switch

```csharp
// ❌ C# kräver break (fall-through ej tillåtet som i C)
switch (value)
{
    case 1:
        DoSomething();  // Error: Control cannot fall through
    case 2:
        DoSomethingElse();
        break;
}

// ✅ Explicit break eller return
switch (value)
{
    case 1:
        DoSomething();
        break;
    case 2:
        DoSomethingElse();
        break;
}
```

---

## ✅ Sammanfattning

- **Switch expressions** - moderna, kortare syntax
- **Pattern matching** - kraftfullt för type checking
- **foreach** föredras över for för collections
- **LINQ** för deklarativ data-manipulation
""",
}


# ============================================================================
# NODE 4: METHODS & FUNCTIONS
# ============================================================================

DOTNET_NODE_4_METHODS = {
    "node_id": 4,
    "title": "Methods & Functions",
    "slug": "csharp-methods",
    "description": "Metoder, parametrar, return values och lambda expressions",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 100,
    "topics_covered": [
        "methods", "parameters", "return types", "ref", "out",
        "optional parameters", "lambda", "delegates"
    ],
    "content": """
# Methods & Functions

> *"Methods are the verbs of your program - they describe what your code does."*

---

## 🎯 Why This Matters

Metoder är grundläggande för:
- **Code reuse** - skriv en gång, använd överallt
- **Abstraction** - gömma komplexitet
- **Testing** - isolerade enheter att testa

---

## 🧠 Method Anatomy

```
┌─────────────────────────────────────────────────────────────────┐
│                      METHOD ANATOMY                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   public static int Add(int a, int b)                           │
│   ──────  ────── ───  ─── ─────────────                         │
│     │       │     │    │        │                                │
│     │       │     │    │        └── Parameters                   │
│     │       │     │    └── Method name                          │
│     │       │     └── Return type                                │
│     │       └── Optional modifier (static = no instance needed) │
│     └── Access modifier (public, private, protected, internal)  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Basic Methods

```csharp
// Method that returns a value
int Add(int a, int b)
{
    return a + b;
}

// Expression-bodied method (kort syntax)
int Multiply(int a, int b) => a * b;

// Void method (returns nothing)
void PrintMessage(string message)
{
    Console.WriteLine(message);
}

// Usage
int sum = Add(5, 3);       // 8
int product = Multiply(4, 2);  // 8
PrintMessage("Hello!");
```

---

## 💻 Parameters

```csharp
// REGULAR PARAMETERS (by value)
void ModifyValue(int x)
{
    x = 100;  // Only modifies local copy
}

int num = 10;
ModifyValue(num);
Console.WriteLine(num);  // Still 10

// REF PARAMETER (by reference)
void ModifyByRef(ref int x)
{
    x = 100;  // Modifies the original
}

ModifyByRef(ref num);
Console.WriteLine(num);  // Now 100

// OUT PARAMETER (must be assigned in method)
bool TryParse(string input, out int result)
{
    if (int.TryParse(input, out result))
        return true;

    result = 0;
    return false;
}

if (TryParse("42", out int value))
{
    Console.WriteLine($"Parsed: {value}");
}

// IN PARAMETER (readonly reference)
void ProcessLargeStruct(in LargeStruct data)
{
    // data cannot be modified
    // Passed by reference for performance
}
```

---

## 💻 Optional & Named Parameters

```csharp
// Optional parameters (must be last)
void Greet(string name, string greeting = "Hello")
{
    Console.WriteLine($"{greeting}, {name}!");
}

Greet("Alice");           // Hello, Alice!
Greet("Bob", "Hi");       // Hi, Bob!

// Named parameters
void CreateUser(string name, int age, string email = "")
{
    Console.WriteLine($"Name: {name}, Age: {age}, Email: {email}");
}

CreateUser(name: "Alice", age: 25);
CreateUser(age: 30, name: "Bob");  // Order doesn't matter with names

// Params (variable number of arguments)
int Sum(params int[] numbers)
{
    return numbers.Sum();
}

Console.WriteLine(Sum(1, 2, 3));        // 6
Console.WriteLine(Sum(1, 2, 3, 4, 5));  // 15
```

---

## 💻 Lambda Expressions

```csharp
// Traditional method
bool IsEven(int n)
{
    return n % 2 == 0;
}

// Lambda expression (anonymous function)
Func<int, bool> isEven = n => n % 2 == 0;

// Lambda with multiple parameters
Func<int, int, int> add = (a, b) => a + b;

// Lambda with statement body
Func<int, int> factorial = n =>
{
    int result = 1;
    for (int i = 1; i <= n; i++)
        result *= i;
    return result;
};

// Action (void lambda)
Action<string> print = message => Console.WriteLine(message);

// Usage med LINQ
int[] numbers = { 1, 2, 3, 4, 5 };
var evens = numbers.Where(n => n % 2 == 0);
var doubled = numbers.Select(n => n * 2);
```

---

## 💻 Local Functions

```csharp
int Calculate(int x)
{
    // Local function - only accessible within Calculate
    int Square(int n) => n * n;
    int Cube(int n) => n * n * n;

    return Square(x) + Cube(x);
}

// Static local function (can't capture variables)
int ProcessData(int[] data)
{
    static int Validate(int value) => value >= 0 ? value : 0;

    return data.Select(Validate).Sum();
}
```

---

## 💻 Method Overloading

```csharp
class Calculator
{
    // Same name, different parameters
    public int Add(int a, int b) => a + b;
    public double Add(double a, double b) => a + b;
    public int Add(int a, int b, int c) => a + b + c;
    public string Add(string a, string b) => a + b;
}

var calc = new Calculator();
Console.WriteLine(calc.Add(1, 2));       // 3 (int)
Console.WriteLine(calc.Add(1.5, 2.5));   // 4.0 (double)
Console.WriteLine(calc.Add(1, 2, 3));    // 6 (int)
Console.WriteLine(calc.Add("Hello", "World"));  // HelloWorld
```

---

## ⚠️ Vanliga Problem

### Problem 1: Modifying parameters unintentionally

```csharp
// ❌ Oväntat beteende med reference types
void ModifyList(List<int> list)
{
    list.Add(100);  // Modifierar originalet!
}

// ✅ Skapa en kopia om du inte vill modifiera
void SafeModifyList(List<int> list)
{
    var copy = new List<int>(list);
    copy.Add(100);
}
```

### Problem 2: Nullable reference types

```csharp
// ❌ Potential null reference
string GetMessage(string? input)
{
    return input.ToUpper();  // Warning!
}

// ✅ Handle null
string GetMessage(string? input)
{
    return input?.ToUpper() ?? "DEFAULT";
}
```

---

## 🎮 Hands-on: String Utilities

```csharp
static class StringUtils
{
    public static string Reverse(string input)
        => new string(input.Reverse().ToArray());

    public static bool IsPalindrome(string input)
    {
        var cleaned = input.ToLower().Replace(" ", "");
        return cleaned == Reverse(cleaned);
    }

    public static string Truncate(string input, int maxLength, string suffix = "...")
        => input.Length <= maxLength
            ? input
            : input[..(maxLength - suffix.Length)] + suffix;
}

// Test
Console.WriteLine(StringUtils.Reverse("hello"));        // olleh
Console.WriteLine(StringUtils.IsPalindrome("A man a plan a canal Panama"));  // true
Console.WriteLine(StringUtils.Truncate("Hello World", 8));  // Hello...
```

---

## ✅ Sammanfattning

- **ref** - modifiera original variabel
- **out** - returnera flera värden
- **params** - variabel antal argument
- **Lambda** - kortfattade anonyma funktioner
- **Overloading** - samma namn, olika parametrar
""",
}


# Export all nodes from Block 1
BLOCK_1_NODES = [
    DOTNET_NODE_1_INTRO,
    DOTNET_NODE_2_TYPES,
    DOTNET_NODE_3_CONTROL_FLOW,
    DOTNET_NODE_4_METHODS,
]
