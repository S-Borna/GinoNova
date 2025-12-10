"""
C# & .NET SkillsMap - Block 3: ASP.NET Core Basics
Nodes 9-12: Introduction, Routing, Middleware, Configuration
"""

from typing import Any

# ============================================================================
# NODE 9: ASP.NET CORE INTRODUCTION
# ============================================================================

DOTNET_NODE_9_ASPNET_INTRO = {
    "node_id": 9,
    "title": "ASP.NET Core Introduction",
    "slug": "aspnet-introduction",
    "description": "Introduktion till ASP.NET Core och web development",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "aspnet core", "web api", "minimal api", "project structure",
        "kestrel", "hosting", "program.cs"
    ],
    "content": """# ASP.NET Core Introduction

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor ASP.NET Core ar viktigt |
|----------|-------------------------------|
| **Performance** | #1 pa TechEmpower benchmarks |
| **Cross-platform** | Windows, Linux, macOS |
| **Cloud-native** | Perfekt for containerization |
| **Unified** | Web, API, real-time, microservices |

Du maste forsta:

- **Kestrel** - inbyggd high-performance server
- **Middleware pipeline** - request/response flow
- **Minimal API vs Controllers** - nar anvanda vilken

------------------------------------------------------------

## 🧠 ASP.NET Core Architecture

```
+-----------------------------------------------------------------+
|                  ASP.NET CORE REQUEST PIPELINE                   |
+-----------------------------------------------------------------+
|                                                                  |
|  HTTP Request                                                   |
|       |                                                          |
|       ▼                                                          |
|  +---------------------------------------------------------+    |
|  |                      KESTREL                             |    |
|  |              (High-performance web server)               |    |
|  +---------------------------------------------------------+    |
|       |                                                          |
|       ▼                                                          |
|  +---------------------------------------------------------+    |
|  |                   MIDDLEWARE PIPELINE                    |    |
|  |  +---------+ +---------+ +---------+ +---------+        |    |
|  |  | Logging |->|  CORS   |->|  Auth   |->| Routing |        |    |
|  |  +---------+ +---------+ +---------+ +---------+        |    |
|  +---------------------------------------------------------+    |
|       |                                                          |
|       ▼                                                          |
|  +---------------------------------------------------------+    |
|  |                    ENDPOINT                              |    |
|  |            (Controller / Minimal API)                    |    |
|  +---------------------------------------------------------+    |
|       |                                                          |
|       ▼                                                          |
|  HTTP Response                                                  |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 💻 Create Your First API

```bash
# Skapa Minimal API projekt
dotnet new webapi -n MyApi -minimal
cd MyApi

# Projektstruktur
MyApi/
+-- MyApi.csproj           # Projektfil
+-- Program.cs             # Allt i en fil!
+-- appsettings.json       # Configuration
+-- appsettings.Development.json
+-- Properties/
    +-- launchSettings.json  # Dev-inställningar
```

### Minimal API (Modern Approach)

```csharp
// Program.cs - Hela API:et i en fil!
var builder = WebApplication.CreateBuilder(args);

// Add services (dependency injection)
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure middleware
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

// Define endpoints
app.MapGet("/", () => "Hello, World!");

app.MapGet("/api/hello/{name}", (string name) =>
    $"Hello, {name}!");

app.MapGet("/api/weather", () =>
{
    var forecast = Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast(
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            "Sunny"
        ))
        .ToArray();
    return forecast;
});

app.Run();

record WeatherForecast(DateOnly Date, int TemperatureC, string Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
```

### Run and Test

```bash
# Kör i development mode
dotnet run

# Output:
# info: Microsoft.Hosting.Lifetime[14]
#       Now listening on: https://localhost:7001
#       Now listening on: http://localhost:5000

# Öppna Swagger UI
# https://localhost:7001/swagger

# Test med curl
curl https://localhost:7001/api/hello/Alice
# "Hello, Alice!"
```

---

## 💻 Controller-Based API

```csharp
// Controllers/WeatherController.cs
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class WeatherController : ControllerBase
{
    private static readonly string[] Summaries =
    { "Freezing", "Cool", "Warm", "Hot" };

    [HttpGet]
    public IEnumerable<WeatherForecast> Get()
    {
        return Enumerable.Range(1, 5).Select(index =>
            new WeatherForecast(
                DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
                Random.Shared.Next(-20, 55),
                Summaries[Random.Shared.Next(Summaries.Length)]
            ));
    }

    [HttpGet("{id}")]
    public ActionResult<WeatherForecast> GetById(int id)
    {
        if (id <= 0)
            return BadRequest("Invalid ID");

        return new WeatherForecast(
            DateOnly.FromDateTime(DateTime.Now),
            20,
            "Sunny"
        );
    }
}

// Program.cs (med controllers)
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();  // Lägg till
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.MapControllers();  // Map controller endpoints
app.Run();
```

---

## 💻 HTTP Methods in Minimal API

```csharp
// GET - retrieve data
app.MapGet("/api/products", () => GetAllProducts());
app.MapGet("/api/products/{id}", (int id) => GetProduct(id));

// POST - create data
app.MapPost("/api/products", (Product product) =>
{
    // Create product
    return Results.Created($"/api/products/{product.Id}", product);
});

// PUT - update entire resource
app.MapPut("/api/products/{id}", (int id, Product product) =>
{
    // Update product
    return Results.NoContent();
});

// PATCH - partial update
app.MapPatch("/api/products/{id}", (int id, ProductUpdate update) =>
{
    // Partial update
    return Results.Ok(updatedProduct);
});

// DELETE - remove data
app.MapDelete("/api/products/{id}", (int id) =>
{
    // Delete product
    return Results.NoContent();
});
```

---

## 💻 Request/Response Types

```csharp
// Results helper methods
app.MapGet("/api/example", () =>
{
    // Return different status codes
    // return Results.Ok(data);           // 200
    // return Results.Created(uri, data); // 201
    // return Results.NoContent();        // 204
    // return Results.BadRequest();       // 400
    // return Results.NotFound();         // 404
    // return Results.Unauthorized();     // 401
    // return Results.Forbid();           // 403

    return Results.Ok(new { Message = "Success" });
});

// TypedResults for better type inference
app.MapGet("/api/users/{id}", Results<Ok<User>, NotFound> (int id) =>
{
    var user = FindUser(id);
    return user is not null
        ? TypedResults.Ok(user)
        : TypedResults.NotFound();
});
```

---

## ⚠️ Vanliga Problem

### Problem 1: HTTPS redirect i development

```csharp
// ❌ Kan orsaka problem med självundertecknade certifikat
app.UseHttpsRedirection();

// ✅ Endast i production
if (!app.Environment.IsDevelopment())
{
    app.UseHttpsRedirection();
}

// Eller trust dev-certifikat
// dotnet dev-certs https --trust
```

### Problem 2: CORS errors

```csharp
// Lägg till CORS policy
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.WithOrigins("http://localhost:3000")
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

// Använd innan routing
app.UseCors();
```

------------------------------------------------------------

## Snabbreferens

| Kommando | Beskrivning |
|----------|-------------|
| `dotnet new webapi` | Skapa Web API projekt |
| `dotnet run` | Starta applikationen |
| `app.MapGet()` | Definiera GET endpoint |
| `Results.Ok()` | Returnera 200 OK |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|--------|
| Port already in use | Annan process | Andra port i launchSettings.json |
| CORS error | Saknad policy | Lagg till CORS middleware |
| 404 Not Found | Fel route | Kontrollera routing |
| 500 Internal Error | Exception | Kolla loggar |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Minimal API** | For enkla endpoints |
| **Controllers** | For komplex struktur |
| **Kestrel** | Inbyggd high-perf server |
| **Swagger** | Genereras automatiskt |

**Kom ihag:**

- Minimal API for enkla CRUD-operationer
- Controllers for komplex logik och attribut
- Swagger UI pa /swagger for testning
- Kestrel ar production-ready
""",
}


