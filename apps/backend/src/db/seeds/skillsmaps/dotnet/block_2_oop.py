"""
C# & .NET SkillsMap - Block 2: Object-Oriented Programming
Nodes 5-8: Classes, Inheritance, Interfaces, Generics
"""

from typing import Any

# ============================================================================
# NODE 5: CLASSES & OBJECTS
# ============================================================================

DOTNET_NODE_5_CLASSES = {
    "node_id": 5,
    "title": "Classes & Objects",
    "slug": "csharp-classes-objects",
    "description": "Klasser, objekt, properties och constructors",
    "difficulty": "beginner",
    "estimated_minutes": 60,
    "xp_reward": 110,
    "topics_covered": [
        "classes", "objects", "properties", "constructors",
        "access modifiers", "fields", "auto-properties"
    ],
    "content": """
# Classes & Objects

> *"A class is a blueprint, an object is a building made from that blueprint."*

---

## 🎯 Why This Matters

OOP är paradigmen som C# är byggt kring:
- **Encapsulation** - gruppera data och beteende
- **Abstraction** - gömma implementation
- **Maintainability** - organiserad, modulär kod

---

## 🧠 Class Anatomy

```
┌─────────────────────────────────────────────────────────────────┐
│                       CLASS ANATOMY                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  public class Person                                            │
│  {                                                              │
│      // FIELDS (private data)                                   │
│      private string _name;                                      │
│      private int _age;                                          │
│                                                                  │
│      // PROPERTIES (controlled access)                          │
│      public string Name                                         │
│      {                                                          │
│          get => _name;                                          │
│          set => _name = value ?? throw new ArgumentException(); │
│      }                                                          │
│                                                                  │
│      // CONSTRUCTOR (initialization)                            │
│      public Person(string name, int age)                        │
│      {                                                          │
│          _name = name;                                          │
│          _age = age;                                            │
│      }                                                          │
│                                                                  │
│      // METHODS (behavior)                                      │
│      public void Greet() => Console.WriteLine($"Hi, I'm {Name}");│
│  }                                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Basic Class

```csharp
public class Person
{
    // Fields (private by convention)
    private string _firstName;
    private string _lastName;

    // Auto-implemented properties (most common)
    public int Age { get; set; }
    public string Email { get; set; } = "";  // With default

    // Read-only property
    public string FullName => $"{_firstName} {_lastName}";

    // Property with validation
    public string FirstName
    {
        get => _firstName;
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new ArgumentException("Name cannot be empty");
            _firstName = value;
        }
    }

    // Init-only property (can only set in constructor or initializer)
    public Guid Id { get; init; } = Guid.NewGuid();

    // Constructor
    public Person(string firstName, string lastName)
    {
        FirstName = firstName;
        _lastName = lastName;
    }

    // Method
    public void Introduce()
    {
        Console.WriteLine($"Hi, I'm {FullName}, {Age} years old.");
    }
}

// Usage
var person = new Person("Alice", "Smith") { Age = 25 };
person.Introduce();
Console.WriteLine(person.Id);
```

---

## 💻 Constructors

```csharp
public class Product
{
    public string Name { get; }
    public decimal Price { get; set; }
    public int Stock { get; set; }

    // Primary constructor (.NET 8+)
    // public class Product(string name, decimal price);

    // Default constructor
    public Product()
    {
        Name = "Unknown";
        Price = 0;
    }

    // Parameterized constructor
    public Product(string name, decimal price)
    {
        Name = name;
        Price = price;
    }

    // Constructor chaining
    public Product(string name) : this(name, 0)
    {
        // Additional initialization
    }

    // Copy constructor
    public Product(Product other)
    {
        Name = other.Name;
        Price = other.Price;
        Stock = other.Stock;
    }
}

// Usage
var p1 = new Product();                    // Default
var p2 = new Product("Laptop", 999.99m);   // Parameterized
var p3 = new Product("Phone");             // Chained
var p4 = new Product(p2);                  // Copy
```

---

## 💻 Access Modifiers

```csharp
public class BankAccount
{
    // private - only this class
    private decimal _balance;

    // protected - this class and derived classes
    protected string AccountType;

    // internal - same assembly
    internal string BankCode;

    // public - everywhere
    public string AccountNumber { get; }

    // protected internal - same assembly OR derived classes
    protected internal void LogTransaction() { }

    // private protected - same assembly AND derived classes
    private protected void InternalAudit() { }
}
```

### Access Modifier Summary

| Modifier | Same Class | Derived (Same Assembly) | Same Assembly | Derived (Other Assembly) | Other Assembly |
|----------|:----------:|:-----------------------:|:-------------:|:------------------------:|:--------------:|
| `private` | ✅ | ❌ | ❌ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ❌ | ✅ | ❌ |
| `internal` | ✅ | ✅ | ✅ | ❌ | ❌ |
| `protected internal` | ✅ | ✅ | ✅ | ✅ | ❌ |
| `private protected` | ✅ | ✅ | ❌ | ❌ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 💻 Static Members

```csharp
public class Counter
{
    // Static field - shared across all instances
    private static int _instanceCount = 0;

    // Static property
    public static int InstanceCount => _instanceCount;

    // Instance property
    public int Id { get; }

    public Counter()
    {
        _instanceCount++;
        Id = _instanceCount;
    }

    // Static method
    public static void ResetCount() => _instanceCount = 0;
}

// Usage
var c1 = new Counter();  // Id: 1
var c2 = new Counter();  // Id: 2
Console.WriteLine(Counter.InstanceCount);  // 2
Counter.ResetCount();
```

---

## 💻 Records (Immutable Data Classes)

```csharp
// Record - immutable by default, value equality
public record Person(string FirstName, string LastName, int Age);

// Usage
var p1 = new Person("Alice", "Smith", 25);
var p2 = new Person("Alice", "Smith", 25);

Console.WriteLine(p1 == p2);  // true (value equality)

// With-expression (creates copy with changes)
var p3 = p1 with { Age = 26 };

// Deconstruction
var (first, last, age) = p1;

// Record with additional members
public record Employee(string Name, string Department)
{
    public DateTime HireDate { get; init; } = DateTime.Now;

    public void Print() => Console.WriteLine($"{Name} - {Department}");
}
```

---

## ⚠️ Vanliga Problem

### Problem 1: Null reference i properties

```csharp
// ❌ Dåligt
public class User
{
    public string Name { get; set; }  // Can be null!
}

// ✅ Bättre - required eller nullable
public class User
{
    public required string Name { get; set; }  // Must be set
}

// Eller explicit nullable
public class User
{
    public string? Name { get; set; }  // Explicitly nullable
}
```

### Problem 2: Mutable state

```csharp
// ❌ Risk för oväntade ändringar
public class Order
{
    public List<string> Items { get; set; } = new();
}

// ✅ Encapsulate mutations
public class Order
{
    private readonly List<string> _items = new();
    public IReadOnlyList<string> Items => _items;

    public void AddItem(string item) => _items.Add(item);
}
```

---

## ✅ Sammanfattning

- **Classes** kapslar in data och beteende
- **Properties** ger kontrollerad åtkomst
- **Constructors** initialiserar objekt
- **Records** för immutable data med value equality
- **Access modifiers** styr synlighet
""",
}


