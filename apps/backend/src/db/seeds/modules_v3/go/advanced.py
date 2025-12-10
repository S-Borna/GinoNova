"""
Go Advanced - Tasks 11-20 (DevOps Focus)
Premium Bootcamp-Quality Content
"""

TASKS_ADVANCED = [
    {
        "title": "Go for DevOps - CLI Tools",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 🛠️ Go for DevOps - CLI Tools

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
- Bygga CLI-verktyg med Cobra
- Hantera flags och arguments
- Skapa interaktiva prompts
- Distribuera cross-platform binaries

---

## 📖 CLI med Cobra

```go
// Installation
// go get -u github.com/spf13/cobra@latest

package main

import (
    "fmt"
    "os"

    "github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
    Use:   "devops-cli",
    Short: "A DevOps CLI tool",
    Long:  `A comprehensive CLI for DevOps operations.`,
}

var deployCmd = &cobra.Command{
    Use:   "deploy [environment]",
    Short: "Deploy to environment",
    Args:  cobra.ExactArgs(1),
    Run: func(cmd *cobra.Command, args []string) {
        env := args[0]
        force, _ := cmd.Flags().GetBool("force")
        fmt.Printf("Deploying to %s (force=%v)\n", env, force)
    },
}

func init() {
    deployCmd.Flags().BoolP("force", "f", false, "Force deployment")
    rootCmd.AddCommand(deployCmd)
}

func main() {
    if err := rootCmd.Execute(); err != nil {
        os.Exit(1)
    }
}
```

---

## 🏗️ Projekt Struktur

```
devops-cli/
+-- cmd/
|   +-- root.go
|   +-- deploy.go
|   +-- status.go
|   +-- config.go
+-- internal/
|   +-- deploy/
|   +-- config/
+-- main.go
+-- go.mod
```

---

## 🔧 Cross-Platform Build

```bash
# Build för olika plattformar
GOOS=linux GOARCH=amd64 go build -o bin/cli-linux
GOOS=darwin GOARCH=arm64 go build -o bin/cli-macos
GOOS=windows GOARCH=amd64 go build -o bin/cli.exe

# Med ldflags för mindre binary
go build -ldflags="-s -w" -o cli

# Goreleaser för releases
# .goreleaser.yaml
builds:
  - env:
      - CGO_ENABLED=0
    goos:
      - linux
      - darwin
      - windows
```

---

## 🏋️ Övningar

### Övning 1: Status Command
```go
var statusCmd = &cobra.Command{
    Use:   "status",
    Short: "Check service status",
    Run: func(cmd *cobra.Command, args []string) {
        services := []string{"api", "db", "cache"}
        for _, s := range services {
            fmt.Printf("%-10s [OK]\n", s)
        }
    },
}
```

---

## 📚 Sammanfattning

| Verktyg | Användning |
|---------|-----------|
| Cobra | CLI framework |
| Viper | Konfiguration |
| GOOS/GOARCH | Cross-compile |
| ldflags | Optimera binary |

**Nästa steg:** HTTP Servers & APIs

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "HTTP Servers & APIs",
        "difficulty": "hard",
        "estimated_minutes": 60,
        "xp_reward": 165,
        "content": r"""
# 🌐 HTTP Servers & APIs

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
- Bygga HTTP servers med net/http och Gin
- Implementera RESTful APIs
- Hantera middleware
- Validera input

---

## 📖 net/http Basics

```go
package main

import (
    "encoding/json"
    "net/http"
)

func main() {
    http.HandleFunc("/health", healthHandler)
    http.HandleFunc("/api/users", usersHandler)

    http.ListenAndServe(":8080", nil)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("OK"))
}

func usersHandler(w http.ResponseWriter, r *http.Request) {
    switch r.Method {
    case http.MethodGet:
        users := []User{{ID: 1, Name: "Alice"}}
        json.NewEncoder(w).Encode(users)
    case http.MethodPost:
        var user User
        json.NewDecoder(r.Body).Decode(&user)
        json.NewEncoder(w).Encode(user)
    }
}
```

---

## 🚀 Gin Framework

```go
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()

    // Routes
    r.GET("/health", func(c *gin.Context) {
        c.JSON(200, gin.H{"status": "ok"})
    })

    api := r.Group("/api")
    {
        api.GET("/users", getUsers)
        api.POST("/users", createUser)
        api.GET("/users/:id", getUser)
        api.PUT("/users/:id", updateUser)
        api.DELETE("/users/:id", deleteUser)
    }

    r.Run(":8080")
}

func getUser(c *gin.Context) {
    id := c.Param("id")
    c.JSON(200, gin.H{"id": id})
}

func createUser(c *gin.Context) {
    var user User
    if err := c.ShouldBindJSON(&user); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    c.JSON(201, user)
}
```

---

## 🔒 Middleware

```go
// Auth middleware
func AuthMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        token := c.GetHeader("Authorization")
        if token == "" {
            c.AbortWithStatusJSON(401, gin.H{"error": "unauthorized"})
            return
        }
        // Validate token...
        c.Next()
    }
}

// Logging middleware
func LoggingMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        start := time.Now()
        c.Next()
        duration := time.Since(start)
        log.Printf("%s %s %d %v", c.Request.Method, c.Request.URL.Path,
            c.Writer.Status(), duration)
    }
}

// Apply
r.Use(LoggingMiddleware())
api.Use(AuthMiddleware())
```

---

## 🏋️ Övningar

### Övning 1: Complete API
```go
type Todo struct {
    ID        int    `json:"id"`
    Title     string `json:"title" binding:"required"`
    Completed bool   `json:"completed"`
}

var todos = []Todo{}
var nextID = 1

func getTodos(c *gin.Context) {
    c.JSON(200, todos)
}

func createTodo(c *gin.Context) {
    var todo Todo
    if err := c.ShouldBindJSON(&todo); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    todo.ID = nextID
    nextID++
    todos = append(todos, todo)
    c.JSON(201, todo)
}
```

---

## 📚 Sammanfattning

| Framework | Styrka |
|-----------|--------|
| net/http | Standard library |
| Gin | Snabb, middleware |
| Echo | Minimalistisk |
| Fiber | Express-liknande |

**Nästa steg:** Working with Databases

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Working with Databases",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 💾 Working with Databases

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
- Ansluta till databaser med database/sql
- Använda GORM ORM
- Hantera migrations
- Connection pooling

---

## 📖 database/sql

```go
import (
    "database/sql"
    _ "github.com/lib/pq"  // PostgreSQL driver
)

func main() {
    db, err := sql.Open("postgres",
        "host=localhost user=dev password=secret dbname=app sslmode=disable")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // Connection pool settings
    db.SetMaxOpenConns(25)
    db.SetMaxIdleConns(5)
    db.SetConnMaxLifetime(5 * time.Minute)

    // Ping
    if err := db.Ping(); err != nil {
        log.Fatal(err)
    }
}

// Query
func getUsers(db *sql.DB) ([]User, error) {
    rows, err := db.Query("SELECT id, name, email FROM users")
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    var users []User
    for rows.Next() {
        var u User
        if err := rows.Scan(&u.ID, &u.Name, &u.Email); err != nil {
            return nil, err
        }
        users = append(users, u)
    }
    return users, rows.Err()
}

// Prepared statement
func getUser(db *sql.DB, id int) (*User, error) {
    var u User
    err := db.QueryRow("SELECT id, name FROM users WHERE id = $1", id).
        Scan(&u.ID, &u.Name)
    if err == sql.ErrNoRows {
        return nil, nil
    }
    return &u, err
}
```

---

## 🚀 GORM

```go
import "gorm.io/gorm"
import "gorm.io/driver/postgres"

type User struct {
    gorm.Model
    Name  string `gorm:"size:100;not null"`
    Email string `gorm:"uniqueIndex"`
    Posts []Post
}

type Post struct {
    gorm.Model
    Title   string
    Content string
    UserID  uint
}

func main() {
    dsn := "host=localhost user=dev password=secret dbname=app"
    db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        log.Fatal(err)
    }

    // Auto migrate
    db.AutoMigrate(&User{}, &Post{})

    // Create
    user := User{Name: "Alice", Email: "alice@test.com"}
    db.Create(&user)

    // Read
    var users []User
    db.Find(&users)
    db.First(&user, 1)
    db.Where("email = ?", "alice@test.com").First(&user)

    // Update
    db.Model(&user).Update("Name", "Alice Updated")

    // Delete
    db.Delete(&user, 1)

    // Preload relations
    db.Preload("Posts").Find(&users)
}
```

---

## 🏋️ Övningar

### Övning 1: Repository Pattern
```go
type UserRepository interface {
    Create(user *User) error
    FindByID(id uint) (*User, error)
    FindAll() ([]User, error)
}

type gormUserRepo struct {
    db *gorm.DB
}

func (r *gormUserRepo) Create(user *User) error {
    return r.db.Create(user).Error
}

func (r *gormUserRepo) FindByID(id uint) (*User, error) {
    var user User
    err := r.db.First(&user, id).Error
    return &user, err
}
```

---

## 📚 Sammanfattning

| Paket | Användning |
|-------|-----------|
| database/sql | Standard interface |
| GORM | Full ORM |
| sqlx | Extended sql |
| sqlc | Type-safe queries |

**Nästa step:** Testing in Go

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
    {
        "title": "Testing in Go",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 155,
        "content": r"""
# 🧪 Testing in Go

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
- Skriva unit tests med testing package
- Använda table-driven tests
- Mocka dependencies
- Benchmarking och coverage

---

## 📖 Unit Tests

```go
// math.go
package math

func Add(a, b int) int {
    return a + b
}

func Divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    if result != 5 {
        t.Errorf("Add(2, 3) = %d; want 5", result)
    }
}

func TestDivide(t *testing.T) {
    result, err := Divide(10, 2)
    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
    if result != 5 {
        t.Errorf("Divide(10, 2) = %f; want 5", result)
    }
}

func TestDivideByZero(t *testing.T) {
    _, err := Divide(10, 0)
    if err == nil {
        t.Error("expected error for division by zero")
    }
}
```

---

## 📊 Table-Driven Tests

```go
func TestAddTableDriven(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -1, -2},
        {"zero", 0, 0, 0},
        {"mixed", -1, 1, 0},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; want %d",
                    tt.a, tt.b, result, tt.expected)
            }
        })
    }
}
```

---

## 🎭 Mocking

```go
// Interface
type UserStore interface {
    GetUser(id int) (*User, error)
    SaveUser(user *User) error
}

// Mock
type MockUserStore struct {
    users map[int]*User
}

func (m *MockUserStore) GetUser(id int) (*User, error) {
    user, ok := m.users[id]
    if !ok {
        return nil, errors.New("not found")
    }
    return user, nil
}

// Test
func TestUserService(t *testing.T) {
    mock := &MockUserStore{
        users: map[int]*User{
            1: {ID: 1, Name: "Alice"},
        },
    }

    service := NewUserService(mock)
    user, err := service.GetUser(1)

    if err != nil {
        t.Fatalf("unexpected error: %v", err)
    }
    if user.Name != "Alice" {
        t.Errorf("got %s; want Alice", user.Name)
    }
}
```

---

## ⏱️ Benchmarks

```go
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(2, 3)
    }
}

// Kör: go test -bench=.
// Output:
// BenchmarkAdd-8   1000000000   0.3 ns/op
```

---

## 📈 Coverage

```bash
# Kör med coverage
go test -cover ./...

# Generera HTML rapport
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

---

## 📚 Sammanfattning

| Kommando | Funktion |
|----------|----------|
| go test | Kör tester |
| go test -v | Verbose |
| go test -run Name | Kör specifik test |
| go test -bench=. | Benchmarks |
| go test -cover | Coverage |

**Nästa steg:** Docker & Kubernetes with Go

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Docker & Kubernetes with Go",
        "difficulty": "hard",
        "estimated_minutes": 60,
        "xp_reward": 170,
        "content": r"""
# 🐳 Docker & Kubernetes with Go

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
- Skriva optimerade Dockerfiles för Go
- Interagera med Docker API
- Använda Kubernetes client-go
- Bygga operators

---

## 📖 Optimerad Dockerfile

```dockerfile
# Multi-stage build
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Cache dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /app/server ./cmd/server

# Final stage
FROM scratch

COPY --from=builder /app/server /server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

EXPOSE 8080
USER 1000

ENTRYPOINT ["/server"]
```

---

## 🔧 Docker SDK

```go
import (
    "github.com/docker/docker/client"
    "github.com/docker/docker/api/types"
)

func main() {
    cli, err := client.NewClientWithOpts(client.FromEnv)
    if err != nil {
        log.Fatal(err)
    }

    // List containers
    containers, _ := cli.ContainerList(ctx, types.ContainerListOptions{})
    for _, c := range containers {
        fmt.Printf("%s: %s\n", c.ID[:12], c.Image)
    }

    // Pull image
    reader, _ := cli.ImagePull(ctx, "nginx:latest", types.ImagePullOptions{})
    io.Copy(os.Stdout, reader)

    // Run container
    resp, _ := cli.ContainerCreate(ctx, &container.Config{
        Image: "nginx:latest",
    }, nil, nil, nil, "my-nginx")
    cli.ContainerStart(ctx, resp.ID, types.ContainerStartOptions{})
}
```

---

## ☸️ Kubernetes client-go

```go
import (
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

func main() {
    config, _ := clientcmd.BuildConfigFromFlags("",
        os.Getenv("HOME")+"/.kube/config")
    clientset, _ := kubernetes.NewForConfig(config)

    // List pods
    pods, _ := clientset.CoreV1().Pods("default").
        List(ctx, metav1.ListOptions{})
    for _, pod := range pods.Items {
        fmt.Printf("%s: %s\n", pod.Name, pod.Status.Phase)
    }

    // Create deployment
    deployment := &appsv1.Deployment{
        ObjectMeta: metav1.ObjectMeta{
            Name: "nginx-deployment",
        },
        Spec: appsv1.DeploymentSpec{
            Replicas: int32Ptr(3),
            // ...
        },
    }
    clientset.AppsV1().Deployments("default").Create(ctx, deployment, metav1.CreateOptions{})
}
```

---

## 🏋️ Övningar

### Övning 1: Pod Watcher
```go
watch, _ := clientset.CoreV1().Pods("default").
    Watch(ctx, metav1.ListOptions{})

for event := range watch.ResultChan() {
    pod := event.Object.(*v1.Pod)
    fmt.Printf("%s: %s\n", event.Type, pod.Name)
}
```

---

## 📚 Sammanfattning

| Paket | Användning |
|-------|-----------|
| docker/docker | Docker SDK |
| client-go | Kubernetes client |
| controller-runtime | Operator framework |

**Nästa steg:** Observability

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Observability - Logging & Metrics",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 160,
        "content": r"""
# 📊 Observability - Logging & Metrics

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
- Strukturerad logging med zerolog/zap
- Exponera Prometheus metrics
- Distributed tracing
- Health checks

---

## 📖 Strukturerad Logging

```go
// zerolog
import "github.com/rs/zerolog/log"

log.Info().
    Str("user", "alice").
    Int("attempt", 3).
    Msg("Login successful")

// Output: {"level":"info","user":"alice","attempt":3,"message":"Login successful"}

// zap (performant)
import "go.uber.org/zap"

logger, _ := zap.NewProduction()
defer logger.Sync()

logger.Info("Login successful",
    zap.String("user", "alice"),
    zap.Int("attempt", 3),
)
```

---

## 📈 Prometheus Metrics

```go
import (
    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
    httpRequests = prometheus.NewCounterVec(
        prometheus.CounterOpts{
            Name: "http_requests_total",
            Help: "Total HTTP requests",
        },
        []string{"method", "path", "status"},
    )

    httpDuration = prometheus.NewHistogramVec(
        prometheus.HistogramOpts{
            Name:    "http_request_duration_seconds",
            Help:    "HTTP request duration",
            Buckets: prometheus.DefBuckets,
        },
        []string{"method", "path"},
    )
)

func init() {
    prometheus.MustRegister(httpRequests, httpDuration)
}

func metricsMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()

        next.ServeHTTP(w, r)

        duration := time.Since(start).Seconds()
        httpRequests.WithLabelValues(r.Method, r.URL.Path, "200").Inc()
        httpDuration.WithLabelValues(r.Method, r.URL.Path).Observe(duration)
    })
}

