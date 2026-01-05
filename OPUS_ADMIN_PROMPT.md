# 🎯 PROMPT FÖR OPUS: Bygg Ny Admin Dashboard från Grunden

## 📋 Kontext

Du arbetar med **DevOpsHub** - en e-learningplattform för DevOps-utbildning. Läs först `PROJECT_OVERVIEW.md` för fullständig översikt av projektet.

**Tech Stack:**
- **Frontend:** Next.js 16 (App Router) + TypeScript + Tailwind CSS + Radix UI
- **Backend:** FastAPI + Python 3.11 + PostgreSQL + SQLAlchemy
- **Auth:** JWT (backend) + NextAuth (frontend)
- **State:** TanStack Query v5
- **Real-time:** Implementera med din egen lösning

**Database Tables (Relevanta):**
```sql
users (
  id, email, username, is_admin, email_verified,
  created_at, last_activity_at, oauth_provider,
  xp, level, current_streak,
  ai_quiz_access, premium_modules_access, etc.
)

studyflow_sessions (for activity tracking)
progress (for learning stats)
ai_usage_logs (for AI usage)
```

---

## ⚠️ VIKTIGA INSTRUKTIONER

### 🚫 IGNORERA BEFINTLIG ADMIN-KOD HELT

Det finns redan en admin-sida i:
- `/apps/frontend/src/app/(app)/admin/`
- `/apps/backend/src/api/admin.py`

**RIV INTE NER DEN GAMLA KODEN MANUELLT** - bygg bara din nya lösning UTAN att titta på den gamla.

**Skapa istället:**
- `/apps/frontend/src/app/(app)/admin-v2/` (ny katalog)
- `/apps/backend/src/api/routes/admin_v2.py` (ny fil)

När den nya är klar och testad kan vi senare ta bort den gamla.

### ✅ KRAV PÅ IMPLEMENTATION

1. **MÅSTE FUNGERA** - Inga placeholders, inga TODOs, inga "implement later"
2. **INGA KODBLOCK SOM IGNORERAS** - All kod du skriver måste vara komplett
3. **REAL-TIME DATA** - Använd polling (eller WebSocket om du vill)
4. **RESPONSIVE DESIGN** - Fungerar på desktop och tablets
5. **PROPER ERROR HANDLING** - Alla edge cases hanterade
6. **LOADING STATES** - Skeleton loaders, inte bara spinners
7. **OPTIMISTIC UPDATES** - UI uppdateras direkt, rollback vid error
8. **ACCESSIBILITY** - ARIA labels, keyboard navigation

---

## 🎨 FEATURES ATT IMPLEMENTERA

### 1. 📊 Dashboard Overview (Landing Page)

**URL:** `/admin-v2`

**Widgets att visa:**

#### Real-Time Stats Cards
```
┌─────────────────────────────────────────────────────────────┐
│  [🟢 Online Now]    [👥 Total Users]    [📅 New Today]     │
│     15 users          1,234             23                   │
│  ↑ +3 from 5m ago    ↑ +45 this week   ↓ -2 vs yesterday   │
└─────────────────────────────────────────────────────────────┘
```

**Implementera:**
- Online users count (last_activity_at < 5 minutes ago)
- Total registered users
- New users today/this week/this month
- Active users (logged in last 24h)
- Trend indicators (↑↓ med färg)

#### Activity Graph
```
┌─────────────────────────────────────────────────────────────┐
│  User Activity Last 7 Days                                   │
│                                                              │
│  [Line/Bar Chart showing daily active users]                │
│  - New registrations per day                                │
│  - Active users per day                                     │
│  - Study sessions per day                                   │
└─────────────────────────────────────────────────────────────┘
```

**Använd:** Recharts eller Chart.js eller liknande

#### Quick Actions
```
┌─────────────────────────────────────────────────────────────┐
│  Quick Actions                                               │
│  [View All Users] [Recent Activity] [AI Usage] [Analytics]  │
└─────────────────────────────────────────────────────────────┘
```

