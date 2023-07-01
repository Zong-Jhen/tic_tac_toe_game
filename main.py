# This is from the previous .py file because calling API are similar
# https://github.com/zxcqwe4906/python_backend_code_examples/blob/main/9_project1/template_example.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
from game import Game, Player
from utls import html_str_to_board, get_turn_from_html_str
from fastapi.responses import RedirectResponse, HTMLResponse
from random_player import RandomPlayer

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_html(request: Request, board: Optional[str] = '000000000'):
    # whose turn? count 1 and 2 first:
    # count_dict = {'1':0, '2':0} # 一開始都是0
    # for c in board:
    #     if c == '1':
    #         count_dict['1'] += 1 # 看到1, 字典1後面的數字+1
    #     elif c == '2':
    #         count_dict['2'] += 1 # 看到1, 字典1後面的數字+1
    # # use if else to check who is the next
    # if count_dict['1'] == count_dict['2']: # 1先下
    #     turn = '1'
    # elif count_dict['1'] - count_dict['2'] ==1: # 輪到2
    #     turn = '2'
    # else:  # 其他情形都出錯
    #     raise ValueError("board invalid")

    turn = get_turn_from_html_str(board)
    
    g = Game(Player(0), Player(1))
    g.board = html_str_to_board(board)
    is_end = g.is_end()
    # print(f'is_end:{is_end}') # 檢查結果
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


@app.get("/ai")
def ai_move(request: Request, board: Optional[str] = '000000000'):
    # decide move
    turn = get_turn_from_html_str(board)
    p = RandomPlayer(int(turn))
    move = p.generate_move(html_str_to_board(board)) #字串轉成二維
    # print(f'move:{move}') # 連線檢查http://127.0.0.1:8000/ai?board=010000000

    new_board = board[:move-1] + turn + board[move:] #把新的點放上去
    # print(f'new_board: {new_board}')  # 連線檢查http://127.0.0.1:8000/ai?board=010000000

   
    # call / api
    # from redirect_response.py
    return RedirectResponse(f'/?board={new_board}') # 顯示新的結果
    # / 是 main.py 裡面 app.get("/") 對應到的 function 
    # ? 是指帶入的 query parameter, 會把相關資訊帶入 function 內 board 參數
    # {}內是變數