# Analytics System Implementation

## Overview

The analytics system provides comprehensive tracking and reporting of user activity, learning progress, and platform usage. This system replaces all mock data with real database-backed analytics for investor-ready reporting.

## Architecture

### Components

1. **Analytics Service** (`src/services/analytics_service.py`)
   - Core service layer handling all analytics operations
   - Event tracking and storage
   - Data aggregation and computation
   - Leaderboard generation
   - Platform-wide statistics

2. **Database Models** (`src/db/models_analytics.py`)
   - `AnalyticsEvent`: Tracks individual user events
   - `DailyStats`: Aggregated daily statistics per user
   - `UserInsights`: Computed learning patterns and insights
   - `ModuleAnalytics`: Module-level engagement metrics

3. **API Routes** (`src/api/routes/analytics.py`)
   - Event tracking endpoints
   - User analytics endpoints
   - Leaderboard endpoints
   - Admin overview endpoints

## Database Schema

### analytics_events
Tracks every user action on the platform.

```sql
CREATE TABLE analytics_events (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    event_type VARCHAR(100) NOT NULL,  -- page_view, task_complete, etc.
    event_data JSONB DEFAULT '{}',
    session_id VARCHAR(100),
    ip_address VARCHAR(45),
    user_agent VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for fast queries
CREATE INDEX ix_analytics_user_id ON analytics_events(user_id);
CREATE INDEX ix_analytics_event_type ON analytics_events(event_type);
CREATE INDEX ix_analytics_created_at ON analytics_events(created_at);
CREATE INDEX ix_analytics_user_type_date ON analytics_events(user_id, event_type, created_at);
```

### daily_stats
Pre-aggregated daily statistics for fast dashboard queries.

```sql
CREATE TABLE daily_stats (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    date DATE NOT NULL,
    study_minutes INTEGER DEFAULT 0,
    tasks_completed INTEGER DEFAULT 0,
    tasks_attempted INTEGER DEFAULT 0,
    xp_earned INTEGER DEFAULT 0,
    sessions_count INTEGER DEFAULT 0,
    ai_calls INTEGER DEFAULT 0,
    hints_used INTEGER DEFAULT 0,
    modules_touched JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, date)
);
```

### user_insights
Computed insights about user learning patterns.