#### System Health
```
┌─────────────────────────────────────────────────────────────┐
│  System Health                                               │
│  ✅ Database: Connected (12ms latency)                      │
│  ✅ Redis: Connected (3ms latency)                          │
│  ✅ API: Healthy (150ms avg response)                       │
│  ⚠️  OpenAI: Rate limit: 85% used                           │
└─────────────────────────────────────────────────────────────┘
```

---

### 2. 👥 User Management (Huvudfunktion)

**URL:** `/admin-v2/users`

#### User Table med Advanced Features

**Columns:**
```
| Status | Avatar | Name/Email | Role | Created | Last Active | XP/Level | Actions |
|   🟢   |   [img] | John Doe   | User | 2024-01-15 | 2 min ago  | 1,250/5 | [...]  |
|        |        | john@ex.com|      |            |            |         |        |
|   🔴   |   [img] | Jane Smith | Admin| 2023-12-01 | 3 days ago | 5,420/12| [...]  |
```

**Status Indicators:**
- 🟢 **Online** (last_activity_at < 5 min)
- 🟡 **Away** (last_activity_at < 1 hour)
- 🔴 **Offline** (last_activity_at > 1 hour)
- 🚫 **Banned** (special status)

**Filters & Search:**
```
┌─────────────────────────────────────────────────────────────┐
│  [🔍 Search users...]  [Status: All ▼]  [Role: All ▼]      │
│                                                              │
│  [Date Range: Last 7 days ▼]  [Sort: Last Active ▼]        │
│                                                              │
│  Quick Filters:                                             │
│  [ ] Online now   [ ] Banned   [ ] Admins   [ ] Premium     │
└─────────────────────────────────────────────────────────────┘
```

**Implementera:**
- Real-time search (debounced, 300ms)
- Multi-filter kombinationer
- Column sorting (client-side för synliga rader)
- Pagination (50 users per page)
- Bulk actions (select multiple users)

#### Actions per User (Dropdown Menu)

När man klickar [...] på en användare:

```
┌─────────────────────────┐
│  👁️  View Details       │
│  ✏️  Edit User          │
│  ─────────────────────  │
│  🚪 Force Logout        │
│  🔒 Ban User            │
│  🗑️  Delete User        │
│  ─────────────────────  │
│  👑 Toggle Admin        │
│  ⭐ Manage Permissions  │
└─────────────────────────┘
```

**Implementera varje action med:**
- Confirmation dialog (inte bara alert())
- Loading state
- Success/Error toasts
- Optimistic UI update
- API call med proper error handling

**Exempel - Ban User:**
```typescript
// Klick på "Ban User" →
// 1. Visa dialog:
"Are you sure you want to ban john@example.com?
This will immediately log them out and prevent future logins.

Reason (optional):
[Text input for ban reason]

[Cancel] [Ban User]"

// 2. När confirmed:
// - Visa loading spinner på button
// - POST /api/admin-v2/users/{id}/ban
// - Optimistically update UI (status → banned)
// - Toast: "User banned successfully"
// - If error: Rollback UI + Toast error
```

---

### 3. 👤 User Detail Page

