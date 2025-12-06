"""
C# & .NET SkillsMap - Block 5: Production & DevOps
Nodes 17-20: Testing, Logging, Docker, Deployment
"""

from typing import Any

# ============================================================================
# NODE 17: UNIT TESTING
# ============================================================================

DOTNET_NODE_17_TESTING = {
    "node_id": 17,
    "title": "Unit Testing with xUnit",
    "slug": "dotnet-unit-testing",
    "description": "Testa din kod med xUnit och Moq",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "xunit", "moq", "unit tests", "integration tests",
        "test doubles", "assertions", "code coverage"
    ],
    "content": """
# Unit Testing with xUnit

> *"Tests are the first client of your code."*

---

## 🎯 Why This Matters

Testing ger:
- **Confidence** - refaktorera utan rädsla
- **Documentation** - tester visar hur koden ska användas
- **Design** - testbar kod är bättre kod
- **CI/CD** - automatiserad kvalitetskontroll

---

## 🧠 Testing Pyramid

```
┌─────────────────────────────────────────────────────────────────┐
│                    TESTING PYRAMID                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                         △                                        │
│                        /│\\                                       │
│                       / │ \\                                      │
│                      /  │  \\     E2E Tests                       │
│                     /───────\\   (Few, Slow, Expensive)           │
│                    /    │    \\                                   │
│                   /     │     \\                                  │
│                  / Integration \\  Integration Tests              │
│                 /───────────────\\  (Some, Medium)                │
│                /        │        \\                               │
│               /         │         \\                              │
│              /    Unit Tests       \\  Unit Tests                 │
│             ──────────────────────── (Many, Fast, Cheap)         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Setup

```bash
# Skapa test projekt
dotnet new xunit -n MyApp.Tests
cd MyApp.Tests

# Lägg till projektref
dotnet add reference ../MyApp/MyApp.csproj

# Lägg till mocking library
dotnet add package Moq
dotnet add package FluentAssertions
dotnet add package Microsoft.EntityFrameworkCore.InMemory
```

---

## 💻 Basic Test Structure

```csharp
// UserServiceTests.cs
using Xunit;
using FluentAssertions;

public class UserServiceTests
{
    // Fact = single test
    [Fact]
    public void GetFullName_ShouldCombineFirstAndLastName()
    {
        // Arrange
        var user = new User { FirstName = "John", LastName = "Doe" };
        var service = new UserService();

        // Act
        var result = service.GetFullName(user);

        // Assert
        result.Should().Be("John Doe");
    }

    // Theory = parameterized test
    [Theory]
    [InlineData("", "Doe", "Doe")]
    [InlineData("John", "", "John")]
    [InlineData("John", "Doe", "John Doe")]
    public void GetFullName_ShouldHandleEmptyNames(
        string firstName,
        string lastName,
        string expected)
    {
        // Arrange
        var user = new User { FirstName = firstName, LastName = lastName };
        var service = new UserService();

        // Act
        var result = service.GetFullName(user);

        // Assert
        result.Should().Be(expected);
    }

    // Test exceptions
    [Fact]
    public void GetUser_ShouldThrowWhenIdIsNegative()
    {
        // Arrange
        var service = new UserService();

        // Act
        Action act = () => service.GetUser(-1);

        // Assert
        act.Should().Throw<ArgumentException>()
           .WithMessage("*invalid*");
    }
}
```

---

## 💻 Mocking with Moq

```csharp
using Moq;

public class OrderServiceTests
{
    private readonly Mock<IUserRepository> _userRepoMock;
    private readonly Mock<IOrderRepository> _orderRepoMock;
    private readonly Mock<IEmailService> _emailServiceMock;
    private readonly OrderService _sut;  // System Under Test

    public OrderServiceTests()
    {
        _userRepoMock = new Mock<IUserRepository>();
        _orderRepoMock = new Mock<IOrderRepository>();
        _emailServiceMock = new Mock<IEmailService>();

        _sut = new OrderService(
            _userRepoMock.Object,
            _orderRepoMock.Object,
            _emailServiceMock.Object);
    }

    [Fact]
    public async Task CreateOrder_ShouldSaveAndSendEmail()
    {
        // Arrange
        var user = new User { Id = 1, Email = "test@test.com" };
        var request = new CreateOrderRequest { UserId = 1, Amount = 100 };

        _userRepoMock
            .Setup(r => r.GetByIdAsync(1))
            .ReturnsAsync(user);

        _orderRepoMock
            .Setup(r => r.AddAsync(It.IsAny<Order>()))
            .ReturnsAsync((Order o) => { o.Id = 1; return o; });

        // Act
        var result = await _sut.CreateOrderAsync(request);

        // Assert
        result.Should().NotBeNull();
        result.Id.Should().Be(1);

        // Verify interactions
        _orderRepoMock.Verify(
            r => r.AddAsync(It.Is<Order>(o => o.Amount == 100)),
            Times.Once);

        _emailServiceMock.Verify(
            e => e.SendAsync(
                user.Email,
                It.Is<string>(s => s.Contains("Order"))),
            Times.Once);
    }

    [Fact]
    public async Task CreateOrder_ShouldThrowWhenUserNotFound()
    {
        // Arrange
        _userRepoMock
            .Setup(r => r.GetByIdAsync(It.IsAny<int>()))
            .ReturnsAsync((User?)null);

        var request = new CreateOrderRequest { UserId = 999 };

        // Act
        Func<Task> act = () => _sut.CreateOrderAsync(request);

        // Assert
        await act.Should().ThrowAsync<NotFoundException>()
            .WithMessage("*User*not found*");
    }
}
```

---

## 💻 Integration Tests

```csharp
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.EntityFrameworkCore;

public class UsersEndpointTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;
    private readonly WebApplicationFactory<Program> _factory;

    public UsersEndpointTests(WebApplicationFactory<Program> factory)
    {
        _factory = factory.WithWebHostBuilder(builder =>
        {
            builder.ConfigureServices(services =>
            {
                // Replace database with in-memory
                var descriptor = services.SingleOrDefault(
                    d => d.ServiceType == typeof(DbContextOptions<AppDbContext>));

                if (descriptor != null)
                    services.Remove(descriptor);

                services.AddDbContext<AppDbContext>(options =>
                {
                    options.UseInMemoryDatabase("TestDb");
                });
            });
        });

        _client = _factory.CreateClient();
    }

    [Fact]
    public async Task GetUsers_ShouldReturnOk()
    {
        // Act
        var response = await _client.GetAsync("/api/users");

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.OK);

        var users = await response.Content
            .ReadFromJsonAsync<List<UserResponse>>();
        users.Should().NotBeNull();
    }

    [Fact]
    public async Task CreateUser_ShouldReturn201()
    {
        // Arrange
        var request = new CreateUserRequest("John", "john@test.com", "Password123");

        // Act
        var response = await _client.PostAsJsonAsync("/api/users", request);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.Created);
        response.Headers.Location.Should().NotBeNull();

        var user = await response.Content.ReadFromJsonAsync<UserResponse>();
        user!.Name.Should().Be("John");
    }

    [Fact]
    public async Task CreateUser_WithInvalidEmail_ShouldReturn400()
    {
        // Arrange
        var request = new CreateUserRequest("John", "invalid-email", "Password123");

        // Act
        var response = await _client.PostAsJsonAsync("/api/users", request);

        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.BadRequest);
    }
}
```

---

## 💻 Test Fixtures & Setup

```csharp
// Shared context across tests
public class DatabaseFixture : IDisposable
{
    public AppDbContext Context { get; }

    public DatabaseFixture()
    {
        var options = new DbContextOptionsBuilder<AppDbContext>()
            .UseInMemoryDatabase("TestDb_" + Guid.NewGuid())
            .Options;

        Context = new AppDbContext(options);
        SeedData();
    }

    private void SeedData()
    {
        Context.Users.AddRange(
            new User { Id = 1, Name = "Test User 1" },
            new User { Id = 2, Name = "Test User 2" }
        );
        Context.SaveChanges();
    }

    public void Dispose() => Context.Dispose();
}

// Use fixture
public class UserRepositoryTests : IClassFixture<DatabaseFixture>
{
    private readonly DatabaseFixture _fixture;

    public UserRepositoryTests(DatabaseFixture fixture)
    {
        _fixture = fixture;
    }

    [Fact]
    public async Task GetById_ShouldReturnUser()
    {
        var repo = new UserRepository(_fixture.Context);
        var user = await repo.GetByIdAsync(1);
        user.Should().NotBeNull();
    }
}
```

---

## 💻 Kör Tester

```bash
# Kör alla tester
dotnet test

# Med verbose output
dotnet test --logger "console;verbosity=detailed"

# Specifik test
dotnet test --filter "FullyQualifiedName~CreateOrder"

# Med code coverage
dotnet test --collect:"XPlat Code Coverage"

# Generera rapport
dotnet tool install -g dotnet-reportgenerator-globaltool
reportgenerator -reports:"coverage.cobertura.xml" -targetdir:"coverage"
```

---

## ✅ Sammanfattning

- **xUnit** är standard för .NET testing
- **Moq** för att mocka dependencies
- **FluentAssertions** för läsbara asserts
- **WebApplicationFactory** för integration tests
- **Kör tester ofta** - snabb feedback loop
""",
}


