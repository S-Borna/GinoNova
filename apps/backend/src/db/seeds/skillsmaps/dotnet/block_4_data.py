"""
C# & .NET SkillsMap - Block 4: Data Access & APIs
Nodes 13-16: Entity Framework, Database, REST API, Validation
"""

from typing import Any

# ============================================================================
# NODE 13: ENTITY FRAMEWORK CORE
# ============================================================================

DOTNET_NODE_13_EF_CORE = {
    "node_id": 13,
    "title": "Entity Framework Core",
    "slug": "ef-core-introduction",
    "description": "ORM med Entity Framework Core",
    "difficulty": "intermediate",
    "estimated_minutes": 70,
    "xp_reward": 120,
    "topics_covered": [
        "entity framework", "orm", "dbcontext", "models",
        "migrations", "code first", "database first"
    ],
    "content": """
# Entity Framework Core

> *"EF Core lets you work with databases using .NET objects."*

---

## 🎯 Why This Matters

Entity Framework Core är standard ORM för .NET:
- **Productivity** - skriv C#, inte SQL
- **Type safety** - kompilator-fel istället för runtime
- **Migrations** - versionera din databas
- **Cross-database** - samma kod för SQL Server, PostgreSQL, SQLite

---

## 🧠 EF Core Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  ENTITY FRAMEWORK CORE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  YOUR C# CODE                                                   │
│       │                                                          │
│       ▼                                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                     DbContext                             │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐         │   │
│  │  │ DbSet<User>│  │DbSet<Order>│  │DbSet<Item> │         │   │
│  │  └────────────┘  └────────────┘  └────────────┘         │   │
│  └──────────────────────────────────────────────────────────┘   │
│       │                                                          │
│       ▼                                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Database Provider                            │   │
│  │   SqlServer │ PostgreSQL │ SQLite │ InMemory             │   │
│  └──────────────────────────────────────────────────────────┘   │
│       │                                                          │
│       ▼                                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    DATABASE                               │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Setup

```bash
# Installera EF Core packages
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
# Eller för PostgreSQL:
dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL
# Eller för SQLite:
dotnet add package Microsoft.EntityFrameworkCore.Sqlite

# EF Core tools för migrations
dotnet tool install --global dotnet-ef
dotnet add package Microsoft.EntityFrameworkCore.Design
```

---

## 💻 Define Models (Entities)

```csharp
// Models/User.cs
public class User
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public string Email { get; set; } = "";
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;

    // Navigation properties
    public ICollection<Order> Orders { get; set; } = new List<Order>();
}

// Models/Order.cs
public class Order
{
    public int Id { get; set; }
    public DateTime OrderDate { get; set; } = DateTime.UtcNow;
    public decimal TotalAmount { get; set; }
    public OrderStatus Status { get; set; } = OrderStatus.Pending;

    // Foreign key
    public int UserId { get; set; }

    // Navigation property
    public User User { get; set; } = null!;
    public ICollection<OrderItem> Items { get; set; } = new List<OrderItem>();
}

public enum OrderStatus
{
    Pending,
    Processing,
    Shipped,
    Delivered,
    Cancelled
}

// Models/OrderItem.cs
public class OrderItem
{
    public int Id { get; set; }
    public string ProductName { get; set; } = "";
    public int Quantity { get; set; }
    public decimal UnitPrice { get; set; }

    public int OrderId { get; set; }
    public Order Order { get; set; } = null!;
}
```

---

## 💻 DbContext

```csharp
// Data/AppDbContext.cs
using Microsoft.EntityFrameworkCore;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options)
    {
    }

    // DbSets represent tables
    public DbSet<User> Users => Set<User>();
    public DbSet<Order> Orders => Set<Order>();
    public DbSet<OrderItem> OrderItems => Set<OrderItem>();

    // Fluent API configuration
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // User configuration
        modelBuilder.Entity<User>(entity =>
        {
            entity.HasKey(u => u.Id);
            entity.Property(u => u.Name).HasMaxLength(100).IsRequired();
            entity.Property(u => u.Email).HasMaxLength(255).IsRequired();
            entity.HasIndex(u => u.Email).IsUnique();
        });

        // Order configuration
        modelBuilder.Entity<Order>(entity =>
        {
            entity.HasKey(o => o.Id);
            entity.Property(o => o.TotalAmount).HasPrecision(18, 2);

            // Relationship
            entity.HasOne(o => o.User)
                  .WithMany(u => u.Orders)
                  .HasForeignKey(o => o.UserId)
                  .OnDelete(DeleteBehavior.Cascade);
        });

        // Seed data
        modelBuilder.Entity<User>().HasData(
            new User { Id = 1, Name = "Admin", Email = "admin@example.com" }
        );
    }
}
```

---

## 💻 Register DbContext

```csharp
// Program.cs
builder.Services.AddDbContext<AppDbContext>(options =>
{
    options.UseSqlServer(
        builder.Configuration.GetConnectionString("DefaultConnection"));

    // Development options
    if (builder.Environment.IsDevelopment())
    {
        options.EnableSensitiveDataLogging();
        options.EnableDetailedErrors();
    }
});

// appsettings.json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=MyApp;Trusted_Connection=true;TrustServerCertificate=true"
  }
}
```

---

## 💻 Migrations

```bash
# Skapa första migration
dotnet ef migrations add InitialCreate

# Genererar fil: Migrations/20241206120000_InitialCreate.cs

# Applicera migration till databas
dotnet ef database update

# Visa SQL utan att köra
dotnet ef migrations script

# Rollback
dotnet ef database update PreviousMigrationName

# Ta bort senaste migration (om inte applicerad)
dotnet ef migrations remove
```

---

## 💻 CRUD Operations

```csharp
// Create
public async Task<User> CreateUserAsync(User user)
{
    _context.Users.Add(user);
    await _context.SaveChangesAsync();
    return user;
}

// Read
public async Task<User?> GetUserAsync(int id)
{
    return await _context.Users
        .Include(u => u.Orders)  // Eager loading
        .FirstOrDefaultAsync(u => u.Id == id);
}

public async Task<List<User>> GetAllUsersAsync()
{
    return await _context.Users
        .OrderBy(u => u.Name)
        .ToListAsync();
}

// Update
public async Task UpdateUserAsync(User user)
{
    _context.Users.Update(user);
    await _context.SaveChangesAsync();
}

// Delete
public async Task DeleteUserAsync(int id)
{
    var user = await _context.Users.FindAsync(id);
    if (user != null)
    {
        _context.Users.Remove(user);
        await _context.SaveChangesAsync();
    }
}
```

---

## ⚠️ Vanliga Problem

### Problem 1: N+1 Query Problem

```csharp
// ❌ N+1 queries
var users = await _context.Users.ToListAsync();
foreach (var user in users)
{
    Console.WriteLine(user.Orders.Count);  // Query per user!
}

// ✅ Eager loading
var users = await _context.Users
    .Include(u => u.Orders)
    .ToListAsync();
```

### Problem 2: Tracking issues

```csharp
// ❌ Tracking conflict
var user = await _context.Users.FindAsync(1);
_context.Users.Update(newUserWithSameId);  // Error!

// ✅ No tracking for read-only
var user = await _context.Users
    .AsNoTracking()
    .FirstOrDefaultAsync(u => u.Id == 1);
```

---

## ✅ Sammanfattning

- **DbContext** är gateway till databasen
- **Migrations** versionerar schema
- **Fluent API** för detaljerad konfiguration
- **Include** för eager loading
- **AsNoTracking** för read-only queries
""",
}