**URL:** `/admin-v2/users/[userId]`

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│  ← Back to Users                                            │
│                                                              │
│  ┌────────────────┐  John Doe                              │
│  │   [Avatar]     │  john@example.com                       │
│  │                │  🟢 Online (Active 2 min ago)           │
│  └────────────────┘  User since: Jan 15, 2024              │
│                                                              │
│  [Edit Profile] [Ban User] [Force Logout] [Delete]         │
│                                                              │
│  ──────────────────────────────────────────────────────────│
│                                                              │
│  TABS:                                                      │
│  [Overview] [Activity] [Learning Progress] [AI Usage]      │
│                                                              │
│  === TAB: OVERVIEW ===                                      │
│                                                              │
│  Account Information                                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Email:          john@example.com                     │  │
│  │ Username:       johndoe                              │  │
│  │ Role:           User                                 │  │
│  │ Email Verified: ✅ Yes                               │  │
│  │ OAuth Provider: Google                               │  │
│  │ Created:        Jan 15, 2024 14:32                   │  │
│  │ Last Login:     2 minutes ago                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Gamification                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ XP:             1,250 points                         │  │
│  │ Level:          5 (Champion)                         │  │
│  │ Current Streak: 12 days 🔥                           │  │
│  │ Longest Streak: 23 days                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Permissions                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ [ ] Admin Access                                     │  │
│  │ [✓] AI Quiz Access                                   │  │
│  │ [✓] Premium Modules                                  │  │
│  │ [✓] Study Room Access                                │  │
│  │ [✓] Skillpath Access                                 │  │
│  │                                                       │  │
│  │ [Save Changes]                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  === TAB: ACTIVITY ===                                      │
│                                                              │
│  Recent Activity (Last 7 days)                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 📚 Completed task: "Docker Basics"        2 min ago  │  │
│  │ 🎯 Started study session                  1 hour ago │  │
│  │ ✅ Finished Module: "Linux Commands"      Yesterday  │  │
│  │ 💬 Used AI Assistant (Dallas)             Yesterday  │  │
│  │ 📖 Logged in                               2 days ago│  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  Study Sessions                                             │
│  [Line chart showing study hours per day]                  │
│                                                              │
│  === TAB: LEARNING PROGRESS ===                             │
│                                                              │
│  Modules Completed: 3/15                                    │
│  Tasks Completed: 45/180                                    │
│  Labs Completed: 8/30                                       │
│                                                              │
│  [Progress visualization - module tree or progress bars]   │
│                                                              │
│  === TAB: AI USAGE ===                                      │
│                                                              │
│  Total AI Requests: 234                                     │
│  Total Tokens: 45,320                                       │
│  Estimated Cost: $2.15                                      │
│                                                              │
│  [Chart showing AI usage over time]                        │
│                                                              │
│  Recent AI Interactions                                     │
│  [Table with timestamp, feature, tokens, cost]             │
└─────────────────────────────────────────────────────────────┘
```

**Implementera:**
- Editable fields med inline editing eller edit mode
- Real-time updates (polling every 30s för activity)
- Permission toggles som sparar direkt (optimistic)
- Activity timeline med ikoner och timestamps
- Charts för study sessions och AI usage

---

### 4. 📈 Analytics & Insights

**URL:** `/admin-v2/analytics`

**Sections:**

#### User Growth
```
┌─────────────────────────────────────────────────────────────┐
│  User Growth                                                 │
│                                                              │
│  [Line chart]                                               │
│  - Total users over time                                    │
│  - New registrations per week                               │
│  - Active users per week                                    │
│                                                              │
│  Time Range: [Last 7 days ▼] [Last 30 days] [Last 90 days] │
└─────────────────────────────────────────────────────────────┘
```

#### User Activity Heatmap
```
┌─────────────────────────────────────────────────────────────┐
│  Activity Heatmap (When are users most active?)             │
│                                                              │
│       Mon  Tue  Wed  Thu  Fri  Sat  Sun                     │
│  00h  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]                     │
│  04h  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]  [ ]                     │
│  08h  [█]  [█]  [█]  [█]  [█]  [ ]  [ ]   ← Peak hours     │
│  12h  [█]  [█]  [█]  [█]  [█]  [ ]  [ ]                     │
│  16h  [▓]  [▓]  [▓]  [▓]  [▓]  [ ]  [ ]                     │
│  20h  [▒]  [▒]  [▒]  [▒]  [░]  [░]  [░]                     │
└─────────────────────────────────────────────────────────────┘
```

#### Top Users
```
┌─────────────────────────────────────────────────────────────┐
│  Top Users                                                   │
│                                                              │
│  Most Active:                                               │
│  1. John Doe - 45 study sessions this week                  │
│  2. Jane Smith - 38 study sessions this week                │
│  3. ...                                                     │
│                                                              │
│  Highest XP:                                                │
│  1. Alice - 12,450 XP (Level 24)                           │
│  2. Bob - 9,820 XP (Level 19)                              │
│  3. ...                                                     │
└─────────────────────────────────────────────────────────────┘
```

#### System Stats
```
┌─────────────────────────────────────────────────────────────┐
│  System Statistics                                           │
│                                                              │
│  Total Study Sessions: 5,432                                │
│  Total Tasks Completed: 23,456                              │
│  Total AI Requests: 8,901                                   │
│  Avg Session Duration: 42 minutes                           │
│  Most Popular Module: "Docker Fundamentals"                 │
└─────────────────────────────────────────────────────────────┘
```

---

### 5. 🤖 AI Usage Monitoring

**URL:** `/admin-v2/ai-usage`

**Features:**
- Total AI requests (all users)
- Total tokens consumed
- Total cost
- Cost per user
- Cost trends over time
- Most expensive users
- Most used AI features (Dallas, Quiz, Summary, etc.)
- Rate limit warnings

**Table:**
```
| User        | Requests | Tokens  | Cost   | Last Used  | Actions |
|-------------|----------|---------|--------|------------|---------|
| John Doe    | 234      | 45,320  | $2.15  | 2 min ago  | [View]  |
| Jane Smith  | 156      | 32,100  | $1.52  | 1 hour ago | [View]  |
```

---

### 6. ⚙️ Settings & Configuration

**URL:** `/admin-v2/settings`

**Sections:**

#### System Settings
```
┌─────────────────────────────────────────────────────────────┐
│  Lockdown Mode                                               │
│  [✓] Enable lockdown mode (only allowed emails can login)   │
│                                                              │
│  Allowed Emails (one per line):                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ admin@example.com                                      │ │
│  │ user@example.com                                       │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  [Save Settings]                                            │
└─────────────────────────────────────────────────────────────┘
```

#### AI Settings
```
┌─────────────────────────────────────────────────────────────┐
│  OpenAI Configuration                                        │
│  API Key: sk-*********************** [Edit]                 │
│  Model: gpt-4-turbo-preview                                 │
│  Max Tokens: 2000                                           │
│                                                              │
│  Rate Limiting                                              │
│  Max requests per user per day: [100]                       │
│                                                              │
│  [Save Settings]                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 TEKNISKA KRAV

