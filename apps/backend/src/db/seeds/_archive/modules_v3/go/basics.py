"""
Go Programming - Tasks 1-10 (Basics)
Premium Bootcamp-Quality Content
"""

TASKS_BASICS = [
    {
        "title": "Go Introduktion & Installation",
        "difficulty": "easy",
        "estimated_minutes": 45,
        "xp_reward": 100,
        "content": r"""
# 🚀 Go Introduktion & Installation

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå varför Go skapades och dess styrkor
- Installera Go på ditt system
- Förstå Go workspace och GOPATH
- Skriva ditt första Go-program

---

## 📖 Varför Go?

Go (Golang) skapades av Google 2009 för att lösa problem med:
- Långsam kompilering i C++
- Komplex dependency management
- Svårt att skriva concurrent kod

### Go's Styrkor

| Feature | Beskrivning |
|---------|-------------|
| Snabb kompilering | Sekunder, inte minuter |
| Enkel syntax | Lätt att lära, lätt att läsa |
| Inbyggd concurrency | Goroutines & channels |
| Statisk typning | Fångar fel vid kompilering |
| Garbage collection | Automatisk minneshantering |
| Single binary | Ingen runtime dependency |

### Vem använder Go?

```
+-----------------------------------------------------------------+
|  Docker, Kubernetes, Terraform, Prometheus, Grafana, Hugo      |
|  Cloudflare, Uber, Twitch, Dropbox, SoundCloud, Netflix        |
+-----------------------------------------------------------------+
```

---

## 🛠️ Installation

### macOS

```bash
# Homebrew (rekommenderat)
brew install go

# Verifiera
go version
# go version go1.22.0 darwin/arm64
```

### Ubuntu/Debian

```bash
# Via apt (kan vara äldre version)
sudo apt update && sudo apt install golang-go

# Eller ladda ner senaste
wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz

# Lägg till i PATH (~/.bashrc eller ~/.zshrc)
export PATH=$PATH:/usr/local/go/bin
```

### Verifiera installation

```bash
go version
go env GOROOT
go env GOPATH
```

---

## 📁 Go Workspace

### Modern Go (Go Modules)

```bash
# Skapa projekt
mkdir myproject && cd myproject

# Initiera modul
go mod init github.com/username/myproject

# Struktur
myproject/
+-- go.mod          # Dependencies
+-- go.sum          # Checksums
+-- main.go         # Entry point
+-- internal/       # Private packages
+-- pkg/            # Public packages
+-- cmd/            # Multiple binaries
```

### go.mod

```go
module github.com/username/myproject

go 1.22

require (
    github.com/gin-gonic/gin v1.9.1
)
```

---

## 👋 Hello World

### main.go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### Kör programmet

```bash
# Kör direkt
go run main.go

# Bygg binary
go build -o myapp main.go
./myapp

# Installera globalt
go install
```

---

## 🏋️ Övningar

### Övning 1: Setup
```bash
mkdir go-practice && cd go-practice
go mod init go-practice
echo 'package main

import "fmt"

func main() {
    fmt.Println("Go is awesome!")
}' > main.go
go run main.go
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| go version | Visa version |
| go mod init | Skapa modul |
| go run | Kör program |
| go build | Bygg binary |
| go install | Installera |

**Nästa steg:** Go Syntax & Typer

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Go Syntax & Typer",
        "difficulty": "easy",
        "estimated_minutes": 50,
        "xp_reward": 120,
        "content": r"""
# 📝 Go Syntax & Typer

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Go's grundläggande syntax
- Arbeta med variabler och konstanter
- Använda Go's inbyggda typer
- Förstå type inference

---

## 📖 Variabler

### Deklaration

```go
package main

import "fmt"

func main() {
    // Explicit typ
    var name string = "Go"
    var age int = 15

    // Type inference
    var language = "Golang"  // string
    var year = 2009          // int

    // Short declaration (vanligast)
    city := "Stockholm"
    count := 42

    // Flera samtidigt
    var x, y int = 1, 2
    a, b := "hello", true

    fmt.Println(name, age, language, year, city, count)
}
```

### Zero Values

```go
var i int      // 0
var f float64  // 0.0
var b bool     // false
var s string   // "" (tom sträng)
var p *int     // nil
```

---

## 🔢 Grundläggande Typer

### Numeriska typer

```go
// Integers
var i8 int8   = 127          // -128 till 127
var i16 int16 = 32767
var i32 int32 = 2147483647
var i64 int64 = 9223372036854775807
var i int     = 42           // Plattformsberoende (32/64 bit)

// Unsigned integers
var u8 uint8  = 255
var u uint    = 42

// Floats
var f32 float32 = 3.14
var f64 float64 = 3.141592653589793

// Complex
var c complex128 = 1 + 2i
```

### Strings & Runes

```go
// Strings (UTF-8)
s := "Hello, 世界"
fmt.Println(len(s))        // 13 bytes
fmt.Println(len([]rune(s))) // 9 characters

// Raw strings
raw := `Line 1
Line 2
No escape: \n`

// Rune (Unicode code point)
r := '世'  // rune (alias för int32)
```

### Booleans

```go
t := true
f := false

// Operatorer
and := t && f  // false
or := t || f   // true
not := !t      // false
```

---

## 🔄 Type Conversion

```go
// Go kräver explicit konvertering
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)

// String konvertering
import "strconv"

s := strconv.Itoa(42)        // int till string
i, _ := strconv.Atoi("42")   // string till int

f, _ := strconv.ParseFloat("3.14", 64)
s = strconv.FormatFloat(f, 'f', 2, 64)
```

---

## 📦 Konstanter

```go
const Pi = 3.14159
const (
    StatusOK = 200
    StatusNotFound = 404
)

// iota - auto-increment
const (
    Sunday = iota  // 0
    Monday         // 1
    Tuesday        // 2
)

// iota med uttryck
const (
    KB = 1 << (10 * iota)  // 1
    MB                      // 1024
    GB                      // 1048576
)
```

---

## 🏋️ Övningar

### Övning 1: Typer
```go
package main

import "fmt"

func main() {
    name := "DevOps Engineer"
    years := 5
    salary := 75000.50
    employed := true

    fmt.Printf("Name: %s\n", name)
    fmt.Printf("Years: %d\n", years)
    fmt.Printf("Salary: %.2f\n", salary)
    fmt.Printf("Employed: %t\n", employed)
}
```

---

## 📚 Sammanfattning

| Typ | Zero Value | Exempel |
|-----|------------|---------|
| int | 0 | 42 |
| float64 | 0.0 | 3.14 |
| string | "" | "hello" |
| bool | false | true |
| pointer | nil | &x |

**Nästa steg:** Control Flow

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Control Flow",
        "difficulty": "easy",
        "estimated_minutes": 45,
        "xp_reward": 110,
        "content": r"""
# 🔀 Control Flow

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Använda if/else och switch
- Förstå Go's for-loop (enda loop-typen)
- Arbeta med range
- Använda defer, panic, recover

---

## 📖 If/Else

```go
// Basic
if x > 0 {
    fmt.Println("positive")
} else if x < 0 {
    fmt.Println("negative")
} else {
    fmt.Println("zero")
}

// Med statement (vanligt i Go)
if err := doSomething(); err != nil {
    fmt.Println("Error:", err)
}

// err är endast tillgänglig inom if-blocket
if value, ok := cache[key]; ok {
    fmt.Println("Found:", value)
}
```

---

## 🔄 Switch

```go
// Basic switch
switch day {
case "Monday":
    fmt.Println("Start of week")
case "Friday":
    fmt.Println("TGIF!")
case "Saturday", "Sunday":
    fmt.Println("Weekend!")
default:
    fmt.Println("Midweek")
}

// Switch utan expression (if-else ersättning)
switch {
case score >= 90:
    grade = "A"
case score >= 80:
    grade = "B"
case score >= 70:
    grade = "C"
default:
    grade = "F"
}

// Type switch
switch v := i.(type) {
case int:
    fmt.Printf("Integer: %d\n", v)
case string:
    fmt.Printf("String: %s\n", v)
default:
    fmt.Printf("Unknown type\n")
}
```

---

## 🔁 For Loop

Go har endast `for` - ingen while eller do-while.

```go
// Classic for
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// While-style
for count > 0 {
    count--
}

// Infinite loop
for {
    // break to exit
    if done {
        break
    }
}

// Range over slice
nums := []int{1, 2, 3}
for index, value := range nums {
    fmt.Printf("%d: %d\n", index, value)
}

// Range over map
m := map[string]int{"a": 1, "b": 2}
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}

// Range over string (runes)
for i, r := range "Go 世界" {
    fmt.Printf("%d: %c\n", i, r)
}

// Ignorera index/value med _
for _, v := range nums {
    fmt.Println(v)
}
```

---

## ⏸️ Defer

```go
// Defer kör vid function return
func example() {
    defer fmt.Println("3. Last")
    defer fmt.Println("2. Second")
    fmt.Println("1. First")
}
// Output: 1, 2, 3 (LIFO order)

// Vanligt användningsfall - cleanup
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()  // Garanterar stängning

    // ... läs fil ...
    return nil
}
```

---

## 🏋️ Övningar

### Övning 1: FizzBuzz
```go
for i := 1; i <= 100; i++ {
    switch {
    case i%15 == 0:
        fmt.Println("FizzBuzz")
    case i%3 == 0:
        fmt.Println("Fizz")
    case i%5 == 0:
        fmt.Println("Buzz")
    default:
        fmt.Println(i)
    }
}
```

---

## 📚 Sammanfattning

| Koncept | Go Syntax |
|---------|-----------|
| If med statement | `if x := f(); x > 0` |
| Switch | Ingen fallthrough default |
| For | Enda loop-typen |
| Range | Iterera collections |
| Defer | LIFO cleanup |

**Nästa steg:** Functions

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Functions",
        "difficulty": "easy",
        "estimated_minutes": 50,
        "xp_reward": 130,
        "content": r"""
# ⚡ Functions

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Definiera och anropa funktioner
- Förstå multiple return values
- Arbeta med variadic functions
- Använda closures och anonymous functions

---

## 📖 Grundläggande Functions

```go
// Basic function
func greet(name string) string {
    return "Hello, " + name
}

// Multiple parameters samma typ
func add(a, b int) int {
    return a + b
}

// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// Användning
result, err := divide(10, 2)
if err != nil {
    log.Fatal(err)
}

// Ignorera return value
result, _ = divide(10, 2)
```

---

## 📛 Named Return Values

```go
func rectangle(width, height float64) (area, perimeter float64) {
    area = width * height
    perimeter = 2 * (width + height)
    return  // Naked return
}

// Kan också vara explicit
func rectangle2(w, h float64) (area, perimeter float64) {
    area = w * h
    perimeter = 2 * (w + h)
    return area, perimeter
}
```

---

## 📦 Variadic Functions

```go
// Accepterar valfritt antal argument
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}

// Användning
sum(1, 2, 3)        // 6
sum(1, 2, 3, 4, 5)  // 15

// Spread slice
nums := []int{1, 2, 3}
sum(nums...)  // 6
```

---

## 🔄 Functions som Values

```go
// Function som variabel
var operation func(int, int) int

operation = func(a, b int) int {
    return a + b
}
fmt.Println(operation(2, 3))  // 5

// Function som parameter
func apply(fn func(int) int, value int) int {
    return fn(value)
}

double := func(x int) int { return x * 2 }
fmt.Println(apply(double, 5))  // 10
```

---

## 🔒 Closures

```go
// Closure - fångar variabler från scope
func counter() func() int {
    count := 0
    return func() int {
        count++
        return count
    }
}

c := counter()
fmt.Println(c())  // 1
fmt.Println(c())  // 2
fmt.Println(c())  // 3

// Praktiskt exempel - middleware
func withLogging(fn func()) func() {
    return func() {
        log.Println("Before")
        fn()
        log.Println("After")
    }
}
```

---

## 🏋️ Övningar

### Övning 1: Calculator
```go
func calculator(op string) func(a, b float64) float64 {
    switch op {
    case "+":
        return func(a, b float64) float64 { return a + b }
    case "-":
        return func(a, b float64) float64 { return a - b }
    case "*":
        return func(a, b float64) float64 { return a * b }
    case "/":
        return func(a, b float64) float64 { return a / b }
    default:
        return nil
    }
}

add := calculator("+")
fmt.Println(add(10, 5))  // 15
```

---

## 📚 Sammanfattning

| Feature | Syntax |
|---------|--------|
| Multiple returns | `func f() (int, error)` |
| Named returns | `func f() (x int)` |
| Variadic | `func f(nums ...int)` |
| Closure | `func() func() int` |

**Nästa steg:** Structs & Methods

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Structs & Methods",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 140,
        "content": r"""
# 🏗️ Structs & Methods

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Definiera och använda structs
- Skapa methods på structs
- Förstå pointer vs value receivers
- Använda embedding för komposition

---

## 📖 Structs

```go
// Definiera struct
type User struct {
    ID        int
    Name      string
    Email     string
    Active    bool
    CreatedAt time.Time
}

// Skapa instans
user1 := User{
    ID:     1,
    Name:   "Alice",
    Email:  "alice@example.com",
    Active: true,
}

// Kortare (alla fält i ordning)
user2 := User{2, "Bob", "bob@example.com", true, time.Now()}

// Zero value struct
var user3 User  // Alla fält får zero values

// Access fields
fmt.Println(user1.Name)
user1.Active = false
```

---

## 🔧 Methods

```go
type Rectangle struct {
    Width  float64
    Height float64
}

// Value receiver (kopierar struct)
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

// Pointer receiver (modifierar original)
func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

// Användning
rect := Rectangle{10, 5}
fmt.Println(rect.Area())  // 50

rect.Scale(2)
fmt.Println(rect.Area())  // 200
```

### Value vs Pointer Receiver

```
+-----------------------------------------------------------------+
|                 RECEIVER GUIDELINES                             |
+-----------------------------------------------------------------+
|                                                                 |
|   Använd POINTER receiver när:                                 |
|   • Method ska modifiera struct                                |
|   • Struct är stor (undvik kopiering)                         |
|   • Konsistens (om en method använder pointer)                |
|                                                                 |
|   Använd VALUE receiver när:                                   |
|   • Struct är liten och immutable                              |
|   • Method läser bara data                                     |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## 🔗 Struct Embedding

```go
// Komposition istället för arv
type Person struct {
    Name string
    Age  int
}

func (p Person) Greet() string {
    return "Hi, I'm " + p.Name
}

type Employee struct {
    Person              // Embedded
    EmployeeID string
    Department string
}

// Employee får Person's methods
emp := Employee{
    Person:     Person{Name: "Alice", Age: 30},
    EmployeeID: "E001",
    Department: "Engineering",
}

fmt.Println(emp.Name)    // Direkt access
fmt.Println(emp.Greet()) // Promoted method
```

---

## 🏷️ Tags

```go
type User struct {
    ID       int    `json:"id" db:"user_id"`
    Name     string `json:"name" validate:"required"`
    Email    string `json:"email" validate:"email"`
    Password string `json:"-"`  // Ignoreras i JSON
}

// Reflection för att läsa tags
import "reflect"

t := reflect.TypeOf(User{})
field, _ := t.FieldByName("Name")
fmt.Println(field.Tag.Get("json"))  // "name"
```

---

## 🏋️ Övningar

### Övning 1: Bank Account
```go
type BankAccount struct {
    Owner   string
    Balance float64
}

func (a *BankAccount) Deposit(amount float64) {
    a.Balance += amount
}

func (a *BankAccount) Withdraw(amount float64) error {
    if amount > a.Balance {
        return errors.New("insufficient funds")
    }
    a.Balance -= amount
    return nil
}

func (a BankAccount) String() string {
    return fmt.Sprintf("%s: $%.2f", a.Owner, a.Balance)
}
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| Struct | Grupperar data |
| Method | Funktion på typ |
| Value receiver | Kopierar |
| Pointer receiver | Modifierar |
| Embedding | Komposition |
| Tags | Metadata |

**Nästa steg:** Interfaces

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Interfaces",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 145,
        "content": r"""
# 🔌 Interfaces

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå implicit interface implementation
- Definiera och använda interfaces
- Arbeta med empty interface
- Type assertions och type switches

---

## 📖 Interface Basics

```go
// Interface definierar beteende
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Composition
type ReadWriter interface {
    Reader
    Writer
}
```

### Implicit Implementation

```go
// Ingen "implements" keyword
type MyFile struct {
    data []byte
}

// MyFile implementerar Reader automatiskt
func (f *MyFile) Read(p []byte) (n int, err error) {
    copy(p, f.data)
    return len(f.data), nil
}

// Nu kan MyFile användas var Reader förväntas
var r Reader = &MyFile{data: []byte("hello")}
```

---

## 🎯 Praktiskt Exempel

```go
// Interface
type Shape interface {
    Area() float64
    Perimeter() float64
}

// Implementationer
type Rectangle struct {
    Width, Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.Width + r.Height)
}

type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.Radius
}

// Polymorfism
func PrintShapeInfo(s Shape) {
    fmt.Printf("Area: %.2f, Perimeter: %.2f\n", s.Area(), s.Perimeter())
}

PrintShapeInfo(Rectangle{10, 5})
PrintShapeInfo(Circle{7})
```

---

## 📦 Empty Interface

```go
// interface{} eller any (Go 1.18+)
var i interface{}

i = 42
i = "hello"
i = struct{ X int }{1}

// Användning i funktioner
func PrintAnything(v interface{}) {
    fmt.Println(v)
}

// Slice av anything
data := []interface{}{1, "two", 3.0, true}
```

---

## 🔍 Type Assertions

```go
var i interface{} = "hello"

// Type assertion
s := i.(string)
fmt.Println(s)  // "hello"

// Safe assertion
s, ok := i.(string)
if ok {
    fmt.Println("String:", s)
}

// Type switch
func describe(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Printf("Integer: %d\n", v)
    case string:
        fmt.Printf("String: %s\n", v)
    case bool:
        fmt.Printf("Boolean: %t\n", v)
    default:
        fmt.Printf("Unknown: %T\n", v)
    }
}
```

---

## 🏋️ Övningar

### Övning 1: Stringer Interface
```go
type Person struct {
    Name string
    Age  int
}

// Implementera fmt.Stringer
func (p Person) String() string {
    return fmt.Sprintf("%s (%d years)", p.Name, p.Age)
}

p := Person{"Alice", 30}
fmt.Println(p)  // "Alice (30 years)"
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| Interface | Definierar beteende |
| Implicit impl | Ingen "implements" |
| Empty interface | `interface{}` eller `any` |
| Type assertion | `v.(Type)` |
| Type switch | `switch v := i.(type)` |

**Nästa steg:** Error Handling

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Error Handling",
        "difficulty": "medium",
        "estimated_minutes": 50,
        "xp_reward": 140,
        "content": r"""
# ⚠️ Error Handling

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå Go's error handling philosophy
- Skapa och returnera errors
- Wrappa errors med context
- Använda errors.Is och errors.As

---

## 📖 Error Basics

```go
// error är ett interface
type error interface {
    Error() string
}

// Returnera error
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// Hantera error
result, err := divide(10, 0)
if err != nil {
    log.Fatal(err)
}
```

---

## 🏗️ Skapa Errors

```go
import (
    "errors"
    "fmt"
)

// Simple error
err := errors.New("something went wrong")

// Formatted error
err := fmt.Errorf("failed to process %s: invalid format", filename)

// Custom error type
type ValidationError struct {
    Field   string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation error on %s: %s", e.Field, e.Message)
}

// Sentinel errors
var (
    ErrNotFound     = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)
```

---

## 🔗 Error Wrapping

```go
// Wrap error med context
func readConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("readConfig: %w", err)
    }

    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return nil, fmt.Errorf("readConfig: parse error: %w", err)
    }

    return &cfg, nil
}

