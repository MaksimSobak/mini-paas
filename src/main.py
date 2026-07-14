import subprocess

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.post("/clone")
async def clone():

    subprocess.run(
        ["bash", "scripts/clone.sh"],
        check=True,
    )

    return JSONResponse(
        {
            "message": "Clone script executed successfully."
        }
    )