func main() {
    http.Handle("/metrics", promhttp.Handler())
}
```

---

## 🏥 Health Checks

```go
type HealthChecker struct {
    db    *sql.DB
    redis *redis.Client
}

func (h *HealthChecker) Check() map[string]string {
    status := make(map[string]string)

    // DB check
    if err := h.db.Ping(); err != nil {
        status["db"] = "unhealthy"
    } else {
        status["db"] = "healthy"
    }

    // Redis check
    if _, err := h.redis.Ping(ctx).Result(); err != nil {
        status["redis"] = "unhealthy"
    } else {
        status["redis"] = "healthy"
    }

    return status
}

// Endpoint
r.GET("/health", func(c *gin.Context) {
    status := checker.Check()
    c.JSON(200, status)
})

r.GET("/ready", func(c *gin.Context) {
    status := checker.Check()
    for _, v := range status {
        if v == "unhealthy" {
            c.JSON(503, status)
            return
        }
    }
    c.JSON(200, status)
})
```

---

## 📚 Sammanfattning

| Verktyg | Användning |
|---------|-----------|
| zerolog/zap | Strukturerad logging |
| prometheus | Metrics |
| OpenTelemetry | Tracing |
| /health, /ready | Health checks |

**Nästa steg:** Configuration Management

> 💡 **Pro Tip:** Automatisera allt du gör mer än två gånger. Din framtida jag kommer tacka dig.
"""
    },
    {
        "title": "Configuration Management",
        "difficulty": "medium",
        "estimated_minutes": 45,
        "xp_reward": 140,
        "content": r"""
# ⚙️ Configuration Management

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
- Hantera config med Viper
- Environment variables
- Config validation
- Secrets management

---

## 📖 Viper

```go
import "github.com/spf13/viper"