// Unwrap
err := readConfig("config.json")
if errors.Is(err, os.ErrNotExist) {
    fmt.Println("Config file not found")
}
```

---

## 🔍 errors.Is och errors.As

```go
// errors.Is - jämför med sentinel
if errors.Is(err, os.ErrNotExist) {
    // Filen finns inte
}

if errors.Is(err, ErrNotFound) {
    // Vår custom sentinel
}

// errors.As - extrahera typed error
var pathErr *os.PathError
if errors.As(err, &pathErr) {
    fmt.Println("Failed path:", pathErr.Path)
}

var valErr ValidationError
if errors.As(err, &valErr) {
    fmt.Println("Invalid field:", valErr.Field)
}
```

---

## 🏋️ Övningar

### Övning 1: Custom Error
```go
type HTTPError struct {
    StatusCode int
    Message    string
}

func (e HTTPError) Error() string {
    return fmt.Sprintf("HTTP %d: %s", e.StatusCode, e.Message)
}

func fetchUser(id int) (*User, error) {
    if id <= 0 {
        return nil, HTTPError{400, "invalid user ID"}
    }
    // ...
    return nil, HTTPError{404, "user not found"}
}
```

---

## 📚 Sammanfattning

| Funktion | Användning |
|----------|-----------|
| errors.New | Skapa simple error |
| fmt.Errorf | Formaterad error |
| fmt.Errorf %w | Wrap error |
| errors.Is | Jämför errors |
| errors.As | Extrahera typ |

**Nästa steg:** Slices & Maps

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Slices & Maps",
        "difficulty": "medium",
        "estimated_minutes": 55,
        "xp_reward": 145,
        "content": r"""
# 📊 Slices & Maps

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå arrays vs slices
- Manipulera slices effektivt
- Arbeta med maps
- Förstå underlying arrays och capacity

---

## 📖 Arrays

```go
// Fixed size - sällan används direkt
var arr [5]int                    // [0,0,0,0,0]
arr2 := [3]string{"a", "b", "c"}
arr3 := [...]int{1, 2, 3, 4}      // Compiler räknar

