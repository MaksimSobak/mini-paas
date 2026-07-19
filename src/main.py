import subprocess
import os
import uuid

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="src/static"),
    name="static",
)

templates = Jinja2Templates(directory="src/templates")


class DeployRequest(BaseModel):
    url: str
    folder: str


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.post("/deploy")
async def deploy(data: DeployRequest):
    try:
        project_path = os.path.join("repositories", data.folder)

        image_name = f"image-{uuid.uuid4().hex[:8]}"
        container_name = f"container-{uuid.uuid4().hex[:8]}"

        # Клонирование репозитория
        subprocess.run(
            [
                "bash",
                "scripts/clone.sh",
                data.url,
                project_path,
            ],
            check=True,
        )

        # Сборка Docker-образа
        subprocess.run(
            [
                "bash",
                "scripts/build.sh",
                project_path,
                image_name,
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        # Запуск контейнера
        subprocess.run(
            [
                "bash",
                "scripts/run.sh",
                image_name,
                container_name,
            ],
            check=True,
        )

        return {
            "message": "Application deployed successfully.",
            "image": image_name,
            "container": container_name,
        }

    except subprocess.CalledProcessError as e:
        return JSONResponse(
            status_code=500,
            content={
                "stdout": e.stdout,
                "stderr": e.stderr,
            },
        )
    
    print(project_path)

    