func initConfig() {
    viper.SetConfigName("config")
    viper.SetConfigType("yaml")
    viper.AddConfigPath(".")
    viper.AddConfigPath("/etc/app/")

    // Environment variables
    viper.AutomaticEnv()
    viper.SetEnvPrefix("APP")
    viper.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))

    // Defaults
    viper.SetDefault("server.port", 8080)
    viper.SetDefault("database.max_conns", 10)

    if err := viper.ReadInConfig(); err != nil {
        log.Printf("No config file: %v", err)
    }
}

// config.yaml
// server:
//   port: 8080
//   host: localhost
// database:
//   host: localhost
//   port: 5432
//   name: app

// Användning
port := viper.GetInt("server.port")
dbHost := viper.GetString("database.host")
```

---

## 🏗️ Config Struct

```go
type Config struct {
    Server   ServerConfig   `mapstructure:"server"`
    Database DatabaseConfig `mapstructure:"database"`
    Redis    RedisConfig    `mapstructure:"redis"`
}

type ServerConfig struct {
    Port    int    `mapstructure:"port"`
    Host    string `mapstructure:"host"`
    Timeout int    `mapstructure:"timeout"`
}

func LoadConfig() (*Config, error) {
    var cfg Config
    if err := viper.Unmarshal(&cfg); err != nil {
        return nil, err
    }
    return &cfg, nil
}
```

---

## ✅ Validation

```go
import "github.com/go-playground/validator/v10"

