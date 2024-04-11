from fastapi import APIRouter, Depends

from auth import get_current_username

router = APIRouter(
    prefix="/text",
    dependencies=[Depends(get_current_username)]
)


@router.get("/todo")
def root():
    with open('text_db.txt', 'r') as f:
        content = f.read()
        return content


@router.post("/todo/add")
def add(text: str):
    with open('text_db.txt', 'a') as f:
        f.write(text + '\n')


@router.delete("/todo/del")
def delete(text: str):
    with open('text_db.txt', 'r') as f:
        lines = f.readlines()

    with open('text_db.txt', 'w') as f:
        for line in lines:
            if line.strip("\n") != text:
                f.write(line)
