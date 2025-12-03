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
# BLOCK 11: TESTING (Node 11)
# ============================================================================

GO_NODE_11_TESTING = {
    "id": "go-11-testing",
    "title": "Testing",
    "description": "Write tests with Go's built-in testing package",
    "content": """
# Testing

> *"Go has testing built-in—no external frameworks needed."*

---

## 🎯 Why This Matters

Tests ensure reliability:
- Catch bugs early
- Safe refactoring
- Documentation through tests

---

## 💡 Basic Tests

```go
// math.go
package math

func Add(a, b int) int {
    return a + b
}

// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    if result != 5 {
        t.Errorf("Add(2,3) = %d; want 5", result)
    }
}
```

```bash
go test ./...
go test -v ./...
go test -cover ./...
```

---

## 🔧 Table-Driven Tests

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.expected {
                t.Errorf("got %d, want %d", got, tt.expected)
            }
        })
    }
}
```

---

## 🎯 Test Helpers

```go
func TestDeploy(t *testing.T) {
    // Skip in short mode
    if testing.Short() {
        t.Skip("skipping integration test")
    }

    // Cleanup
    t.Cleanup(func() {
        cleanupResources()
    })

    // Parallel tests
    t.Parallel()
}
```

---

## 🔥 Pro Tips

### 1. Use testify
```go
import "github.com/stretchr/testify/assert"

func TestAdd(t *testing.T) {
    assert.Equal(t, 5, Add(2, 3))
}
```

### 2. Run Specific Test
```bash
go test -run TestAdd ./...
```

---

## 🛠️ Hands-on Exercise

Write tests for a deploy function:
1. Table-driven tests
2. Test error cases
3. Run with coverage

---

## 📚 Resources

- [Go Testing](https://go.dev/doc/tutorial/add-a-test)
""",
    "xp_reward": 200,
    "estimated_time": "35 minutes",
    "difficulty": "intermediate",
    "order_index": 11,
    "tags": ["go", "testing", "unit-tests", "tdd"],
}


# ============================================================================
# BLOCK 12: HTTP (Node 12)
# ============================================================================

GO_NODE_12_HTTP = {
    "id": "go-12-http",
    "title": "HTTP Servers & Clients",
    "description": "Build HTTP APIs and clients in Go",
    "content": """
# HTTP Servers & Clients

> *"Go's net/http is production-ready out of the box."*

---

## 🎯 Why This Matters

HTTP is everywhere:
- REST APIs
- Health checks
- Webhooks
- Metrics endpoints

---

## 💡 HTTP Server

```go
package main

import (
    "encoding/json"
    "net/http"
)

func main() {
    http.HandleFunc("/health", healthHandler)
    http.HandleFunc("/api/pods", podsHandler)

    http.ListenAndServe(":8080", nil)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("OK"))
}

func podsHandler(w http.ResponseWriter, r *http.Request) {
    pods := []string{"pod-1", "pod-2"}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(pods)
}
```

---

## 🔧 HTTP Client

```go
import (
    "io"
    "net/http"
    "time"
)

// Create client with timeout
client := &http.Client{
    Timeout: 10 * time.Second,
}

// GET request
resp, err := client.Get("http://api.example.com/pods")
if err != nil {
    log.Fatal(err)
}
defer resp.Body.Close()

body, _ := io.ReadAll(resp.Body)
fmt.Println(string(body))

// POST request
data := bytes.NewBuffer([]byte(`{"name":"nginx"}`))
resp, err := client.Post(
    "http://api.example.com/pods",
    "application/json",
    data,
)
```

---

## 🎯 Middleware

```go
func loggingMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s", r.Method, r.URL.Path)
        next.ServeHTTP(w, r)
    })
}

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/api/", apiHandler)

    handler := loggingMiddleware(mux)
    http.ListenAndServe(":8080", handler)
}
```

---

## 🔥 Pro Tips

### 1. Always Set Timeouts
```go
server := &http.Server{
    Addr:         ":8080",
    ReadTimeout:  5 * time.Second,
    WriteTimeout: 10 * time.Second,
}
```

### 2. Graceful Shutdown
```go
go server.ListenAndServe()
<-quit
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
server.Shutdown(ctx)
```

---

## 🛠️ Hands-on Exercise

Build a simple API:
1. /health endpoint
2. /api/services GET
3. /api/deploy POST

---

## 📚 Resources

- [Go HTTP](https://pkg.go.dev/net/http)
""",
    "xp_reward": 200,
    "estimated_time": "35 minutes",
    "difficulty": "intermediate",
    "order_index": 12,
    "tags": ["go", "http", "api", "server"],
}