# ============================================================================
# NODE 18: LOGGING & MONITORING
# ============================================================================

DOTNET_NODE_18_LOGGING = {
    "node_id": 18,
    "title": "Logging & Monitoring",
    "slug": "dotnet-logging",
    "description": "Strukturerad logging med Serilog",
    "difficulty": "intermediate",
    "estimated_minutes": 50,
    "xp_reward": 100,
    "topics_covered": [
        "ilogger", "serilog", "structured logging", "log levels",
        "correlation ids", "health checks", "metrics"
    ],
    "content": """
# Logging & Monitoring

> *"If you can't measure it, you can't improve it."*

---

## 🎯 Why This Matters

Logging är kritiskt i produktion:
- **Debugging** - hitta problem snabbt
- **Auditing** - spåra vad som hände
- **Performance** - identifiera flaskhalsar
- **Alerting** - veta när något går fel

---

## 🧠 Log Levels

```
┌─────────────────────────────────────────────────────────────────┐
│                     LOG LEVELS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TRACE       ──────►  Most detailed, typically dev only         │
│                       "Entering method ProcessOrder"             │
│                                                                  │
│  DEBUG       ──────►  Detailed info for debugging               │
│                       "Processing order 123 with 5 items"        │
│                                                                  │
│  INFORMATION ──────►  General app flow                          │
│                       "Order 123 created successfully"           │
│                                                                  │
│  WARNING     ──────►  Something unexpected but handled          │
│                       "Retry attempt 2 of 3 for payment"         │
│                                                                  │
│  ERROR       ──────►  Error that should be investigated         │
│                       "Payment failed for order 123"             │
│                                                                  │
│  CRITICAL    ──────►  System is unusable                        │
│                       "Database connection lost"                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Built-in ILogger

```csharp
public class OrderService
{
    private readonly ILogger<OrderService> _logger;

    public OrderService(ILogger<OrderService> logger)
    {
        _logger = logger;
    }

    public async Task<Order> CreateOrderAsync(CreateOrderRequest request)
    {
        _logger.LogInformation(
            "Creating order for user {UserId} with {ItemCount} items",
            request.UserId,
            request.Items.Count);

        try
        {
            var order = await ProcessOrder(request);

            _logger.LogInformation(
                "Order {OrderId} created successfully. Total: {Amount:C}",
                order.Id,
                order.TotalAmount);

            return order;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex,
                "Failed to create order for user {UserId}",
                request.UserId);
            throw;
        }
    }
}

// Log with scopes
using (_logger.BeginScope(new Dictionary<string, object>
{
    ["OrderId"] = orderId,
    ["UserId"] = userId
}))
{
    _logger.LogInformation("Processing payment");
    // All logs in scope will have OrderId and UserId
}
```

---

## 💻 Serilog Setup

```bash
dotnet add package Serilog.AspNetCore
dotnet add package Serilog.Sinks.Console
dotnet add package Serilog.Sinks.Seq
dotnet add package Serilog.Enrichers.Environment
```

```csharp
// Program.cs
using Serilog;

Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .MinimumLevel.Override("Microsoft.AspNetCore", LogEventLevel.Warning)
    .Enrich.FromLogContext()
    .Enrich.WithMachineName()
    .Enrich.WithEnvironmentName()
    .WriteTo.Console(outputTemplate:
        "[{Timestamp:HH:mm:ss} {Level:u3}] {Message:lj} {Properties:j}{NewLine}{Exception}")
    .WriteTo.Seq("http://localhost:5341")  // Seq log server
    .CreateLogger();

try
{
    var builder = WebApplication.CreateBuilder(args);
    builder.Host.UseSerilog();

    var app = builder.Build();

    // Request logging middleware
    app.UseSerilogRequestLogging(options =>
    {
        options.EnrichDiagnosticContext = (diagnosticContext, httpContext) =>
        {
            diagnosticContext.Set("RequestHost", httpContext.Request.Host.Value);
            diagnosticContext.Set("UserAgent", httpContext.Request.Headers["User-Agent"]);
        };
    });

    app.MapControllers();
    app.Run();
}
catch (Exception ex)
{
    Log.Fatal(ex, "Application terminated unexpectedly");
}
finally
{
    Log.CloseAndFlush();
}
```

---

## 💻 appsettings.json Configuration

```json
{
  "Serilog": {
    "Using": ["Serilog.Sinks.Console", "Serilog.Sinks.File"],
    "MinimumLevel": {
      "Default": "Information",
      "Override": {
        "Microsoft": "Warning",
        "Microsoft.Hosting.Lifetime": "Information",
        "System": "Warning"
      }
    },
    "WriteTo": [
      {
        "Name": "Console",
        "Args": {
          "theme": "Serilog.Sinks.SystemConsole.Themes.AnsiConsoleTheme::Code"
        }
      },
      {
        "Name": "File",
        "Args": {
          "path": "logs/app-.log",
          "rollingInterval": "Day",
          "retainedFileCountLimit": 7
        }
      }
    ],
    "Enrich": ["FromLogContext", "WithMachineName", "WithThreadId"]
  }
}
```

---

## 💻 Correlation IDs

```csharp
// Middleware för att tracka requests
public class CorrelationIdMiddleware
{
    private readonly RequestDelegate _next;
    private const string CorrelationIdHeader = "X-Correlation-Id";

    public CorrelationIdMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        var correlationId = context.Request.Headers[CorrelationIdHeader]
            .FirstOrDefault() ?? Guid.NewGuid().ToString();

        context.Items["CorrelationId"] = correlationId;
        context.Response.Headers[CorrelationIdHeader] = correlationId;

        using (LogContext.PushProperty("CorrelationId", correlationId))
        {
            await _next(context);
        }
    }
}

// Register: app.UseMiddleware<CorrelationIdMiddleware>();
```

---

## 💻 Health Checks

```csharp
// Program.cs
builder.Services.AddHealthChecks()
    .AddDbContextCheck<AppDbContext>("database")
    .AddRedis(connectionString, "redis")
    .AddUrlGroup(new Uri("https://api.example.com"), "external-api");

app.MapHealthChecks("/health", new HealthCheckOptions
{
    ResponseWriter = async (context, report) =>
    {
        context.Response.ContentType = "application/json";
        var result = new
        {
            status = report.Status.ToString(),
            checks = report.Entries.Select(e => new
            {
                name = e.Key,
                status = e.Value.Status.ToString(),
                duration = e.Value.Duration.TotalMilliseconds
            })
        };
        await context.Response.WriteAsJsonAsync(result);
    }
});

// Response:
// {
//   "status": "Healthy",
//   "checks": [
//     { "name": "database", "status": "Healthy", "duration": 12.3 },
//     { "name": "redis", "status": "Healthy", "duration": 5.1 }
//   ]
// }
```

---

## ⚠️ Logging Best Practices

```csharp
// ❌ String interpolation (defeats structured logging)
_logger.LogInformation($"User {userId} created order {orderId}");

// ✅ Message templates (structured, searchable)
_logger.LogInformation("User {UserId} created order {OrderId}", userId, orderId);

// ❌ Logging sensitive data
_logger.LogInformation("User logged in with password {Password}", password);

// ✅ Never log sensitive data
_logger.LogInformation("User {UserId} logged in successfully", userId);

// ❌ Too much logging
_logger.LogInformation("Entering method");
_logger.LogInformation("Variable x = 5");
_logger.LogInformation("Exiting method");

// ✅ Meaningful logs
_logger.LogInformation("Processing payment {PaymentId} for {Amount:C}", paymentId, amount);
```

---

## ✅ Sammanfattning

- **ILogger** är standard interface
- **Serilog** för kraftfull structured logging
- **Correlation IDs** för request tracing
- **Health checks** för monitoring
- **Log levels** - rätt nivå för rätt info
""",
}