# ============================================================================
# NODE 10: ROUTING & ENDPOINTS
# ============================================================================

DOTNET_NODE_10_ROUTING = {
    "node_id": 10,
    "title": "Routing & Endpoints",
    "slug": "aspnet-routing",
    "description": "URL routing, route parameters och constraints",
    "difficulty": "intermediate",
    "estimated_minutes": 55,
    "xp_reward": 110,
    "topics_covered": [
        "routing", "route parameters", "constraints", "route groups",
        "endpoint filters", "model binding"
    ],
    "content": """# Routing och Endpoints

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor routing ar viktigt |
|----------|---------------------------|
| **Clean URLs** | /api/users/123 istallet for ?id=123 |
| **RESTful** | Verbs via HTTP methods |
| **Discoverability** | Sjalvbeskrivande endpoints |
| **Versioning** | /api/v1/users vs /api/v2/users |

Du maste forsta:

- **Route parameters** - {id} for dynamiska segment
- **Constraints** - :int, :guid for validering
- **Route groups** - organisera relaterade endpoints

------------------------------------------------------------

---

## 🧠 Routing Patterns

```
+-----------------------------------------------------------------+
|                     ROUTING PATTERNS                             |
+-----------------------------------------------------------------+
|                                                                  |
|  PATTERN                   |  EXAMPLE URL                       |
|  ------------------------------------------------------------   |
|  /api/users                |  /api/users                        |
|  /api/users/{id}           |  /api/users/123                    |
|  /api/users/{id}/orders    |  /api/users/123/orders             |
|  /api/products/{*slug}     |  /api/products/electronics/phones  |
|  /api/v{version}/items     |  /api/v2/items                     |
|                                                                  |
|  CONSTRAINTS                                                    |
|  ------------------------------------------------------------   |
|  {id:int}                  |  Only integers                     |
|  {name:alpha}              |  Only letters                      |
|  {id:range(1,100)}         |  Between 1 and 100                 |
|  {filename:regex(.*\\.pdf)}|  Matches regex                     |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 💻 Route Parameters

```csharp
// Simple parameter
app.MapGet("/api/users/{id}", (int id) =>
    $"User ID: {id}");

// Multiple parameters
app.MapGet("/api/users/{userId}/orders/{orderId}",
    (int userId, int orderId) =>
    $"User {userId}, Order {orderId}");

// Optional parameter
app.MapGet("/api/products/{category?}", (string? category) =>
    category is null ? "All products" : $"Category: {category}");

// Catch-all parameter (slug)
app.MapGet("/api/files/{*path}", (string path) =>
    $"File path: {path}");
// /api/files/docs/reports/2024.pdf -> path = "docs/reports/2024.pdf"

// From query string
app.MapGet("/api/search", (string q, int page = 1, int size = 10) =>
    $"Search: {q}, Page: {page}, Size: {size}");
// /api/search?q=dotnet&page=2&size=20
```

---

## 💻 Route Constraints

```csharp
// Integer constraint
app.MapGet("/api/users/{id:int}", (int id) =>
    $"User ID (int): {id}");

// GUID constraint
app.MapGet("/api/orders/{id:guid}", (Guid id) =>
    $"Order ID (GUID): {id}");

// Range constraint
app.MapGet("/api/page/{num:range(1,100)}", (int num) =>
    $"Page: {num}");

// String length
app.MapGet("/api/code/{code:length(6)}", (string code) =>
    $"Code: {code}");

// Regex constraint
app.MapGet("/api/products/{sku:regex(^[A-Z]{{2}}-\\d{{4}}$)}",
    (string sku) => $"SKU: {sku}");
// Matches: AB-1234, XY-9999

// Multiple constraints
app.MapGet("/api/users/{id:int:min(1)}", (int id) =>
    $"User ID: {id}");

// Available constraints:
// int, long, decimal, double, float, bool, datetime, guid
// alpha (letters only), required, length(n), minlength(n), maxlength(n)
// min(n), max(n), range(min, max), regex(pattern)
```

---

## 💻 Route Groups

```csharp
// Group endpoints with common prefix
var users = app.MapGroup("/api/users")
    .WithTags("Users");  // Swagger grouping

users.MapGet("/", () => "Get all users");
users.MapGet("/{id}", (int id) => $"Get user {id}");
users.MapPost("/", (User user) => Results.Created($"/api/users/{user.Id}", user));
users.MapPut("/{id}", (int id, User user) => Results.NoContent());
users.MapDelete("/{id}", (int id) => Results.NoContent());

// Nested groups
var api = app.MapGroup("/api");

var v1 = api.MapGroup("/v1");
v1.MapGet("/products", () => "V1 products");

var v2 = api.MapGroup("/v2");
v2.MapGet("/products", () => "V2 products with new fields");

// Group with filters
var authenticated = app.MapGroup("/api/secure")
    .RequireAuthorization();  // All endpoints require auth

authenticated.MapGet("/profile", () => "User profile");
authenticated.MapGet("/settings", () => "User settings");
```

---

## 💻 Model Binding

```csharp
// From body (JSON)
app.MapPost("/api/users", (User user) =>
{
    // user populated from JSON body
    return Results.Created($"/api/users/{user.Id}", user);
});

// From route, query, and body combined
app.MapPut("/api/users/{id}", (
    int id,                    // From route
    [FromQuery] bool notify,   // From query string
    [FromBody] User user       // From body
) =>
{
    // PUT /api/users/123?notify=true
    return Results.NoContent();
});

// From header
app.MapGet("/api/data", ([FromHeader(Name = "X-Api-Key")] string apiKey) =>
    $"API Key: {apiKey}");

// From services (DI)
app.MapGet("/api/time", ([FromServices] ITimeService time) =>
    time.GetCurrentTime());

// Complex binding
public record CreateUserRequest(
    string Name,
    string Email,
    int Age
);

app.MapPost("/api/users", (CreateUserRequest request) =>
{
    // Automatic JSON deserialization
    return Results.Ok(request);
});
```

---

## 💻 Endpoint Filters

```csharp
// Validation filter
app.MapPost("/api/users", (User user) => Results.Ok(user))
    .AddEndpointFilter(async (context, next) =>
    {
        var user = context.GetArgument<User>(0);
        if (string.IsNullOrEmpty(user.Name))
        {
            return Results.BadRequest("Name is required");
        }
        return await next(context);
    });

// Logging filter
app.MapGet("/api/products", () => "Products")
    .AddEndpointFilter(async (context, next) =>
    {
        var logger = context.HttpContext.RequestServices
            .GetRequiredService<ILogger<Program>>();

        logger.LogInformation("Request started");
        var result = await next(context);
        logger.LogInformation("Request completed");

        return result;
    });

// Reusable filter
public class ValidationFilter<T> : IEndpointFilter
{
    public async ValueTask<object?> InvokeAsync(
        EndpointFilterInvocationContext context,
        EndpointFilterDelegate next)
    {
        var argument = context.GetArgument<T>(0);

        // Validate using FluentValidation or similar
        var validationResult = Validate(argument);
        if (!validationResult.IsValid)
        {
            return Results.BadRequest(validationResult.Errors);
        }

        return await next(context);
    }
}

app.MapPost("/api/users", (User user) => Results.Ok(user))
    .AddEndpointFilter<ValidationFilter<User>>();
```

---

## ⚠️ Vanliga Problem

### Problem 1: Route conflicts

```csharp
// ❌ Konflikt - vilken ska matcha /api/users/active?
app.MapGet("/api/users/{id}", (string id) => ...);
app.MapGet("/api/users/active", () => ...);

// ✅ Sätt constraint eller ordna routes
app.MapGet("/api/users/active", () => ...);  // Först (literal)
app.MapGet("/api/users/{id:int}", (int id) => ...);  // Sedan (constraint)
```

### Problem 2: Case sensitivity

```csharp
// Routes är case-insensitive by default
// /api/Users == /api/users == /API/USERS
```

------------------------------------------------------------

## Snabbreferens

| Syntax | Beskrivning |
|--------|-------------|
| `{id}` | Route parameter |
| `{id:int}` | Med constraint |
| `{id?}` | Optional parameter |
| `{*catchAll}` | Catch-all parameter |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|--------|
| Route conflict | Tvetydiga routes | Anvand constraints |
| 404 Not Found | Fel parameter-typ | Kontrollera constraint |
| Model binding failed | Fel format | Validera input |
| Wrong method | GET vs POST | Kontrollera HTTP verb |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Route parameters** | {id} for dynamiska segment |
| **Constraints** | :int, :guid for validering |
| **Route groups** | Organiserar endpoints |
| **Model binding** | Automatisk deserialisering |

**Kom ihag:**

- Anvand constraints for typsakerhet
- Literal routes for specifika matchar
- Route groups for gemensam prefix/middleware
- Case-insensitive by default
""",
}


