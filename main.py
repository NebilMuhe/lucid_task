from fastapi import FastAPI
from routers import auth_router, post_router
import uvicorn

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(post_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