# ============================================================================
# NODE 6: INHERITANCE & POLYMORPHISM
# ============================================================================

DOTNET_NODE_6_INHERITANCE = {
    "node_id": 6,
    "title": "Inheritance & Polymorphism",
    "slug": "csharp-inheritance",
    "description": "Arv, virtuella metoder och polymorfism",
    "difficulty": "intermediate",
    "estimated_minutes": 65,
    "xp_reward": 120,
    "topics_covered": [
        "inheritance", "virtual", "override", "abstract",
        "sealed", "base", "polymorphism"
    ],
    "content": """
# Inheritance & Polymorphism

> *"Favor composition over inheritance, but know when inheritance is the right tool."*

---

## 🎯 Why This Matters

Arv möjliggör:
- **Code reuse** - återanvänd basklass-kod
- **Polymorphism** - behandla olika typer enhetligt
- **Extensibility** - utöka utan att modifiera

---

## 🧠 Inheritance Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    INHERITANCE HIERARCHY                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                        Animal (base)                            │
│                    ┌──────┴──────┐                              │
│                    │             │                               │
│                  Dog           Cat                               │
│                   │                                              │
│              GermanShepherd                                      │
│                                                                  │
│  ══════════════════════════════════════════════════════════     │
│  Animal animal = new Dog();  // Polymorphism!                   │
│  animal.MakeSound();         // Calls Dog's implementation      │
│  ══════════════════════════════════════════════════════════     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Basic Inheritance

```csharp
// Base class
public class Animal
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Animal(string name)
    {
        Name = name;
    }

    public void Eat()
    {
        Console.WriteLine($"{Name} is eating.");
    }

    // Virtual - can be overridden
    public virtual void MakeSound()
    {
        Console.WriteLine("Some generic sound");
    }
}

// Derived class
public class Dog : Animal
{
    public string Breed { get; set; }

    // Call base constructor
    public Dog(string name, string breed) : base(name)
    {
        Breed = breed;
    }

    // Override virtual method
    public override void MakeSound()
    {
        Console.WriteLine("Woof!");
    }

    // New method (specific to Dog)
    public void Fetch()
    {
        Console.WriteLine($"{Name} is fetching.");
    }
}

// Usage
Dog dog = new Dog("Max", "Labrador");
dog.Eat();        // From Animal
dog.MakeSound();  // Overridden: "Woof!"
dog.Fetch();      // Dog-specific

// Polymorphism
Animal animal = dog;
animal.MakeSound();  // Still "Woof!" (runtime dispatch)
// animal.Fetch();   // ❌ Not accessible through Animal reference
```

---

## 💻 Abstract Classes

```csharp
// Abstract - cannot be instantiated
public abstract class Shape
{
    public string Color { get; set; }

    protected Shape(string color)
    {
        Color = color;
    }

    // Abstract method - MUST be implemented by derived classes
    public abstract double CalculateArea();

    // Virtual method - CAN be overridden
    public virtual void Draw()
    {
        Console.WriteLine($"Drawing a {Color} shape");
    }

    // Regular method - inherited as-is
    public void PrintInfo()
    {
        Console.WriteLine($"Area: {CalculateArea()}");
    }
}

public class Circle : Shape
{
    public double Radius { get; set; }

    public Circle(string color, double radius) : base(color)
    {
        Radius = radius;
    }

    // Must implement abstract method
    public override double CalculateArea()
    {
        return Math.PI * Radius * Radius;
    }
}

public class Rectangle : Shape
{
    public double Width { get; set; }
    public double Height { get; set; }

    public Rectangle(string color, double width, double height) : base(color)
    {
        Width = width;
        Height = height;
    }

    public override double CalculateArea()
    {
        return Width * Height;
    }

    public override void Draw()
    {
        base.Draw();  // Call base implementation
        Console.WriteLine($"Rectangle: {Width}x{Height}");
    }
}

// Usage
// Shape s = new Shape("red");  // ❌ Cannot instantiate abstract
Shape circle = new Circle("red", 5);
Shape rect = new Rectangle("blue", 4, 3);

circle.PrintInfo();  // Area: 78.54...
rect.PrintInfo();    // Area: 12
```

---

## 💻 Sealed Classes

```csharp
// Sealed - cannot be inherited
public sealed class SecureConnection
{
    public void Connect() { }
}

// ❌ Error: cannot inherit from sealed
// public class MyConnection : SecureConnection { }

// Sealed method - prevent further override
public class Animal
{
    public virtual void Move() { }
}

public class Bird : Animal
{
    public sealed override void Move()
    {
        Console.WriteLine("Flying");
    }
}

public class Penguin : Bird
{
    // ❌ Error: cannot override sealed
    // public override void Move() { }
}
```

---

## 💻 Polymorphism in Practice

```csharp
public abstract class Employee
{
    public string Name { get; set; }
    public decimal BaseSalary { get; set; }

    public abstract decimal CalculatePayment();
}

public class FullTimeEmployee : Employee
{
    public decimal Bonus { get; set; }

    public override decimal CalculatePayment()
    {
        return BaseSalary + Bonus;
    }
}

public class Contractor : Employee
{
    public int HoursWorked { get; set; }
    public decimal HourlyRate { get; set; }

    public override decimal CalculatePayment()
    {
        return HoursWorked * HourlyRate;
    }
}

// Polymorphic usage
List<Employee> employees = new()
{
    new FullTimeEmployee { Name = "Alice", BaseSalary = 5000, Bonus = 500 },
    new Contractor { Name = "Bob", HoursWorked = 160, HourlyRate = 50 }
};

decimal totalPayroll = 0;
foreach (Employee emp in employees)
{
    decimal payment = emp.CalculatePayment();  // Polymorphic call
    Console.WriteLine($"{emp.Name}: {payment:C}");
    totalPayroll += payment;
}
Console.WriteLine($"Total: {totalPayroll:C}");
```

---

## 💻 Type Checking

```csharp
Animal animal = new Dog("Max", "Labrador");

// is operator
if (animal is Dog)
{
    Console.WriteLine("It's a dog!");
}

// is with pattern matching
if (animal is Dog dog)
{
    Console.WriteLine($"Dog breed: {dog.Breed}");
}

// as operator (returns null if cast fails)
Dog? maybeDog = animal as Dog;
if (maybeDog != null)
{
    maybeDog.Fetch();
}

// Direct cast (throws if fails)
Dog definitelyDog = (Dog)animal;
```

---

## ⚠️ Vanliga Problem

### Problem 1: Forgetting virtual/override

```csharp
// ❌ Hiding, not overriding
public class Animal
{
    public void Speak() => Console.WriteLine("...");
}

public class Dog : Animal
{
    public new void Speak() => Console.WriteLine("Woof!");  // Hiding!
}

Animal a = new Dog();
a.Speak();  // "..." - NOT "Woof!"

// ✅ Proper override
public class Animal
{
    public virtual void Speak() => Console.WriteLine("...");
}

public class Dog : Animal
{
    public override void Speak() => Console.WriteLine("Woof!");
}
```

---

## ✅ Sammanfattning

- **Inheritance** med `:` syntax
- **virtual/override** för polymorfism
- **abstract** tvingar implementation
- **sealed** förhindrar arv
- **Favor composition** för flexibilitet
""",
}