### Backend (FastAPI)

**Skapa:** `/apps/backend/src/api/routes/admin_v2.py`

**Endpoints att implementera:**

```python
# Dashboard stats
GET  /api/admin-v2/stats/overview
GET  /api/admin-v2/stats/activity
GET  /api/admin-v2/stats/system-health

# User management
GET    /api/admin-v2/users                    # List all users (paginated)
GET    /api/admin-v2/users/{id}               # Get user details
PUT    /api/admin-v2/users/{id}               # Update user
DELETE /api/admin-v2/users/{id}               # Delete user
POST   /api/admin-v2/users/{id}/ban           # Ban user
POST   /api/admin-v2/users/{id}/unban         # Unban user
POST   /api/admin-v2/users/{id}/force-logout  # Force logout
POST   /api/admin-v2/users/{id}/toggle-admin  # Toggle admin status
PUT    /api/admin-v2/users/{id}/permissions   # Update permissions

# Analytics
GET  /api/admin-v2/analytics/user-growth
GET  /api/admin-v2/analytics/activity-heatmap
GET  /api/admin-v2/analytics/top-users

# AI Usage
GET  /api/admin-v2/ai-usage/overview
GET  /api/admin-v2/ai-usage/by-user
GET  /api/admin-v2/ai-usage/{user_id}

# Settings
GET  /api/admin-v2/settings
PUT  /api/admin-v2/settings
```

