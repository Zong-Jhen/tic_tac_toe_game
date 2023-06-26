
# 一些需要轉換的小程式放在這裡, 再import

def get_turn_from_html_str(board_str: str) -> str:
    count_dict = {'1':0, '2':0} # 一開始都是0
    for c in board_str:
        if c == '1':
            count_dict['1'] += 1 # 看到1, 字典1後面的數字+1
        elif c == '2':
            count_dict['2'] += 1 # 看到1, 字典1後面的數字+1
    # use if else to check who is the next
    if count_dict['1'] == count_dict['2']: # 1先下
        return '1'
    elif count_dict['1'] - count_dict['2'] ==1: # 輪到2
        return '2'
    else:  # 其他情形都出錯
        raise ValueError("board invalid")

def html_str_to_board(board_str:str):
    return_board = []
    temp_list = []
    for c in board_str:
        temp_list.append(int(c)) # 原本c是字串 轉成數字
        if len(temp_list) >= 3:
            return_board.append(temp_list)
            temp_list = []
    return return_board

# 用dender init測試, random_player.py 也有做過
if __name__ == "__main__":
    print(html_str_to_board("120120021"))