import random

while True:
    zero_flag_view = [
        {'x': 1, 'y': 1},
        {'x': 1, 'y': 0},
        {'x': 1, 'y': -1},
        {'x': 0, 'y': 1},
        {'x': 0, 'y': -1},
        {'x': -1, 'y': 1},
        {'x': -1, 'y': 0},
        {'x': -1, 'y': -1}
    ]
    zero_flag = [1, 0, -1]
    zero_set = []
    zero_mine = []
    zero_list = []
    for setx in range(1, 9):
        list_0 = []
        for sety in range(1, 9):
            list_0.append('')
        zero_list.append(list_0)
    list = []
    for setx in range(1, 9):
        list_0 = []
        for sety in range(1, 9):
            list_0.append('')
        list.append(list_0)
    list_set = []
    for setx in range(1, 9):
        list_0 = []
        for sety in range(1, 9):
            set = str(setx) + str(sety)
            list_0.append(set)
        list_set.append(list_0)
    list_flag = []
    for setx in range(1, 9):
        for sety in range(1, 9):
            set = str(setx) + str(sety)
            list_flag.append(set)
    def mine(list):
        setx = random.randint(0, 7)
        sety = random.randint(0, 7)
        if list[setx][sety] == 'B':
            mine(list)
        else:
            list[setx][sety] = 'B'
        return list

    for index in range(10):
        list = mine(list)
    def check_mine(list):
        for setx in range(8):
            for sety in range(8):
                if list[setx][sety] != 'B':
                    mine_number = 0
                    if setx != 7:
                        if list[setx+1][sety] == 'B':
                            mine_number += 1
                    if setx != 0:
                        if list[setx-1][sety] == 'B':
                            mine_number += 1
                    if setx != 7 and sety != 7:
                        if list[setx+1][sety+1] == 'B':
                            mine_number += 1
                    if setx != 7 and sety != 0:
                        if list[setx+1][sety-1] == 'B':
                            mine_number += 1
                    if setx != 0 and sety != 7:
                        if list[setx-1][sety+1] == 'B':
                            mine_number += 1
                    if setx != 0 and sety != 0:
                        if list[setx-1][sety-1] == 'B':
                            mine_number += 1
                    if sety != 7:
                        if list[setx][sety+1] == 'B':
                            mine_number += 1
                    if sety != 0:
                        if list[setx][sety-1] == 'B':
                            mine_number += 1
                    list[setx][sety] = str(mine_number)
        return list

    def list_to_str(list, setx, sety):
        list_str = ''
        for indexx in range(setx):
            for indexy in range(sety):
                res = list[indexx][indexy]
                list_str = list_str + res
                list_str = list_str + ' '
            list_str = list_str + '\n'
        return list_str

    list = check_mine(list)
    frequency = 0
    flag = 0
    mine_flag = 10
    mine_good_flag = 0
    tips = 3
    while True:
        print(list)
        print('还有' + str(10 - mine_good_flag) + '个地雷')
        print('雷阵（B代表雷，Q代表红旗，括号内代表你做的标记）:')
        str_set = list_to_str(list_set, 8, 8)
        print(str_set)
        tips_flag = input('是否要用提示？还有' + str(tips) + '次')
        if tips_flag == '是':
            tip_set = input('请输入你要查看的坐标（Q代表你标的红旗）：')
            if tip_set in list_flag:
                tips -= 1
                mine = list[int(tip_set[0]) - 1][int(tip_set[1]) - 1]
                mine = mine + ' '
                list_set[int(tip_set[0]) - 1][int(tip_set[1]) - 1] = mine
                print('这个位置的数字是：' + mine)
                if mine != 'B':
                    frequency += 1
            else:
                print('坐标不正确，请根据上图中坐标填写')
        choose = input('请选择查看/排雷/标记')
        if choose == '查看':
            set = input('请输入您要查看的坐标：（Q代表你标的红旗）')
            if set in list_flag:
                mine = list[int(set[0]) - 1][int(set[1]) - 1]
                mine += ' '
                if mine == 'B':
                    print('boom!')
                    print('你输了(╥╯^╰╥)')
                    print('雷池埋雷情况为：（B代表雷）')
                    list_str = list_to_str(list, 8, 8)
                    print(list_str)
                    flag = 1
                else:
                    def check_zero(set, mine, frequency, zero_flag):
                        global zero_list
                        list_set[int(set[0]) - 1][int(set[1]) - 1] = mine
                        print('这个位置的数字是：' + mine)
                        frequency += 1
                        print(set)
                        if mine == '0 ':
                            num = '0 '
                            old_set = set
                            for index in zero_flag_view:
                                print('又一次扫描')
                                while num == '0 ':
                                    print('扫描被调用')
                                    print(set)
                                    x = index['x']
                                    y = index['y']
                                    setx = set[:1]
                                    sety = set[-1:]
                                    setx = int(setx)
                                    setx += x
                                    setx -= 1
                                    sety = int(sety)
                                    sety += y
                                    sety -= 1
                                    if setx == '9' or setx == '0' or sety == '9' or sety == '0':
                                        break
                                    try:
                                        num = list[setx][sety]
                                    except IndexError:
                                        break
                                    else:
                                        if num != '0':
                                            break
                                        num += ' '
                                        list_set[setx][sety] = num
                                        frequency += 1
                                        setx += 1
                                        sety += 1
                                        set = str(setx) + str(sety)
                                        print('setx:' + str(setx))
                                        print('sety:' + str(sety))
                                        print('set:' + str(set))
                                        print('num:' + str(num))
                                set = old_set
                                num_list = ['0']
                    check_zero(set, mine, frequency, zero_flag)
            elif set not in list_flag:
                print('坐标不正确，请根据上图中坐标填写')
        elif choose == '排雷':
            mine_set = input('请输入你要标/取红旗的坐标')
            if mine_set in list_flag:
                if list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1].count('Q') == 0:
                    if mine_flag == 0:
                        print('十个红旗已用完，若还想标注，请取出一些红旗')
                    else:
                        number = list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1]
                        list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1] = number + 'Q'
                        if list[int(mine_set[0]) - 1][int(mine_set[1]) - 1] == 'B':
                            mine_good_flag += 1
                            mine_flag -= 1
                        else:
                            mine_flag -= 1
                        if mine_good_flag == 10:
                            print('恭喜你，游戏胜利！')
                            print('雷池埋雷情况为：（B代表雷）')
                            list_str = list_to_str(list, 8, 8)
                            print(list_str)
                            flag = 1
                else:
                    number = list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1]
                    number = number.replace('Q', '')
                    list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1] = number
                    if list[int(mine_set[0]) - 1][int(mine_set[1]) - 1] == 'B':
                        mine_good_flag -= 1
                        mine_flag += 1
                    else:
                        mine_flag += 1
            else:
                print('坐标不正确，请根据上图中坐标填写')
        elif choose == '标记':
            set = input('请输入你要标记的坐标：')
            if set in list_flag:
                label = input('请输入你要标记什么：')
                if len(label) == 0:
                    print('标记不能为空')
                elif len(label) > 3:
                    print('标记最多3个字符')
                else:
                    if list_set[int(set[0]) - 1][int(set[1]) - 1].count('(') == 0:
                        number = list_set[int(set[0]) - 1][int(set[1]) - 1]
                        number = number + '(' + label + ')'
                        list_set[int(set[0]) - 1][int(set[1]) - 1] = number
                    else:
                        print('提示：一个坐标的标记如有多个，则以旧换新')
                        number = list_set[int(set[0]) - 1][int(set[1]) - 1]
                        number = number[:2]
                        number = number + '(' + label + ')'
                        list_set[int(set[0]) - 1][int(set[1]) - 1] = number
            else:
                print('输入的坐标不合理')

        else:
            print('请输入查看/排雷/标记')
        if flag == 1:
            print('游戏结束')
            flag_gameover = input('是否再来一局？（输入是/否）（输入其他默认退出）')
            if flag_gameover == '是':
                break
            if flag_gameover != '是':
                print('欢迎下次再来~(*^▽^*)')
                flag = 2
                break
    if flag == 2:
        break