# ============================================================================
# NODE 14: DATABASE QUERIES
# ============================================================================

DOTNET_NODE_14_QUERIES = {
    "node_id": 14,
    "title": "Advanced EF Core Queries",
    "slug": "ef-core-queries",
    "description": "LINQ queries, projections och performance",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 120,
    "topics_covered": [
        "linq", "projections", "filtering", "pagination",
        "raw sql", "stored procedures", "performance"
    ],
    "content": """
# Advanced EF Core Queries

> *"A well-crafted query is worth a thousand optimizations."*

---

## 🎯 Why This Matters

Effektiva databas-queries är kritiska:
- **Performance** - undvik N+1 och over-fetching
- **Scalability** - queries som skalar med data
- **Maintainability** - läsbar, testbar kod

---

## 💻 LINQ Queries

```csharp
// Method syntax (recommended)
var users = await _context.Users
    .Where(u => u.CreatedAt > DateTime.UtcNow.AddDays(-30))
    .OrderByDescending(u => u.CreatedAt)
    .Take(10)
    .ToListAsync();

// Query syntax
var users = await (
    from u in _context.Users
    where u.CreatedAt > DateTime.UtcNow.AddDays(-30)
    orderby u.CreatedAt descending
    select u
).Take(10).ToListAsync();

// Complex filtering
var orders = await _context.Orders
    .Where(o =>
        o.Status == OrderStatus.Pending &&
        o.TotalAmount > 100 &&
        o.User.Email.Contains("@company.com"))
    .ToListAsync();

// String operations
var users = await _context.Users
    .Where(u =>
        EF.Functions.Like(u.Name, "%smith%") ||  // SQL LIKE
        u.Email.StartsWith("admin"))
    .ToListAsync();
```

---

## 💻 Projections (Select)

```csharp
// Project to DTO (avoids loading entire entity)
public record UserDto(int Id, string Name, string Email);

var users = await _context.Users
    .Select(u => new UserDto(u.Id, u.Name, u.Email))
    .ToListAsync();

// Anonymous type projection
var summary = await _context.Users
    .Select(u => new
    {
        u.Id,
        u.Name,
        OrderCount = u.Orders.Count,
        TotalSpent = u.Orders.Sum(o => o.TotalAmount)
    })
    .ToListAsync();

// Conditional projection
var users = await _context.Users
    .Select(u => new UserDto(
        u.Id,
        u.Name,
        u.Email.Contains("@") ? u.Email : "No email"))
    .ToListAsync();
```

---

## 💻 Joins & Relationships

```csharp
// Include (eager loading)
var users = await _context.Users
    .Include(u => u.Orders)
        .ThenInclude(o => o.Items)
    .ToListAsync();

// Filtered include
var users = await _context.Users
    .Include(u => u.Orders.Where(o => o.Status == OrderStatus.Pending))
    .ToListAsync();

// Explicit loading
var user = await _context.Users.FindAsync(1);
await _context.Entry(user)
    .Collection(u => u.Orders)
    .LoadAsync();

// Join (manual)
var query = from u in _context.Users
            join o in _context.Orders on u.Id equals o.UserId
            where o.TotalAmount > 100
            select new { u.Name, o.TotalAmount };
```

---

## 💻 Aggregations

```csharp
// Count
int userCount = await _context.Users.CountAsync();
int activeOrders = await _context.Orders
    .CountAsync(o => o.Status == OrderStatus.Pending);

// Sum, Average, Min, Max
decimal totalRevenue = await _context.Orders.SumAsync(o => o.TotalAmount);
decimal avgOrderValue = await _context.Orders.AverageAsync(o => o.TotalAmount);
decimal maxOrder = await _context.Orders.MaxAsync(o => o.TotalAmount);

// Any, All
bool hasOrders = await _context.Orders.AnyAsync();
bool allShipped = await _context.Orders
    .AllAsync(o => o.Status == OrderStatus.Shipped);

// Group By
var ordersByStatus = await _context.Orders
    .GroupBy(o => o.Status)
    .Select(g => new
    {
        Status = g.Key,
        Count = g.Count(),
        Total = g.Sum(o => o.TotalAmount)
    })
    .ToListAsync();

// Group By with ordering
var topCustomers = await _context.Users
    .Select(u => new
    {
        u.Name,
        TotalOrders = u.Orders.Count,
        TotalSpent = u.Orders.Sum(o => o.TotalAmount)
    })
    .OrderByDescending(x => x.TotalSpent)
    .Take(10)
    .ToListAsync();
```

---

## 💻 Pagination

```csharp
// Basic pagination
public async Task<List<User>> GetUsersPagedAsync(int page, int pageSize)
{
    return await _context.Users
        .OrderBy(u => u.Id)
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .ToListAsync();
}

// With total count
public record PagedResult<T>(List<T> Items, int TotalCount, int Page, int PageSize)
{
    public int TotalPages => (int)Math.Ceiling(TotalCount / (double)PageSize);
    public bool HasPrevious => Page > 1;
    public bool HasNext => Page < TotalPages;
}

public async Task<PagedResult<User>> GetUsersPagedAsync(int page, int pageSize)
{
    var query = _context.Users.OrderBy(u => u.Id);

    var totalCount = await query.CountAsync();
    var items = await query
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .ToListAsync();

    return new PagedResult<User>(items, totalCount, page, pageSize);
}
```

---

## 💻 Raw SQL

```csharp
// Raw SQL query (for complex scenarios)
var users = await _context.Users
    .FromSqlRaw("SELECT * FROM Users WHERE Name LIKE {0}", "%smith%")
    .ToListAsync();

// Interpolated (safe from SQL injection)
var name = "smith";
var users = await _context.Users
    .FromSqlInterpolated($"SELECT * FROM Users WHERE Name LIKE {name}")
    .ToListAsync();

// ExecuteSql for non-query
await _context.Database.ExecuteSqlRawAsync(
    "UPDATE Users SET LastLoginAt = {0} WHERE Id = {1}",
    DateTime.UtcNow, userId);

// Stored procedure
var users = await _context.Users
    .FromSqlRaw("EXEC GetActiveUsers @MinOrders = {0}", 5)
    .ToListAsync();
```

---

## 💻 Query Performance

```csharp
// Use AsNoTracking for read-only
var users = await _context.Users
    .AsNoTracking()  // Faster for read-only
    .ToListAsync();

// Split queries for multiple includes
var users = await _context.Users
    .Include(u => u.Orders)
    .Include(u => u.Addresses)
    .AsSplitQuery()  // Separate queries instead of big JOIN
    .ToListAsync();

// Compiled queries (for hot paths)
private static readonly Func<AppDbContext, int, Task<User?>> GetUserById =
    EF.CompileAsyncQuery((AppDbContext ctx, int id) =>
        ctx.Users.FirstOrDefault(u => u.Id == id));

public Task<User?> GetUserAsync(int id) => GetUserById(_context, id);
```

---

## ⚠️ Vanliga Problem

### Problem 1: Client evaluation

```csharp
// ❌ Runs on client (loads ALL data first!)
var users = await _context.Users
    .ToListAsync()
    .Where(u => SomeComplexMethod(u.Name));

// ✅ Database evaluation
var users = await _context.Users
    .Where(u => u.Name.Contains("smith"))
    .ToListAsync();
```

---

## ✅ Sammanfattning

- **Projections** minskar data transfer
- **Include** för eager loading
- **AsNoTracking** för read-only
- **Pagination** med Skip/Take
- **Compiled queries** för hot paths
""",
}