# ============================================================================
# BLOCK 13: JSON (Node 13)
# ============================================================================

GO_NODE_13_JSON = {
    "id": "go-13-json",
    "title": "JSON & YAML",
    "description": "Parse and generate JSON/YAML in Go",
    "content": """
# JSON & YAML

> *"JSON tags on structs make serialization effortless."*

---

## 🎯 Why This Matters

Config and API data:
- Kubernetes manifests
- API responses
- Configuration files

---

## 💡 JSON Encoding

```go
import "encoding/json"

type Pod struct {
    Name      string `json:"name"`
    Namespace string `json:"namespace"`
    Replicas  int    `json:"replicas,omitempty"`
}

// Struct to JSON
pod := Pod{Name: "nginx", Namespace: "default"}
data, err := json.Marshal(pod)
// {"name":"nginx","namespace":"default"}

// Pretty print
data, _ := json.MarshalIndent(pod, "", "  ")
```

---

## 🔧 JSON Decoding

```go
jsonStr := `{"name":"nginx","namespace":"default"}`

var pod Pod
err := json.Unmarshal([]byte(jsonStr), &pod)
if err != nil {
    log.Fatal(err)
}
fmt.Println(pod.Name)  // nginx

// From reader
decoder := json.NewDecoder(r.Body)
err := decoder.Decode(&pod)
```

---

## 🎯 YAML (with gopkg.in/yaml.v3)

```go
import "gopkg.in/yaml.v3"

type Deployment struct {
    APIVersion string `yaml:"apiVersion"`
    Kind       string `yaml:"kind"`
    Metadata   struct {
        Name string `yaml:"name"`
    } `yaml:"metadata"`
}

// Parse YAML
yamlStr := `
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
`

var dep Deployment
yaml.Unmarshal([]byte(yamlStr), &dep)

// Generate YAML
data, _ := yaml.Marshal(dep)
```

---

## 🔧 Dynamic JSON

```go
// Unknown structure
var data map[string]interface{}
json.Unmarshal(jsonBytes, &data)

// Access dynamically
name := data["name"].(string)

// json.RawMessage for delayed parsing
type Response struct {
    Type string          `json:"type"`
    Data json.RawMessage `json:"data"`
}
```

---

## 🔥 Pro Tips

### 1. Use omitempty
```go
type Config struct {
    Host    string `json:"host"`
    Port    int    `json:"port,omitempty"`
    Timeout int    `json:"timeout,omitempty"`
}
```

### 2. Custom Marshal
```go
func (t Time) MarshalJSON() ([]byte, error) {
    return []byte(t.Format(`"2006-01-02"`)), nil
}
```

---

## 🛠️ Hands-on Exercise

1. Parse a K8s deployment YAML
2. Modify replicas
3. Output as JSON

---

## 📚 Resources

- [Go JSON](https://go.dev/blog/json)
""",
    "xp_reward": 175,
    "estimated_time": "30 minutes",
    "difficulty": "intermediate",
    "order_index": 13,
    "tags": ["go", "json", "yaml", "serialization"],
}


# ============================================================================
# BLOCK 14: CLI TOOLS (Node 14)
# ============================================================================

