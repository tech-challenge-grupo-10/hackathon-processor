"""
Main application entry point.
"""
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Image Analysis Microservice",
        description="A microservice for image analysis using AI models with RAG capabilities",
        version="1.0.0",
    )
    
    @app.get("/")
    async def root():
        """Root endpoint."""
        return {
            "message": "Welcome to Image Analysis Microservice",
            "version": "1.0.0",
            "note": "Database initialization should be done outside the app for full features."
        }
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {"status": "healthy"}
    
    @app.get("/ready")
    async def ready():
        """Ready check endpoint."""
        # Initialize database here for health checks
        from app.infrastructure.database.database import Database
        db = Database()
        # Create tables but don't commit until actual use
        return {"ready": True}
    
    return app


# Create the application
app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
