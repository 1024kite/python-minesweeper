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
    print('??????????????????')
    choose = input('1??????????????????2??????????????????3??????????????????')
    if choose == '1':
        while True:
            print('??????' + str(10 - mine_good_flag) + '?????????')
            print('?????????B????????????Q????????????????????????????????????????????????:')
            str_set = list_to_str(list_set, 8, 8)
            print(str_set)
            tips_flag = input('???????????????????????????' + str(tips) + '???')
            if tips_flag == '???':
                tip_set = input('?????????????????????????????????Q???????????????????????????')
                if tip_set in list_flag:
                    tips -= 1
                    mine = list[int(tip_set[0]) - 1][int(tip_set[1]) - 1]
                    mine = mine + ' '
                    list_set[int(tip_set[0]) - 1][int(tip_set[1]) - 1] = mine
                    print('???????????????????????????' + mine)
                    if mine != 'B':
                        frequency += 1
                else:
                    print('????????????????????????????????????????????????')
            choose = input('???????????????/??????/??????')
            if choose == '??????':
                set = input('????????????????????????????????????Q????????????????????????')
                if set in list_flag:
                    mine = list[int(set[0]) - 1][int(set[1]) - 1]
                    mine += ' '
                    if mine == 'B':
                        print('boom!')
                        print('?????????(??????^??????)')
                        print('???????????????????????????B????????????')
                        list_str = list_to_str(list, 8, 8)
                        print(list_str)
                        flag = 1
                    else:
                        def check_zero(set, mine, frequency, zero_flag):
                            global zero_list
                            global flag
                            list_set[int(set[0]) - 1][int(set[1]) - 1] = mine
                            frequency += 1
                            print(set)
                            if mine == 'B ':
                                print('BOOM!,???????????????')
                                flag = 1
                            if mine == '0 ':
                                num = '0 '
                                old_set = set
                                for index in zero_flag_view:
                                    num = '0 '
                                    while num == '0 ':
                                        x = index['x']
                                        y = index['y']
                                        setx = set[:1]
                                        sety = set[-1:]
                                        if x == -1:
                                            setx = int(setx)
                                            setx -= 2
                                        else:
                                            setx = int(setx)
                                            setx += x
                                            setx -= 1
                                        if y == -1:
                                            sety = int(sety)
                                            sety -= 2
                                        else:
                                            sety = int(sety)
                                            sety += y
                                            sety -= 1
                                        if int(setx) > 9 or int(setx) < 0 or int(sety) > 9 or int(sety) < 0:
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
                                    set = old_set
                                    num_list = ['0']
                        check_zero(set, mine, frequency, zero_flag)
                elif set not in list_flag:
                    print('????????????????????????????????????????????????')
            elif choose == '??????':
                mine_set = input('??????????????????/??????????????????')
                if mine_set in list_flag:
                    if list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1].count('Q') == 0:
                        if mine_flag == 0:
                            print('???????????????????????????????????????????????????????????????')
                        else:
                            number = list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1]
                            list_set[int(mine_set[0]) - 1][int(mine_set[1]) - 1] = number + 'Q'
                            if list[int(mine_set[0]) - 1][int(mine_set[1]) - 1] == 'B':
                                mine_good_flag += 1
                                mine_flag -= 1
                            else:
                                mine_flag -= 1
                            if mine_good_flag == 10:
                                print('???????????????????????????')
                                print('???????????????????????????B????????????')
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
                    print('????????????????????????????????????????????????')
            elif choose == '??????':
                set = input('?????????????????????????????????')
                if set in list_flag:
                    label = input('??????????????????????????????')
                    if len(label) == 0:
                        print('??????????????????')
                    elif len(label) > 3:
                        print('????????????3?????????')
                    else:
                        if list_set[int(set[0]) - 1][int(set[1]) - 1].count('(') == 0:
                            number = list_set[int(set[0]) - 1][int(set[1]) - 1]
                            number = number + '(' + label + ')'
                            list_set[int(set[0]) - 1][int(set[1]) - 1] = number
                        else:
                            print('????????????????????????????????????????????????????????????')
                            number = list_set[int(set[0]) - 1][int(set[1]) - 1]
                            number = number[:2]
                            number = number + '(' + label + ')'
                            list_set[int(set[0]) - 1][int(set[1]) - 1] = number
                else:
                    print('????????????????????????')

            else:
                print('???????????????/??????/??????')
            if flag == 1:
                print('????????????')
                print('')
                break
    elif choose == '2':
        print('?????????????????????')
        print('??????????????????????????????????????????????????????????????????1973??????????????????????????????????????????????????????????????????')
        print('??????windows????????????????????????????????????????????????????????????????????????????????????')
        print('??????????????????????????????????????????????????????????????????????????????')
        print('???????????????????????????????????????????????????????????????????????????????????????')
        print('????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')
        print('?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')
        print('??????????????????????????????????????????????????????')
        print('')
    elif choose == '3':
        print('??????????????????(*^???^*)~')
        break
    else:
        print('?????????1/2/3')