# ============================================================================
# NODE 19: DOCKER & CONTAINERS
# ============================================================================

DOTNET_NODE_19_DOCKER = {
    "node_id": 19,
    "title": "Docker for .NET",
    "slug": "dotnet-docker",
    "description": "Containerisera .NET applikationer",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 120,
    "topics_covered": [
        "dockerfile", "multi-stage builds", "docker compose",
        "environment variables", "volumes", "networking"
    ],
    "content": """
# Docker for .NET

> *"Build once, run anywhere."*

---

## 🎯 Why This Matters

Docker för .NET ger:
- **Consistency** - samma miljö överallt
- **Isolation** - inga dependency-konflikter
- **Scalability** - enkelt att skala
- **DevOps** - smidig CI/CD pipeline

---

## 🧠 Docker Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DOCKER ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                     HOST MACHINE                           │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │                 DOCKER ENGINE                        │  │  │
│  │  │                                                      │  │  │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │  │  │
│  │  │  │Container│  │Container│  │Container│             │  │  │
│  │  │  │   API   │  │   DB    │  │  Redis  │             │  │  │
│  │  │  │ :5000   │  │ :5432   │  │ :6379   │             │  │  │
│  │  │  └─────────┘  └─────────┘  └─────────┘             │  │  │
│  │  │       │                                             │  │  │
│  │  │  ┌────────────────────────────────────────────┐    │  │  │
│  │  │  │            Docker Network                   │    │  │  │
│  │  │  └────────────────────────────────────────────┘    │  │  │
│  │  │                                                      │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Basic Dockerfile

```dockerfile
# Simple Dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["MyApp.csproj", "./"]
RUN dotnet restore
COPY . .
RUN dotnet build -c Release -o /app/build

FROM build AS publish
RUN dotnet publish -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

---

## 💻 Optimized Multi-Stage Dockerfile

```dockerfile
# Dockerfile (production-optimized)

# === BUILD STAGE ===
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copy csproj first for layer caching
COPY ["src/MyApp.Api/MyApp.Api.csproj", "src/MyApp.Api/"]
COPY ["src/MyApp.Core/MyApp.Core.csproj", "src/MyApp.Core/"]
COPY ["src/MyApp.Data/MyApp.Data.csproj", "src/MyApp.Data/"]
RUN dotnet restore "src/MyApp.Api/MyApp.Api.csproj"

# Copy everything and build
COPY . .
RUN dotnet build "src/MyApp.Api/MyApp.Api.csproj" -c Release -o /app/build

# === PUBLISH STAGE ===
FROM build AS publish
RUN dotnet publish "src/MyApp.Api/MyApp.Api.csproj" \\
    -c Release \\
    -o /app/publish \\
    --no-restore \\
    /p:UseAppHost=false

# === RUNTIME STAGE ===
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final

# Security: run as non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /app
COPY --from=publish /app/publish .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD wget --no-verbose --tries=1 --spider http://localhost:80/health || exit 1

ENV ASPNETCORE_URLS=http://+:80
ENV ASPNETCORE_ENVIRONMENT=Production

ENTRYPOINT ["dotnet", "MyApp.Api.dll"]
```

---

## 💻 .dockerignore

```
# .dockerignore
**/bin/
**/obj/
**/.git
**/.vs
**/.vscode
**/node_modules/
**/*.md
**/Dockerfile*
**/.dockerignore
**/.env
**/appsettings.Development.json
```

---

## 💻 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:80"
    environment:
      - ASPNETCORE_ENVIRONMENT=Development
      - ConnectionStrings__DefaultConnection=Server=db;Database=MyApp;User=sa;Password=YourPassword123!;TrustServerCertificate=true
      - Redis__ConnectionString=redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - app-network
    restart: unless-stopped

  db:
    image: mcr.microsoft.com/mssql/server:2022-latest
    environment:
      - ACCEPT_EULA=Y
      - SA_PASSWORD=YourPassword123!
    ports:
      - "1433:1433"
    volumes:
      - sqlserver-data:/var/opt/mssql
    healthcheck:
      test: /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "YourPassword123!" -Q "SELECT 1"
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - app-network

  seq:
    image: datalust/seq:latest
    environment:
      - ACCEPT_EULA=Y
    ports:
      - "5341:80"
    volumes:
      - seq-data:/data
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  sqlserver-data:
  redis-data:
  seq-data:
```

---

## 💻 Docker Commands

```bash
# Build image
docker build -t myapp:latest .

# Run container
docker run -d -p 5000:80 --name myapp myapp:latest

# Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs -f api
docker-compose ps

# Debug
docker exec -it myapp /bin/sh
docker logs myapp -f

# Clean up
docker system prune -a
```

---

## 💻 Environment Configuration

```csharp
// Program.cs - environment-aware config
var builder = WebApplication.CreateBuilder(args);

// Docker sets these automatically
builder.Configuration
    .AddJsonFile("appsettings.json", optional: false)
    .AddJsonFile($"appsettings.{builder.Environment.EnvironmentName}.json", optional: true)
    .AddEnvironmentVariables();  // Override from Docker env

// Use config
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
```

---

## ✅ Sammanfattning

- **Multi-stage builds** minskar image size
- **Layer caching** snabbar upp builds
- **Docker Compose** för multi-container apps
- **Health checks** för container orchestration
- **Non-root user** för security
""",
}