type Config struct {
    Port     int    `validate:"required,min=1,max=65535"`
    Host     string `validate:"required,hostname"`
    Database string `validate:"required,url"`
}

func (c *Config) Validate() error {
    validate := validator.New()
    return validate.Struct(c)
}
```

---

## 📚 Sammanfattning

| Källa | Prioritet |
|-------|-----------|
| Flags | Högst |
| Env vars | Hög |
| Config file | Medium |
| Defaults | Lägst |

**Nästa steg:** Error Handling Patterns

> 💡 **Pro Tip:** Lär dig läsa loggfiler effektivt - de berättar alltid vad som gick fel.
"""
    },
    {
        "title": "Error Handling Patterns",
        "difficulty": "hard",
        "estimated_minutes": 50,
        "xp_reward": 155,
        "content": r"""
# 🚨 Error Handling Patterns

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
- Implementera error wrapping
- Använda sentinel errors
- Custom error types
- Graceful shutdown

---

## 📖 Error Wrapping

```go
import "fmt"

func readConfig(path string) error {
    data, err := os.ReadFile(path)
    if err != nil {
        return fmt.Errorf("readConfig %s: %w", path, err)
    }
    // ...
    return nil
}

// Unwrapping chain
if errors.Is(err, os.ErrNotExist) {
    // Handle missing file
}
```

---

## 🎯 Domain Errors

```go
// Sentinel errors
var (
    ErrNotFound      = errors.New("not found")
    ErrUnauthorized  = errors.New("unauthorized")
    ErrValidation    = errors.New("validation error")
)

