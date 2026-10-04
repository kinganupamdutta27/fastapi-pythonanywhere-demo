from fastapi import FastAPI
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI)->AsyncIterator[None]:
    print("Application Start UP")
    try:
        # Startup logic
        print("Application starting...")

        yield

    except Exception:
        print("Application startup/runtime failure")
        raise

    finally:
        # Shutdown logic
        print("Application shutting down...")

app = FastAPI(
    title="FastAPI-Demo-PythonAnywhere", 
    description="This is my domo FastApi App",
    version="1.0.0",
    debug=True,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
    )

@app.get(path="/health", tags=["Health"], description="Health Check Endpoint for app")
async def getHealth()->dict[str,str]:
    return {"message":"Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="127.0.0.1", port=8698, reload=True)