# ============================================================================
# NODE 15: REST API DESIGN
# ============================================================================

DOTNET_NODE_15_REST_API = {
    "node_id": 15,
    "title": "REST API Design",
    "slug": "aspnet-rest-api",
    "description": "Designa och implementera RESTful APIs",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "rest", "http methods", "status codes", "dto",
        "api versioning", "hateoas", "documentation"
    ],
    "content": """
# REST API Design

> *"A well-designed API is a love letter to your future self."*

---

## 🎯 Why This Matters

Bra API design ger:
- **Developer experience** - lätt att förstå och använda
- **Maintainability** - enkel att utvida
- **Consistency** - förutsägbart beteende

---

## 🧠 REST Principles

```
┌─────────────────────────────────────────────────────────────────┐
│                    REST API DESIGN                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  RESOURCE-BASED URLS                                            │
│  ────────────────────────────────────────────────────────────   │
│  ✅ /api/users                  (noun, plural)                  │
│  ✅ /api/users/123              (specific resource)             │
│  ✅ /api/users/123/orders       (nested resource)               │
│  ❌ /api/getUsers               (verb in URL)                   │
│  ❌ /api/user                   (singular)                      │
│                                                                  │
│  HTTP METHODS                                                   │
│  ────────────────────────────────────────────────────────────   │
│  GET      /api/users           → List users                     │
│  GET      /api/users/123       → Get user 123                   │
│  POST     /api/users           → Create user                    │
│  PUT      /api/users/123       → Replace user 123               │
│  PATCH    /api/users/123       → Update user 123 (partial)      │
│  DELETE   /api/users/123       → Delete user 123                │
│                                                                  │
│  STATUS CODES                                                   │
│  ────────────────────────────────────────────────────────────   │
│  200 OK              → Success with body                        │
│  201 Created         → Resource created (POST)                  │
│  204 No Content      → Success without body (DELETE)            │
│  400 Bad Request     → Client error (validation)                │
│  401 Unauthorized    → Not authenticated                        │
│  403 Forbidden       → Authenticated but not allowed            │
│  404 Not Found       → Resource doesn't exist                   │
│  409 Conflict        → Resource conflict                        │
│  422 Unprocessable   → Validation failed                        │
│  500 Server Error    → Unexpected error                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 DTOs (Data Transfer Objects)

```csharp
// Request DTOs
public record CreateUserRequest(
    string Name,
    string Email,
    string Password
);

public record UpdateUserRequest(
    string? Name,
    string? Email
);

// Response DTOs
public record UserResponse(
    int Id,
    string Name,
    string Email,
    DateTime CreatedAt
);

public record UserDetailResponse(
    int Id,
    string Name,
    string Email,
    DateTime CreatedAt,
    List<OrderSummary> RecentOrders
);

public record OrderSummary(
    int Id,
    DateTime OrderDate,
    decimal TotalAmount,
    string Status
);

// Mapping (manual)
public static UserResponse ToResponse(this User user) => new(
    user.Id,
    user.Name,
    user.Email,
    user.CreatedAt
);

// Or use AutoMapper
// builder.Services.AddAutoMapper(typeof(MappingProfile));
```

---

## 💻 Complete CRUD Controller

```csharp
[ApiController]
[Route("api/[controller]")]
[Produces("application/json")]
public class UsersController : ControllerBase
{
    private readonly IUserService _userService;

    public UsersController(IUserService userService)
    {
        _userService = userService;
    }

    /// <summary>
    /// Get all users with optional filtering
    /// </summary>
    [HttpGet]
    [ProducesResponseType(typeof(List<UserResponse>), 200)]
    public async Task<ActionResult<List<UserResponse>>> GetUsers(
        [FromQuery] string? search,
        [FromQuery] int page = 1,
        [FromQuery] int pageSize = 20)
    {
        var users = await _userService.GetUsersAsync(search, page, pageSize);
        return Ok(users.Select(u => u.ToResponse()));
    }

    /// <summary>
    /// Get a specific user by ID
    /// </summary>
    [HttpGet("{id}")]
    [ProducesResponseType(typeof(UserDetailResponse), 200)]
    [ProducesResponseType(404)]
    public async Task<ActionResult<UserDetailResponse>> GetUser(int id)
    {
        var user = await _userService.GetUserAsync(id);

        if (user is null)
            return NotFound();

        return Ok(user.ToDetailResponse());
    }

    /// <summary>
    /// Create a new user
    /// </summary>
    [HttpPost]
    [ProducesResponseType(typeof(UserResponse), 201)]
    [ProducesResponseType(typeof(ValidationProblemDetails), 400)]
    public async Task<ActionResult<UserResponse>> CreateUser(
        CreateUserRequest request)
    {
        var user = await _userService.CreateUserAsync(request);

        return CreatedAtAction(
            nameof(GetUser),
            new { id = user.Id },
            user.ToResponse());
    }

    /// <summary>
    /// Update an existing user
    /// </summary>
    [HttpPut("{id}")]
    [ProducesResponseType(typeof(UserResponse), 200)]
    [ProducesResponseType(404)]
    public async Task<ActionResult<UserResponse>> UpdateUser(
        int id,
        UpdateUserRequest request)
    {
        var user = await _userService.UpdateUserAsync(id, request);

        if (user is null)
            return NotFound();

        return Ok(user.ToResponse());
    }

    /// <summary>
    /// Delete a user
    /// </summary>
    [HttpDelete("{id}")]
    [ProducesResponseType(204)]
    [ProducesResponseType(404)]
    public async Task<IActionResult> DeleteUser(int id)
    {
        var deleted = await _userService.DeleteUserAsync(id);

        if (!deleted)
            return NotFound();

        return NoContent();
    }
}
```

---

## 💻 Minimal API Version

```csharp
// Program.cs - samma funktionalitet, mindre kod
var users = app.MapGroup("/api/users")
    .WithTags("Users");

users.MapGet("/", async (
    IUserService service,
    string? search,
    int page = 1,
    int pageSize = 20) =>
{
    var result = await service.GetUsersAsync(search, page, pageSize);
    return Results.Ok(result.Select(u => u.ToResponse()));
});

users.MapGet("/{id}", async (int id, IUserService service) =>
{
    var user = await service.GetUserAsync(id);
    return user is null
        ? Results.NotFound()
        : Results.Ok(user.ToDetailResponse());
});

users.MapPost("/", async (CreateUserRequest request, IUserService service) =>
{
    var user = await service.CreateUserAsync(request);
    return Results.Created($"/api/users/{user.Id}", user.ToResponse());
});

users.MapPut("/{id}", async (int id, UpdateUserRequest request, IUserService service) =>
{
    var user = await service.UpdateUserAsync(id, request);
    return user is null ? Results.NotFound() : Results.Ok(user.ToResponse());
});

users.MapDelete("/{id}", async (int id, IUserService service) =>
{
    var deleted = await service.DeleteUserAsync(id);
    return deleted ? Results.NoContent() : Results.NotFound();
});
```

---

## 💻 API Versioning

```csharp
// Install: Asp.Versioning.Http
builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;

    // Version in URL: /api/v1/users
    options.ApiVersionReader = new UrlSegmentApiVersionReader();
});

// Version via route
app.MapGet("/api/v{version:apiVersion}/users", () => "V1 users")
    .WithApiVersionSet(versionSet)
    .MapToApiVersion(1.0);

app.MapGet("/api/v{version:apiVersion}/users", () => "V2 users with new fields")
    .WithApiVersionSet(versionSet)
    .MapToApiVersion(2.0);
```

---

## ⚠️ Vanliga Problem

### Problem 1: Exposing internal models

```csharp
// ❌ Returnerar entity direkt
[HttpGet("{id}")]
public Task<User> GetUser(int id) => _context.Users.FindAsync(id);

// ✅ Returnera DTO
[HttpGet("{id}")]
public async Task<UserResponse?> GetUser(int id)
{
    var user = await _context.Users.FindAsync(id);
    return user?.ToResponse();
}
```

---

## ✅ Sammanfattning

- **Resource-based URLs** - nouns, not verbs
- **HTTP methods** för CRUD
- **DTOs** separerar API från domain
- **Status codes** kommunicerar resultat
- **Versioning** för backward compatibility
""",
}