# ============================================================================
# NODE 20: DEPLOYMENT & CI/CD
# ============================================================================

DOTNET_NODE_20_DEPLOYMENT = {
    "node_id": 20,
    "title": "Deployment & CI/CD",
    "slug": "dotnet-deployment",
    "description": "Deploy .NET apps med GitHub Actions",
    "difficulty": "advanced",
    "estimated_minutes": 70,
    "xp_reward": 140,
    "topics_covered": [
        "github actions", "azure", "aws", "kubernetes",
        "ci/cd pipeline", "secrets management", "environments"
    ],
    "content": """
# Deployment & CI/CD

> *"If it's not in production, it doesn't exist."*

---

## 🎯 Why This Matters

Modern deployment ger:
- **Speed** - snabbare releases
- **Quality** - automatiserad testning
- **Reliability** - reproducerbara deploys
- **Confidence** - rollback möjlighet

---

## 🧠 CI/CD Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                     CI/CD PIPELINE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────┐    ┌──────┐    ┌──────┐    ┌────────┐    ┌──────────┐ │
│  │ Git │───►│Build │───►│ Test │───►│Package │───►│  Deploy  │ │
│  │Push │    │      │    │      │    │        │    │          │ │
│  └─────┘    └──────┘    └──────┘    └────────┘    └──────────┘ │
│     │          │           │            │              │        │
│     │          │           │            │              ▼        │
│     │          │           │            │         ┌────────┐   │
│     │          │           │            │         │  Prod  │   │
│     │          │           │            ▼         └────────┘   │
│     │          │           │       ┌────────┐                  │
│     │          │           │       │Registry│                  │
│     │          │           ▼       └────────┘                  │
│     │          │      ┌────────┐                               │
│     │          │      │Coverage│                               │
│     │          ▼      └────────┘                               │
│     │     ┌────────┐                                           │
│     │     │ Restore│                                           │
│     ▼     └────────┘                                           │
│  ┌─────┐                                                       │
│  │Clone│                                                       │
│  └─────┘                                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 GitHub Actions - Complete Pipeline

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  DOTNET_VERSION: '8.0.x'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # === BUILD & TEST ===
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Setup .NET
      uses: actions/setup-dotnet@v4
      with:
        dotnet-version: ${{ env.DOTNET_VERSION }}

    - name: Restore dependencies
      run: dotnet restore

    - name: Build
      run: dotnet build --no-restore -c Release

    - name: Test with coverage
      run: |
        dotnet test --no-build -c Release \\
          --collect:"XPlat Code Coverage" \\
          --results-directory ./coverage

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        directory: ./coverage

    - name: Upload build artifacts
      uses: actions/upload-artifact@v4
      with:
        name: app
        path: src/MyApp.Api/bin/Release/net8.0/

  # === DOCKER BUILD ===
  docker:
    needs: build
    runs-on: ubuntu-latest
    if: github.event_name == 'push'

    permissions:
      contents: read
      packages: write

    steps:
    - uses: actions/checkout@v4

    - name: Log in to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=sha,prefix=
          type=ref,event=branch
          type=semver,pattern={{version}}

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  # === DEPLOY TO STAGING ===
  deploy-staging:
    needs: docker
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    environment: staging

    steps:
    - name: Deploy to Azure Web App (Staging)
      uses: azure/webapps-deploy@v2
      with:
        app-name: ${{ secrets.AZURE_WEBAPP_NAME_STAGING }}
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE_STAGING }}
        images: '${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}'

  # === DEPLOY TO PRODUCTION ===
  deploy-production:
    needs: docker
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production

    steps:
    - name: Deploy to Azure Web App (Production)
      uses: azure/webapps-deploy@v2
      with:
        app-name: ${{ secrets.AZURE_WEBAPP_NAME_PROD }}
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE_PROD }}
        images: '${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}'
```

---

## 💻 Azure Deployment

```bash
# Azure CLI - skapa resurser
az group create --name myapp-rg --location northeurope

# App Service Plan
az appservice plan create \\
    --name myapp-plan \\
    --resource-group myapp-rg \\
    --sku B1 \\
    --is-linux

# Web App
az webapp create \\
    --name myapp-api \\
    --resource-group myapp-rg \\
    --plan myapp-plan \\
    --deployment-container-image-name ghcr.io/myorg/myapp:latest

# Configure app settings
az webapp config appsettings set \\
    --name myapp-api \\
    --resource-group myapp-rg \\
    --settings \\
        ASPNETCORE_ENVIRONMENT=Production \\
        ConnectionStrings__DefaultConnection="@Microsoft.KeyVault(VaultName=myapp-kv;SecretName=DbConnection)"
```

---

## 💻 Kubernetes Deployment

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-api
  labels:
    app: myapp-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp-api
  template:
    metadata:
      labels:
        app: myapp-api
    spec:
      containers:
      - name: api
        image: ghcr.io/myorg/myapp:latest
        ports:
        - containerPort: 80
        env:
        - name: ASPNETCORE_ENVIRONMENT
          value: "Production"
        - name: ConnectionStrings__DefaultConnection
          valueFrom:
            secretKeyRef:
              name: myapp-secrets
              key: db-connection
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 10

---
apiVersion: v1
kind: Service
metadata:
  name: myapp-api-service
spec:
  selector:
    app: myapp-api
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

## 💻 Secrets Management

```csharp
// Azure Key Vault integration
builder.Configuration.AddAzureKeyVault(
    new Uri($"https://{vaultName}.vault.azure.net/"),
    new DefaultAzureCredential());

// User Secrets (development)
// dotnet user-secrets set "ConnectionStrings:DefaultConnection" "..."
builder.Configuration.AddUserSecrets<Program>();

// Environment variables (production)
builder.Configuration.AddEnvironmentVariables();
```

---

## 💻 Health Checks för Load Balancers

```csharp
builder.Services.AddHealthChecks()
    .AddCheck("self", () => HealthCheckResult.Healthy(), tags: ["live"])
    .AddDbContextCheck<AppDbContext>(tags: ["ready"])
    .AddRedis(connectionString, tags: ["ready"]);

// Liveness - är appen alive?
app.MapHealthChecks("/health/live", new HealthCheckOptions
{
    Predicate = check => check.Tags.Contains("live")
});

// Readiness - är appen redo för trafik?
app.MapHealthChecks("/health/ready", new HealthCheckOptions
{
    Predicate = check => check.Tags.Contains("ready")
});
```

---

## ✅ Sammanfattning

- **GitHub Actions** automatiserar CI/CD
- **Multi-environment** (staging → production)
- **Container deployment** till Azure/K8s
- **Secrets** hanteras säkert
- **Health checks** för orchestration
- **Rollback** via container tags
""",
}


# Export all nodes from Block 5
BLOCK_5_NODES = [
    DOTNET_NODE_17_TESTING,
    DOTNET_NODE_18_LOGGING,
    DOTNET_NODE_19_DOCKER,
    DOTNET_NODE_20_DEPLOYMENT,
]