// Custom error types
type ValidationError struct {
    Field   string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Message)
}

func (e ValidationError) Is(target error) bool {
    return target == ErrValidation
}

// Usage
func validateUser(u User) error {
    if u.Email == "" {
        return ValidationError{
            Field:   "email",
            Message: "required",
        }
    }
    return nil
}

err := validateUser(user)
if errors.Is(err, ErrValidation) {
    var ve ValidationError
    if errors.As(err, &ve) {
        fmt.Printf("Field %s: %s\n", ve.Field, ve.Message)
    }
}
```

---

## 🛑 Graceful Shutdown

```go
func main() {
    srv := &http.Server{Addr: ":8080"}

    go func() {
        if err := srv.ListenAndServe(); err != http.ErrServerClosed {
            log.Fatal(err)
        }
    }()

    // Wait for interrupt
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit

    log.Println("Shutting down...")

    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    if err := srv.Shutdown(ctx); err != nil {
        log.Fatal(err)
    }

    log.Println("Server stopped")
}
```

---

## 📚 Sammanfattning

| Pattern | Användning |
|---------|-----------|
| Wrapping | Lägg till context |
| Sentinel | Kända fel |
| Custom types | Rik information |
| Graceful shutdown | Cleanup |

**Nästa steg:** Performance Optimization

> 💡 **Pro Tip:** Testa i en dev-miljö först. Produktion är inte platsen för experiment.
"""
    },
    {
        "title": "Performance Optimization",
        "difficulty": "hard",
        "estimated_minutes": 55,
        "xp_reward": 165,
        "content": r"""
# ⚡ Performance Optimization

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
- Profilera Go-applikationer
- Optimera minnesanvändning
- Reducera allocations
- Connection pooling

---

## 📖 Profiling

```go
import _ "net/http/pprof"