```sql
CREATE TABLE user_insights (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) UNIQUE,
    -- Study patterns
    total_study_hours FLOAT DEFAULT 0,
    avg_session_length INTEGER DEFAULT 0,
    favorite_study_time VARCHAR(20),  -- morning, afternoon, evening, night
    most_active_day VARCHAR(10),      -- monday, tuesday, etc.
    -- Performance
    strongest_skill VARCHAR(100),
    weakest_skill VARCHAR(100),
    avg_task_completion_time INTEGER,
    accuracy_rate FLOAT,
    -- Engagement
    longest_streak INTEGER DEFAULT 0,
    current_streak INTEGER DEFAULT 0,
    streak_start_date DATE,
    last_active_date DATE,
    -- Predictions
    estimated_completion_date DATE,
    recommended_pace VARCHAR(50),
    -- Metadata
    calculated_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### module_analytics
Aggregated statistics per module for admin insights.

```sql
CREATE TABLE module_analytics (
    id UUID PRIMARY KEY,
    module_id UUID UNIQUE,
    module_slug VARCHAR(100) NOT NULL,
    total_enrollments INTEGER DEFAULT 0,
    active_users INTEGER DEFAULT 0,
    completions INTEGER DEFAULT 0,
    completion_rate FLOAT DEFAULT 0,
    avg_completion_time FLOAT,
    avg_score FLOAT,
    difficulty_rating FLOAT,
    avg_rating FLOAT,
    rating_count INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT NOW()
);
```

## API Endpoints

### Event Tracking

#### POST /api/analytics/event
Track a user event.

```javascript
POST /api/analytics/event?user_id=<uuid>
{
  "event_type": "task_complete",
  "event_data": {
    "task_id": "...",
    "duration_seconds": 300,
    "score": 95
  },
  "session_id": "optional-session-id"
}
```

**Tracked Event Types:**
- `page_view` - Page navigation
- `task_start` - User starts a task
- `task_complete` - User completes a task
- `task_hint_used` - User requests a hint
- `module_start` - User starts a module
- `module_complete` - User completes a module
- `session_start` - Study session begins
- `session_end` - Study session ends
- `ai_chat` - AI assistant interaction
- `certificate_earned` - User earns certificate
- `badge_earned` - User earns badge
- `streak_continued` - Daily streak continued

### User Analytics

#### GET /api/analytics/user/{user_id}
Get comprehensive analytics summary for a user.

```json
{
  "total_study_hours": 24.5,
  "tasks_completed": 87,
  "current_streak": 12,
  "longest_streak": 15,
  "favorite_time": "evening",
  "weekly_activity": [45, 60, 30, 90, 120, 0, 75]
}
```

#### GET /api/analytics/user/{user_id}/daily?days=30
Get daily statistics for the last N days.

```json
{
  "user_id": "...",
  "start_date": "2026-01-01",
  "end_date": "2026-01-30",
  "daily_stats": [
    {
      "date": "2026-01-13",
      "study_minutes": 120,
      "tasks_completed": 5,
      "xp_earned": 250,
      "sessions_count": 3,
      "ai_calls": 8
    },
    // ... more days
  ]
}
```

#### GET /api/analytics/user/{user_id}/activity-heatmap?weeks=12
Get GitHub-style activity heatmap data.

```json
{
  "user_id": "...",
  "weeks": 12,
  "data": {
    "2026-01-13": 8,
    "2026-01-12": 5,
    // ... more dates (activity score = tasks + sessions)
  }
}
```

### Leaderboards

#### GET /api/analytics/leaderboard?period=week&metric=xp&limit=10
Get top users by various metrics.

**Parameters:**
- `period`: `day`, `week`, `month`, `all`
- `metric`: `xp`, `tasks`, `streak`, `hours`
- `limit`: 1-100 (default: 10)

```json
{
  "period": "week",
  "metric": "xp",
  "leaderboard": [
    {
      "rank": 1,
      "user_id": "...",
      "name": "John Doe",
      "avatar_url": "...",
      "value": 2500
    },
    // ... more users
  ]
}
```

### Admin Analytics

#### GET /api/analytics/admin/overview
Platform-wide analytics overview (admin only).

```json
{
  "total_users": 1543,
  "active_today": 127,
  "active_this_week": 432,
  "total_study_hours": 8234.5,
  "tasks_completed_today": 289,
  "popular_modules": ["module-uuid-1", "module-uuid-2"],
  "conversion_rate": 0
}
```

## Data Flow

### 1. Event Tracking
```
User Action → Frontend Event → POST /analytics/event → AnalyticsEvent DB → Daily Stats Aggregation
```

### 2. Daily Stats Update
```
Task Completion / Study Session → update_daily_stats() → Aggregate from:
  - Progress table (tasks)
  - StudyflowSession table (sessions)
  - AIUsageLog table (AI calls)
  - ExamResult table (exams)
```

### 3. Analytics Dashboard
```
Frontend Request → Analytics Service → Query Aggregated Data → Format Response → Display
```

## Performance Optimizations

1. **Pre-aggregated Daily Stats**
   - Instead of querying raw events, we maintain daily aggregates
   - Reduces query time from seconds to milliseconds

2. **Strategic Indexes**
   - Composite indexes on (user_id, event_type, created_at)
   - Unique index on (user_id, date) for daily_stats
   - All foreign keys are indexed

3. **Caching Strategy**
   - Leaderboards can be cached in Redis (5-minute TTL)
   - Platform overview stats cached (1-minute TTL)
   - User analytics computed on-demand but cacheable

## Data Retention

- **analytics_events**: Keep 90 days (configurable)
- **daily_stats**: Keep forever (small footprint)
- **user_insights**: Updated weekly
- **module_analytics**: Updated daily

## Migration

To enable the analytics system:

```bash
# Run the migration
cd apps/backend
alembic upgrade head

