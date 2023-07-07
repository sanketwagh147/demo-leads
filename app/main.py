from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import leads, health
from loguru import logger

app = FastAPI(title="Demo Leads", debug=True)


origin = ["*"]
app.add_middleware(
    CORSMiddleware, allow_origins=origin, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(leads.router)
app.include_router(health.router)