GO_NODE_14_CLI = {
    "id": "go-14-cli",
    "title": "CLI Tools",
    "description": "Build command-line tools with Cobra",
    "content": """
# CLI Tools

> *"kubectl, docker, terraform—all built with Go CLI frameworks."*

---

## 🎯 Why This Matters

CLI tools are DevOps bread and butter:
- Automation scripts
- Developer tools
- Admin utilities

---

## 💡 Basic CLI with Cobra

```go
package main

import (
    "fmt"
    "github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
    Use:   "devops",
    Short: "DevOps CLI tool",
}

var deployCmd = &cobra.Command{
    Use:   "deploy [service]",
    Short: "Deploy a service",
    Args:  cobra.ExactArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
        env, _ := cmd.Flags().GetString("env")
        fmt.Printf("Deploying %s to %s\\n", args[0], env)
    },
}

func init() {
    deployCmd.Flags().StringP("env", "e", "dev", "Environment")
    rootCmd.AddCommand(deployCmd)
}

func main() {
    rootCmd.Execute()
}
```

```bash
./devops deploy api --env prod
```

---

## 🔧 Subcommands

```go
// devops get pods
// devops get services

var getCmd = &cobra.Command{
    Use:   "get",
    Short: "Get resources",
}

var getPodsCmd = &cobra.Command{
    Use:   "pods",
    Short: "Get pods",
    Run: func(cmd *cobra.Command, args []string) {
        // List pods
    },
}

func init() {
    getCmd.AddCommand(getPodsCmd)
    rootCmd.AddCommand(getCmd)
}
```

---

## 🎯 Flags & Config

```go
var cfgFile string

func init() {
    // Persistent flags (all commands)
    rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file")

    // Local flags (this command only)
    deployCmd.Flags().IntP("replicas", "r", 1, "Number of replicas")

    // Required flag
    deployCmd.MarkFlagRequired("env")
}
```

---

## 🔧 Output Formatting

```go
import "github.com/olekukonko/tablewriter"

func printTable(pods []Pod) {
    table := tablewriter.NewWriter(os.Stdout)
    table.SetHeader([]string{"Name", "Status", "Age"})

    for _, p := range pods {
        table.Append([]string{p.Name, p.Status, p.Age})
    }

    table.Render()
}
```

---

## 🔥 Pro Tips

### 1. Use Viper for Config
```go
import "github.com/spf13/viper"

viper.SetConfigName("config")
viper.AddConfigPath(".")
viper.ReadInConfig()
host := viper.GetString("host")
```

### 2. Add Completion
```go
rootCmd.AddCommand(completionCmd)
// ./devops completion bash
```

---

## 🛠️ Hands-on Exercise

Build a CLI with:
1. deploy <service>
2. status <service>
3. logs <service> --tail

---

## 📚 Resources

- [Cobra](https://github.com/spf13/cobra)
""",
    "xp_reward": 225,
    "estimated_time": "40 minutes",
    "difficulty": "intermediate",
    "order_index": 14,
    "tags": ["go", "cli", "cobra", "tools"],
}


# ============================================================================
# BLOCK 15: FILES (Node 15)
# ============================================================================