func main() {
    go func() {
        log.Println(http.ListenAndServe(":6060", nil))
    }()
    // ...
}

// CPU profile
// go tool pprof http://localhost:6060/debug/pprof/profile?seconds=30

// Memory profile
// go tool pprof http://localhost:6060/debug/pprof/heap

// Goroutine profile
// go tool pprof http://localhost:6060/debug/pprof/goroutine
```

---

## 🧠 Memory Optimization

```go
// Preallocate slices
// Dåligt
var items []Item
for _, data := range dataset {
    items = append(items, process(data))
}

// Bra
items := make([]Item, 0, len(dataset))
for _, data := range dataset {
    items = append(items, process(data))
}

// Sync.Pool för återanvändning
var bufferPool = sync.Pool{
    New: func() interface{} {
        return new(bytes.Buffer)
    },
}

func process() {
    buf := bufferPool.Get().(*bytes.Buffer)
    defer func() {
        buf.Reset()
        bufferPool.Put(buf)
    }()
    // Use buffer
}
```

---

## 🔌 Connection Pooling

```go
// HTTP client
client := &http.Client{
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 10,
        IdleConnTimeout:     90 * time.Second,
    },
    Timeout: 10 * time.Second,
}

// Database
db.SetMaxOpenConns(25)
db.SetMaxIdleConns(5)
db.SetConnMaxLifetime(5 * time.Minute)
```

---

## 📚 Sammanfattning

| Teknik | Effekt |
|--------|--------|
| pprof | Hitta bottlenecks |
| Preallocate | Färre allocations |
| sync.Pool | Återanvänd objects |
| Pooling | Återanvänd connections |

**Grattis! Du har slutfört Go Mastery!** 🎉

> 💡 **Pro Tip:** Commita ofta, pusha dagligen. Små commits är lättare att granska och rollbacka.
"""
    },
    {
        "title": "Building Production-Ready Services",
        "difficulty": "hard",
        "estimated_minutes": 60,
        "xp_reward": 175,
        "content": r"""
# 🏭 Building Production-Ready Services

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
- Strukturera production-grade Go services
- Implementera circuit breakers
- Rate limiting
- Complete service example

---

## 📖 Service Structure

```
myservice/
+-- cmd/
|   +-- server/
|       +-- main.go
+-- internal/
|   +-- api/
|   |   +-- handlers.go
|   |   +-- middleware.go
|   |   +-- routes.go
|   +-- domain/
|   |   +-- user.go
|   |   +-- errors.go
|   +-- repository/
|   |   +-- user_repo.go
|   +-- service/
|       +-- user_service.go
+-- pkg/
|   +-- httputil/
+-- config/
|   +-- config.yaml
+-- Dockerfile
+-- Makefile
+-- go.mod
```

---

## 🔄 Circuit Breaker

```go
import "github.com/sony/gobreaker"

