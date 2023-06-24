# This is from the previous .py file because calling API are similar
# https://github.com/zxcqwe4906/python_backend_code_examples/blob/main/9_project1/template_example.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from game import Game, Player
from utls import html_str_to_board

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get(request: Request, board: Optional[str] = '000000000'):
    # whose turn? count 1 and 2 first:
    count_dict = {'1':0, '2':0} # 一開始都是0
    for c in board:
        if c == '1':
            count_dict['1'] += 1 # 看到1, 字典1後面的數字+1
        elif c == '2':
            count_dict['2'] += 1 # 看到1, 字典1後面的數字+1
    # use if else to check who is the next
    if count_dict['1'] == count_dict['2']: # 1先下
        turn = '1'
    elif count_dict['1'] - count_dict['2'] ==1: # 輪到2
        turn = '2'
    else:  # 其他情形都出錯
        raise ValueError("board invalid")
    
    g = Game(Player(0), Player(1))
    g.board = html_str_to_board(board)
    is_end = g.is_end()
    print(f'is_end:{is_end}') # 檢查結果
    if is_end == 1:
        end_text = 'Circle win!!'
    elif is_end == 2:
        end_text = 'Cross win!!'
    elif is_end == 3:    
        end_text = 'Draw!!'
    else:
        end_text = ''

    return templates.TemplateResponse(
        "tic_tac_toe.html",
        {
            "request": request,
            "board": board,
            "turn": turn,
            "is_end": is_end,
            "end_text": end_text,
        }
    )