**Example Response - Overview Stats:**
```json
{
  "online_users": 15,
  "online_trend": 3,
  "total_users": 1234,
  "total_users_trend": 45,
  "new_users_today": 23,
  "new_users_trend": -2,
  "active_users_24h": 156,
  "active_users_week": 543,
  "total_study_sessions": 5432,
  "avg_session_duration_minutes": 42,
  "total_tasks_completed": 23456,
  "total_ai_requests": 8901,
  "ai_cost_total": 234.56,
  "ai_cost_today": 12.34
}
```

**Example Response - Users List:**
```json
{
  "users": [
    {
      "id": "uuid",
      "email": "john@example.com",
      "username": "johndoe",
      "avatar_url": "https://...",
      "is_admin": false,
      "is_banned": false,
      "email_verified": true,
      "oauth_provider": "google",
      "created_at": "2024-01-15T14:32:00Z",
      "last_activity_at": "2024-01-20T10:30:00Z",
      "xp": 1250,
      "level": 5,
      "current_streak": 12,
      "permissions": {
        "ai_quiz_access": true,
        "premium_modules_access": true,
        "study_room_access": true,
        "skillpath_access": true
      },
      "stats": {
        "modules_completed": 3,
        "tasks_completed": 45,
        "study_sessions": 23,
        "ai_requests": 234
      },
      "status": "online|away|offline"
    }
  ],
  "total": 1234,
  "page": 1,
  "page_size": 50,
  "total_pages": 25
}
```

**Viktiga implementationsdetaljer:**

1. **Online Status Calculation:**
```python
# Beräkna status baserat på last_activity_at
def get_user_status(last_activity: datetime) -> str:
    now = datetime.utcnow()
    diff = (now - last_activity).total_seconds()

    if diff < 300:  # 5 minutes
        return "online"
    elif diff < 3600:  # 1 hour
        return "away"
    else:
        return "offline"
```

2. **Proper Pagination:**
```python
@router.get("/users")
async def get_users(
    page: int = 1,
    page_size: int = 50,
    search: str = None,
    status: str = None,  # online|away|offline|banned
    role: str = None,    # admin|user
    sort: str = "last_activity",  # last_activity|created|email
    order: str = "desc",
    db: Session = Depends(get_db)
):
    # Implement proper filtering, sorting, pagination
    ...
```

3. **Force Logout Implementation:**
```python
# Använd Redis eller JWT blacklist för att invalidera tokens
# Alternativt: Uppdatera en "session_version" i user table
```

4. **Permission System:**
```python
# Middleware för att checka admin access
async def require_admin(
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(403, "Admin access required")
    return current_user

# Använd på alla admin routes
@router.get("/users", dependencies=[Depends(require_admin)])
```

### Frontend (Next.js)

**Skapa:** `/apps/frontend/src/app/(app)/admin-v2/`

**Structure:**
```
admin-v2/
  page.tsx                    # Dashboard overview
  layout.tsx                  # Admin layout med sidebar
  users/
    page.tsx                  # User list
    [userId]/
      page.tsx                # User detail
  analytics/
    page.tsx                  # Analytics page
  ai-usage/
    page.tsx                  # AI usage monitoring
  settings/
    page.tsx                  # Settings
```

**Components att skapa:**
```
components/admin-v2/
  Sidebar.tsx                 # Admin navigation
  StatsCard.tsx               # Reusable stat card
  UserTable.tsx               # User table med filters
  UserRow.tsx                 # User row med actions
  UserStatusBadge.tsx         # Status indicator (online/offline)
  ActivityTimeline.tsx        # Activity feed
  PermissionToggle.tsx        # Permission toggle switch
  UserActionsMenu.tsx         # Dropdown actions menu
  ConfirmDialog.tsx           # Reusable confirmation dialog
  Charts/
    ActivityChart.tsx         # Activity line/bar chart
    ActivityHeatmap.tsx       # Heatmap for user activity
    UserGrowthChart.tsx       # User growth chart
```

**State Management:**

Använd TanStack Query för all data:

```typescript
// hooks/admin/useAdminStats.ts
export function useAdminStats() {
  return useQuery({
    queryKey: ['admin', 'stats'],
    queryFn: () => api.get('/api/admin-v2/stats/overview'),
    refetchInterval: 30000, // Poll every 30s
  })
}

// hooks/admin/useUsers.ts
export function useUsers(filters: UserFilters) {
  return useQuery({
    queryKey: ['admin', 'users', filters],
    queryFn: () => api.get('/api/admin-v2/users', { params: filters }),
    keepPreviousData: true,
  })
}

// hooks/admin/useBanUser.ts
export function useBanUser() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ userId, reason }: { userId: string, reason?: string }) =>
      api.post(`/api/admin-v2/users/${userId}/ban`, { reason }),

    onMutate: async ({ userId }) => {
      // Optimistic update
      await queryClient.cancelQueries(['admin', 'users'])

      const previousUsers = queryClient.getQueryData(['admin', 'users'])

      queryClient.setQueryData(['admin', 'users'], (old: any) => ({
        ...old,
        users: old.users.map((u: any) =>
          u.id === userId ? { ...u, is_banned: true } : u
        )
      }))

      return { previousUsers }
    },

    onError: (err, variables, context) => {
      // Rollback on error
      queryClient.setQueryData(['admin', 'users'], context.previousUsers)
      toast.error('Failed to ban user')
    },

    onSuccess: () => {
      toast.success('User banned successfully')
      queryClient.invalidateQueries(['admin', 'users'])
    }
  })
}
```

**Real-time Updates:**

Implementera polling för real-time data:

```typescript
// Dashboard stats - poll every 30s
useQuery({
  queryKey: ['admin', 'stats'],
  queryFn: fetchStats,
  refetchInterval: 30000,
})

// User list - poll every minute when viewing
useQuery({
  queryKey: ['admin', 'users'],
  queryFn: fetchUsers,
  refetchInterval: 60000,
})

// User detail - poll every 30s when viewing specific user
useQuery({
  queryKey: ['admin', 'users', userId],
  queryFn: () => fetchUser(userId),
  refetchInterval: 30000,
})
```

---

## 🎨 UI/UX KRAV

### Design System

Använd Radix UI + Tailwind för konsistent design:

**Color Scheme:**
- Online: `text-green-500` / `bg-green-500`
- Away: `text-yellow-500` / `bg-yellow-500`
- Offline: `text-gray-400` / `bg-gray-400`
- Banned: `text-red-500` / `bg-red-500`
- Admin: `text-purple-500` / `bg-purple-500`

**Status Badge Example:**
```typescript
<span className={cn(
  "inline-flex items-center px-2 py-1 rounded-full text-xs font-medium",
  status === 'online' && "bg-green-100 text-green-700",
  status === 'away' && "bg-yellow-100 text-yellow-700",
  status === 'offline' && "bg-gray-100 text-gray-700",
  status === 'banned' && "bg-red-100 text-red-700"
)}>
  <span className="w-2 h-2 rounded-full bg-current mr-1" />
  {status}
</span>
```

**Confirmation Dialog:**
Använd Radix Dialog med proper styling:

```typescript
<AlertDialog>
  <AlertDialogTrigger>Ban User</AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Are you sure?</AlertDialogTitle>
      <AlertDialogDescription>
        This will ban {user.email} and immediately log them out.
        They will not be able to login until unbanned.
      </AlertDialogDescription>
    </AlertDialogHeader>

    <div className="my-4">
      <Label>Reason (optional)</Label>
      <Textarea
        placeholder="Enter ban reason..."
        value={reason}
        onChange={(e) => setReason(e.target.value)}
      />
    </div>

    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction
        onClick={handleBan}
        className="bg-red-600 hover:bg-red-700"
      >
        {isLoading ? <Spinner /> : 'Ban User'}
      </AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

### Loading States

**Skeleton Loaders för Tables:**
```typescript
function UserTableSkeleton() {
  return (
    <div className="space-y-2">
      {[...Array(10)].map((_, i) => (
        <div key={i} className="flex items-center gap-4 p-4 border rounded">
          <Skeleton className="w-10 h-10 rounded-full" />
          <div className="flex-1 space-y-2">
            <Skeleton className="h-4 w-48" />
            <Skeleton className="h-3 w-32" />
          </div>
          <Skeleton className="h-8 w-24" />
          <Skeleton className="h-8 w-8" />
        </div>
      ))}
    </div>
  )
}
```

### Toast Notifications

Använd Sonner eller radix-toast:

```typescript
import { toast } from 'sonner'