fmt.Println(len(arr))  // 5
arr[0] = 10
```

---

## 🔪 Slices

```go
// Dynamisk storlek - används oftast
var s []int               // nil slice
s = make([]int, 5)        // len=5, cap=5
s = make([]int, 5, 10)    // len=5, cap=10

// Literal
nums := []int{1, 2, 3, 4, 5}

// Slicing
sub := nums[1:4]   // [2,3,4]
sub := nums[:3]    // [1,2,3]
sub := nums[2:]    // [3,4,5]
copy := nums[:]    // hela slicen

// Append
nums = append(nums, 6)
nums = append(nums, 7, 8, 9)
nums = append(nums, other...)
```

### Slice Internals

```
+-----------------------------------------------------------------+
|                     SLICE STRUCTURE                             |
+-----------------------------------------------------------------+
|                                                                 |
|   slice := []int{1, 2, 3, 4, 5}                                |
|                                                                 |
|   +-------------+                                              |
|   |   pointer   |----> [1][2][3][4][5]  (underlying array)    |
|   |   length: 5 |                                              |
|   |   capacity:5|                                              |
|   +-------------+                                              |
|                                                                 |
|   sub := slice[1:3]                                            |
|                                                                 |
|   +-------------+                                              |
|   |   pointer   |---------> [2][3]                            |
|   |   length: 2 |                                              |
|   |   capacity:4|      (delar samma underlying array!)        |
|   +-------------+                                              |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## 🗺️ Maps