# ============================================================================
# NODE 7: INTERFACES
# ============================================================================

DOTNET_NODE_7_INTERFACES = {
    "node_id": 7,
    "title": "Interfaces & Abstraction",
    "slug": "csharp-interfaces",
    "description": "Interfaces, multiple inheritance och SOLID",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 120,
    "topics_covered": [
        "interfaces", "implementation", "multiple interfaces",
        "default implementation", "dependency injection"
    ],
    "content": """
# Interfaces & Abstraction

> *"Program to an interface, not an implementation."* — Gang of Four

---

## 🎯 Why This Matters

Interfaces är fundamentala för:
- **Loose coupling** - byt implementation utan att ändra kod
- **Testability** - mocka beroenden enkelt
- **SOLID principles** - särskilt D (Dependency Inversion)

---

## 🧠 Interface vs Abstract Class

```
┌─────────────────────────────────────────────────────────────────┐
│            INTERFACE vs ABSTRACT CLASS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INTERFACE                     │  ABSTRACT CLASS                │
│  ─────────────────────────────┼───────────────────────────────  │
│  Defines contract (what)      │  Defines template (how)         │
│  No state (before C# 8)       │  Can have state (fields)        │
│  Multiple inheritance OK      │  Single inheritance only        │
│  All members public           │  Any access modifier            │
│  Default implementations OK   │  Mix of abstract & concrete     │
│                                                                  │
│  Use when:                    │  Use when:                       │
│  - Unrelated classes          │  - Related classes (is-a)       │
│  - Multiple behaviors         │  - Shared implementation        │
│  - API contracts              │  - Base behavior + extension    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Basic Interface

```csharp
// Interface definition
public interface IVehicle
{
    // Properties
    string Model { get; }
    int Speed { get; set; }

    // Methods
    void Start();
    void Stop();

    // Default implementation (C# 8+)
    void Honk() => Console.WriteLine("Beep!");
}

// Implementation
public class Car : IVehicle
{
    public string Model { get; }
    public int Speed { get; set; }

    public Car(string model)
    {
        Model = model;
    }

    public void Start()
    {
        Console.WriteLine($"{Model} engine started.");
    }

    public void Stop()
    {
        Speed = 0;
        Console.WriteLine($"{Model} stopped.");
    }

    // Can override default implementation
    public void Honk()
    {
        Console.WriteLine("Beep beep!");
    }
}

// Usage
IVehicle vehicle = new Car("Toyota");
vehicle.Start();
vehicle.Honk();
```

---

## 💻 Multiple Interfaces

```csharp
public interface IFlyable
{
    void Fly();
}

public interface ISwimmable
{
    void Swim();
}

public interface IWalkable
{
    void Walk();
}

// Duck implements multiple interfaces
public class Duck : IFlyable, ISwimmable, IWalkable
{
    public void Fly() => Console.WriteLine("Duck is flying");
    public void Swim() => Console.WriteLine("Duck is swimming");
    public void Walk() => Console.WriteLine("Duck is walking");
}

// Usage - treat duck as different types
Duck duck = new Duck();
IFlyable flyer = duck;
ISwimmable swimmer = duck;

flyer.Fly();
swimmer.Swim();
```

---

## 💻 Interface Segregation

```csharp
// ❌ Fat interface - violates ISP
public interface IWorker
{
    void Work();
    void Eat();
    void Sleep();
    void Code();
    void Manage();
}

// ✅ Segregated interfaces
public interface IWorkable
{
    void Work();
}

public interface IFeedable
{
    void Eat();
}

public interface ICodable
{
    void Code();
}

public interface IManageable
{
    void Manage();
}

// Combine what's needed
public class Developer : IWorkable, IFeedable, ICodable
{
    public void Work() => Console.WriteLine("Working...");
    public void Eat() => Console.WriteLine("Eating...");
    public void Code() => Console.WriteLine("Coding...");
}

public class Manager : IWorkable, IFeedable, IManageable
{
    public void Work() => Console.WriteLine("Working...");
    public void Eat() => Console.WriteLine("Eating...");
    public void Manage() => Console.WriteLine("Managing...");
}
```

---

## 💻 Dependency Injection Pattern

```csharp
// Interface
public interface IEmailService
{
    Task SendAsync(string to, string subject, string body);
}

// Implementation
public class SmtpEmailService : IEmailService
{
    public async Task SendAsync(string to, string subject, string body)
    {
        // Real SMTP implementation
        Console.WriteLine($"Sending email to {to}");
        await Task.Delay(100);  // Simulate
    }
}

// Consumer - depends on interface, not implementation
public class OrderService
{
    private readonly IEmailService _emailService;

    // Inject dependency through constructor
    public OrderService(IEmailService emailService)
    {
        _emailService = emailService;
    }

    public async Task PlaceOrderAsync(Order order)
    {
        // Process order...
        await _emailService.SendAsync(
            order.CustomerEmail,
            "Order Confirmation",
            $"Your order #{order.Id} has been placed."
        );
    }
}

// Usage
IEmailService emailService = new SmtpEmailService();
var orderService = new OrderService(emailService);

// For testing - use mock
public class MockEmailService : IEmailService
{
    public List<string> SentEmails { get; } = new();

    public Task SendAsync(string to, string subject, string body)
    {
        SentEmails.Add($"{to}: {subject}");
        return Task.CompletedTask;
    }
}
```

---

## 💻 Generic Interfaces

```csharp
// Generic interface
public interface IRepository<T> where T : class
{
    Task<T?> GetByIdAsync(int id);
    Task<IEnumerable<T>> GetAllAsync();
    Task AddAsync(T entity);
    Task UpdateAsync(T entity);
    Task DeleteAsync(int id);
}

// Implementation
public class UserRepository : IRepository<User>
{
    private readonly List<User> _users = new();

    public Task<User?> GetByIdAsync(int id)
        => Task.FromResult(_users.FirstOrDefault(u => u.Id == id));

    public Task<IEnumerable<User>> GetAllAsync()
        => Task.FromResult(_users.AsEnumerable());

    public Task AddAsync(User user)
    {
        _users.Add(user);
        return Task.CompletedTask;
    }

    public Task UpdateAsync(User user)
    {
        var existing = _users.FirstOrDefault(u => u.Id == user.Id);
        if (existing != null)
        {
            existing.Name = user.Name;
        }
        return Task.CompletedTask;
    }

    public Task DeleteAsync(int id)
    {
        _users.RemoveAll(u => u.Id == id);
        return Task.CompletedTask;
    }
}
```

---

## ⚠️ Vanliga Problem

### Problem 1: Leaking implementation details

```csharp
// ❌ Implementation leaked
public interface IUserService
{
    SqlConnection GetConnection();  // Implementation detail!
}

// ✅ Abstract away implementation
public interface IUserService
{
    Task<User?> GetUserAsync(int id);
}
```

---

## ✅ Sammanfattning

- **Interfaces** definierar kontrakt
- **Multiple interfaces** möjliggör flexibilitet
- **Dependency Injection** för loose coupling
- **Generic interfaces** för återanvändbarhet
- **Segregera** interfaces efter ansvar
""",
}


