"""
Go (Golang) SkillsMap — Systems Programming for DevOps
======================================================

20 nodes covering Go from basics to DevOps tooling.
Akhilesh-style pedagogy: Hook → Concept → Code → Pro Tips → Hands-on

Block 1: Introduction
Block 2: Variables & Types
Block 3: Control Flow
Block 4: Functions
Block 5: Structs
Block 6: Interfaces
Block 7: Error Handling
Block 8: Goroutines
Block 9: Channels
Block 10: Packages
Block 11: Testing
Block 12: HTTP
Block 13: JSON
Block 14: CLI Tools
Block 15: Files
Block 16: Concurrency Patterns
Block 17: Context
Block 18: Modules
Block 19: DevOps Tools
Block 20: Capstone
"""

from typing import Any

# ============================================================================
# BLOCK 1: INTRODUCTION (Node 1)
# ============================================================================

GO_NODE_01_INTRODUCTION = {
    "id": "go-01-introduction",
    "title": "Go Introduction",
    "description": "Understand why Go dominates DevOps tooling",
    "content": """
# Go Introduction

> *"Go is the language of the cloud. Docker, Kubernetes, Terraform—all written in Go."*

---

## 🎯 Why This Matters

Go powers modern DevOps infrastructure:
- **Docker** — Container runtime
- **Kubernetes** — Container orchestration  
- **Terraform** — Infrastructure as Code
- **Prometheus** — Monitoring
- **Grafana Loki** — Log aggregation

Why Go for DevOps?
- Single binary deployment (no dependencies)
- Fast compilation
- Built-in concurrency
- Cross-compilation to any platform

---

## 💡 Core Concepts

### Hello World

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, DevOps!")
}
```

### Compile & Run

```bash
# Run directly
go run main.go

# Build binary
go build -o myapp main.go
./myapp

# Cross-compile for Linux
GOOS=linux GOARCH=amd64 go build -o myapp-linux main.go
```

---

## 🔧 Setup

```bash
# Install Go (macOS)
brew install go

# Verify
go version

# Set up workspace
mkdir -p ~/go/src/devops-tools
cd ~/go/src/devops-tools
go mod init devops-tools
```

---

## 🔥 Pro Tips

### 1. Use Go Modules
```bash
go mod init myproject
go mod tidy
```

### 2. Format Code
```bash
go fmt ./...
```

### 3. Check for Issues
```bash
go vet ./...
```

---

## 🛠️ Hands-on Exercise

1. Install Go
2. Create a hello world program
3. Build and run it
4. Cross-compile for a different OS

---

## 📚 Resources

- [Go Tour](https://go.dev/tour/)
- [Effective Go](https://go.dev/doc/effective_go)
""",
    "xp_reward": 150,
    "estimated_time": "30 minutes",
    "difficulty": "beginner",
    "order_index": 1,
    "tags": ["go", "golang", "introduction", "devops"],
}


# ============================================================================
# BLOCK 2: VARIABLES & TYPES (Node 2)
# ============================================================================