# ============================================================================
# NODE 11: MIDDLEWARE
# ============================================================================

DOTNET_NODE_11_MIDDLEWARE = {
    "node_id": 11,
    "title": "Middleware Pipeline",
    "slug": "aspnet-middleware",
    "description": "Request/response pipeline och custom middleware",
    "difficulty": "intermediate",
    "estimated_minutes": 55,
    "xp_reward": 110,
    "topics_covered": [
        "middleware", "request pipeline", "custom middleware",
        "exception handling", "logging", "cors"
    ],
    "content": """# Middleware Pipeline

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor middleware ar viktigt |
|----------|------------------------------|
| **Authentication** | Vem ar du? |
| **Authorization** | Far du gora detta? |
| **Logging** | Vad hander? |
| **Error handling** | Vad gick fel? |

Du maste forsta:

- **Pipeline order** - ordningen ar kritisk
- **Use vs Run** - middleware chain vs terminal
- **Custom middleware** - reusable logic

------------------------------------------------------------

## 🧠 Middleware Pipeline

```
+-----------------------------------------------------------------+
|                   MIDDLEWARE PIPELINE                            |
+-----------------------------------------------------------------+
|                                                                  |
|  REQUEST ->                                                      |
|                                                                  |
|  +--------------+                                               |
|  |  Exception   | <- Catches all exceptions                      |
|  |   Handler    |                                               |
|  +------+-------+                                               |
|         ▼                                                        |
|  +--------------+                                               |
|  |    HTTPS     | <- Redirects HTTP to HTTPS                     |
|  |  Redirect    |                                               |
|  +------+-------+                                               |
|         ▼                                                        |
|  +--------------+                                               |
|  |   Static     | <- Serves wwwroot files                        |
|  |    Files     |                                               |
|  +------+-------+                                               |
|         ▼                                                        |
|  +--------------+                                               |
|  |    CORS      | <- Cross-origin headers                        |
|  +------+-------+                                               |
|         ▼                                                        |
|  +--------------+                                               |
|  |    Auth      | <- Who are you?                                |
|  +------+-------+                                               |
|         ▼                                                        |
|  +--------------+                                               |
|  |   Routing    | <- Match endpoint                              |
|  +------+-------+                                               |
|         ▼                                                        |
|  +--------------+                                               |
|  |  Endpoint    | <- Your code!                                  |
|  +--------------+                                               |
|                                                                  |
|  <- RESPONSE                                                     |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 💻 Built-in Middleware

```csharp
var builder = WebApplication.CreateBuilder(args);

// Add services
builder.Services.AddCors();
builder.Services.AddAuthentication();
builder.Services.AddAuthorization();

var app = builder.Build();

// MIDDLEWARE ORDER MATTERS!
// 1. Exception handling (first - catches everything)
app.UseExceptionHandler("/error");

// 2. HSTS (HTTP Strict Transport Security)
if (!app.Environment.IsDevelopment())
{
    app.UseHsts();
}

// 3. HTTPS redirection
app.UseHttpsRedirection();

// 4. Static files
app.UseStaticFiles();

// 5. Routing (prepares for endpoint matching)
app.UseRouting();

// 6. CORS (must be after routing, before auth)
app.UseCors();

// 7. Authentication (who are you?)
app.UseAuthentication();

// 8. Authorization (are you allowed?)
app.UseAuthorization();

// 9. Custom middleware
app.UseMiddleware<RequestLoggingMiddleware>();

// 10. Endpoints (your controllers/handlers)
app.MapControllers();

app.Run();
```

---

## 💻 Custom Middleware (Inline)

```csharp
// Simple inline middleware
app.Use(async (context, next) =>
{
    // Before endpoint
    Console.WriteLine($"Request: {context.Request.Path}");
    var stopwatch = Stopwatch.StartNew();

    await next();  // Call next middleware

    // After endpoint
    stopwatch.Stop();
    Console.WriteLine($"Response: {stopwatch.ElapsedMilliseconds}ms");
});

// Terminal middleware (doesn't call next)
app.Map("/health", app =>
{
    app.Run(async context =>
    {
        await context.Response.WriteAsync("Healthy");
    });
});

// Conditional middleware
app.UseWhen(
    context => context.Request.Path.StartsWithSegments("/api"),
    appBuilder => appBuilder.UseMiddleware<ApiLoggingMiddleware>()
);
```

---

## 💻 Custom Middleware (Class)

```csharp
// RequestLoggingMiddleware.cs
public class RequestLoggingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<RequestLoggingMiddleware> _logger;

    public RequestLoggingMiddleware(
        RequestDelegate next,
        ILogger<RequestLoggingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        // Before
        var requestId = Guid.NewGuid().ToString()[..8];
        _logger.LogInformation(
            "[{RequestId}] {Method} {Path}",
            requestId,
            context.Request.Method,
            context.Request.Path);

        var stopwatch = Stopwatch.StartNew();

        try
        {
            await _next(context);
        }
        finally
        {
            // After
            stopwatch.Stop();
            _logger.LogInformation(
                "[{RequestId}] Completed in {ElapsedMs}ms with {StatusCode}",
                requestId,
                stopwatch.ElapsedMilliseconds,
                context.Response.StatusCode);
        }
    }
}

// Extension method for cleaner registration
public static class MiddlewareExtensions
{
    public static IApplicationBuilder UseRequestLogging(
        this IApplicationBuilder builder)
    {
        return builder.UseMiddleware<RequestLoggingMiddleware>();
    }
}

// Usage
app.UseRequestLogging();
```

---

## 💻 Exception Handling Middleware

```csharp
// Global exception handler
public class ExceptionHandlingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<ExceptionHandlingMiddleware> _logger;

    public ExceptionHandlingMiddleware(
        RequestDelegate next,
        ILogger<ExceptionHandlingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Unhandled exception occurred");
            await HandleExceptionAsync(context, ex);
        }
    }

    private static async Task HandleExceptionAsync(
        HttpContext context,
        Exception exception)
    {
        context.Response.ContentType = "application/json";

        var (statusCode, message) = exception switch
        {
            ArgumentException => (400, exception.Message),
            KeyNotFoundException => (404, "Resource not found"),
            UnauthorizedAccessException => (401, "Unauthorized"),
            _ => (500, "An error occurred")
        };

        context.Response.StatusCode = statusCode;

        var response = new
        {
            error = message,
            statusCode = statusCode,
            timestamp = DateTime.UtcNow
        };

        await context.Response.WriteAsJsonAsync(response);
    }
}
```

---

## 💻 CORS Configuration

```csharp
// Configure CORS
builder.Services.AddCors(options =>
{
    // Named policy
    options.AddPolicy("AllowFrontend", policy =>
    {
        policy.WithOrigins("http://localhost:3000", "https://myapp.com")
              .AllowAnyHeader()
              .AllowAnyMethod()
              .AllowCredentials();  // For cookies
    });

    // Default policy
    options.AddDefaultPolicy(policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

// Use default policy
app.UseCors();

// Or use named policy
app.UseCors("AllowFrontend");

// Or per-endpoint
app.MapGet("/api/public", () => "Public")
    .RequireCors("AllowFrontend");
```

---

## ⚠️ Vanliga Problem

### Problem 1: Middleware order

```csharp
// ❌ CORS efter Authorization fungerar inte
app.UseAuthorization();
app.UseCors();  // Too late!

// ✅ CORS före Authorization
app.UseCors();
app.UseAuthorization();
```

### Problem 2: Response already started

```csharp
// ❌ Kan inte ändra response efter att body skrivits
public async Task InvokeAsync(HttpContext context)
{
    await _next(context);
    context.Response.StatusCode = 200;  // Error: Response already started
}

// ✅ Checka först
if (!context.Response.HasStarted)
{
    context.Response.StatusCode = 200;
}
```

------------------------------------------------------------

## Snabbreferens

| Metod | Beskrivning |
|-------|-------------|
| `Use()` | Middleware som anropar next |
| `Run()` | Terminal middleware |
| `Map()` | Branch pipeline |
| `UseWhen()` | Conditional middleware |

------------------------------------------------------------

## Vanliga fel och losningar

| Fel | Orsak | Losning |
|-----|-------|---------|
| CORS fails | Fel ordning | CORS fore Authorization |
| Response started | Skriver for sent | Checka HasStarted |
| Missing next | Glomde await | await _next(context) |
| Wrong order | Authn efter Authz | Authn fore Authz |

------------------------------------------------------------

## Key Takeaways

| Punkt | Forklaring |
|-------|------------|
| **Middleware order** | Kritiskt for korrekt beteende |
| **Use** | Anropar next i chain |
| **Run** | Terminal middleware |
| **Custom middleware** | Reusable logic |

**Kom ihag:**

- Exception middleware forst i pipeline
- CORS fore Authentication
- Authentication fore Authorization
- Routing nara slutet
""",
}


