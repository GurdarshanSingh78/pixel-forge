from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# --- FIX: Re-import the database creation function ---
from app.models.job import create_db_and_tables
from app.routes import images
from app.core.paths import TEMPLATES_DIR, DOWNLOADS_DIR
from app.services.job_scheduler import check_for_jobs

app = FastAPI()

# Mount static and download directories
app.mount("/downloads", StaticFiles(directory=DOWNLOADS_DIR), name="downloads")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

scheduler = AsyncIOScheduler()

@app.on_event("startup")
def on_startup():
    print("INFO:     Server starting up...")
    
    # --- THIS IS THE FIX ---
    # We add the database and table creation back to the startup event.
    # This ensures it runs correctly for local development.
    print("INFO:     Creating database and tables if they don't exist...")
    create_db_and_tables()
    
    print("INFO:     Starting background job scheduler...")
    scheduler.add_job(check_for_jobs, "interval", seconds=30, id="main_job_worker", replace_existing=True)
    scheduler.start()
    print("INFO:     Startup complete.")

# Include API routes
app.include_router(images.router, prefix="/api")

# Serve the main page
templates = Jinja2Templates(directory=TEMPLATES_DIR)
@app.get("/", include_in_schema=False)
async def serve_home(request: Request):
    # --- FIX: explicitly name 'request' and 'name' ---
    return templates.TemplateResponse(request=request, name="index.html")