GO_NODE_02_VARIABLES = {
    "id": "go-02-variables",
    "title": "Variables & Types",
    "description": "Master Go's type system and variable declarations",
    "content": """
# Variables & Types

> *"Go is statically typed but feels dynamic with type inference."*

---

## 🎯 Why This Matters

Strong typing catches bugs at compile time:
- No runtime type errors
- Clear API contracts
- Better tooling support

---

## 💡 Variable Declarations

```go
package main

import "fmt"

func main() {
    // Explicit type
    var name string = "DevOps"
    var port int = 8080
    var enabled bool = true
    
    // Type inference
    var message = "Hello"  // string inferred
    
    // Short declaration (most common)
    host := "localhost"
    timeout := 30
    
    // Multiple variables
    var x, y int = 10, 20
    a, b := "hello", "world"
    
    // Constants
    const maxRetries = 3
    const apiVersion = "v1"
    
    fmt.Printf("Server: %s:%d\\n", host, port)
}
```

---

## 🔧 Basic Types

```go
// Strings
name := "kubernetes"
length := len(name)

// Numbers
port := 8080          // int
ratio := 0.75         // float64
var count int64 = 1000000

// Booleans
enabled := true
disabled := !enabled

// Zero values (defaults)
var s string   // ""
var n int      // 0
var b bool     // false
var f float64  // 0.0
```

---

## 🎯 Type Conversions

```go
// Explicit conversion required
var i int = 42
var f float64 = float64(i)
var s string = strconv.Itoa(i)

// String to int
port, err := strconv.Atoi("8080")
if err != nil {
    log.Fatal(err)
}
```

---

## 🔥 Pro Tips

### 1. Use Short Declaration
```go
// Prefer this
name := "value"

// Over this
var name string = "value"
```

### 2. Group Related Vars
```go
var (
    host    = "localhost"
    port    = 8080
    timeout = 30
)
```

---

## 🛠️ Hands-on Exercise

Create config variables for a service:
- host, port, timeout
- Print formatted output

---

## 📚 Resources

- [Go Types](https://go.dev/ref/spec#Types)
""",
    "xp_reward": 150,
    "estimated_time": "25 minutes",
    "difficulty": "beginner",
    "order_index": 2,
    "tags": ["go", "variables", "types", "basics"],
}


# ============================================================================
# BLOCK 3: CONTROL FLOW (Node 3)
# ============================================================================

GO_NODE_03_CONTROL_FLOW = {
    "id": "go-03-control-flow",
    "title": "Control Flow",
    "description": "Master if, for, and switch statements in Go",
    "content": """
# Control Flow

> *"Go has only one loop: for. But it does everything."*

---

## 🎯 Why This Matters

Clean control flow = readable DevOps scripts:
- Simple iteration over resources
- Clear conditional logic
- No complex loop constructs to remember

---

## 💡 If Statements

```go
// Basic if
if status == "running" {
    fmt.Println("Service is up")
}

// If with initialization
if err := startService(); err != nil {
    log.Fatal(err)
}

// If-else
if count > 0 {
    fmt.Println("Has items")
} else {
    fmt.Println("Empty")
}

// If-else chain
if status == "running" {
    fmt.Println("Running")
} else if status == "pending" {
    fmt.Println("Starting...")
} else {
    fmt.Println("Stopped")
}
```

---

## 🔧 For Loops

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
    if done {
        break
    }
}

// Range over slice
pods := []string{"pod-1", "pod-2", "pod-3"}
for i, pod := range pods {
    fmt.Printf("%d: %s\\n", i, pod)
}

// Range over map
config := map[string]string{
    "host": "localhost",
    "port": "8080",
}
for key, value := range config {
    fmt.Printf("%s=%s\\n", key, value)
}
```

---

## 🎯 Switch

```go
// Basic switch
switch status {
case "running":
    fmt.Println("Up")
case "pending", "starting":
    fmt.Println("Starting...")
default:
    fmt.Println("Unknown")
}

// Switch with no expression
switch {
case score >= 90:
    fmt.Println("A")
case score >= 80:
    fmt.Println("B")
default:
    fmt.Println("C")
}
```

---

## 🔥 Pro Tips

### 1. Prefer Range
```go
// Use range, not index
for _, pod := range pods {
    fmt.Println(pod)
}
```

### 2. Break with Labels
```go
outer:
for _, ns := range namespaces {
    for _, pod := range ns.Pods {
        if pod.Name == target {
            break outer
        }
    }
}
```

---

## 🛠️ Hands-on Exercise

Write a loop that:
1. Iterates over a list of services
2. Checks each service status
3. Counts running vs stopped

---

## 📚 Resources

- [Go Control Structures](https://go.dev/tour/flowcontrol/1)
""",
    "xp_reward": 150,
    "estimated_time": "25 minutes",
    "difficulty": "beginner",
    "order_index": 3,
    "tags": ["go", "control-flow", "loops", "conditions"],
}


# ============================================================================
# BLOCK 4: FUNCTIONS (Node 4)
# ============================================================================

