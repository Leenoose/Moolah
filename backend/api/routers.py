from fastapi import APIRouter
from .endpoints import read

router = APIRouter()
router.include_router(read.router)
