from fastapi import FastAPI
from app.routes.task_routes import router as task_router

# Initialize the FastAPI application
app = FastAPI(
    title="Task Manager API",
    description=(
        "A production-ready task management backend. Features request and response "
        "validation with Pydantic, clean architecture structure, in-memory data store, "
        "and auto-generated Swagger API documentation."
    ),
    version="1.0.0",
    docs_url="/docs",      # Interactive Swagger UI
    redoc_url="/redoc",    # Clean documentation alternative
)

# Register the routes for Tasks
app.include_router(task_router)

@app.get("/", tags=["Root"], summary="Api Root Endpoint")
def read_root():
    """
    Root endpoint that returns a welcome message and points users to Swagger documentation.
    """
    return {
        "message": "Welcome to the Task Manager API.",
        "documentation": "Go to /docs to view the interactive Swagger documentation."
    }