# The migration will create:
# - analytics_events table
# - daily_stats table
# - user_insights table
# - module_analytics table
# - All necessary indexes
```

## Usage Examples

### Backend: Track an Event

```python
from src.services.analytics_service import AnalyticsService

analytics = AnalyticsService(db)
analytics.track_event(
    user_id=user.id,
    event_type="task_complete",
    event_data={
        "task_id": str(task.id),
        "duration_seconds": 420,
        "xp_earned": 25
    }
)
```

### Backend: Get User Analytics

```python
analytics = AnalyticsService(db)
summary = analytics.get_user_analytics_summary(user_id)
# Returns dict with total_study_hours, tasks_completed, streaks, etc.
```

### Backend: Update Daily Stats

```python
analytics = AnalyticsService(db)
daily_stats = analytics.update_daily_stats(user_id)
# Aggregates today's data from all sources
```

### Frontend: Track Page View

```typescript
// Track page view when user navigates
await fetch(`/api/analytics/event?user_id=${userId}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    event_type: 'page_view',
    event_data: {
      page: '/modules/linux-fundamentals',
      referrer: document.referrer
    }
  })
});
```

### Frontend: Display User Analytics

```typescript
const response = await fetch(`/api/analytics/user/${userId}`);
const analytics = await response.json();

console.log(`Study hours: ${analytics.total_study_hours}`);
console.log(`Current streak: ${analytics.current_streak} days`);
console.log(`Favorite time: ${analytics.favorite_time}`);
```

## Admin Dashboard Integration

The admin dashboard at `/admin/analytics` now displays:

✅ **Real User Metrics**
- Total users, active users (today/week)
- New registrations (today/yesterday)
- Online users (live count)

✅ **Real Study Metrics**
- Total study hours platform-wide
- Tasks completed (today/all-time)
- Average session duration

✅ **Real AI Usage**
- Total AI requests
- Cost tracking (USD)
- Per-user usage

✅ **Real Exam Statistics**
- Total exams taken
- Average scores
- Pass rates
- Top performers
- Recent exam results

## Benefits for Investors

1. **Real-Time Metrics**: All dashboard data is live, not mocked
2. **Engagement Tracking**: See actual user activity patterns
3. **Cost Monitoring**: Track AI usage and costs accurately
4. **Performance Insights**: Identify popular content and drop-off points
5. **Growth Metrics**: Retention, daily active users, study hours
6. **Audit Trail**: Every user action is logged and traceable

## Next Steps

### Short-term Enhancements
- [ ] Add Redis caching for leaderboards
- [ ] Implement automated daily stats aggregation (cron job)
- [ ] Add retention cohort analysis
- [ ] Create analytics email reports

### Long-term Features
- [ ] Machine learning insights (predict churn, recommend content)
- [ ] A/B testing framework
- [ ] Funnel analysis (registration → first task → completion)
- [ ] Revenue analytics (when payment system is live)

## Security Considerations

1. **Admin-only Endpoints**: Platform-wide stats require admin role
2. **User Privacy**: Users can only view their own analytics
3. **Data Anonymization**: IP addresses can be anonymized in analytics
4. **GDPR Compliance**: Users can request deletion of analytics data

## Troubleshooting

### Daily Stats Not Updating
```python
# Manually trigger update
analytics = AnalyticsService(db)
analytics.update_daily_stats(user_id, target_date=date.today())
```

### Leaderboard Shows No Data
- Check that users have completed activities in the specified period
- Verify Progress table has xp_earned and completed_at data
- Check StudyflowSession table has actual_duration data

### Event Tracking Fails
- Ensure user_id is valid UUID
- Check event_type is in allowed list (or ignore warning)
- Verify database connection is active

## Monitoring

Key metrics to monitor:
- `analytics_events` table growth rate
- Query performance on leaderboard endpoints
- Daily stats aggregation errors
- API endpoint response times

## Conclusion

The analytics system transforms the DevOpsHub platform from a prototype with mock data to a production-ready application with comprehensive tracking and reporting. All admin dashboards now display real, actionable metrics suitable for investor presentations and acquisition due diligence.

**Status**: ✅ Production Ready
**Last Updated**: 2026-01-13
**Migration Required**: Yes (run `alembic upgrade head`)