```go
// Skapa map
var m map[string]int           // nil map
m = make(map[string]int)       // Initierad
m = map[string]int{"a": 1}     // Literal

// CRUD
m["key"] = 100                 // Create/Update
value := m["key"]              // Read
delete(m, "key")               // Delete

// Check existence
value, ok := m["key"]
if ok {
    fmt.Println("Found:", value)
}

// Iterate
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}
```

---

## 🛠️ Common Operations

```go
// Copy slice (inte reference)
src := []int{1, 2, 3}
dst := make([]int, len(src))
copy(dst, src)

// Filter
var filtered []int
for _, v := range nums {
    if v > 5 {
        filtered = append(filtered, v)
    }
}

// Contains (map approach)
set := make(map[string]bool)
set["a"] = true
if set["a"] {
    // exists
}
```

---

## 🏋️ Övningar

### Övning 1: Slice Operations
```go
nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

// Filter even
var evens []int
for _, n := range nums {
    if n%2 == 0 {
        evens = append(evens, n)
    }
}

// Sum
sum := 0
for _, n := range nums {
    sum += n
}
```

---

## 📚 Sammanfattning

| Operation | Syntax |
|-----------|--------|
| Skapa slice | `make([]T, len, cap)` |
| Append | `s = append(s, v)` |
| Slice | `s[start:end]` |
| Map create | `make(map[K]V)` |
| Map check | `v, ok := m[k]` |
| Delete | `delete(m, k)` |

