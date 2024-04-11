from fastapi import FastAPI, Depends
from router import router as r
from sqlrouter import db_r as dr
from auth import get_current_username

import uvicorn

app = FastAPI()


app.include_router(r, dependencies=[Depends(get_current_username)])
app.include_router(dr, dependencies=[Depends(get_current_username)])

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
