from fastapi import FastAPI, Request
from typing import Optional
import card_match

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import requests, random

app = FastAPI()


pl = card_match.PlayingCards()
pl.start()



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



def flatten_list(list_p):
    list_req = []
    for i in list_p:
        list_req.extend(i)
    return list_req


@app.get('/', response_class=HTMLResponse)
def move(request: Request, row_: Optional[int] = None, col_: Optional[int] = None):
    if row_ is not None and col_ is not None:
        your_move = pl.click(row_, col_)
    else:
        your_move = pl.pcard

    return templates.TemplateResponse('home.html', {'request': request, 'elements': flatten_list(your_move), 'elements2': flatten_list(flatten_list(your_move)), 'count': pl.count} )
    # return your_move


@app.get('/reset_game', response_class=HTMLResponse)
def reset(request: Request):
    pl.start()
    return RedirectResponse('/')
    # return templates.TemplateResponse('home.html', context={'request': request})
    # return your_move




print(app.url_path_for('move'))
