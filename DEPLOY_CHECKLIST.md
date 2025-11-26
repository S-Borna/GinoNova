# First Deploy Checklist (CMP Step 11)

## Frontend → Netlify

1. Create new Netlify project.
2. Connect GitHub repo.
3. Set build command:
   npm run build --workspaces=frontend
4. Set publish directory:
   apps/frontend/.next
5. Add environment variables from:
   apps/frontend/.env.netlify.example
6. Click "Deploy site".

## Backend → Railway

1. Create new Railway service.
2. Choose "Deploy from GitHub".
3. Railway will auto-detect Dockerfile.
4. Add environment variables from:
   apps/backend/.env.railway.example
5. Confirm start command:
   poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
6. Click "Deploy service".