GO_NODE_15_FILES = {
    "id": "go-15-files",
    "title": "File Operations",
    "description": "Read, write, and manipulate files in Go",
    "content": """
# File Operations

> *"Go makes file I/O simple and safe with defer."*

---

## 🎯 Why This Matters

File operations are core to DevOps:
- Config files
- Log processing
- Data transformation

---

## 💡 Reading Files

```go
import (
    "os"
    "io"
    "bufio"
)

// Read entire file
data, err := os.ReadFile("config.yaml")
if err != nil {
    log.Fatal(err)
}
fmt.Println(string(data))

// Read line by line
file, _ := os.Open("logs.txt")
defer file.Close()

scanner := bufio.NewScanner(file)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
```

---

## 🔧 Writing Files

```go
// Write entire file
content := []byte("apiVersion: v1")
err := os.WriteFile("output.yaml", content, 0644)

// Write with file handle
file, err := os.Create("output.txt")
if err != nil {
    log.Fatal(err)
}
defer file.Close()

file.WriteString("Hello\\n")
file.Write([]byte("World"))
```

---

## 🎯 File Info & Directories

```go
// Check if exists
if _, err := os.Stat("config.yaml"); os.IsNotExist(err) {
    fmt.Println("File not found")
}

// Create directory
os.MkdirAll("output/logs", 0755)

// List directory
entries, _ := os.ReadDir(".")
for _, e := range entries {
    fmt.Println(e.Name())
}

// Walk directory tree
filepath.Walk(".", func(path string, info os.FileInfo, err error) error {
    if !info.IsDir() && strings.HasSuffix(path, ".yaml") {
        fmt.Println(path)
    }
    return nil
})
```

---

## 🔧 Temp Files

```go
// Create temp file
tmpFile, err := os.CreateTemp("", "deploy-*.yaml")
if err != nil {
    log.Fatal(err)
}
defer os.Remove(tmpFile.Name())

tmpFile.WriteString("content")
```

---

## 🔥 Pro Tips

### 1. Always Use defer
```go
f, err := os.Open(path)
if err != nil {
    return err
}
defer f.Close()  // Always runs
```

### 2. Check Errors
```go
if err := os.WriteFile(path, data, 0644); err != nil {
    return fmt.Errorf("write %s: %w", path, err)
}
```

---

## 🛠️ Hands-on Exercise

1. Read all YAML files in a directory
2. Modify a field
3. Write to new files

---

## 📚 Resources

- [Go os package](https://pkg.go.dev/os)
""",
    "xp_reward": 175,
    "estimated_time": "30 minutes",
    "difficulty": "intermediate",
    "order_index": 15,
    "tags": ["go", "files", "io", "filesystem"],
}


# ============================================================================
# BLOCK 16: CONCURRENCY PATTERNS (Node 16)
# ============================================================================

GO_NODE_16_CONCURRENCY = {
    "id": "go-16-concurrency-patterns",
    "title": "Concurrency Patterns",
    "description": "Master advanced concurrency patterns in Go",
    "content": """
# Concurrency Patterns

> *"Worker pools, fan-out/fan-in—Go makes concurrency patterns elegant."*

---

## 🎯 Why This Matters

Scale your tools:
- Parallel deployments
- Concurrent health checks
- Batch processing

---

## 💡 Worker Pool

```go
func workerPool(jobs <-chan Job, results chan<- Result, workers int) {
    var wg sync.WaitGroup

    for i := 0; i < workers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for job := range jobs {
                results <- process(job)
            }
        }()
    }

    wg.Wait()
    close(results)
}
```

---

## 🔧 Fan-Out/Fan-In

```go
func fanOut(input <-chan int, n int) []<-chan int {
    outputs := make([]<-chan int, n)
    for i := 0; i < n; i++ {
        outputs[i] = worker(input)
    }
    return outputs
}

func fanIn(inputs ...<-chan int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup

    for _, in := range inputs {
        wg.Add(1)
        go func(ch <-chan int) {
            defer wg.Done()
            for v := range ch {
                out <- v
            }
        }(in)
    }

    go func() {
        wg.Wait()
        close(out)
    }()

    return out
}
```

---

## 🎯 Rate Limiting

```go
func rateLimited(requests <-chan Request) {
    limiter := time.NewTicker(100 * time.Millisecond)
    defer limiter.Stop()

    for req := range requests {
        <-limiter.C  // Wait for tick
        go process(req)
    }
}
```

---

## 🔥 Pro Tips

### 1. Use errgroup
```go
import "golang.org/x/sync/errgroup"

g, ctx := errgroup.WithContext(ctx)
for _, svc := range services {
    svc := svc
    g.Go(func() error {
        return deploy(ctx, svc)
    })
}
return g.Wait()
```

---

## 🛠️ Hands-on Exercise

Create a parallel deployer:
1. Worker pool for deployments
2. Rate limiting
3. Collect results

---

## 📚 Resources

- [Go Concurrency Patterns](https://go.dev/blog/pipelines)
""",
    "xp_reward": 250,
    "estimated_time": "45 minutes",
    "difficulty": "advanced",
    "order_index": 16,
    "tags": ["go", "concurrency", "patterns", "goroutines"],
}