GO_NODE_04_FUNCTIONS = {
    "id": "go-04-functions",
    "title": "Functions",
    "description": "Write clean, reusable functions in Go",
    "content": """
# Functions

> *"Go functions can return multiple values—perfect for error handling."*

---

## 🎯 Why This Matters

Functions are the building blocks:
- Multiple return values (data + error)
- First-class functions
- Defer for cleanup

---

## 💡 Basic Functions

```go
// Simple function
func greet(name string) {
    fmt.Printf("Hello, %s!\\n", name)
}

// With return value
func add(a, b int) int {
    return a + b
}

// Multiple parameters same type
func multiply(a, b, c int) int {
    return a * b * c
}
```

---

## 🔧 Multiple Return Values

```go
// Return value and error (Go idiom)
func getConfig(key string) (string, error) {
    value := os.Getenv(key)
    if value == "" {
        return "", fmt.Errorf("config %s not set", key)
    }
    return value, nil
}

// Usage
value, err := getConfig("API_KEY")
if err != nil {
    log.Fatal(err)
}
fmt.Println(value)

// Named return values
func divide(a, b float64) (result float64, err error) {
    if b == 0 {
        err = errors.New("division by zero")
        return
    }
    result = a / b
    return
}
```

---

## 🎯 Variadic Functions

```go
// Accept any number of arguments
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}

// Usage
sum(1, 2, 3)
sum(1, 2, 3, 4, 5)

// Spread a slice
numbers := []int{1, 2, 3}
sum(numbers...)
```

---

## 🔧 Defer

```go
// Defer executes when function returns
func readFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()  // Runs at end
    
    // Read file...
    return nil
}

// Multiple defers (LIFO order)
func example() {
    defer fmt.Println("3")
    defer fmt.Println("2")
    defer fmt.Println("1")
    // Prints: 1, 2, 3
}
```

---

## 🔥 Pro Tips

### 1. Always Check Errors
```go
result, err := doSomething()
if err != nil {
    return err  // Propagate up
}
```

### 2. Use Defer for Cleanup
```go
mu.Lock()
defer mu.Unlock()
```

---

## 🛠️ Hands-on Exercise

Write a function that:
1. Takes a service name
2. Checks if it's running
3. Returns status and error

---

## 📚 Resources

- [Go Functions](https://go.dev/tour/moretypes/24)
""",
    "xp_reward": 175,
    "estimated_time": "30 minutes",
    "difficulty": "beginner",
    "order_index": 4,
    "tags": ["go", "functions", "defer", "errors"],
}


# ============================================================================
# BLOCK 5: STRUCTS (Node 5)
# ============================================================================

GO_NODE_05_STRUCTS = {
    "id": "go-05-structs",
    "title": "Structs",
    "description": "Define custom types with structs",
    "content": """
# Structs

> *"Structs are Go's way of creating custom types—perfect for modeling resources."*

---

## 🎯 Why This Matters

Structs model real-world entities:
- Pods, Services, Deployments
- Configuration objects
- API responses

---

## 💡 Defining Structs

```go
// Basic struct
type Pod struct {
    Name      string
    Namespace string
    Status    string
    Replicas  int
}

// Create instance
pod := Pod{
    Name:      "nginx",
    Namespace: "default",
    Status:    "Running",
    Replicas:  3,
}

// Access fields
fmt.Println(pod.Name)
pod.Status = "Pending"
```

---

## 🔧 Struct Methods

```go
type Service struct {
    Name string
    Port int
    Host string
}

// Method with receiver
func (s Service) URL() string {
    return fmt.Sprintf("http://%s:%d", s.Host, s.Port)
}

// Pointer receiver (can modify)
func (s *Service) SetPort(port int) {
    s.Port = port
}

// Usage
svc := Service{Name: "api", Port: 8080, Host: "localhost"}
fmt.Println(svc.URL())  // http://localhost:8080
svc.SetPort(9090)
```

---

## 🎯 Embedded Structs

```go
// Base struct
type Metadata struct {
    Name      string
    Namespace string
    Labels    map[string]string
}

// Embedding
type Deployment struct {
    Metadata           // Embedded
    Replicas  int
    Image     string
}

// Access embedded fields directly
dep := Deployment{
    Metadata: Metadata{Name: "api", Namespace: "prod"},
    Replicas: 3,
}
fmt.Println(dep.Name)  // Access directly
```

---

## 🔧 Struct Tags

```go
// JSON tags for serialization
type Config struct {
    Host     string `json:"host"`
    Port     int    `json:"port"`
    Timeout  int    `json:"timeout,omitempty"`
    internal string `json:"-"`  // Ignored
}

// YAML tags
type K8sResource struct {
    APIVersion string `yaml:"apiVersion"`
    Kind       string `yaml:"kind"`
}
```

---

## 🔥 Pro Tips

### 1. Use Pointer Receivers
```go
// For large structs or mutations
func (p *Pod) Restart() error {
    p.Status = "Restarting"
    return nil
}
```

### 2. Constructor Functions
```go
func NewPod(name string) *Pod {
    return &Pod{
        Name:      name,
        Namespace: "default",
        Status:    "Pending",
    }
}
```

---

## 🛠️ Hands-on Exercise

Create a Deployment struct:
1. Name, Namespace, Replicas, Image
2. Add a Scale method
3. Add a String method for display

---

## 📚 Resources

- [Go Structs](https://go.dev/tour/moretypes/2)
""",
    "xp_reward": 175,
    "estimated_time": "30 minutes",
    "difficulty": "beginner",
    "order_index": 5,
    "tags": ["go", "structs", "types", "methods"],
}