// Success
toast.success('User banned successfully')

// Error
toast.error('Failed to ban user', {
  description: error.message
})

// Loading (with promise)
toast.promise(
  banUser(userId),
  {
    loading: 'Banning user...',
    success: 'User banned successfully',
    error: 'Failed to ban user'
  }
)
```

---

## ✅ TESTING CHECKLIST

Testa att allt fungerar:

- [ ] Dashboard visar korrekt stats
- [ ] Online/offline status uppdateras (max 30s delay)
- [ ] User table pagination fungerar
- [ ] Search filtrerar korrekt
- [ ] Status filter fungerar (online/offline/banned)
- [ ] Sorting fungerar på alla columns
- [ ] Ban user - confirmation dialog → API call → optimistic update
- [ ] Unban user fungerar
- [ ] Force logout fungerar
- [ ] Delete user - confirmation → API call → user försvinner från lista
- [ ] Toggle admin fungerar
- [ ] Permission toggles sparar korrekt
- [ ] User detail page visar all info
- [ ] Activity timeline uppdateras
- [ ] Charts renderas korrekt
- [ ] AI usage stats visar korrekt data
- [ ] Settings sparas korrekt
- [ ] Error handling - API errors visar toast
- [ ] Loading states - skeleton loaders visas
- [ ] Responsive - fungerar på tablet
- [ ] No console errors
- [ ] No TypeScript errors

---

## 🚀 IMPLEMENTATION PLAN

### Fas 1: Backend Foundation (1-2 timmar)

1. Skapa `/apps/backend/src/api/routes/admin_v2.py`
2. Implementera alla endpoints med proper responses
3. Lägg till admin middleware/dependency
4. Testa endpoints med curl/Postman
5. Verifiera permissions fungerar

### Fas 2: Frontend Structure (1 timme)

1. Skapa folder structure under `/admin-v2/`
2. Skapa layout med sidebar navigation
3. Setup routing
4. Skapa API client functions
5. Setup TanStack Query hooks

### Fas 3: Dashboard (1-2 timmar)

1. Stats cards med real-time data
2. Activity chart
3. Quick actions
4. System health indicators
5. Polling för auto-refresh

### Fas 4: User Management (2-3 timmar)

1. User table med columns
2. Status indicators
3. Filters och search
4. Pagination
5. Actions menu för varje user
6. Confirmation dialogs
7. Optimistic updates
8. Error handling

### Fas 5: User Detail Page (1-2 timmar)

1. Layout med tabs
2. Overview tab - all user info
3. Activity tab - timeline
4. Learning progress tab - stats & charts
5. AI usage tab - logs
6. Editable permissions

### Fas 6: Analytics & AI Usage (1-2 timmar)

1. Charts för user growth
2. Activity heatmap
3. Top users lists
4. AI usage overview
5. AI usage per user

### Fas 7: Settings (30 min)

1. Lockdown mode toggle
2. Allowed emails management
3. Save functionality

### Fas 8: Polish & Testing (1 timme)

1. Loading states överallt
2. Error boundaries
3. Toast notifications
4. Responsive adjustments
5. Accessibility (ARIA labels)
6. Cross-browser testing

---

## 💡 KREATIVA TILLÄGG (Bonus Features)

Om du har tid och vill imponera:

### 1. Bulk Actions
```
[ ] Select All
[✓] John Doe
[✓] Jane Smith
[ ] Bob Wilson