var cb *gobreaker.CircuitBreaker

func init() {
    cb = gobreaker.NewCircuitBreaker(gobreaker.Settings{
        Name:        "external-api",
        MaxRequests: 3,
        Interval:    10 * time.Second,
        Timeout:     30 * time.Second,
        ReadyToTrip: func(counts gobreaker.Counts) bool {
            return counts.ConsecutiveFailures > 5
        },
    })
}

func callExternalAPI() (string, error) {
    result, err := cb.Execute(func() (interface{}, error) {
        resp, err := http.Get("https://api.external.com/data")
        if err != nil {
            return nil, err
        }
        defer resp.Body.Close()
        body, _ := io.ReadAll(resp.Body)
        return string(body), nil
    })

    if err != nil {
        return "", err
    }
    return result.(string), nil
}
```

---

## ⏱️ Rate Limiting

```go
import "golang.org/x/time/rate"

// Per-client rate limiting
type RateLimiter struct {
    clients map[string]*rate.Limiter
    mu      sync.Mutex
    rate    rate.Limit
    burst   int
}

func (rl *RateLimiter) GetLimiter(clientID string) *rate.Limiter {
    rl.mu.Lock()
    defer rl.mu.Unlock()

    limiter, exists := rl.clients[clientID]
    if !exists {
        limiter = rate.NewLimiter(rl.rate, rl.burst)
        rl.clients[clientID] = limiter
    }
    return limiter
}

// Middleware
func RateLimitMiddleware(rl *RateLimiter) gin.HandlerFunc {
    return func(c *gin.Context) {
        clientID := c.ClientIP()
        limiter := rl.GetLimiter(clientID)

        if !limiter.Allow() {
            c.AbortWithStatusJSON(429, gin.H{
                "error": "rate limit exceeded",
            })
            return
        }
        c.Next()
    }
}
```

---

## 🏗️ Complete Service

```go
// cmd/server/main.go
func main() {
    cfg := config.Load()
    logger := logging.NewLogger(cfg.LogLevel)

    // Dependencies
    db := database.Connect(cfg.Database)
    defer db.Close()

    cache := redis.Connect(cfg.Redis)
    defer cache.Close()

    // Repositories
    userRepo := repository.NewUserRepository(db)

    // Services
    userService := service.NewUserService(userRepo, cache)

    // HTTP Server
    router := api.NewRouter(cfg, logger, userService)
    srv := &http.Server{
        Addr:         cfg.Server.Address,
        Handler:      router,
        ReadTimeout:  cfg.Server.ReadTimeout,
        WriteTimeout: cfg.Server.WriteTimeout,
    }

    // Graceful shutdown
    go func() {
        logger.Info("Starting server", "addr", srv.Addr)
        if err := srv.ListenAndServe(); err != http.ErrServerClosed {
            logger.Error("Server error", "error", err)
        }
    }()

    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit

    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    logger.Info("Shutting down...")
    srv.Shutdown(ctx)
    logger.Info("Server stopped")
}
```

---

## 📚 Sammanfattning

| Pattern | Beskrivning |
|---------|-------------|
| Clean Architecture | Separation of concerns |
| Circuit Breaker | Fault tolerance |
| Rate Limiting | Protect resources |
| Graceful Shutdown | Clean cleanup |
| Dependency Injection | Testability |

**🎉 Grattis! Du har slutfört Go Programming Mastery!**

> 💡 **Pro Tip:** Dokumentera VARFÖR, inte VAD. Koden visar vad, kommentarer förklarar varför.
"""
    },
]