# ============================================================================
# NODE 8: GENERICS & COLLECTIONS
# ============================================================================

DOTNET_NODE_8_GENERICS = {
    "node_id": 8,
    "title": "Generics & Collections",
    "slug": "csharp-generics",
    "description": "Generiska typer, constraints och avancerade collections",
    "difficulty": "intermediate",
    "estimated_minutes": 60,
    "xp_reward": 120,
    "topics_covered": [
        "generics", "type parameters", "constraints",
        "list", "dictionary", "queue", "stack", "hashset"
    ],
    "content": """
# Generics & Collections

> *"Generics provide type safety without the cost of boxing or casting."*

---

## 🎯 Why This Matters

Generics ger:
- **Type safety** vid compile-time
- **Code reuse** utan duplicering
- **Performance** - inga boxing/unboxing-kostnader

---

## 🧠 Collections Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                   .NET COLLECTIONS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LIST<T>            Ordered, indexed, duplicates OK             │
│  └─ List<string> names = ["Alice", "Bob", "Alice"]              │
│                                                                  │
│  DICTIONARY<K,V>    Key-value pairs, unique keys                │
│  └─ Dictionary<string, int> ages = { ["Alice"] = 25 }           │
│                                                                  │
│  HASHSET<T>         Unique values, fast lookup                  │
│  └─ HashSet<int> ids = { 1, 2, 3 }                              │
│                                                                  │
│  QUEUE<T>           FIFO (First In, First Out)                  │
│  └─ Queue<Task> tasks = ...                                     │
│                                                                  │
│  STACK<T>           LIFO (Last In, First Out)                   │
│  └─ Stack<Action> undoStack = ...                               │
│                                                                  │
│  LINKEDLIST<T>      Doubly linked, efficient insert/remove      │
│  └─ LinkedList<Node> nodes = ...                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 Generic Classes

```csharp
// Generic class
public class Box<T>
{
    private T _content;

    public Box(T content)
    {
        _content = content;
    }

    public T GetContent() => _content;
    public void SetContent(T content) => _content = content;
}

// Usage with different types
Box<int> intBox = new Box<int>(42);
Box<string> stringBox = new Box<string>("Hello");
Box<DateTime> dateBox = new Box<DateTime>(DateTime.Now);

int number = intBox.GetContent();      // Type safe!
string text = stringBox.GetContent();  // No casting needed

// Multiple type parameters
public class Pair<TFirst, TSecond>
{
    public TFirst First { get; set; }
    public TSecond Second { get; set; }

    public Pair(TFirst first, TSecond second)
    {
        First = first;
        Second = second;
    }
}

var pair = new Pair<string, int>("Age", 25);
```

---

## 💻 Generic Constraints

```csharp
// where T : class (reference type only)
public class Repository<T> where T : class
{
    public void Add(T item) { }
}

// where T : struct (value type only)
public class ValueContainer<T> where T : struct
{
    public T? Value { get; set; }
}

// where T : new() (must have parameterless constructor)
public class Factory<T> where T : new()
{
    public T Create() => new T();
}

// where T : BaseClass (must inherit from BaseClass)
public class AnimalShelter<T> where T : Animal
{
    public void Adopt(T animal) { }
}

// where T : IInterface (must implement interface)
public class Sorter<T> where T : IComparable<T>
{
    public T GetMax(T a, T b) => a.CompareTo(b) > 0 ? a : b;
}

// Multiple constraints
public class DataStore<T> where T : class, IEntity, new()
{
    public T CreateAndSave()
    {
        var entity = new T();
        // Save logic
        return entity;
    }
}
```

---

## 💻 Generic Methods

```csharp
public class Utilities
{
    // Generic method
    public static T GetDefault<T>() => default(T)!;

    // With constraints
    public static T Max<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) > 0 ? a : b;
    }

    // Swap values
    public static void Swap<T>(ref T a, ref T b)
    {
        T temp = a;
        a = b;
        b = temp;
    }
}

// Usage
int maxInt = Utilities.Max(5, 10);           // 10
string maxStr = Utilities.Max("apple", "banana");  // banana

int x = 1, y = 2;
Utilities.Swap(ref x, ref y);  // x=2, y=1
```

---

## 💻 Common Collections

```csharp
// LIST
List<string> names = new() { "Alice", "Bob" };
names.Add("Charlie");
names.Insert(0, "Zara");
names.Remove("Bob");
bool hasAlice = names.Contains("Alice");
names.Sort();
string first = names[0];

// DICTIONARY
Dictionary<string, int> scores = new()
{
    ["Alice"] = 100,
    ["Bob"] = 85
};

scores["Charlie"] = 90;
if (scores.TryGetValue("Alice", out int score))
{
    Console.WriteLine($"Alice: {score}");
}

foreach (var kvp in scores)
{
    Console.WriteLine($"{kvp.Key}: {kvp.Value}");
}

// HASHSET (unique values, O(1) lookup)
HashSet<int> uniqueIds = new() { 1, 2, 3 };
uniqueIds.Add(2);  // No effect - already exists
bool contains = uniqueIds.Contains(2);  // true, O(1)

// Set operations
HashSet<int> setA = new() { 1, 2, 3 };
HashSet<int> setB = new() { 2, 3, 4 };
setA.UnionWith(setB);      // { 1, 2, 3, 4 }
setA.IntersectWith(setB);  // { 2, 3 }
setA.ExceptWith(setB);     // { 1 }

// QUEUE (FIFO)
Queue<string> queue = new();
queue.Enqueue("First");
queue.Enqueue("Second");
string next = queue.Dequeue();  // "First"
string peek = queue.Peek();     // "Second" (doesn't remove)

// STACK (LIFO)
Stack<string> stack = new();
stack.Push("First");
stack.Push("Second");
string top = stack.Pop();   // "Second"
string peekTop = stack.Peek();  // "First"
```

---

## 💻 LINQ with Collections

```csharp
List<Person> people = new()
{
    new("Alice", 25),
    new("Bob", 30),
    new("Charlie", 25)
};

// Query syntax
var adults = from p in people
             where p.Age >= 18
             orderby p.Name
             select p;

// Method syntax (preferred)
var adultsMethod = people
    .Where(p => p.Age >= 18)
    .OrderBy(p => p.Name)
    .ToList();

// Grouping
var byAge = people.GroupBy(p => p.Age);
foreach (var group in byAge)
{
    Console.WriteLine($"Age {group.Key}: {group.Count()} people");
}

// Aggregations
int totalAge = people.Sum(p => p.Age);
double avgAge = people.Average(p => p.Age);
int maxAge = people.Max(p => p.Age);
Person? oldest = people.MaxBy(p => p.Age);

// Dictionary from collection
Dictionary<string, int> nameToAge = people
    .ToDictionary(p => p.Name, p => p.Age);
```

---

## ⚠️ Vanliga Problem

### Problem 1: Modifying collection during iteration

```csharp
// ❌ Throws InvalidOperationException
foreach (var item in list)
{
    if (item.ShouldRemove)
        list.Remove(item);  // Cannot modify during foreach!
}

// ✅ Use RemoveAll or iterate backwards
list.RemoveAll(item => item.ShouldRemove);

// Or iterate backwards with for
for (int i = list.Count - 1; i >= 0; i--)
{
    if (list[i].ShouldRemove)
        list.RemoveAt(i);
}
```

---

## ✅ Sammanfattning

- **Generics** ger type safety och code reuse
- **Constraints** begränsar tillåtna typer
- **List<T>** för ordnade sekvenser
- **Dictionary<K,V>** för key-value lookups
- **HashSet<T>** för unika värden
- **LINQ** för deklarativa queries
""",
}


# Export all nodes from Block 2
BLOCK_2_NODES = [
    DOTNET_NODE_5_CLASSES,
    DOTNET_NODE_6_INHERITANCE,
    DOTNET_NODE_7_INTERFACES,
    DOTNET_NODE_8_GENERICS,
]
