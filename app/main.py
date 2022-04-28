from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from .database import Session
from .make_plot import query_table, make_plot
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index(request: Request, db: Session = Depends(get_db)):
    result, member_name = query_table(db)
    make_plot(result, member_name)
    return templates.TemplateResponse("main.html", context={"request": request})