# ============================================================================
# BLOCK 6: INTERFACES (Node 6)
# ============================================================================

GO_NODE_06_INTERFACES = {
    "id": "go-06-interfaces",
    "title": "Interfaces",
    "description": "Write flexible code with Go interfaces",
    "content": """
# Interfaces

> *"If it walks like a duck and quacks like a duck, it's a duck."*

---

## 🎯 Why This Matters

Interfaces enable:
- Flexible, testable code
- Plugin architectures
- Mock implementations

---

## 💡 Defining Interfaces

```go
// Interface definition
type Runner interface {
    Run() error
}

// Any type with Run() implements Runner
type Pod struct {
    Name string
}

func (p Pod) Run() error {
    fmt.Printf("Running pod %s\\n", p.Name)
    return nil
}

type Job struct {
    Name string
}

func (j Job) Run() error {
    fmt.Printf("Running job %s\\n", j.Name)
    return nil
}

// Use interface
func execute(r Runner) error {
    return r.Run()
}

// Works with both
execute(Pod{Name: "nginx"})
execute(Job{Name: "backup"})
```

---

## 🔧 Common Interfaces

```go
// io.Reader and io.Writer
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// Stringer (like __str__ in Python)
type Stringer interface {
    String() string
}

func (p Pod) String() string {
    return fmt.Sprintf("Pod<%s>", p.Name)
}
```

---

## 🎯 Empty Interface

```go
// interface{} accepts any type
func printAny(v interface{}) {
    fmt.Printf("%v\\n", v)
}

// Go 1.18+ use 'any'
func printAnything(v any) {
    fmt.Printf("%v\\n", v)
}

// Type assertion
func process(v interface{}) {
    if s, ok := v.(string); ok {
        fmt.Println("String:", s)
    }
}

// Type switch
func describe(v interface{}) {
    switch t := v.(type) {
    case string:
        fmt.Println("String:", t)
    case int:
        fmt.Println("Int:", t)
    default:
        fmt.Println("Unknown type")
    }
}
```

---

## 🔥 Pro Tips

### 1. Small Interfaces
```go
// Prefer small interfaces
type Closer interface {
    Close() error
}
```

### 2. Accept Interfaces, Return Structs
```go
func NewService(store DataStore) *Service {
    return &Service{store: store}
}
```

---

## 🛠️ Hands-on Exercise

Create a Deployer interface:
1. Deploy() and Rollback() methods
2. Implement for Kubernetes and Docker
3. Write a function that accepts Deployer

---

## 📚 Resources

- [Go Interfaces](https://go.dev/tour/methods/9)
""",
    "xp_reward": 200,
    "estimated_time": "35 minutes",
    "difficulty": "intermediate",
    "order_index": 6,
    "tags": ["go", "interfaces", "polymorphism", "design"],
}