# ============================================================================
# BLOCK 17: CONTEXT (Node 17)
# ============================================================================

GO_NODE_17_CONTEXT = {
    "id": "go-17-context",
    "title": "Context",
    "description": "Manage timeouts and cancellation with context",
    "content": """
# Context

> *"Context carries deadlines and cancellation signals across API boundaries."*

---

## 🎯 Why This Matters

Context enables:
- Timeout propagation
- Request cancellation
- Graceful shutdown

---

## 💡 Basic Context

```go
import "context"

// With timeout
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

// With cancel
ctx, cancel := context.WithCancel(context.Background())
defer cancel()

// Check if done
select {
case <-ctx.Done():
    return ctx.Err()
default:
    // Continue work
}
```

---

## 🔧 Using Context

```go
func deploy(ctx context.Context, name string) error {
    // Check if cancelled
    if ctx.Err() != nil {
        return ctx.Err()
    }

    // Make HTTP request with context
    req, _ := http.NewRequestWithContext(ctx, "POST", url, body)
    resp, err := client.Do(req)

    // Long operation with context
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        default:
            // Do work
        }
    }
}
```

---

## 🎯 Context Values

```go
// Define key type
type ctxKey string
const requestIDKey ctxKey = "requestID"

// Set value
ctx := context.WithValue(ctx, requestIDKey, "abc123")

// Get value
if id, ok := ctx.Value(requestIDKey).(string); ok {
    log.Printf("Request ID: %s", id)
}
```

---

## 🔧 HTTP with Context

```go
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()

    result, err := fetchData(ctx)
    if err == context.Canceled {
        return  // Client disconnected
    }
    if err == context.DeadlineExceeded {
        http.Error(w, "Timeout", 504)
        return
    }
}
```

---

## 🔥 Pro Tips

### 1. Always Pass Context First
```go
func DoWork(ctx context.Context, args ...any) error
```

### 2. Don't Store in Structs
```go
// Pass through function calls instead
```

---

## 🛠️ Hands-on Exercise

1. Create a deployer with timeout
2. Cancel on SIGINT
3. Propagate context to workers

---

## 📚 Resources

- [Go Context](https://pkg.go.dev/context)
""",
    "xp_reward": 200,
    "estimated_time": "35 minutes",
    "difficulty": "intermediate",
    "order_index": 17,
    "tags": ["go", "context", "timeout", "cancellation"],
}


# ============================================================================
# BLOCK 18: GO MODULES (Node 18)
# ============================================================================

