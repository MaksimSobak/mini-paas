import subprocess
import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory="src/static"),
    name="static"
)


templates = Jinja2Templates(
    directory="src/templates"
)


class CloneRequest(BaseModel):
    url: str
    folder: str



@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )



@app.post("/clone")
async def clone(data: CloneRequest):

    try:

        subprocess.run(
            [
                "bash",
                "scripts/clone.sh",
                data.url,
                data.folder
            ],
            check=True
        )


        return {
            "message":
            f"Repository cloned into {data.folder}"
        }


    except subprocess.CalledProcessError:

        return JSONResponse(
            {
                "message":
                "Clone failed"
            },
            status_code=500
        )