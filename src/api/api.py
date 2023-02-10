from ninja import NinjaAPI
from api.teasers.views import router as ts_router

api = NinjaAPI(
    title="Teasers project API",
    description="API for Teasers project web application.",
)
api.add_router("/teasers", ts_router)
