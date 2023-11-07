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
from pydantic_web_editor import WebEditorConfig, copy_static_folder


from tropoloco.model.awslambda import Function


app = FastAPI()


home = os.path.expanduser("~")

ui_static_path = os.path.join(home, ".tropoloco", "static")
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
            PackageLoader("tropoloco", "templates"),
            FileSystemLoader("templates"),
        ]
    ),
    autoescape=select_autoescape(["html", "xml"]),
)


@app.get("/")
def hello():
    web_editor_config = WebEditorConfig(
        title="Example Pydantic Editor demoing Schema Org's About Page",
        model=Function,
        start_val={},
    )
    return HTMLResponse(web_editor_config.html)