Actions for 2 selected users:
[Ban Selected] [Delete Selected] [Export Selected]
```

### 2. Export to CSV
```
[Export Users to CSV]
→ Downloads CSV with all user data
```

### 3. User Impersonation (för debugging)
```
[Login as User]
→ Loggar in som den användaren (för debugging)
→ Banner: "You are impersonating John Doe [Exit Impersonation]"
```

### 4. Activity Log för Admin Actions
```
Audit Log:
- Admin "alice@example.com" banned user "bob@example.com" (2 min ago)
- Admin "alice@example.com" deleted user "spam@example.com" (1 hour ago)
```

### 5. Real-time Notifications
```
Toast popup när ny user registrerar:
"New user registered: john@example.com"
```

### 6. Advanced Search
```
Search by:
- Email (contains)
- Username (contains)
- Created date range
- Last active date range
- XP range
- Module progress

Save search filters as "presets"
```

---

## 🎯 SUCCESS CRITERIA

Din implementation är lyckad när:

✅ **Funktionalitet:**
- Alla endpoints fungerar
- All CRUD operations för users fungerar
- Real-time updates (polling) fungerar
- Online/offline status uppdateras korrekt
- Force logout fungerar omedelbart
- Ban/unban fungerar
- Delete user fungerar
- Permission updates fungerar

✅ **UX:**
- Inga loading delays >100ms för UI interactions
- Optimistic updates känns instant
- Confirmation dialogs för destructive actions
- Toast notifications för all actions
- Error messages är tydliga och hjälpsamma
- Loading states visar vad som händer

✅ **Code Quality:**
- Inga TypeScript errors
- Inga console errors
- Proper error handling överallt
- No TODOs eller placeholders
- Kod är läsbar och väl strukturerad
- Components är <300 rader

✅ **Performance:**
- User table laddar <500ms
- Charts renderas <200ms
- Real-time updates inte mer än 30s delay
- No memory leaks från polling
- Pagination fungerar smooth

---

## 📝 DELIVERABLES

När du är klar, provide:

1. **All kod för:**
   - `/apps/backend/src/api/routes/admin_v2.py`
   - `/apps/backend/src/schemas/admin_v2.py` (om behövs)
   - `/apps/frontend/src/app/(app)/admin-v2/**` (all pages)
   - `/apps/frontend/src/components/admin-v2/**` (all components)
   - `/apps/frontend/src/hooks/admin/**` (all hooks)

2. **Instructions för:**
   - Hur man registrerar nya routes (i main.py)
   - Hur man når admin dashboard (/admin-v2)
   - Hur man testar funktionaliteten

3. **Demo checklist:**
   - Hur man verifierar att allt fungerar

---

## ⚡ QUICK START EFTER IMPLEMENTATION

```bash
# 1. Backend - registrera routes
# I /apps/backend/src/main.py, lägg till:
from src.api.routes import admin_v2
app.include_router(admin_v2.router, prefix="/api/admin-v2", tags=["admin-v2"])

# 2. Starta dev servers
npm run dev

# 3. Logga in som admin
# Gå till http://localhost:3000/login
# Använd admin credentials

# 4. Navigera till admin
# Gå till http://localhost:3000/admin-v2

# 5. Testa funktionalitet
# - Verifiera dashboard stats
# - Gå till users
# - Testa ban/unban
# - Testa force logout
# - Verifiera real-time updates
```

---

## 🎯 SLUTORD

Du är **Claude Opus** - den mest kraftfulla AI-modellen.

Jag förväntar mig:
- **Komplett, fungerande kod** - ingen pseudocode
- **Kreativa lösningar** - imponera mig
- **Production-ready quality** - detta ska deployas direkt
- **Inga genvägar** - implementera allt ordentligt

**Lycka till! Bygg den bästa admin-dashboarden som någonsin skapats.** 🚀