**Nästa steg:** Concurrency - Goroutines

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Concurrency - Goroutines",
        "difficulty": "medium",
        "estimated_minutes": 60,
        "xp_reward": 160,
        "content": r"""
# ⚡ Concurrency - Goroutines

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå goroutines vs threads
- Starta och hantera goroutines
- Synkronisera med WaitGroup
- Undvika race conditions

---

## 📖 Goroutines

```go
// Starta goroutine med go keyword
go doSomething()

go func() {
    fmt.Println("Anonymous goroutine")
}()

// Exempel
func main() {
    go sayHello("Alice")
    go sayHello("Bob")

    time.Sleep(time.Second)  // Vänta (dålig praxis)
}

func sayHello(name string) {
    fmt.Println("Hello,", name)
}
```

### Goroutines vs Threads

```
+-----------------------------------------------------------------+
|               GOROUTINES vs OS THREADS                          |
+-----------------------------------------------------------------+
|                                                                 |
|   Goroutines:                   OS Threads:                    |
|   • ~2KB stack                  • ~1MB stack                   |
|   • Managed by Go runtime       • Managed by OS                |
|   • Cooperative scheduling      • Preemptive                   |
|   • Millions möjliga            • Tusentals max                |
|   • Snabba att skapa            • Dyra att skapa               |
|                                                                 |
+-----------------------------------------------------------------+
```

---

## 🔄 WaitGroup

```go
import "sync"

func main() {
    var wg sync.WaitGroup

    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            fmt.Println("Worker", id)
        }(i)
    }

    wg.Wait()  // Vänta på alla goroutines
    fmt.Println("All done")
}
```

---

## ⚠️ Race Conditions

```go
// RACE CONDITION - FEL!
var counter int

func main() {
    for i := 0; i < 1000; i++ {
        go func() {
            counter++  // Inte thread-safe!
        }()
    }
    time.Sleep(time.Second)
    fmt.Println(counter)  // Oförutsägbart resultat
}

// LÖSNING 1: Mutex
var (
    counter int
    mu      sync.Mutex
)

func main() {
    for i := 0; i < 1000; i++ {
        go func() {
            mu.Lock()
            counter++
            mu.Unlock()
        }()
    }
}

// LÖSNING 2: Atomic
import "sync/atomic"

var counter int64

func main() {
    for i := 0; i < 1000; i++ {
        go func() {
            atomic.AddInt64(&counter, 1)
        }()
    }
}
```

---

## 🔍 Race Detector

```bash
# Kör med race detection
go run -race main.go
go test -race ./...
```

---

## 🏋️ Övningar

### Övning 1: Parallel Workers
```go
func main() {
    var wg sync.WaitGroup
    jobs := []string{"job1", "job2", "job3", "job4", "job5"}

    for _, job := range jobs {
        wg.Add(1)
        go func(j string) {
            defer wg.Done()
            fmt.Printf("Processing %s\n", j)
            time.Sleep(100 * time.Millisecond)
            fmt.Printf("Done %s\n", j)
        }(job)
    }

    wg.Wait()
}
```

---

## 📚 Sammanfattning

| Koncept | Beskrivning |
|---------|-------------|
| go func() | Starta goroutine |
| WaitGroup | Synkronisera goroutines |
| Mutex | Skydda shared state |
| Atomic | Lock-free operations |
| -race | Detecta race conditions |

**Nästa steg:** Channels

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Channels",
        "difficulty": "hard",
        "estimated_minutes": 60,
        "xp_reward": 170,
        "content": r"""