# ============================================================================
# BLOCK 7: ERROR HANDLING (Node 7)
# ============================================================================

GO_NODE_07_ERROR_HANDLING = {
    "id": "go-07-error-handling",
    "title": "Error Handling",
    "description": "Master Go's explicit error handling pattern",
    "content": """
# Error Handling

> *"Errors are values in Go—handle them explicitly, not exceptionally."*

---

## 🎯 Why This Matters

Go's error handling:
- No exceptions to catch
- Errors are explicit return values
- Forces you to handle failures

---

## 💡 Basic Error Handling

```go
// Functions return errors
func readConfig(path string) ([]byte, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, err
    }
    return data, nil
}

// Always check errors
data, err := readConfig("config.yaml")
if err != nil {
    log.Fatalf("Failed to read config: %v", err)
}
```

---

## 🔧 Creating Errors

```go
import (
    "errors"
    "fmt"
)

// Simple error
err := errors.New("something went wrong")

// Formatted error
err := fmt.Errorf("failed to connect to %s: %w", host, originalErr)

// Custom error type
type NotFoundError struct {
    Resource string
    ID       string
}

func (e *NotFoundError) Error() string {
    return fmt.Sprintf("%s not found: %s", e.Resource, e.ID)
}

// Return custom error
func getPod(id string) (*Pod, error) {
    pod := findPod(id)
    if pod == nil {
        return nil, &NotFoundError{Resource: "Pod", ID: id}
    }
    return pod, nil
}
```

---

## 🎯 Error Wrapping

```go
// Wrap errors with context
func deployService(name string) error {
    if err := pullImage(name); err != nil {
        return fmt.Errorf("deploy %s: %w", name, err)
    }
    return nil
}

// Check wrapped errors
if errors.Is(err, os.ErrNotExist) {
    fmt.Println("File not found")
}

// Get underlying error type
var notFound *NotFoundError
if errors.As(err, &notFound) {
    fmt.Printf("Resource: %s\\n", notFound.Resource)
}
```

---

## 🔧 Sentinel Errors

```go
// Define sentinel errors
var (
    ErrNotFound     = errors.New("resource not found")
    ErrUnauthorized = errors.New("unauthorized")
    ErrTimeout      = errors.New("operation timed out")
)

// Use in functions
func getResource(id string) (*Resource, error) {
    if !exists(id) {
        return nil, ErrNotFound
    }
    return resource, nil
}

// Check
if err == ErrNotFound {
    // Handle not found
}
```

---

## 🔥 Pro Tips

### 1. Add Context
```go
// Wrap with context
return fmt.Errorf("creating pod %s: %w", name, err)
```

### 2. Don't Ignore Errors
```go
// Bad
data, _ := readFile(path)

// Good
data, err := readFile(path)
if err != nil {
    return err
}
```

---

## 🛠️ Hands-on Exercise

Create error handling for a deploy function:
1. Custom DeployError type
2. Wrap underlying errors
3. Check error types

---

## 📚 Resources

- [Go Error Handling](https://go.dev/blog/error-handling-and-go)
""",
    "xp_reward": 200,
    "estimated_time": "35 minutes",
    "difficulty": "intermediate",
    "order_index": 7,
    "tags": ["go", "errors", "error-handling", "patterns"],
}


# ============================================================================
# BLOCK 8: GOROUTINES (Node 8)
# ============================================================================