GO_NODE_18_MODULES = {
    "id": "go-18-modules",
    "title": "Go Modules Deep Dive",
    "description": "Master Go module management and dependency handling",
    "content": """
# Go Modules Deep Dive

> *"go.mod is your project's DNA—manage it carefully."*

---

## 🎯 Why This Matters

Professional Go projects need:
- Reproducible builds
- Version control
- Dependency management

---

## 💡 go.mod Basics

```go
// go.mod
module github.com/myorg/devops-tool

go 1.21

require (
    github.com/spf13/cobra v1.7.0
    github.com/spf13/viper v1.16.0
    k8s.io/client-go v0.28.0
)

require (
    // Indirect dependencies
    github.com/inconshreveable/mousetrap v1.1.0 // indirect
)
```

---

## 🔧 Module Commands

```bash
# Initialize
go mod init github.com/user/project

# Add dependency
go get github.com/spf13/cobra@latest
go get github.com/spf13/cobra@v1.7.0

# Update all
go get -u ./...

# Clean up
go mod tidy

# Download
go mod download

# Verify
go mod verify

# Why is this here?
go mod why -m k8s.io/api
```

---

## 🎯 Version Selection

```bash
# Get specific version
go get github.com/pkg@v1.2.3

# Get latest
go get github.com/pkg@latest

# Get from branch
go get github.com/pkg@main

# Get from commit
go get github.com/pkg@abc123
```

---

## 🔧 Vendoring

```bash
# Create vendor directory
go mod vendor

# Build with vendor
go build -mod=vendor ./...

# Verify vendor
go mod verify
```

---

## 🔥 Pro Tips

### 1. Use go.sum
```bash
# Always commit go.sum
git add go.mod go.sum
```

### 2. Replace for Local Dev
```go
// go.mod
replace github.com/myorg/shared => ../shared
```

---

## 🛠️ Hands-on Exercise

1. Create a new module
2. Add 3 dependencies
3. Create and test vendor

---

## 📚 Resources

- [Go Modules Ref](https://go.dev/ref/mod)
""",
    "xp_reward": 175,
    "estimated_time": "30 minutes",
    "difficulty": "intermediate",
    "order_index": 18,
    "tags": ["go", "modules", "dependencies", "versioning"],
}


# ============================================================================
# BLOCK 19: DEVOPS TOOLS (Node 19)
# ============================================================================

GO_NODE_19_DEVOPS = {
    "id": "go-19-devops-tools",
    "title": "Building DevOps Tools",
    "description": "Create production-ready DevOps utilities in Go",
    "content": """
# Building DevOps Tools

> *"Go is THE language for DevOps tooling. Docker, K8s, Terraform—all Go."*

---

## 🎯 Why This Matters

Build tools like the pros:
- Single binary distribution
- Cross-platform
- High performance

---

## 💡 K8s Client Example

```go
import (
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
)

func main() {
    config, err := clientcmd.BuildConfigFromFlags("",
        os.Getenv("HOME")+"/.kube/config")
    if err != nil {
        log.Fatal(err)
    }

    client, err := kubernetes.NewForConfig(config)
    if err != nil {
        log.Fatal(err)
    }

    pods, err := client.CoreV1().Pods("default").
        List(context.TODO(), metav1.ListOptions{})

    for _, pod := range pods.Items {
        fmt.Printf("%s: %s\\n", pod.Name, pod.Status.Phase)
    }
}
```

---

## 🔧 Docker Client

```go
import (
    "github.com/docker/docker/client"
    "github.com/docker/docker/api/types"
)

func listContainers() {
    cli, _ := client.NewClientWithOpts(client.FromEnv)

    containers, _ := cli.ContainerList(
        context.Background(),
        types.ContainerListOptions{},
    )

    for _, c := range containers {
        fmt.Printf("%s: %s\\n", c.Names[0], c.State)
    }
}
```

---

## 🎯 Health Check Service

```go
type HealthChecker struct {
    targets []string
    client  *http.Client
}

func (h *HealthChecker) CheckAll(ctx context.Context) []Result {
    results := make(chan Result, len(h.targets))
    var wg sync.WaitGroup

    for _, target := range h.targets {
        wg.Add(1)
        go func(url string) {
            defer wg.Done()
            results <- h.check(ctx, url)
        }(target)
    }

    wg.Wait()
    close(results)

    var all []Result
    for r := range results {
        all = append(all, r)
    }
    return all
}
```

---

## 🔥 Pro Tips

### 1. Cross-Compile
```bash
GOOS=linux GOARCH=amd64 go build -o tool-linux
GOOS=darwin GOARCH=arm64 go build -o tool-mac
```

### 2. Embed Version
```bash
go build -ldflags "-X main.version=1.0.0"
```

---

## 🛠️ Hands-on Exercise

Build a health checker:
1. Check multiple URLs
2. Concurrent checks
3. JSON output

---

## 📚 Resources

- [client-go](https://github.com/kubernetes/client-go)
""",
    "xp_reward": 250,
    "estimated_time": "45 minutes",
    "difficulty": "advanced",
    "order_index": 19,
    "tags": ["go", "devops", "kubernetes", "docker"],
}