# 📡 Channels

## Varför detta är viktigt

> **"Kunskap utan praktik är bara teori – här bygger vi verkliga färdigheter."**

```
+---------------------------------------------------------------------+
|                    DEVOPS CONTINUOUS FLOW                            |
+---------------------------------------------------------------------+
|   Code --▶ Build --▶ Test --▶ Deploy --▶ Monitor --▶ Feedback      |
+---------------------------------------------------------------------+
```

### Vad du kommer lära dig

- ✅ Förstå kärnkoncepten på djupet
- ✅ Tillämpa kunskapen praktiskt
- ✅ Undvika vanliga misstag
- ✅ Bygga robusta lösningar

---


## Lärande mål
- Förstå channels som kommunikationsmekanism
- Använda buffered vs unbuffered channels
- Implementera patterns med select
- Hantera channel closing

---

## 📖 Channel Basics

```go
// Skapa channel
ch := make(chan int)          // Unbuffered
ch := make(chan int, 10)      // Buffered

// Send och receive
ch <- 42        // Send
value := <-ch   // Receive

// Directional channels
func send(ch chan<- int) {    // Send-only
    ch <- 42
}

func receive(ch <-chan int) { // Receive-only
    v := <-ch
}
```

---

## 🔄 Unbuffered vs Buffered