GO_NODE_08_GOROUTINES = {
    "id": "go-08-goroutines",
    "title": "Goroutines",
    "description": "Write concurrent code with goroutines",
    "content": """
# Goroutines

> *"Goroutines are lightweight threads—spin up thousands without worry."*

---

## 🎯 Why This Matters

Concurrency is essential for:
- Parallel API calls
- Background tasks
- Handling multiple connections

---

## 💡 Basic Goroutines

```go
// Start a goroutine
func main() {
    go sayHello()  // Runs concurrently
    
    // Main continues
    fmt.Println("Main running")
    
    // Wait (crude way)
    time.Sleep(time.Second)
}

func sayHello() {
    fmt.Println("Hello from goroutine!")
}
```

---

## 🔧 Anonymous Goroutines

```go
// Inline goroutine
go func() {
    fmt.Println("Anonymous goroutine")
}()

// With parameters
name := "deploy"
go func(n string) {
    fmt.Printf("Running %s\\n", n)
}(name)  // Pass value, don't capture
```

---

## 🎯 WaitGroup

```go
import "sync"

func main() {
    var wg sync.WaitGroup
    
    services := []string{"api", "web", "worker"}
    
    for _, svc := range services {
        wg.Add(1)
        go func(name string) {
            defer wg.Done()
            deploy(name)
        }(svc)
    }
    
    wg.Wait()  // Wait for all
    fmt.Println("All deployed!")
}

func deploy(name string) {
    fmt.Printf("Deploying %s...\\n", name)
    time.Sleep(time.Second)
}
```

---

## 🔧 Common Pattern

```go
// Process items concurrently
func processAll(items []string) {
    var wg sync.WaitGroup
    
    for _, item := range items {
        wg.Add(1)
        go func(i string) {
            defer wg.Done()
            process(i)
        }(item)
    }
    
    wg.Wait()
}
```

---

## 🔥 Pro Tips

### 1. Always Pass Values
```go
// Wrong - captures loop variable
for _, s := range services {
    go func() {
        fmt.Println(s)  // Race condition!
    }()
}

// Correct
for _, s := range services {
    go func(svc string) {
        fmt.Println(svc)
    }(s)
}
```

### 2. Use WaitGroup for Sync
```go
var wg sync.WaitGroup
wg.Add(n)
// ... spawn goroutines
wg.Wait()
```

---

## 🛠️ Hands-on Exercise

Deploy 5 services concurrently:
1. Use WaitGroup
2. Simulate deploy time
3. Print when all done

---

## 📚 Resources

- [Go Concurrency](https://go.dev/tour/concurrency/1)
""",
    "xp_reward": 225,
    "estimated_time": "40 minutes",
    "difficulty": "intermediate",
    "order_index": 8,
    "tags": ["go", "goroutines", "concurrency", "async"],
}


# ============================================================================
# BLOCK 9: CHANNELS (Node 9)
# ============================================================================

GO_NODE_09_CHANNELS = {
    "id": "go-09-channels",
    "title": "Channels",
    "description": "Communicate between goroutines with channels",
    "content": """
# Channels

> *"Don't communicate by sharing memory; share memory by communicating."*

---

## 🎯 Why This Matters

Channels enable:
- Safe communication between goroutines
- Synchronization
- Fan-out/fan-in patterns

---

## 💡 Basic Channels

```go
// Create channel
ch := make(chan string)

// Send to channel
go func() {
    ch <- "Hello"
}()

// Receive from channel
msg := <-ch
fmt.Println(msg)
```

---

## 🔧 Buffered Channels

```go
// Unbuffered - blocks until received
ch := make(chan int)

// Buffered - holds n items
ch := make(chan int, 3)

ch <- 1  // Non-blocking
ch <- 2
ch <- 3
ch <- 4  // Blocks! Buffer full
```

---

## 🎯 Range & Close

```go
func main() {
    ch := make(chan string)
    
    go func() {
        pods := []string{"pod-1", "pod-2", "pod-3"}
        for _, p := range pods {
            ch <- p
        }
        close(ch)  // Signal done
    }()
    
    // Range receives until closed
    for pod := range ch {
        fmt.Println("Received:", pod)
    }
}
```

---

## 🔧 Select Statement

```go
func main() {
    ch1 := make(chan string)
    ch2 := make(chan string)
    
    go func() {
        time.Sleep(time.Second)
        ch1 <- "one"
    }()
    
    go func() {
        time.Sleep(2 * time.Second)
        ch2 <- "two"
    }()
    
    // Wait for first result
    select {
    case msg := <-ch1:
        fmt.Println(msg)
    case msg := <-ch2:
        fmt.Println(msg)
    case <-time.After(3 * time.Second):
        fmt.Println("timeout")
    }
}
```

---

## 🔥 Pro Tips

### 1. Close Only From Sender
```go
// Sender closes
go func() {
    defer close(ch)
    for _, item := range items {
        ch <- item
    }
}()
```

### 2. Check If Closed
```go
val, ok := <-ch
if !ok {
    fmt.Println("Channel closed")
}
```

---

## 🛠️ Hands-on Exercise

Create a pipeline:
1. Generate numbers
2. Square them
3. Print results
Using 3 goroutines and channels

---

## 📚 Resources

- [Go Channels](https://go.dev/tour/concurrency/2)
""",
    "xp_reward": 225,
    "estimated_time": "40 minutes",
    "difficulty": "intermediate",
    "order_index": 9,
    "tags": ["go", "channels", "concurrency", "communication"],
}