# ============================================================================
# BLOCK 20: CAPSTONE (Node 20)
# ============================================================================

GO_NODE_20_CAPSTONE = {
    "id": "go-20-capstone",
    "title": "Go DevOps Capstone",
    "description": "Build a complete DevOps automation tool in Go",
    "content": """
# Go DevOps Capstone

> *"Combine everything you've learned into a production-ready tool."*

---

## 🎯 Project Overview

Build **DevOps Commander** - a CLI tool that:
- Deploys services to Kubernetes
- Monitors health endpoints
- Manages configuration

---

## 💡 Project Structure

```
devops-cmd/
├── cmd/
│   └── root.go
│   └── deploy.go
│   └── status.go
├── internal/
│   ├── k8s/
│   │   └── client.go
│   ├── health/
│   │   └── checker.go
│   └── config/
│       └── loader.go
├── pkg/
│   └── types/
│       └── types.go
├── main.go
├── go.mod
└── Makefile
```

---

## 🔧 Core Implementation

```go
// cmd/deploy.go
var deployCmd = &cobra.Command{
    Use:   "deploy [service]",
    Short: "Deploy a service",
    RunE: func(cmd *cobra.Command, args []string) error {
        ctx, cancel := context.WithTimeout(
            context.Background(),
            timeout,
        )
        defer cancel()

        client, err := k8s.NewClient(kubeconfig)
        if err != nil {
            return err
        }

        return client.Deploy(ctx, &types.DeployRequest{
            Service:   args[0],
            Namespace: namespace,
            Replicas:  replicas,
            Image:     image,
        })
    },
}
```

---

## 🎯 Requirements

### 1. CLI Commands
- `deploy <service>` - Deploy with options
- `status [service]` - Show status
- `health` - Check all endpoints

### 2. Features
- Context with timeout
- Graceful shutdown (SIGINT)
- JSON/table output formats
- Config file support

### 3. Code Quality
- Unit tests (80%+ coverage)
- Error handling
- Logging with levels

---

## 🔧 Makefile

```makefile
.PHONY: build test lint

build:
	go build -ldflags "-X main.version=$(VERSION)" -o bin/devops-cmd

test:
	go test -v -cover ./...

lint:
	golangci-lint run

release:
	GOOS=linux GOARCH=amd64 go build -o bin/devops-cmd-linux
	GOOS=darwin GOARCH=arm64 go build -o bin/devops-cmd-darwin
```

---

## 🔥 Success Criteria

- [ ] All commands work
- [ ] Tests pass with 80%+ coverage
- [ ] Cross-compiles successfully
- [ ] Config file support
- [ ] Graceful shutdown

---

## 🏆 Congratulations!

You've mastered Go for DevOps:
- Concurrency patterns
- CLI development
- K8s/Docker integration
- Professional project structure

**You're ready to build production tools!**
""",
    "xp_reward": 300,
    "estimated_time": "90 minutes",
    "difficulty": "advanced",
    "order_index": 20,
    "tags": ["go", "capstone", "project", "devops"],
}


# ============================================================================
# SKILLSMAP DEFINITION (Complete - All 20 Blocks)
# ============================================================================
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
            GO_NODE_11_TESTING,
            GO_NODE_12_HTTP,
            GO_NODE_13_JSON,
            GO_NODE_14_CLI,
            GO_NODE_15_FILES,
            GO_NODE_16_CONCURRENCY,
            GO_NODE_17_CONTEXT,
            GO_NODE_18_MODULES,
            GO_NODE_19_DEVOPS,
            GO_NODE_20_CAPSTONE,
        ],
    }


# Export for seeding
GO_SKILLSMAP = get_go_skillsmap()
