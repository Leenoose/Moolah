from fastapi import APIRouter

router = APIRouter()


@router.get("/hello_world")
def test():
    return "hello world!"


@router.get("/add/")
async def add(x: int, y: int):
    return x + y