# ============================================================================
# NODE 12: CONFIGURATION & DEPENDENCY INJECTION
# ============================================================================

DOTNET_NODE_12_CONFIG = {
    "node_id": 12,
    "title": "Configuration & Dependency Injection",
    "slug": "aspnet-configuration",
    "description": "Konfiguration, options pattern och DI",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "configuration", "appsettings", "environment", "options pattern",
        "dependency injection", "service lifetimes"
    ],
    "content": """# Configuration och Dependency Injection

------------------------------------------------------------

## Varfor viktigt for DevOps?

| Scenario | Varfor config/DI ar viktigt |
|----------|----------------------------|
| **Environment-specific** | dev vs staging vs prod |
| **Secrets management** | Hall hemligheter sakra |
| **Testability** | Byt ut beroenden enkelt |
| **Loose coupling** | Flexibel arkitektur |

Du maste forsta:

- **Configuration sources** - prioritetsordning
- **Options pattern** - strongly-typed config
- **DI lifetimes** - Transient, Scoped, Singleton

------------------------------------------------------------

## 🧠 Configuration Sources

```
+-----------------------------------------------------------------+
|                  CONFIGURATION SOURCES                           |
|                  (i prioritetsordning)                           |
+-----------------------------------------------------------------+
|                                                                  |
|  1. appsettings.json           <- Bas-konfiguration              |
|         ▼                                                        |
|  2. appsettings.{Environment}.json  <- Environment-specific      |
|         ▼                                                        |
|  3. User Secrets (Development) <- Lokala hemligheter             |
|         ▼                                                        |
|  4. Environment Variables      <- Container/cloud config          |
|         ▼                                                        |
|  5. Command Line Arguments     <- Runtime overrides              |
|                                                                  |
|  SENARE KÄLLOR SKRIVER ÖVER TIDIGARE!                           |
|                                                                  |
+-----------------------------------------------------------------+
```

---

## 💻 appsettings.json

```json
// appsettings.json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=MyApp;"
  },
  "AppSettings": {
    "ApiTitle": "My API",
    "MaxPageSize": 100,
    "EnableFeatureX": false
  },
  "Email": {
    "SmtpServer": "smtp.example.com",
    "Port": 587,
    "FromAddress": "noreply@example.com"
  }
}

// appsettings.Development.json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=MyApp_Dev;"
  },
  "AppSettings": {
    "EnableFeatureX": true  // Override for dev
  }
}
```

---

## 💻 Reading Configuration

```csharp
// Direct access (not recommended for complex config)
var apiTitle = builder.Configuration["AppSettings:ApiTitle"];
var maxPageSize = builder.Configuration.GetValue<int>("AppSettings:MaxPageSize");

// Connection string helper
var connString = builder.Configuration.GetConnectionString("DefaultConnection");

// Bind to object
var emailSettings = new EmailSettings();
builder.Configuration.GetSection("Email").Bind(emailSettings);

// Inline in endpoint
app.MapGet("/config", (IConfiguration config) =>
{
    return new
    {
        ApiTitle = config["AppSettings:ApiTitle"],
        Environment = builder.Environment.EnvironmentName
    };
});
```

---

## 💻 Options Pattern (Recommended)

```csharp
// Define strongly-typed options class
public class EmailSettings
{
    public const string SectionName = "Email";

    public string SmtpServer { get; set; } = "";
    public int Port { get; set; } = 587;
    public string FromAddress { get; set; } = "";
}

public class AppSettings
{
    public const string SectionName = "AppSettings";

    public string ApiTitle { get; set; } = "";
    public int MaxPageSize { get; set; } = 50;
    public bool EnableFeatureX { get; set; }
}

// Register options
builder.Services.Configure<EmailSettings>(
    builder.Configuration.GetSection(EmailSettings.SectionName));

builder.Services.Configure<AppSettings>(
    builder.Configuration.GetSection(AppSettings.SectionName));

// Use in service
public class EmailService
{
    private readonly EmailSettings _settings;

    // IOptions<T> - read once at startup
    public EmailService(IOptions<EmailSettings> options)
    {
        _settings = options.Value;
    }

    // IOptionsSnapshot<T> - re-read on each request (scoped)
    // IOptionsMonitor<T> - real-time updates (singleton)
}

// Use in minimal API
app.MapGet("/email-settings", (IOptions<EmailSettings> options) =>
{
    return options.Value;
});
```

---

## 💻 User Secrets (Development)

```bash
# Initialize user secrets
dotnet user-secrets init

# Set secrets
dotnet user-secrets set "Email:Password" "supersecret"
dotnet user-secrets set "ConnectionStrings:DefaultConnection" "Server=..."

# List secrets
dotnet user-secrets list

# Remove secret
dotnet user-secrets remove "Email:Password"

# Secrets stored in:
# Windows: %APPDATA%\Microsoft\UserSecrets\{guid}\secrets.json
# macOS/Linux: ~/.microsoft/usersecrets/{guid}/secrets.json
```

---

## 💻 Dependency Injection

```csharp
// Register services
builder.Services.AddScoped<IUserService, UserService>();
builder.Services.AddTransient<IEmailService, SmtpEmailService>();
builder.Services.AddSingleton<ICacheService, MemoryCacheService>();

// Service lifetimes:
// Transient  - New instance every time requested
// Scoped     - One instance per HTTP request
// Singleton  - One instance for entire app lifetime

// Register with implementation factory
builder.Services.AddScoped<IDbConnection>(sp =>
{
    var config = sp.GetRequiredService<IConfiguration>();
    var connString = config.GetConnectionString("DefaultConnection");
    return new SqlConnection(connString);
});

// Register multiple implementations
builder.Services.AddScoped<INotificationService, EmailNotificationService>();
builder.Services.AddScoped<INotificationService, SmsNotificationService>();

// Inject in endpoint
app.MapGet("/users", async (IUserService userService) =>
{
    return await userService.GetAllAsync();
});

// Inject in controller
[ApiController]
public class UsersController : ControllerBase
{
    private readonly IUserService _userService;

    public UsersController(IUserService userService)
    {
        _userService = userService;
    }
}
```

---

## 💻 Service Registration Patterns

```csharp
// Extension method pattern (clean Program.cs)
public static class ServiceExtensions
{
    public static IServiceCollection AddApplicationServices(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        // Options
        services.Configure<EmailSettings>(
            configuration.GetSection(EmailSettings.SectionName));

        // Services
        services.AddScoped<IUserService, UserService>();
        services.AddScoped<IOrderService, OrderService>();
        services.AddScoped<IEmailService, SmtpEmailService>();

        return services;
    }
}

// Program.cs
builder.Services.AddApplicationServices(builder.Configuration);

// Keyed services (.NET 8+)
builder.Services.AddKeyedScoped<ICache, RedisCache>("redis");
builder.Services.AddKeyedScoped<ICache, MemoryCache>("memory");

// Inject keyed service
app.MapGet("/data", ([FromKeyedServices("redis")] ICache cache) =>
{
    return cache.Get("key");
});
```

---

## ⚠️ Vanliga Problem

### Problem 1: Captive dependency

```csharp
// ❌ Singleton har scoped dependency - PROBLEM!
builder.Services.AddSingleton<MySingleton>();  // Singleton
builder.Services.AddScoped<MyScopedDep>();     // Scoped

public class MySingleton
{
    // MyScopedDep kommer aldrig uppdateras!
    public MySingleton(MyScopedDep dep) { }
}

// ✅ Använd IServiceScopeFactory
public class MySingleton
{
    private readonly IServiceScopeFactory _scopeFactory;

    public void DoWork()
    {
        using var scope = _scopeFactory.CreateScope();
        var dep = scope.ServiceProvider.GetRequiredService<MyScopedDep>();
    }
}
```

---

## ✅ Sammanfattning

- **appsettings.json** för bas-konfiguration
- **Environment-specific** filer för överrides
- **User Secrets** för lokala hemligheter
- **Options Pattern** för strongly-typed config
- **DI lifetimes**: Transient, Scoped, Singleton
""",
}


# Export all nodes from Block 3
BLOCK_3_NODES = [
    DOTNET_NODE_9_ASPNET_INTRO,
    DOTNET_NODE_10_ROUTING,
    DOTNET_NODE_11_MIDDLEWARE,
    DOTNET_NODE_12_CONFIG,
]
