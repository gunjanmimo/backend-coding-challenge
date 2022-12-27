from fastapi import FastAPI

# -------------------------------- local imports ---------------------------#
from apps.planner.routes import planner_routes

app = FastAPI()
# including routers
app.include_router(planner_routes)