```
+-----------------------------------------------------------------+
|                    CHANNEL TYPES                                |
+-----------------------------------------------------------------+
|                                                                 |
|   UNBUFFERED:                                                  |
|   • Synkron - sender blockerar tills receiver tar emot         |
|   • Garanterar leverans                                        |
|   ch := make(chan int)                                         |
|                                                                 |
|   BUFFERED:                                                    |
|   • Asynkron upp till buffer-storlek                          |
|   • Sender blockerar endast när buffer är full                |
|   ch := make(chan int, 10)                                    |
|                                                                 |
+-----------------------------------------------------------------+
```

```go
// Unbuffered - synkron
ch := make(chan int)
go func() {
    ch <- 42  // Blockerar tills någon tar emot
}()
value := <-ch  // Blockerar tills någon skickar

// Buffered - asynkron
ch := make(chan int, 2)
ch <- 1  // Blockerar inte
ch <- 2  // Blockerar inte
ch <- 3  // Blockerar (buffer full)
```

---

## 🎯 Select

```go
// Select - multiplexar channels
select {
case msg := <-ch1:
    fmt.Println("Received from ch1:", msg)
case msg := <-ch2:
    fmt.Println("Received from ch2:", msg)
case ch3 <- 42:
    fmt.Println("Sent to ch3")
default:
    fmt.Println("No channel ready")
}

// Timeout pattern
select {
case result := <-ch:
    fmt.Println(result)
case <-time.After(1 * time.Second):
    fmt.Println("Timeout!")
}

// Non-blocking receive
select {
case msg := <-ch:
    fmt.Println(msg)
default:
    fmt.Println("No message")
}
```