# ============================================================================
# BLOCK 10: PACKAGES (Node 10)
# ============================================================================

GO_NODE_10_PACKAGES = {
    "id": "go-10-packages",
    "title": "Packages & Modules",
    "description": "Organize Go code with packages and modules",
    "content": """
# Packages & Modules

> *"Well-organized packages make code reusable and maintainable."*

---

## 🎯 Why This Matters

Good structure:
- Reusable code
- Clear dependencies
- Easy testing

---

## 💡 Package Basics

```
myproject/
├── go.mod
├── main.go
├── internal/
│   └── config/
│       └── config.go
└── pkg/
    └── k8s/
        └── client.go
```

```go
// main.go
package main

import (
    "myproject/internal/config"
    "myproject/pkg/k8s"
)

// pkg/k8s/client.go
package k8s

func NewClient() *Client {
    return &Client{}
}
```

---

## 🔧 Go Modules

```bash
# Initialize module
go mod init github.com/user/project

# Add dependency
go get github.com/spf13/cobra

# Update dependencies
go mod tidy

# Download all
go mod download
```

---

## 🎯 Visibility Rules

```go
// Exported (Public) - Capitalized
func GetPods() []Pod { }
type Client struct { }

// Unexported (Private) - lowercase
func getPods() []Pod { }
type client struct { }
```

---

## 🔧 Project Layout

```
cmd/           - Entry points
├── server/
│   └── main.go
└── cli/
    └── main.go

internal/      - Private packages
├── config/
└── handlers/

pkg/           - Public packages
├── api/
└── client/

go.mod
go.sum
```

---

## 🔥 Pro Tips

### 1. Use internal/
```
internal/ packages can't be imported
from outside your module
```

### 2. Minimize Dependencies
```bash
go mod why -m <module>
```

---

## 🛠️ Hands-on Exercise

Create a project with:
1. cmd/cli/main.go
2. internal/config/
3. pkg/deployer/

---

## 📚 Resources

- [Go Modules](https://go.dev/ref/mod)
""",
    "xp_reward": 175,
    "estimated_time": "30 minutes",
    "difficulty": "intermediate",
    "order_index": 10,
    "tags": ["go", "packages", "modules", "structure"],
}


# ============================================================================
# SKILLSMAP DEFINITION (Block 1 only)
# ============================================================================

def get_go_skillsmap() -> dict[str, Any]:
    """Return the Go SkillsMap definition."""
    return {
        "id": "go",
        "name": "Go for DevOps",
        "slug": "go",
        "description": "Master Go for building DevOps tools and infrastructure",
        "icon": "go",
        "color": "#00ADD8",  # Go cyan
        "estimated_hours": 25,
        "difficulty": "intermediate",
        "prerequisites": ["linux"],
        "tags": ["go", "golang", "devops", "tools"],
        "nodes": [
            GO_NODE_01_INTRODUCTION,
            GO_NODE_02_VARIABLES,
            GO_NODE_03_CONTROL_FLOW,
            GO_NODE_04_FUNCTIONS,
            GO_NODE_05_STRUCTS,
            GO_NODE_06_INTERFACES,
            GO_NODE_07_ERROR_HANDLING,
            GO_NODE_08_GOROUTINES,
            GO_NODE_09_CHANNELS,
            GO_NODE_10_PACKAGES,
            # Blocks 11-20: Coming next
        ],
    }


# Export for seeding
GO_SKILLSMAP = get_go_skillsmap()