# ============================================================================
# NODE 16: VALIDATION & ERROR HANDLING
# ============================================================================

DOTNET_NODE_16_VALIDATION = {
    "node_id": 16,
    "title": "Validation & Error Handling",
    "slug": "aspnet-validation",
    "description": "Input validation, FluentValidation och felhantering",
    "difficulty": "intermediate",
    "estimated_minutes": 55,
    "xp_reward": 110,
    "topics_covered": [
        "data annotations", "fluent validation", "model state",
        "problem details", "exception handling", "logging"
    ],
    "content": """
# Validation & Error Handling

> *"Never trust user input. Validate everything."*

---

## 🎯 Why This Matters

Validering och felhantering ger:
- **Security** - förhindra injection, overflow
- **Data integrity** - korrekt data i databas
- **User experience** - tydliga felmeddelanden

---

## 💻 Data Annotations

```csharp
using System.ComponentModel.DataAnnotations;

public record CreateUserRequest
{
    [Required(ErrorMessage = "Name is required")]
    [StringLength(100, MinimumLength = 2)]
    public string Name { get; init; } = "";

    [Required]
    [EmailAddress(ErrorMessage = "Invalid email format")]
    public string Email { get; init; } = "";

    [Required]
    [MinLength(8, ErrorMessage = "Password must be at least 8 characters")]
    [RegularExpression(@"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$",
        ErrorMessage = "Password must contain uppercase, lowercase, and number")]
    public string Password { get; init; } = "";

    [Range(18, 120, ErrorMessage = "Age must be between 18 and 120")]
    public int Age { get; init; }

    [Url(ErrorMessage = "Invalid URL format")]
    public string? Website { get; init; }

    [Phone]
    public string? Phone { get; init; }
}

// Controller validates automatically
[HttpPost]
public ActionResult<UserResponse> CreateUser(CreateUserRequest request)
{
    // ModelState is checked automatically by [ApiController]
    // Invalid requests return 400 with validation errors

    var user = _service.CreateUser(request);
    return Created($"/api/users/{user.Id}", user);
}
```

---

## 💻 FluentValidation (Recommended)

```bash
dotnet add package FluentValidation.AspNetCore
```

```csharp
// Validators/CreateUserRequestValidator.cs
using FluentValidation;

public class CreateUserRequestValidator : AbstractValidator<CreateUserRequest>
{
    private readonly IUserRepository _userRepository;

    public CreateUserRequestValidator(IUserRepository userRepository)
    {
        _userRepository = userRepository;

        RuleFor(x => x.Name)
            .NotEmpty().WithMessage("Name is required")
            .Length(2, 100).WithMessage("Name must be 2-100 characters")
            .Matches(@"^[a-zA-Z\\s]+$").WithMessage("Name can only contain letters");

        RuleFor(x => x.Email)
            .NotEmpty().WithMessage("Email is required")
            .EmailAddress().WithMessage("Invalid email format")
            .MustAsync(BeUniqueEmail).WithMessage("Email already exists");

        RuleFor(x => x.Password)
            .NotEmpty()
            .MinimumLength(8)
            .Matches(@"[A-Z]").WithMessage("Password must contain uppercase")
            .Matches(@"[a-z]").WithMessage("Password must contain lowercase")
            .Matches(@"[0-9]").WithMessage("Password must contain number");

        RuleFor(x => x.Age)
            .InclusiveBetween(18, 120);

        // Conditional validation
        When(x => !string.IsNullOrEmpty(x.Website), () =>
        {
            RuleFor(x => x.Website).Must(BeValidUrl);
        });
    }

    private async Task<bool> BeUniqueEmail(string email, CancellationToken ct)
    {
        return !await _userRepository.EmailExistsAsync(email);
    }

    private bool BeValidUrl(string? url)
    {
        return Uri.TryCreate(url, UriKind.Absolute, out _);
    }
}

// Registration
builder.Services.AddValidatorsFromAssemblyContaining<CreateUserRequestValidator>();
```

---

## 💻 Manual Validation

```csharp
// Inject validator
app.MapPost("/api/users", async (
    CreateUserRequest request,
    IValidator<CreateUserRequest> validator,
    IUserService service) =>
{
    var validationResult = await validator.ValidateAsync(request);

    if (!validationResult.IsValid)
    {
        return Results.ValidationProblem(
            validationResult.ToDictionary());
    }

    var user = await service.CreateUserAsync(request);
    return Results.Created($"/api/users/{user.Id}", user);
});

// Auto-validation with filter
builder.Services.AddValidatorsFromAssemblyContaining<Program>();

app.MapPost("/api/users", async (CreateUserRequest request, IUserService service) =>
{
    var user = await service.CreateUserAsync(request);
    return Results.Created($"/api/users/{user.Id}", user);
})
.AddEndpointFilter<ValidationFilter<CreateUserRequest>>();
```

---

## 💻 Problem Details (RFC 7807)

```csharp
// Configure problem details
builder.Services.AddProblemDetails(options =>
{
    options.CustomizeProblemDetails = context =>
    {
        context.ProblemDetails.Instance = context.HttpContext.Request.Path;
        context.ProblemDetails.Extensions["traceId"] =
            context.HttpContext.TraceIdentifier;
    };
});

// Custom problem response
public static IResult ValidationProblem(IDictionary<string, string[]> errors)
{
    return Results.Problem(
        title: "Validation failed",
        statusCode: 400,
        detail: "One or more validation errors occurred",
        extensions: new Dictionary<string, object?>
        {
            ["errors"] = errors
        });
}

// Response format:
// {
//     "type": "https://tools.ietf.org/html/rfc7231#section-6.5.1",
//     "title": "Validation failed",
//     "status": 400,
//     "detail": "One or more validation errors occurred",
//     "instance": "/api/users",
//     "traceId": "00-abc123...",
//     "errors": {
//         "Name": ["Name is required"],
//         "Email": ["Invalid email format"]
//     }
// }
```

---

## 💻 Global Exception Handling

```csharp
// Custom exceptions
public class NotFoundException : Exception
{
    public NotFoundException(string message) : base(message) { }
}

public class ConflictException : Exception
{
    public ConflictException(string message) : base(message) { }
}

// Exception handler middleware
app.UseExceptionHandler(errorApp =>
{
    errorApp.Run(async context =>
    {
        var exception = context.Features.Get<IExceptionHandlerFeature>()?.Error;
        var logger = context.RequestServices.GetRequiredService<ILogger<Program>>();

        logger.LogError(exception, "Unhandled exception");

        var (statusCode, title) = exception switch
        {
            NotFoundException => (404, "Resource not found"),
            ConflictException => (409, "Resource conflict"),
            UnauthorizedAccessException => (401, "Unauthorized"),
            ArgumentException => (400, "Bad request"),
            _ => (500, "An error occurred")
        };

        context.Response.StatusCode = statusCode;
        context.Response.ContentType = "application/problem+json";

        await context.Response.WriteAsJsonAsync(new
        {
            type = $"https://httpstatuses.com/{statusCode}",
            title = title,
            status = statusCode,
            detail = exception?.Message,
            instance = context.Request.Path.Value,
            traceId = context.TraceIdentifier
        });
    });
});
```

---

## ⚠️ Vanliga Problem

### Problem 1: Exposing stack traces

```csharp
// ❌ Never in production
catch (Exception ex)
{
    return BadRequest(ex.ToString());  // Exposes internals!
}

// ✅ Generic message + logging
catch (Exception ex)
{
    _logger.LogError(ex, "Error processing request");
    return StatusCode(500, "An error occurred");
}
```

---

## ✅ Sammanfattning

- **Data Annotations** för enkel validering
- **FluentValidation** för komplex validering
- **Problem Details** för standardiserade fel
- **Global exception handler** för oväntade fel
- **Logga allt**, visa lite för användaren
""",
}


# Export all nodes from Block 4
BLOCK_4_NODES = [
    DOTNET_NODE_13_EF_CORE,
    DOTNET_NODE_14_QUERIES,
    DOTNET_NODE_15_REST_API,
    DOTNET_NODE_16_VALIDATION,
]