---

## 🔒 Channel Closing

```go
// Producer stänger channel
func producer(ch chan<- int) {
    for i := 0; i < 5; i++ {
        ch <- i
    }
    close(ch)  // Signalera att vi är klara
}

// Consumer itererar tills stängd
func consumer(ch <-chan int) {
    for value := range ch {  // Stoppar vid close
        fmt.Println(value)
    }
}

// Check if closed
value, ok := <-ch
if !ok {
    fmt.Println("Channel closed")
}
```

---

## 📊 Common Patterns

### Worker Pool

```go
func workerPool(jobs <-chan int, results chan<- int, id int) {
    for job := range jobs {
        results <- job * 2
    }
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)

    // Start workers
    for w := 0; w < 3; w++ {
        go workerPool(jobs, results, w)
    }

    // Send jobs
    for j := 0; j < 9; j++ {
        jobs <- j
    }
    close(jobs)

    // Collect results
    for r := 0; r < 9; r++ {
        fmt.Println(<-results)
    }
}
```

---

## 🏋️ Övningar

### Övning 1: Pipeline
```go
func generator(nums ...int) <-chan int {
    out := make(chan int)
    go func() {
        for _, n := range nums {
            out <- n
        }
        close(out)
    }()
    return out
}

func square(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        for n := range in {
            out <- n * n
        }
        close(out)
    }()
    return out
}

// Usage
nums := generator(1, 2, 3, 4, 5)
squares := square(nums)
for s := range squares {
    fmt.Println(s)
}
```

---

## 📚 Sammanfattning

| Operation | Syntax |
|-----------|--------|
| Create | `make(chan T, cap)` |
| Send | `ch <- value` |
| Receive | `value := <-ch` |
| Close | `close(ch)` |
| Range | `for v := range ch` |
| Select | Multiplexar channels |

**Nästa steg:** Go for DevOps

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
]
