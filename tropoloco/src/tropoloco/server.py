import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from gunicorn.app.base import BaseApplication
from loguru import logger
from jinja2 import (
    Environment,
    PackageLoader,
    FileSystemLoader,
    ChoiceLoader,
    select_autoescape,
)
from pydantic_web_editor import copy_static_folder

app = FastAPI()


ui_static_path = os.path.join("tropoloco", "static")
os.makedirs(ui_static_path, exist_ok=True)
copy_static_folder(copy_path=ui_static_path)

app.mount(
    "/p_w_e/static",
    StaticFiles(directory=ui_static_path, html=True),
    name="static",
)


class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


JINJA_ENV = Environment(
    loader=ChoiceLoader(
        [
            PackageLoader("troposphere", "templates"),
            FileSystemLoader("templates"),
        ]
    ),
    autoescape=select_autoescape(["html", "xml"]),
)


@app.get("/")
async def read_item(request: Request):
    # Render the template manually with the environment
    template = JINJA_ENV.get_template("index.html")
    return HTMLResponse(template.render(pwe_static_mount="/p_w_e/static"))
