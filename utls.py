
# 一些需要轉換的小程式放在這裡, 再import

def html_str_to_board(board_str:str):
    return_board = []
    temp_list = []
    for c in board_str:
        temp_list.append(int(c)) # 原本c是字串 轉成數字
        if len(temp_list) >= 3:
            return_board.append(temp_list)
            temp_list = []
    return return_board
# 用dender init測試
if __name__ == "__main__":
    print(html_str_to_board("120120021"))