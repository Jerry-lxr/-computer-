#欲传者:hyy(7.6), zmk(6.2-7.?)
# 备忘录=[
# 0.???
# 1.I don't know

enter_counter = 0
while 1:
    try:
        include_list = ''
        from traceback import print_exc
        include_list +=   'traceback-print_exc'
        from sys import exit, exc_info
        include_list += '; sys-exit,exc_info'
        from time import sleep,time
        include_list += '; time-sleep,time'
        from random import randint, choice
        include_list += '; random-randint,choice'
        from colorama import Fore, Back, Style
        include_list += '; colorama(need pip install)-Fore,Back,Style'
        import os
        include_list += '; os'
        from platform import system
        include_list += '; platform-system'
        
        '''(软件名             内存        编号)
        我的电脑             12.56MB        1
        JY瘤懒魕              999MB         2
        deepehink         9.42MB        3
        应用商店                3MB         4
        设置                   1MB          5
        回收站                 2MB          6
        计算题                  1GB         7
        我的世界               24XB         8
        Jindows-coin-installer 24MB        9
        语言选择器             10MB         10
        各种密码转换器         50MB         11
        机器人使命召唤低配版   10KB          12
        '''

        #0 False 1 True
        #作弊部分
        EASY = [
            1,#加载加快
            1,#登录加快
            1,#提前扩容
            1#全部下载
        ]
        VERSION = '1.11.6.6(2024.12.14)至1.12.0(2025.X)过渡版'
        LAST_CODE = '2025.1.5'

        def set_equipment():
            global equipment
            equipment = 'mobile' if "mobile" in system() else 'computer'

        def NCZH(name, how:int, point:int=754933482):#内存转换
            DW = 0
            if name == 0:
                return ['B', 0]
            if name > 0.1:
                DW = [MEMORY_LEVEL[how - 1], round(name, point)]
            for a in range(1, how):
                if a == how - 1:
                    if name < ((1000*(1024**(a-1)))*10)**-1:
                        DW = ['B', round(name*(1000*(1024**(a-1))), point)]
                        break
                    if name < 0.1:
                        if how == 2:
                            DW = ['B', round(name*1000, point)]
                        else:
                            DW = [MEMORY_LEVEL[how-2], round(name*1024, point)]
                elif name < ((1024**a)*10)**-1:
                    DW = [MEMORY_LEVEL[how-a-1], round(name*(1024**a), point)]
                    break
            for a in range(1, len(MEMORY_LEVEL) - how + 1):
                if how == 1:
                    if name > ((1024**(a-1))*1000)*0.1:
                        DW = [MEMORY_LEVEL[a], round(name/(1000*(1024**(a-1))), point)]
                elif name > (1024**a)*0.1:
                    DW = [MEMORY_LEVEL[how-1+a], round(name/(1024**a), point)]
            return DW

        def NCXG(name, how:int, want:int, point:int=754933482):#内存修改
            if name == 0:
                return 0
            if how == want:
                return round(name, point)
            if how == 1:
                return round(name/(1000*(1024**(want-1))), point)
            else:
                if want < how:
                    if want == 1:
                        return round(name*(1000*(1024**(how-2))), point)
                    return round(name*(1024**(how-1)), point)
                return round(want/(1024**(want-how)), point)

        LOADING_EASY = EASY[0]
        LOGIN_EASY = EASY[1]
        MEMORY_EASY = EASY[2]
        SOFTWARE_EASY = EASY[3]
        def loading(title:str, fast=0):#加载
            global display_desktop
            global display_line
            jdt = 0
            if LOADING_EASY:
                while 1:
                    delta = randint(5, 10)
                    if jdt + delta >= 100:
                        delta = 100-jdt
                        if delta == 1:
                            delta = 2
                    for jj in range(1, delta+1):
                        jdt += 1
                        if jdt > 100:
                            jdt = 100
                        print(f'\r{title} {(jdt//2)*jdtpf[0]}{(50-(jdt//2))*jdtpf[1]} {jdt}%/100%', end='')
                    if jdt >= 100:
                        sleep(0.4)
                        print()
                        break
                    sleep(0.08)
            else:
                while 1:
                    puls = randint(5, 10)
                    if jdt + puls >= 100:
                        puls = 100-jdt
                        if puls == 1:
                            puls = 2
                    for jj in range(1, puls+1):
                        jdt += 1
                        if jdt > 100:
                            jdt = 100
                        print('\r', end='')
                        print(f'{title} {(jdt//2)*jdtpf[0]}{(50-(jdt//2))*jdtpf[1]} {jdt}%/100%', end='')
                        sleep(randint(4, 10)/240)
                    if jdt >= 100:
                        sleep(0.5)
                        print()
                        break
                    sleep(fast)

        def gnidaol(title:str, fast=0):#载加
            tdj = 100
            if LOADING_EASY:
                while 1:
                    minus = randint(5, 10)
                    if tdj - minus < 0:
                        minus = tdj
                        if minus == 1:
                            minus = 2
                    for jj in range(1, minus+1):
                        tdj -= 1
                        if tdj < 0:
                            tdj = 0
                        print('\r', end='')
                        print(f'{title} {(tdj//2)*jdtpf[0]}{(50-(tdj//2))*jdtpf[1]} {tdj}%/100%  ', end='')
                    if tdj <= 0:
                        sleep(0.4)
                        print()
                        break
                    sleep(0.08)
            else:
                while 1:
                    minus = randint(5, 10)
                    if tdj - minus < 0:
                        minus = tdj
                        if minus == 1:
                            minus = 2
                    for jj in range(1, minus+1):
                        tdj -= 1
                        if tdj < 100:
                            tdj = 0
                        print('\r', end='')
                        print(f'{title} {(tdj//2)*jdtpf[0]}{(50-(tdj//2))*jdtpf[1]} {tdj}%/100%  ', end='')
                        sleep(randint(4, 10)/240)
                    if tdj <= 0:
                        sleep(0.5)
                        print()
                        break
                    sleep(fast)

        def BLNC(dictionary:dict, which:str):#深度搜索C, D, E盘
            global Cpan_NC
            global Dpan_NC
            global Epan_NC
            for j in range(0, len(dictionary)):
                if type(dictionary[list(dictionary)[j]]) == dict:
                    BLNC(dictionary[list(dictionary)[j]], which)
                else:
                    if (type(dictionary[list(dictionary)[j]]) == int) or (type(dictionary[list(dictionary)[j]]) == float):
                        if which == 'C':
                            Cpan_NC += dictionary[list(dictionary)[j]]
                        if which == 'D':
                            Dpan_NC += dictionary[list(dictionary)[j]]
                        if which == 'E':
                            Epan_NC += dictionary[list(dictionary)[j]]

        def zhuomianNC():#便携式侦测桌面内存
            global zhuomian_NC
            zhuomian_NC = 0
            for jjj in zhuomian:
                zhuomian_NC += zhuomian[jjj][1]

        def get_key(dictionary:dict, value):#输入值得到键
            return [k for k, v in dictionary.items() if v == value][0]

        def of100(num):#百分之几
            return randint(1,100) < num
        
        def if_system_software(a):#如果是系统软件
            return a == '我的电脑' or a == 'JY瘤懒器' or a == 'deepthink' or a == '应用商店' or a == '设置' or a == '回收站'

        def if_cannot_remove(a):#如果不可卸载
            return if_system_software(a)

        def if_shortcuts(a):#如果是快捷键
            return a == 'Alt' or a == 'Tab' or a == 'Ctrl' or a == 'Jin' or a == 'Esc' or a == 'Space' or a == 'Del' or a == 'F1' or a == 'F2' or a == 'F3' or a == 'F4' or a == 'F5' or a == 'F6' or a == 'F7' or a == 'F8' or a == 'F9' or a == 'F10' or a == 'F11' or a == 'F12'

        def AD():
            choose = randint(1, 1)
            if choose == 1:
                print(f'shequ.codemao.cn/user/754933482发现更多    还剩3秒', end='\r')
                sleep(1)
                print(f'此系统的浏览器\'不兼容\',可移至其他浏览器    还剩2秒', end='\r')
                sleep(1)
                print(f'shequ.codemao.cn/user/754933482发现更多    还剩1秒  ', end='\r')
                sleep(1)
                print(f'此系统的浏览器\'不兼容\',可移至其他浏览器    还剩0秒  ', end='\r')
                sleep(1)
            else:
                pass
            print(24 * '  ', end='  \r')

        def browse_code():
            choose = randint(1, 1)
            if choose == 1:
                space = randint(5, 10)
                letter = chr(randint(97, 122))
                print(f'请输入足够的{letter}到上面的{letter}')
                print(f'{space * " "}{letter}')
                trying = input('')
                if trying == 'Alt F4':
                    return 'Alt F4退出'
                return trying == (space + 1) * letter

        def browse_coding():
            coding = browse_code()
            if coding == 'Alt F4退出':
                return 'Alt F4退出'
            elif coding:
                return True
            return browse_coding()

        def clear_data():
            global username
            global PINpassword
            global jdtpf
            global done
            global done2
            global computer
            global browse_history
            zhuomian = default_zhuomian
            username = ''
            PINpassword = [24, '用户114514']
            jdtpf = ['!', '?']
            BIOS_password = ''
            Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
            Dpan = {}
            Epan = {'desktop':[]}
            Jindows_coin_started = False
            Jindows_coin = 0
            done = done2 = False
            browse_history = []
            set_equipment()
            IsRoot = False
            computer = [zhuomian, Cmemory, Dmemory, Ememory, IsUserVIP, Jindows_coin_started, Jindows_coin, equipment, browse_history, real_browse_history, BIOS_password, Cpan, Dpan, Epan]

        def download(tofind):#下载
            find = []
            for jj in RJXX:
                if tofind in RJXX[jj][0] or tofind == '' or tofind in RJXX[jj][8]:
                    if not if_system_software(RJXX[jj][0]):
                        find.append(jj)
            if len(find) > 0:
                for a in range(0, len(find)):
                    print(f'{a+1}.{RJXX[find[a]][0]}')
                jj = input('从以上类似结果选一个')
                if jj == 'Alt F4':
                    return 'Alt F4退出'
                try:
                    if jj == '全部下载' or jj == 'all':
                        for a in range(0, len(find)):
                            bl = {}
                            for jjjj in zhuomian:
                                if RJXX[find[jj-1]][0] == zhuomian[jjjj][0]:
                                    bl['F'] = 1
                                    break
                            if 'F' in bl:
                                continue
                            loading('正在下载'+RJXX[find[a]][0], randint(7, 10)/8)
                            zhuomian[len(zhuomian)+1] = [RJXX[find[a]][0], RJXX[find[a]][2], RJXX[find[a]][0], 0]
                        return '下载成功'
                    else:
                        jj = int(jj)
                        print(f'软件名:{RJXX[find[jj-1]][0]}')
                        print(f'占用内存:{RJXX[find[jj-1]][1]}')
                        print(f'作者:{RJXX[find[jj-1]][3]}')
                        print(f'软件简介:{RJXX[find[jj-1]][4]}')
                        print(f'评论(其中一个):{RJXX[find[jj-1]][5][randint(0,len(RJXX[find[jj-1]][5])-1)]}')
                        print(f'评价(满分5.0):{RJXX[find[jj-1]][6]}')
                        print(f'类别:{RJXX[find[jj-1]][7]}')
                        choose = input('直接回车即可下载, 否则退出')
                        if choose == 'Alt F4':
                            return 'Alt F4退出'
                        if choose == '':
                            for jjjj in zhuomian:
                                if RJXX[find[jj-1]][0] == zhuomian[jjjj][0]:
                                    print('已下载过!')
                                    return '下载失败'
                            zhuomianNC()
                            if NCXG(zhuomian_NC, 3, 1, 4)+NCXG(RJXX[find[jj-1]][2], 3, 1, 4)>NCXG(Ememory[0], Ememory[2], 1, 4):
                                print('内存不足')
                                return '下载失败'
                            else:
                                loading('正在下载'+RJXX[find[jj-1]][0], randint(7, 8)/10)
                                zhuomian[len(zhuomian)+1] = [RJXX[find[jj-1]][0], RJXX[find[jj-1]][2], RJXX[find[jj-1]][0], 0]
                                return '下载成功'
                except:
                    print(Fore.RED + '回答不符合标准' + Fore.RESET)
                    return '下载失败'
            else:
                print('无搜索结果')
                return '下载失败'

        def cmd():#command
            global IsRoot
            print('Jindows [版本 0.0.24]\nJerry (no Corporation).保留所有权利.\n(quit)退出')
            ask = '>>'
            while 1:
                all_command = input(ask)
                if all_command == 'Alt F4':
                    return 'Alt F4退出'
                command = all_command.split(' ')
                for a in range(24):
                    command.append('')
                if all_command == 'quit':
                    break
                elif command[0] == 'Jindows':
                    if command[1] == 'clear':
                        if len(command) == 2:
                            clear_data()
                            break
                    '''elif command[0] == 'BackGround':
                        if command[1] == 'setcolor':
                            if len(command) == 3:
                                try:
                                    exec(f"print(Back.{command[2].upper()} + \'已生效\')")
                                except:
                                    print(f'\'{command[2]}\' 不是一个可生效的颜色')
                            else:
                                print('该命令不完整')
                    '''
                elif all_command == 'root':
                    if not IsRoot:
                        print('想要获取root权限,需要解锁rootlock')
                        password = input('rootlock:')
                        if password == 'Alt F4':
                            return 'Alt F4退出'
                        if password == 'JindowsStartRootPassword754933482ByJerryAndSnk':
                            IsRoot = True
                    else:
                        print('你已经获得Root权限')
                else:
                    print(f'\'{all_command}\' 不是内部或外部命令,也不是可运行的程序.')

        def Jin_L():#锁屏
            while 1:
                if input('回车再次进入') == '':
                    break

        def Jin_I():#设置
            global jdtpf
            print('1.退出')
            print('2.创作者')
            print('3.设置进度条皮肤')
            print('4.文件管理')
            print('5.电脑信息')
            setting_while = True
            while setting_while:
                setting_ask = input('')
                if setting_ask == 'Alt F4' or setting_ask == '1':
                    setting_while = False
                elif setting_ask == '2':
                    print(f'创作者名单:{EDITER}')
                elif setting_ask == '3':
                    while 1:
                        wddn_ask = input('请输入你想要进度条未完成皮肤')
                        if wddn_ask == 'Alt F4':
                            setting_while = False
                            break
                        if len(wddn_ask) != 1:
                            print('需要输入一个字的')
                        else:
                            jdtpf = [wddn_ask]
                            break
                    while 1:
                        wddn_ask = input('请输入你想要进度条已完成皮肤')
                        if wddn_ask == 'Alt F4':  
                            setting_while = False
                            break
                        if len(wddn_ask) != 1:
                            print('需要输入一个字的')
                        else:
                            jdtpf = [wddn_ask, jdtpf[0]]
                            break
                    choose = input('是否需要进度条测试(输入Y代表同意)')
                    if choose == 'Alt F4':
                        setting_while = False
                    if choose == 'Y' or choose == 'y':
                        loading('测试', randint(8, 24)/100)
                elif setting_ask == '4':
                    while 1:
                        try:
                            WenJianSuoYin = input('输入您要查看的位置(输入b退出)')
                            if WenJianSuoYin == 'Alt F4':
                                setting_while = False
                                break
                            if WenJianSuoYin == 'b':
                                break
                            WenJianSuoYin = WenJianSuoYin.split('/')
                            if WenJianSuoYin[0] == 'C:':
                                SuoYin = Cpan
                            elif WenJianSuoYin[0] == 'D:':
                                SuoYin = Dpan
                            elif WenJianSuoYin[0] == 'E:':
                                SuoYin = Epan
                            else:
                                raise SystemError('退出try')
                            for j in range(1, len(WenJianSuoYin)):
                                if type(SuoYin) == dict and type(SuoYin[WenJianSuoYin[j]]) == dict:
                                    SuoYin = SuoYin[WenJianSuoYin[j]]
                                else:
                                    raise SystemError('退出try')
                            SuoYin_printer = list(SuoYin)
                            if len(SuoYin_printer) == 0:
                                print('此文件夹为空')
                            else:
                                for j in range(0, len(SuoYin_printer)):
                                    print(SuoYin_printer[j], end=' ')
                                    if type(SuoYin[SuoYin_printer[j]]) == dict:
                                        print('类:文件夹')
                                    elif type(SuoYin[SuoYin_printer[j]]) == str:
                                        if 'ЈΕſſΥ' in SuoYin[SuoYin_printer[j]]:
                                            print('类:不可打开的文件')
                                        else:
                                            print('类:纯文本(OneLineText)')
                                    elif type(SuoYin[SuoYin_printer[j]]) == int:
                                        print('类:索引内存的区域(无法打开)')
                                    elif type(SuoYin[SuoYin_printer[j]]) == list:
                                        print('类:系统表格(不可打开)')
                                '''while 1:
                                    print('输入对应名继续查找')
                                    print('1.增加')
                                    print('2.重新查找')
                                    reply = input('')
                                    if reply == 'Alt F4':
                                        setting_while = False
                                        break
                                    elif reply == '1':
                                        print('看什么看, 这个根本没法更新')
                                    elif reply == '2':
                                        break
                                    else:
                                        for a in range(0, len(SuoYin)):
                                            if reply == list(SuoYin)[a]:
                                                for j in range(1, len(WenJianSuoYin)):
                                                    if type(SuoYin) == dict and type(SuoYin[WenJianSuoYin[j]]) == dict:
                                                        SuoYin = SuoYin[WenJianSuoYin[j]]
                                                    else:
                                                        raise SystemError('退出try')
                                                SuoYin_printer = list(SuoYin)
                                                if len(SuoYin_printer) == 0:
                                                    print('此文件夹为空')
                                                else:
                                                    for j in range(0, len(SuoYin_printer)):
                                                        print(SuoYin_printer[j], end=' ')
                                                        if type(SuoYin[SuoYin_printer[j]]) == dict:
                                                            print('类:文件夹')
                                                        elif type(SuoYin[SuoYin_printer[j]]) == str:
                                                            if 'ЈΕſſΥ' in SuoYin[SuoYin_printer[j]]:
                                                                print('类:不可打开的文件')
                                                            else:
                                                                print('类:纯文本(OneLineText)')
                                                        elif type(SuoYin[SuoYin_printer[j]]) == int:
                                                            print('类:索引内存的区域(无法打开)')
                                                        elif type(SuoYin[SuoYin_printer[j]]) == list:
                                                            print('类:系统表格(不可打开)')
                                                    break'''
                        except:
                            print(Fore.RED + '文件索引错误' + Fore.RESET)
                elif setting_ask == '5':
                    print(f'''
电脑名称:{COMPUTER_NAME}
电脑版本:{VERSION}({LAST_CODE})
电脑安装日期:2024.3.17
电脑密钥:&#x674E-&#x5E2D-&#x745E;-byLXR-Jerry
''')
                else:
                    print('听不懂您在说什么')

        def Jin_and_anotherkey(key:list):
            temp2 = []
            for a in range(0,len(key)):
                temp = key[a]
                if len(temp) > 1:
                    if if_shortcuts(temp):
                        pass
                    else:
                        for b in range(0, len(temp)):
                            temp2.append(temp[b])
                        continue
                temp2.append(temp)
            key = temp2
            successful = False
            if len(key) == 1:
                if key[0] == 'R' or key[0] == 'r':
                    if (Jin_R := input('输入指令:')) == 'Alt F4':
                        return 'Alt F4退出'
                    elif Jin_R == 'cmd':
                        cmd()
                    else:
                        print(Fore.RED + '无效命令' + Fore.RESET)
                elif key[0] == 'L' or key[0] == 'l':
                    Jin_L()
                elif key[0] == 'I' or key[0] == 'i':
                    has_setting = False
                    for a in zhuomian:
                        if zhuomian[a][0] == '设置':
                            has_setting = True
                            break
                    if has_setting:
                        print('正在跳转设置')
                        sleep(randint(5, 8) / 10)
                        Jin_I()
                    else:
                        print('你需要设置')
                else:
                    successful = True
            else:
                successful = True
            if successful:
                all_key = 'Jin'
                for a in range(0,len(key)):
                    temp = key[a]
                    if len(temp) > 1:
                        if if_shortcuts(temp):
                            pass
                        else:
                            for b in range(0,len(temp)):
                                all_key += f' + {temp[b]}'
                            continue
                    all_key += f' + {temp}'
                print(Fore.RED + f'{all_key} 不是可用的快捷键' + Fore.RESET)

        def Alt_and_anotherkey(key:list):
            temp2 = []
            for a in range(0,len(key)):
                temp = key[a]
                if len(temp) > 1:
                    if if_shortcuts(temp):
                        pass
                    else:
                        for b in range(0, len(temp)):
                            temp2.append(temp[b])
                        continue
                temp2.append(temp)
            key = temp2
            successful = False
            if len(key) == 1:
                if key[0] == 'F4':
                    exit()
                else:
                    successful = True
            else:
                successful = True
            if successful:
                all_key = 'Alt'
                for a in range(0,len(key)):
                    temp = key[a]
                    if len(temp) > 1:
                        if if_shortcuts(temp):
                            pass
                        else:
                            for b in temp:
                                all_key += f' + {b}'
                            continue
                    all_key += f' + {temp}'
                print(Fore.RED + f'{all_key} 不是可用的快捷键' + Fore.RESET)

        class System:
            def wrong():
                raise SystemError(f'{COMPUTER_NAME}未响应')

        #<为保证能网站间跳转而做的类>
        #
        #原理介绍:
        #一个类里必须包含seek和cn
        #如果出现def其它(例如seek), 代表你无法输入XXXX.XX.seek来查看
        #目前正在不思考怎么做斜杠(/)分割
        #
        class JerryHK():
            def seek():
                return '可以使用'
            def cn():
                print(Fore.YELLOW + '系统:请注意, 你打开的是未经该电脑审核的网站' + Fore.RESET)
                print(f'--{COMPUTER_NAME}的黑客系统--')
                while 1:
                    URL_HK_code = input('输入黑客代码')
                    if URL_HK_code == 'Alt F4':
                        return 'Alt F4退出'
                    URL_HK_dm = URL_HK_code.split(' ')
                    for j in range(10):
                        URL_HK_dm.append('')
                    if URL_HK_code == '桌面':
                        print(zhuomian)
                    elif URL_HK_code == 'exit':
                        break
                    elif URL_HK_code == '软件信息':
                        print(RJXX)
                    elif URL_HK_code == 'break':
                        exit()
                    elif URL_HK_code == '扩容':
                        global Cmemory
                        global Dmemory
                        global Ememory
                        Cmemory = Dmemory = Ememory = [754933482, 'XB', 14]
                        print('扩容成功')
        class shequ():
            def seek():
                return '可以使用'
            class codemouse():
                def seek():
                    return '可以使用'
                def cn():
                    WORK = [['coin增加器', 'Jindows官方'], ['尝试卡爆', 'Jerry'], ['凑数用的2', 'Jerry'], ['凑数用的3', 'Jerry'], ['凑数用的4', 'Jerry']]
                    printwork = []
                    print('精选:')
                    for a in range(5):
                        b = WORK[randint(0, len(WORK)-1)]
                        while b in printwork:
                            b = WORK[randint(0, len(WORK)-1)]
                        printwork.append(b)
                        print(f'\t{b[0]}    作者:{b[1]}')
                    while 1:
                        turn = input('搜索名字(直接回车展示全部)(b退出):')
                        if turn == 'Alt F4':
                            return 'Alt F4退出'
                        if turn == 'b':
                            break
                        find = []
                        for jj in range(0, len(WORK)):
                            if turn in WORK[jj][0] or turn == '':
                                find.append(jj)
                        if len(find) > 0:
                            for a in range(0, len(find)):
                                print(f'{a+1}.{WORK[find[a]][0]}    作者:{WORK[find[a]][1]}')
                            jj = input('从以上类似结果选一个')
                            if jj == 'Alt F4':
                                return 'Alt F4退出'
                            while 1:
                                try:
                                    jj = int(jj)
                                    seek = eval(f'shequ.codemouse_work.{WORK[find[jj-1]][0]}.seek()')
                                except:
                                    print(Fore.RED + '回答不符合标准' + Fore.RESET)
                                    break
                                if seek == '可以使用':
                                    exec(f'shequ.codemouse_work.{WORK[find[jj-1]][0]}.cn()')
                                break
                        else:
                            print('无搜索结果')
            class codemouse_work():
                def seek():
                    return '可以使用'
                class coin增加器():
                    def seek():
                        return '可以使用'
                    def cn():
                        loading('加载中', randint(2, 5)/10)
                        if Jindows_coin_started:
                            global Jindows_coin
                            while 1:
                                choose = input('直接回车加金币, 否则退出')
                                if choose == 'Alt F4':
                                    return 'Alt F4退出'
                                if choose == '':
                                    a = randint(1, 5)
                                    Jindows_coin += a
                                    print(f'\n已增加{a}coin')
                                    print('冷却中')
                                    sleep(randint(15, 50)/20)
                                else:
                                    break
                        else:
                            print('未启用Jindows-coin, 可以去应用商店下载Jindows-coin-installer')
                    class check():
                        def seek():
                            return '可以使用'
                        def cn():
                            print('''
<!DOCTYPE JHTML>
<JHTML>
    <head>
        <title>coin增加器</title>
    </head>
    <body>
        <Python>
            while 1:
                choose == input('直接回车加金币, 否则退出')
                if choose == '':
                    a = randint(1, 5)
                    Jindows_coin += a
                    print(f'已增加{a\a}coin')
                    print('冷却中')
                    sleep(randint(15, 50)/20)
                else:
                    break
        </Python>
    </body>
</JHTML>
''')
                class 尝试卡爆():
                    def seek():
                        return '可以使用'
                    def cn():
                        loading('加载中', randint(2, 5)/10)
                        try:
                            a = 2
                            while 1:
                                a = a**a
                                print(a*'卡爆中')
                        except OverflowError:
                            sleep(randint(7, 13)/10)
                            System.wrong()#数值运算超出最大限制
                    class check():
                        def seek():
                            return '可以使用'
                        def cn():
                            print('''
<!DOCTYPE JHTML>
<JHTML>
    <head>
        <title>尝试卡爆</title>
    </head>
    <body>
        <Python>
            a = 2
            while 1:
                a = a**a
                print(a*'卡爆中')
        </Python>
    </body>
</JHTML>
''')
        class jisuanti:
            def seek():
                return '可以使用'
            def cn():
                df = 0
                txt = ['答对', '错了, 答案是']
                print('输入b退出')
                while 1:
                    decision = randint(1, 7)
                    if decision == 1:
                        fn = randint(1, 60)
                        sn = randint(1, 60)
                        r = input(f'{fn}+{sn}=')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn+sn) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}{fn+sn}')
                    elif decision == 2:
                        fn = randint(1, 60)
                        sn = randint(1, 60)
                        while(fn-sn < 0):
                            fn = randint(1, 60)
                            sn = randint(1, 60)
                        r = input(f'{fn}-{sn}=')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn-sn) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}{fn-sn}')
                    elif decision == 3:
                        fn = randint(1, 15)
                        sn = randint(1, 15)
                        r = input(f'{fn}×{sn}=')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn*sn) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}{fn*sn}')
                    elif decision == 4:
                        fn = randint(1, 1000)
                        sn = randint(1, 1000)
                        while(not(fn%sn == 0)):
                            fn = randint(1, 1000)
                            sn = randint(1, 1000)
                        r = input(f'{fn}÷{sn}=')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn/sn) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}{int(fn/sn)}')
                    elif decision == 5:
                        fn = randint(1, 20)
                        sn = randint(2, 3)
                        r = input(f'{fn}^{sn}=')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn**sn) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}{fn**sn}')
                    elif decision == 6:
                        fn = randint(1, 20)
                        r = input(f'{fn}×3.14=')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn*3.14) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}{float(fn*3.14)}')
                    else:
                        fn = randint(2, 10)
                        sn = randint(1, 200)
                        r = input(f'{fn}倍根号{sn}=根号')
                        if r == 'Alt F4':
                            return 'Alt F4退出'
                        if r == 'b':
                            break
                        if str(fn**2+sn) == r:
                            print(txt[0])
                            df += 1
                        else:
                            print(f'{txt[1]}根号{fn**2+sn}')
                print(f'你的得分是{df}')
                return df
        #</为保证能网站间跳转而做的类>

        CHANGELOG = '''
版本0.25时仅有计算题
版本0.5更新了进度条
版本1.7更新了damn脑风格(中途没有将计算题联系在一起)
版本1.7.24更新了日志
版本1.8增加语言转换
版本1.8.7可以修改PIN码以及退出登录
版本1.9优化了代码
版本1.10有很多小更新
版本1.11暂时突破100KB!!!
版本1.11.3支持Python3.6编译
版本1.11.6更新了快捷键并简化了代码
即将更新1.12(浏览器丰富)'''
        RJXX = {
            1:['我的电脑', '12.56MB', 12.56, 'Jindows', '用于查看您的电脑信息', ['连个F盘都没有', '关于C盘,D盘,E盘是只读这件事'], 5.0, '系统软件', 'wddn'],
            2:['JY瘤懒器', '999MB', 999, 'Jindows', '可以来搜索你的疑惑', ['没有无网游戏的浏览器不是浏览器!'], 2.0, '系统软件', 'jyllq'],
            3:['deepthink', '9.42MB', 9.42, 'Jindows', '深度思考，只是只会思考而已', ['服务器繁忙，请稍后再试', '竟然是系统软件，你还怪好心的'], 1.0, '系统软件', 'deepthink'],
            4:['应用商店', '3MB', 3, 'Jindows', '应用商店', ['当下载应用商店需要应用商店'], 4.0, '系统软件', 'yysd'],
            5:['设置', '1MB', 1, 'Jindows', '设置', ['没用'], 4.0, '系统软件', 'sz'],
            6:['回收站', '0B', 0, 'Jindows', '回收站', ['没用'], 4.0, '系统软件', 'hsz'],
            7:['计算题', '1GB', 1024, 'Jerry', '考验计算能力', ['一个简单的问答软件要1GB, 这合理吗'], 2.6, '智力游戏', 'jst'],
            8:['我的世界', '24XB', 24 * (1024 ** 11), 'Jerry', '我的世界, 但是作者从mojang变成了Jerry', ['根本打不开'], 2.4, '游戏', 'wdsj'],
            9:['Jindows-coin-installer', '24MB', 24, 'Jindows', 'Jindows选择性内置功能', ['还行吧'], 3.5, '安装向导', 'jindowscoininstaller'],
            10:['语言选择器', '10MB', 10, 'Jindows', 'Jindows选择性内置功能', ['用处不多'], 2.4, '额外设置', 'yyxzq'],
            11:['各种密码转换器', '50MB', 50, 'Jerry', '摩斯密码转换器', ['谁会用啊'], 2.0, '功能软件', 'gzmmzhq'],
            12:['机器人使命召唤低配版', '10KB', 10/1024, 'Jerry', '使命召唤低配版', ['冷知识:10KB是因为不是你想的那个使命召唤'], 2.0, '游戏', 'jqrsmzhdpb']}
        HOW = '''
"打开" 序号
"卸载" 序号
"下载" 名字
"更新情况"
"软件改名" 序号 修改后名字
"修改PIN码" 修改后PIN码 修改后账号名
"退出登录"
"软件移位" 序号1 序号2
"软件交换" 序号1 序号2
"桌面"'''
        EDITER = f'''
主编:Jerry
副编:snk
灵感者:Jerry
环境搭建:Python
使用库:{include_list}
主设备:Python编译器(mobile)
副设备:VScode(computer)
软件制造者:Jerry
网站制造者:Jerry
设置制造者:Jerry
BIOS制造者:Jerry
广告制造者:Jerry
蓝屏制造者:Jerry
root制造者:Jerry
系统制造者:Jerry
内存制造者:Jerry
快捷键制造者:Jerry
评论制造者:Jerry
日志制造者:Jerry
进度条制造者:Jerry
写代码的人:Jerry
贡献最多的人:Jerry'''
        equipment = 'unknowkn'
        set_equipment()
        COMPUTER_NAME = 'Jerry超级无敌螺旋升天不好用到爆炸吸收日月精华24年的电脑Ultra-Max-Pro+-Mini-Mate-Nova-Note-Neo-Mix-Reno-GT-A-C-T-SE'
        fn = sn = 24
        user_state = 'administrator'
        default_zhuomian = {1:['我的电脑', 12.56, '我的电脑', 0], 2:['JY瘤懒器', 999, 'JY瘤懒器', 0], 3:['deepthink', 9.42, 'deepthink', 0], 4:['应用商店', 3, '应用商店', 0], 5:['设置', 1, '设置', 0], 6:['回收站', 0, '回收站', 0]}
        zhuomian = default_zhuomian
        done2 = True
        username = ''
        PINpassword = [24, '用户114514']
        IsUserVIP = '零氪'
        Cmemory = Dmemory = Ememory = [24, 'B', 1]
        jdtpf = ['!', '?']
        BIOS_password = ''
        Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
        Dpan = {}
        Epan = {'desktop':[]}
        Cpan_NC = Dpan_NC = Epan_NC = 0
        Jindows_coin_started = False
        Jindows_coin = 0
        browse_history = []
        real_browse_history = []
        IsRoot = False
        recycle_bin = []
        computer = [zhuomian, Cmemory, Dmemory, Ememory, IsUserVIP, Jindows_coin_started, Jindows_coin, equipment, browse_history, real_browse_history, BIOS_password, Cpan, Dpan, Epan]
        MEMORY_LEVEL = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'NB', 'DB', 'CB', 'XB']
        while 1:
            #进入电脑前
            while 1:
                if not BIOS_password == '':
                    while 1:
                        if input('请输入BIOS开机密码') == BIOS_password:
                            break
                if (login_ask := input('请问以直接进入(a)还是虚拟机运行(b)')) == 'b':
                    if PINpassword[0] == 24:
                        print('你需要有一个原账号')
                        login_ask == 'a'
                    else:
                        print('不想做虚拟机了, bug比文件管理的bug还多')
                        '''username = ''
                        PINpassword = [24, '用户114514']
                        jdtpf = ['!', '?']
                        BIOS_password = ''
                        memory = [1024, 'GB', 4]
                        user_state = 'virtual'
                        Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
                        Dpan = {}
                        Epan = {'desktop':[]}
                        IsUserVIP = '零氪'
                        printstyle = '正常'
                        zhuomian_list = []
                        for j in zhuomian:
                            zhuomian_list.append(zhuomian[j])
                        Epan = {'desktop':zhuomian_list}
                        break'''
                if login_ask == 'a':
                    if LOGIN_EASY:
                        print(Back.BLUE+Fore.WHITE,end='')
                        start_time = time()
                        loading(f'欢迎', randint(8, 10)/10)
                        end_time = time()
                        elapsed_time = end_time - start_time
                        print(Style.RESET_ALL,end='')
                        Cmemory = [6, 'GB', 4]
                        Dmemory = [5, 'GB', 4]
                        Ememory = [5, 'GB', 4]
                        IsUserVIP = '零氪'
                        zhuomian = computer[0]
                        user_state == 'administrator'
                        Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
                        Dpan = {}
                        Epan = {'desktop':[]}
                        printstyle = '正常'
                        zhuomian_list = []
                        for j in zhuomian:
                            zhuomian_list.append(zhuomian[j])
                        Epan = {'desktop':zhuomian_list}
                        break
                    if PINpassword[0] == 24:
                        print('您的账号因长时间未登录, 需要填入该账号的信息')
                    reply = input('请输入pin码')
                    '''if reply == '754933482':
                        username = 'Jerry'
                        print('账号名:Jerry')
                        print('权限:作者')
                        Cmemory = [100, 'TB', 5]
                        Dmemory = [100, 'TB', 5]
                        Ememory = [100, 'TB', 5]
                        zhuomian = default_zhuomian
                        for a in RJXX:
                            simplify = RJXX[a][0]
                                if simplify == '我的电脑' or simplify == 'JY瘤懒器' or simplify == 'deepsthink' or simplify == '应用商店':
                                    continue
                                zhuomian[len(zhuomian)+1] = [RJXX[a][0], RJXX[a][2], RJXX[a][0], 0]
                        IsUserVIP = '至尊永久VIP'
                        loading('首次启动ing', randint(2, 5)/24)
                        user_state == 'administrator'
                        Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
                        Dpan = {}
                        Epan = {'desktop':[]}
                        printstyle = '正常'
                        zhuomian_list = []
                        for j in zhuomian:
                            zhuomian_list.append(zhuomian[j])
                        Epan = {'desktop':zhuomian_list}
                        break
                    elif reply == '611739633':
                        username = '一只小鲨『Fun』'
                        print('账号名:一只小鲨『Fun』')
                        print('权限:作者小学朋友')
                        Cmemory = [24, 'TB', 5]
                        Dmemory = [24, 'TB', 5]
                        Ememory = [24, 'TB', 5]
                        zhuomian = default_zhuomian
                        loading('首次启动ing', randint(8, 24)/24)
                        IsUserVIP = '至尊永久VIP'
                        user_state == 'administrator'
                        Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
                        Dpan = {}
                        Epan = {'desktop':[]}
                        printstyle = '正常'
                        zhuomian_list = []
                        for j in zhuomian:
                            zhuomian_list.append(zhuomian[j])
                        Epan = {'desktop':zhuomian_list}
                        break
                    el'''
                    if reply == PINpassword[0]:
                        print('账号名:'+PINpassword[1])
                        print('权限:无')
                        start_time = time()
                        loading('首次启动ing', randint(7, 12)/10)
                        end_time = time()
                        elapsed_time = end_time - start_time
                        IsUserVIP = '零氪'
                        Cmemory = [12, 'GB', 4]
                        Dmemory = [10, 'GB', 4]
                        Ememory = [10, 'GB', 4]
                        zhuomian = computer[0]
                        user_state == 'administrator'
                        Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
                        Dpan = {}
                        Epan = {'desktop':[]}
                        printstyle = '正常'
                        zhuomian_list = []
                        for j in zhuomian:
                            zhuomian_list.append(zhuomian[j])
                        Epan = {'desktop':zhuomian_list}
                        break
                    else:
                        if not PINpassword[0] == 24:
                            print('PIN码输入错误')
                            continue
                        print('pin码输入错误, 正在为您开新账号, 您需回答三个问题')
                        if input('牛顿第一定律是谁提出的(a.牛顿  b.科比·布莱恩特  c.蔡徐坤)') == 'a':
                            if input('买一个5块的东西要几块(a.5  b.24  c.8)') == 'a':
                                if input('"apple"的英文是什么(a.apple  b.苹果  c.banana)') == 'a':
                                    print(Fore.GREEN + '验证成功' + Fore.RESET)
                                    print(Back.BLUE+Fore.WHITE,end='')
                                    start_time = time()
                                    loading(f'欢迎', randint(8, 10)/10)
                                    end_time = time()
                                    elapsed_time = end_time - start_time
                                    print(Style.RESET_ALL,end='')
                                    zhuomian = default_zhuomian
                                    Cmemory = [6, 'GB', 4]
                                    Dmemory = [5, 'GB', 4]
                                    Ememory = [5, 'GB', 4]
                                    IsUserVIP = '零氪'
                                    zhuomian = computer[0]
                                    user_state == 'administrator'
                                    Cpan = {'System':{'code':{'about':'ЈΕſſΥ', 'occupy':24}}}
                                    Dpan = {}
                                    Epan = {'desktop':[]}
                                    printstyle = '正常'
                                    zhuomian_list = []
                                    for j in zhuomian:
                                        zhuomian_list.append(zhuomian[j])
                                    Epan = {'desktop':zhuomian_list}
                                    break
                                else:
                                    print('输入错误')
                            else:
                                print('输入错误')
                        else:
                            print('输入错误')
                elif login_ask == 'BIOS':
                    BIOS_password_temp = BIOS_password
                    equipment_temp = equipment
                    while 1:
                        print(f'BIOS 系统:')
                        print(f'1.BIOS开机密码')
                        print(f'2.恢复出厂设置')
                        print(f'3.转为{"电脑端" if equipment_temp == "mobile" else "手机端"}')
                        print(f'4.退出')
                        print(f'5.保存并退出', end='')
                        if (BIOS_ask := input()) == '1':
                            BIOS_password_temp = input('BIOS开机密码:')
                        elif BIOS_ask == '2':
                            if input('确定恢复出厂设置(Y代表同意)') == 'Y':
                                clear_data()
                                break
                        elif BIOS_ask == '3':
                            if equipment_temp == 'mobile':
                                equipment_temp = 'computer'
                            elif equipment_temp == 'computer':
                                equipment_temp = 'mobile'
                        elif BIOS_ask == '4':
                            break
                        elif BIOS_ask == '5':
                            BIOS_password = BIOS_password_temp
                            equipment = equipment_temp
                            break
            if user_state == 'administrator':
                computer = [zhuomian, Cmemory, Dmemory, Ememory, IsUserVIP, Jindows_coin_started, Jindows_coin, equipment, browse_history, real_browse_history, BIOS_password, Cpan, Dpan, Epan]
            elif user_state == 'virtual':
                computer_fake = [zhuomian, Cmemory, Dmemory, Ememory, IsUserVIP, Jindows_coin_started, Jindows_coin, equipment, BIOS_password, Cpan, Dpan, Epan]
            if MEMORY_EASY:
                Cmemory = Dmemory = Ememory = [754933482, 'XB', 14]
            if SOFTWARE_EASY:
                for a in RJXX:
                    if if_cannot_remove(RJXX[a][0]):
                        continue
                    zhuomian[len(zhuomian)+1] = [RJXX[a][0], RJXX[a][2], RJXX[a][0], 0]
            
            #进入电脑后
            enter_counter += 1
            JY_influence = True
            while 1:
                display_desktop = done = True
                display_line = False
                Wrong_Combo = 0
                while done:
                    if display_line:
                        print('---------------------------------------大分割线---------------------------------------')
                    if display_desktop:
                        print('您的桌面:')
                        for j in zhuomian:
                            print('\t', end='')
                            print(f'{j}.', end='')
                            if zhuomian[j][3] == 0:
                                print(zhuomian[j][0])
                            else:
                                print(zhuomian[j][2])
                    if JY_influence:
                        sleep(randint(8,12) / 10)
                        print(f'JY瘤懒器:今日开机时间{round(elapsed_time,1)}秒,超过了{randint(80,99)}.{randint(97,99)}%的人')
                        JY_influence = False
                    all_instruction = input('执行操作(输入how查看如何操作):')
                    display_desktop = display_line = False
                    instruction = all_instruction.split(' ')
                    Successful = True
                    Wrong_Combo_temp = Wrong_Combo
                    Wrong_Combo = 0
                    if printstyle == '我的世界风':
                        if len(all_instruction) == 0:
                            instruction = []
                            Successful = False
                            Wrong_Combo = Wrong_Combo_temp + 1
                        elif all_instruction[0] == '/':
                            b = ''
                            for a in all_instruction:
                                b += a
                            all_instruction = b
                            instruction = all_instruction.split(' ')
                        else:
                            instruction = []
                            Successful = False
                            Wrong_Combo = Wrong_Combo_temp + 1
                    if instruction[0] == 'Jin':
                        if all_instruction == 'Jin':
                            print('1.关机')
                            print('2.取消')
                            choose = input()
                            if choose == '1':
                                raise SystemExit('电脑关机')
                            elif choose == '2':
                                pass
                            else:
                                print('执行操作失败')
                        else:
                            Jin_and_anotherkey(instruction[1:len(instruction)])
                            if IsRoot:
                                def if_cannot_remove(a):
                                    return False
                            continue
                    if instruction[0] == 'Alt':
                        Alt_and_anotherkey(instruction[1:len(instruction)])
                        continue
                    if instruction[0] == 'ULcmd':
                        if len(instruction) == 2:
                            if instruction[1] == 'ErrShutdown':
                                raise SystemError('command error exit')
                    if (instruction_length := len(instruction)) == 1:
                        if all_instruction == 'how':
                            display_line = True
                            print(f'引号内表示文字, 没有引号则代表参数, 括号内表示提示{HOW}')
                        elif all_instruction == '更新情况' or all_instruction == 'updates':
                            print(CHANGELOG)
                        elif all_instruction == '退出登录' or all_instruction == 'logout':
                            done = done2 = False
                            if user_state == 'ainstructioninistrator':
                                computer = [zhuomian, Cmemory, Dmemory, Ememory, IsUserVIP, Jindows_coin_started, Jindows_coin, equipment, browse_history, real_browse_history, BIOS_password, Cpan, Dpan, Epan]
                        elif all_instruction == '下载' or all_instruction == 'download':
                            has_shop = False
                            for a in zhuomian:
                                if zhuomian[a][0] == '应用商店':
                                    has_shop = True
                                    break
                            if has_shop:
                                print('正在跳转应用商店')
                                sleep(randint(5, 8) / 10)
                                if download('') == '下载成功':
                                    display_line = display_desktop = True
                            else:
                                print(f'你需要应用商店才能下载')
                        elif all_instruction == '桌面' or all_instruction == 'desktop':
                            display_desktop = True
                        else:
                            Successful = False
                            Wrong_Combo = Wrong_Combo_temp + 1
                    elif instruction_length == 2:
                        if instruction[0] == '打开' or instruction[0] == 'start':
                            for jj in zhuomian:
                                if instruction[1] == str(jj):
                                    display_line = True
                                    start_software = zhuomian[jj][0]
                                    if start_software == '我的电脑':
                                        print('---------------------------------------大分割线---------------------------------------')
                                        print(f'账号名:{username}')
                                        print(f'使用电脑:{COMPUTER_NAME}(简称Jindows)')
                                        print(f'充值情况:{IsUserVIP}')
                                        if Jindows_coin_started:
                                            print(f'Jindows-coin(s):{Jindows_coin}')
                                        BLNC(Cpan, 'C')
                                        BLNC(Dpan, 'D')
                                        BLNC(Epan, 'E')
                                        zhuomianNC()
                                        strlong = [len(f'{NCZH(Cpan_NC, 3, 3)[1]}{NCZH(Cpan_NC, 3, 3)[0]}'),
                                            len(f'{NCZH(Dpan_NC, 3, 3)[1]}{NCZH(Dpan_NC, 3, 3)[0]}'),
                                            len(f'{NCZH(Epan_NC+zhuomian_NC, 3, 3)[1]}{NCZH(Epan_NC+zhuomian_NC, 3, 3)[0]}')]
                                        longest = max(strlong)
                                        print(f'C盘:约{NCZH(Cpan_NC, 3, 3)[1]}{NCZH(Cpan_NC, 3, 3)[0]}{(longest-strlong[0])*" "}/{Cmemory[0]}{Cmemory[1]}')
                                        print(f'D盘:约{NCZH(Dpan_NC, 3, 3)[1]}{NCZH(Dpan_NC, 3, 3)[0]}{(longest-strlong[1])*" "}/{Dmemory[0]}{Dmemory[1]}')
                                        print(f'E盘:约{NCZH(Epan_NC+zhuomian_NC, 3, 3)[1]}{NCZH(Epan_NC+zhuomian_NC, 3, 3)[0]}{(longest-strlong[2])*" "}/{Ememory[0]}{Ememory[1]}')
                                        choose = input('直接回车进行深度操作')
                                        if choose == 'Alt F4':
                                            break
                                        if choose == '':
                                            print('1.退出')
                                            print('2.显示软件相关信息')
                                            wddn_bool = True
                                            while wddn_bool:
                                                wddn_ask = input('')
                                                if wddn_ask == 'Alt F4':
                                                    wddn_bool = False
                                                elif wddn_ask == '1':
                                                    wddn_bool = False
                                                    continue
                                                elif wddn_ask == '2':
                                                    print('---小分割线---')
                                                    for jjj in zhuomian:
                                                        if zhuomian[jjj][3] == 0:
                                                            print(f'{zhuomian[jjj][0]}占用内存:{NCZH(zhuomian[jjj][1], 3, 2)[1]}{NCZH(zhuomian[jjj][1], 3, 2)[0]}')
                                                        else:
                                                            print(f'{zhuomian[jjj][2]}占用内存:{NCZH(zhuomian[jjj][1], 3, 2)[1]}{NCZH(zhuomian[jjj][1], 3, 2)[0]}')
                                                    print(f'总计内存(精细):{NCZH(zhuomian_NC, 3, 24)[1]}{NCZH(zhuomian_NC, 3, 24)[0]}')
                                                else:
                                                    print(Fore.RED + '听不懂您在说什么, 现在还是进行深度操作' + Fore.RESET)
                                                    continue
                                                print('---小分割线---')
                                            del wddn_bool
                                    elif start_software == 'JY瘤懒器':
                                        #跳转对应网站
                                        while 1:
                                            print_history = ''
                                            if browse_history == []:
                                                print_history = '空'
                                            else:
                                                print_history += '\n'
                                                if len(browse_history) > 0:
                                                    print_history += browse_history[0]
                                                browse_history_right_side_where_start_word = max([len(n) for n in browse_history if browse_history.index(n) % 2 == 0]) + 4
                                                if len(browse_history) > 1:
                                                    print_history += f"{(browse_history_right_side_where_start_word - len(browse_history[0])) * ' '}{browse_history[1]}"
                                                if len(browse_history) > 2:
                                                    print_history += f"\n{browse_history[2]}"
                                                if len(browse_history) > 3:
                                                    print_history += f"{(browse_history_right_side_where_start_word - len(browse_history[2])) * ' '}{browse_history[3]}"
                                                if len(browse_history) > 4:
                                                    print_history += f"\n{browse_history[4]}"
                                                if len(browse_history) > 5:
                                                    print_history += f"{(browse_history_right_side_where_start_word - len(browse_history[4])) * ' '}{browse_history[5]}"
                                            print_history += '\n'
                                            URLinput = input(f'输入网址(b退出)(/查看指令)\n浏览记录:{print_history}')
                                            while not URLinput:
                                                URLinput = input(f'输入网址(b退出)(/查看指令)\n浏览记录:{print_history}')
                                            if URLinput[0] == '/':
                                                if URLinput == '/':
                                                    print(
'''/ command:
/exit
    退出浏览器
/clear
    history
        清空历史记录''')
                                                    continue
                                                else:
                                                    URLsplit = URLinput.split(' ')
                                                    if (lenURLinput := len(URLinput)) == 1:
                                                        if URLsplit[0] == '/exit':
                                                            break
                                                    elif lenURLinput == 2:
                                                        if URLsplit[0] == '/clear':
                                                            if URLsplit[1] == 'history':
                                                                browse_history = []
                                                                print('清空完成')
                                            if URLinput == 'b' or URLinput == 'Alt F4':
                                                break
                                            try:
                                                last = URLinput.split('.')[-1]
                                                if last == 'seek':
                                                    raise SystemError('退出try')
                                                b = ''
                                                for a in range(0, len(URLinput.split('.'))-1):
                                                    b += URLinput.split('.')[a]
                                                    if not a == len(URLinput.split('.'))-2:
                                                        b += '.'
                                                URLinput = b
                                                if URLinput == '':
                                                    Url = last
                                                else:
                                                    Url = f'{URLinput}.{last}'
                                                if Url in browse_history:
                                                    del browse_history[browse_history.index(Url)]
                                                browse_history.append(Url)
                                                will_code = not(Url in real_browse_history)
                                                real_browse_history.append(Url)
                                                if len(browse_history) > 6:
                                                    del browse_history[0]
                                                if eval(f'{URLinput}.seek()') == '可以使用':
                                                    pass
                                                else:
                                                    print(eval(f'{URLinput}.seek()'))
                                                    continue
                                            except:
                                                print('网页无法打开')
                                                continue
                                            if will_code:
                                                browse_coding()
                                            if eval(f'{Url}()') == 'Alt F4退出':
                                                break
                                    elif start_software == 'deepthink':
                                        AD()
                                        Alt_F4 = False
                                        while not Alt_F4:
                                            Problem = ['明明盲人没有瞎, 那为什么看不见', '是先有鸡还是先有蛋', '我一拳打倒了我自己, 我算强大还是脆弱', '为什么警察不去监狱抓人', '为什么烘手机不能把手机给烘了', '为什么冰箱是柜子冰柜是箱子', '站在电梯里为什么说我们坐电梯', '我们晒太阳为什么是太阳晒我们']
                                            ask = input(f'请写上你的疑惑(比如:{choice(Problem)})(输入b退出)')
                                            if ask == 'b' or ask == 'Alt F4':
                                                break
                                            else:
                                                print('思考中...', end='')
                                                sleep(randint(3,7))
                                                print('\r服务器繁忙,请稍后再试')
                                    elif start_software == '应用商店':
                                        choose = input('下载什么')
                                        if choose == 'Alt F4':
                                            break
                                        download(choose)
                                    elif start_software == '设置':
                                        Jin_I()
                                    elif start_software == '回收站':
                                        while 1:
                                            for speak in recycle_bin:
                                                print(f'{recycle_bin.index(speak) + 1}.{speak[2]}')
                                            print('恢复 + 空格 + 序号')
                                            print('删除 + 空格 + 序号')
                                            print('exit')
                                            all_reply = input('执行操作:')
                                            reply = all_reply.split(' ')
                                            if reply[0] == '恢复':
                                                try:
                                                    temp = recycle_bin[int(reply.split(' ')[1]) - 1]
                                                    zhuomian[len(zhuomian)+1] = temp
                                                    del recycle_bin[int(reply.split(' ')[1]) - 1]
                                                    display_desktop = True
                                                except:
                                                    print('无效')
                                            elif reply[0] == '删除':
                                                try:
                                                    del recycle_bin[int(reply.split(' ')[1]) - 1]
                                                except:
                                                    print('无效')
                                            elif all_reply == 'exit' or all_reply == 'Alt F4':
                                                break
                                            else:
                                                print('无效')
                                    elif start_software == '计算题':
                                        display_desktop = True
                                        df = jisuanti.cn()
                                        if Jindows_coin_started:
                                            Jindows_coin += df//2
                                            print(f'增加{df//2}coin')
                                    elif start_software == '我的世界':
                                        AD()
                                        print('正在加载......')
                                        sleep(randint(4, 8))
                                        print(Fore.YELLOW + '系统:我的世界长时间未响应, 可能会在3秒后闪退' + Fore.RESET)
                                        sleep(randint(2, 4))
                                        if randint(1, 50)<10:
                                            class Jinecraft:
                                                def NewUser(a:str='未登录用户'):#假装是我的世界代码导致内存溢出
                                                    System.wrong()#来自系统报错
                                            Jinecraft.NewUser('未登录用户')
                                    elif start_software == 'Jindows-coin-installer':
                                        print('Jindows-coin安装向导')
                                        if Jindows_coin_started:
                                            print('你已安装完成, 可以将此安装向导卸载')
                                            break
                                        choose = input('直接回车下载')
                                        if choose == 'Alt F4':
                                            break
                                        elif choose == '':
                                            loading('正在配置Jindows-coin', randint(9, 20)/15)
                                            Jindows_coin_started = True
                                            print('下载完成, 初始金币24')
                                            Jindows_coin = 24
                                    elif start_software == '语言选择器':
                                        AD()
                                        TOTAL_PRINTSTYLE = ['正常', '我的世界风', '不耐烦']
                                        reply = input('搜索你想要切换的种类(直接回车展示全部)')
                                        if reply == 'Alt F4':
                                            break
                                        find = []
                                        for jj in range(0, len(TOTAL_PRINTSTYLE)):
                                            if reply in TOTAL_PRINTSTYLE[jj] or reply == '':
                                                find.append(jj)
                                        if len(find) > 0:
                                            for a in range(0, len(find)):
                                                print(f'{a+1}.{TOTAL_PRINTSTYLE[find[a]]}')
                                            jj = input('从以上类似结果选一个')
                                            if jj == 'Alt F4':
                                                break
                                            try:
                                                jj = int(jj)
                                                printstyle = TOTAL_PRINTSTYLE[find[jj-1]]
                                            except:
                                                print(Fore.RED + '回答不符合标准' + Fore.RESET)
                                        else:
                                            print('无搜索结果')
                                    elif start_software == '各种密码转换器':
                                        AD()
                                        msmm_encode = {
                                            'a':'.-'     , 'A':'.-'     ,
                                            'b':'-...'   , 'B':'-...'   ,
                                            'c':'-.-.'   , 'C':'-.-.'   ,
                                            'd':'-..'    , 'D':'-..'    ,
                                            'e':'.'      , 'E':'.'      ,
                                            'f':'..-.'   , 'F':'..-.'   ,
                                            'g':'--.'    , 'G':'--.'    ,
                                            'h':'....'   , 'H':'....'   ,
                                            'i':'..'     , 'I':'..'     ,
                                            'j':'.---'   , 'J':'.---'   ,
                                            'k':'-.-'    , 'K':'-.-'    ,
                                            'l':'.-..'   , 'L':'.-..'   ,
                                            'm':'--'     , 'M':'--'     ,
                                            'n':'-.'     , 'N':'-.'     ,
                                            'o':'---'    , 'O':'---'    ,
                                            'p':'.--.'   , 'P':'.--.'   ,
                                            'q':'--.-'   , 'Q':'--.-'   ,
                                            'r':'.-.'    , 'R':'.-.'    ,
                                            's':'...'    , 'S':'...'    ,
                                            't':'-'      , 'T':'-'      ,
                                            'u':'..-'    , 'U':'..-'    ,
                                            'v':'...-'   , 'V':'...-'   ,
                                            'w':'.--'    , 'W':'.--'    ,
                                            'x':'-..-'   , 'X':'-..-'   ,
                                            'y':'-.--'   , 'Y':'-.--'   ,
                                            'z':'--..'   , 'Z':'--..'   ,
                                            '1':'.----'  , '6':'-....'  ,
                                            '2':'..---'  , '7':'--...'  ,
                                            '3':'...--'  , '8':'---..'  ,
                                            '4':'....-'  , '9':'----.'  ,
                                            '5':'.....'  , '0':'-----'  ,
                                            '/':'-..-.'  ,
                                            '_':'..--.-' ,
                                            '$':'...-..-',
                                            '@':'.--.-.' ,
                                            '。':'.-.-.-',
                                            '=':'-...-'  ,
                                            ' ':'.---'   ,
                                            '(':'-.--.'  , '（':'-.--.' ,
                                            ')':'-.--.-' , '）':'-.--.-',
                                            '?':'..--..' , '？':'..--..',
                                            '!':'-.-.--' , '！':'-.-.--',
                                            ', ':'--..--', '，':'--..--',
                                            "'":'.----.' , '‘':'.----.' , '’':'.----.' ,
                                            '"':'.-..-.' , '“':'.-..-.' , '”':'.-..-.' ,
                                            ':':'---...' , '：':'---...',
                                            ';':'-.-.-.' , '；':'-.-.-.'
                                        }
                                        while 1:
                                            reply = input('m进行摩斯密码转换\n否则退出')
                                            if reply == 'Alt F4':
                                                break
                                            elif reply == 'm':
                                                reply = input('a编码b解码否则退出')
                                                if reply == 'Alt F4':
                                                    break
                                                elif reply == 'a':
                                                    msmm = input('内容:')
                                                    if msmm == 'Alt F4':
                                                        break
                                                    output_msmm = ''
                                                    for jj in range(0, len(msmm)):
                                                        output_msmm += msmm_encode[msmm[jj]] if msmm[jj] in list(msmm_encode) else msmm[jj]
                                                        if not jj == len(msmm)-1:
                                                            if not msmm[jj] in list(msmm_encode):
                                                                try:
                                                                    if not msmm[jj+1] in list(msmm_encode):
                                                                        pass
                                                                    else:
                                                                        output_msmm += '/'
                                                                except:
                                                                    pass
                                                            else:
                                                                output_msmm += '/'
                                                    print(f'编码后:{output_msmm}')
                                                elif reply == 'b':
                                                    msmm = input('内容:')
                                                    if msmm == 'Alt F4':
                                                        break
                                                    output_msmm = ''
                                                    for jj in range(0, len(msmm.split('/'))):
                                                        try:
                                                            output_msmm += get_key(msmm_encode, msmm.split('/')[jj])
                                                        except:
                                                            output_msmm += msmm.split('/')[jj]
                                                    print(f'解码后:{output_msmm}')
                                                else:
                                                    break
                                            else:
                                                break
                                    elif start_software == '机器人使命召唤低配版':
                                        loading('正在匹配对局', randint(4, 10)/10)
                                        SMZH_CFL = randint(30,80)#触发率:达到稳定率的概率
                                        SMZH_WDL = int((100 - (SMZH_CFL * randint(6,13)/10)) // 1)#触发率越低,稳定率越高,反之一样
                                        SMZH_CFL_F = randint(30,80)
                                        SMZH_WDL_F = int((100 - (SMZH_CFL * randint(6,15)/10)) // 1)
                                        if of100(SMZH_CFL):
                                            if of100(SMZH_WDL):
                                                SMZH_PERFECT = 'Perfect'
                                                print('你搭得很完整')
                                            else:
                                                if of100(SMZH_WDL):
                                                    SMZH_PERFECT = 'Normal'
                                                    print('你搭得还行,有几率出错')
                                                else:
                                                    SMZH_PERFECT = 'Bad'
                                                    print('你搭得很失败')
                                        else:
                                            if of100(100-SMZH_WDL):
                                                SMZH_PERFECT = 'Perfect'
                                                print('你搭得很完整')
                                            else:
                                                if of100(100-SMZH_WDL):
                                                    SMZH_PERFECT = 'Normal'
                                                    print('你搭得还行,有几率出错')
                                                else:
                                                    SMZH_PERFECT = 'Bad'
                                                    print('你搭得很失败')
                                        sleep(0.3)
                                        if of100(SMZH_CFL_F):
                                            if of100(SMZH_WDL_F):
                                                SMZH_PERFECT_F = 'Perfect'
                                                print('你队友搭得很完整')
                                            else:
                                                if of100(SMZH_WDL_F):
                                                    SMZH_PERFECT_F = 'Normal'
                                                    print('你队友搭得还行,有几率出错')
                                                else:
                                                    SMZH_PERFECT_F = 'Bad'
                                                    print('你队友搭得很失败')
                                        else:
                                            if of100(100-SMZH_WDL_F):
                                                SMZH_PERFECT_F = 'Perfect'
                                                print('你队友搭得很完整')
                                            else:
                                                if of100(100-SMZH_WDL_F):
                                                    SMZH_PERFECT_F = 'Normal'
                                                    print('你队友搭得还行,有几率出错')
                                                else:
                                                    SMZH_PERFECT_F = 'Bad'
                                                    print('你队友搭得很失败')
                                        for SMZH_round in range(1,5):
                                            sleep(0.8)
                                            print(f'回合{SMZH_round}/4')
                                            sleep(0.3)
                                            if SMZH_PERFECT == 'Perfect':
                                                print('自动环节很顺利')
                                            elif SMZH_PERFECT == 'Normal':
                                                if of100(SMZH_CFL):
                                                    if of100(SMZH_WDL):
                                                        print('虽然很差,但是还是很顺利')
                                                    else:
                                                        print('出界了')
                                            else:
                                                print('出界了')
                                            sleep(0.3)
                                            print('手动环节')
                                            sleep(0.3)
                                            if SMZH_PERFECT == 'Perfect' and SMZH_PERFECT_F == 'Perfect':
                                                print('你赢了')
                                            elif SMZH_PERFECT == 'Normal':
                                                if of100(SMZH_CFL):
                                                    print('你输了')
                                                    break
                                                else:
                                                    print('你赢了')
                                            else:
                                                print('你输了')
                                                break
                                            if SMZH_round == 4:
                                                SMZH_round = 5
                                        if SMZH_round == 3:
                                            print('获得三等奖')
                                        elif SMZH_round == 4:
                                            print('喜提二等奖')
                                        elif SMZH_round == 5:
                                            print('荣获一等奖')
                                        else:
                                            print('安慰奖')
                                    break
                        elif instruction[0] == '下载' or instruction[0] == 'download':
                            has_shop = False
                            for a in zhuomian:
                                if zhuomian[a][0] == '应用商店':
                                    has_shop = True
                                    break
                            if has_shop:
                                print('正在跳转应用商店')
                                sleep(randint(5, 8) / 10)
                                if download(instruction[1]) == '下载成功':
                                    display_line = display_desktop = True
                            else:
                                print(f'你需要应用商店才能下载{instruction[1]}')
                        elif instruction[0] == '卸载' or instruction[0] == 'unload':
                            try:
                                if int(instruction[1]) < len(zhuomian)+1:
                                    display_line = display_desktop = True
                                    jj = int(instruction[1])
                                    if input(f'确认删除{zhuomian[jj][2]}吗, 直接回车即可删除') == '':
                                        if if_cannot_remove(zhuomian[jj][0]):
                                            print(Fore.RED + '电脑自带软件无法删除' + Fore.RESET)
                                        else:
                                            recycle_bin.append(zhuomian[jj])
                                            gnidaol(f'正在卸载{zhuomian[jj][2]}', randint(6, 13) / 8)
                                            for jjj in range(jj, len(zhuomian)):
                                                zhuomian[jjj] = zhuomian[jjj+1]
                                            del zhuomian[len(zhuomian)]
                            except:
                                print('无法卸载')
                        else:
                            Successful = False
                            Wrong_Combo = Wrong_Combo_temp + 1
                    elif instruction_length == 3:
                        if instruction[0] == '软件改名' or instruction[0] == 'rename':
                            try:
                                target = int(instruction[1])
                                if target > len(zhuomian)-1:
                                    raise SystemError('退出try')
                            except:
                                print(Fore.RED + '序号出错' + Fore.RESET)
                                continue
                            zhuomian[target] = [zhuomian[target][0], zhuomian[target][1], instruction[2], zhuomian[target][3]+1]
                            display_line = display_desktop = True
                        elif instruction[0] == '修改PIN码' or instruction[0] == 'modifyPIN':
                            PINpassword = [instruction[1] or 'None', instruction[2] or 'None']
                            print(f'您的新建PIN码:{PINpassword[0]}')
                            print(f'您的新建用户名:{PINpassword[1]}')
                        elif instruction[0] == '软件移位' or instruction[0] == 'move':
                            try:
                                ist = int(instruction[1])
                                ond = int(instruction[2])
                                if ist > len(zhuomian) or ond > len(zhuomian):
                                    raise SystemError('退出try')
                            except:
                                print(Fore.RED + '序号出错' + Fore.RESET)
                                continue
                            display_desktop = True
                            if ist > ond:
                                temp0 = zhuomian[ond]
                                zhuomian[ond] = zhuomian[ist]
                                b = 0
                                for a in range(ond + 1, ist + 1):
                                    exec(f'temp{b + 1} = zhuomian[a];zhuomian[a] = temp{b}')
                                    b += 1
                                exec(f'zhuomian[a] = temp{b - 1}')
                            elif ond > ist:
                                temp0 = zhuomian[ist]
                                for a in range(ist, ond):
                                    zhuomian[a] = zhuomian[a + 1]
                                zhuomian[ond] = temp0
                        elif instruction[0] == '软件交换' or instruction[0] == 'exchange':
                            try:
                                ist = int(instruction[1])
                                ond = int(instruction[2])
                                if ist > len(zhuomian) or ond > len(zhuomian):
                                    raise SystemError('退出try')
                            except:
                                print(Fore.RED + '序号出错' + Fore.RESET)
                                continue
                            temp = zhuomian[ist]
                            zhuomian[ist] = zhuomian[ond]
                            zhuomian[ond] = temp
                            display_desktop = True
                        else:
                            Successful = False
                            Wrong_Combo = Wrong_Combo_temp + 1
                    if not Successful:
                        if printstyle == '正常':
                            print(Fore.RED + '听不懂你的意思, 可以等待作者更新此功能' + Fore.RESET)
                        elif printstyle == '我的世界风':
                            print(Fore.RED + f'未知的命令:{all_instruction}, 请检查命令是否存在, 以及您对它是否有使用权限' + Fore.RESET)
                        elif printstyle == '不耐烦':
                            if Wrong_Combo == 0:
                                print('听不懂你的意思, 可以等待作者更新此功能')
                            elif Wrong_Combo == 1:
                                print('真的听不懂你的意思, 请检查一下')
                            elif Wrong_Combo == 2:
                                print('你干嘛~, 就不能再检查一遍吗')
                            elif Wrong_Combo == 3:
                                print('你什么意思啊!故意对着我干是吧')
                            else:
                                if Wrong_Combo > 3:
                                    print(f'不是你什么意思啊, 你{(Wrong_Combo - 2) // 4 * "直"}{(Wrong_Combo % 4) * "~"}接给我坐下!')
                if not done2:
                    break
    except SystemExit:
        dot = 1
        for a in range(20):
            if dot == 6:
                dot = 0
            dot += 1
            print(Fore.WHITE + Back.BLUE + f'\r正在关机{dot * "."}{(6 - dot) * " "}', end='')
            sleep(0.3)
        print(Style.RESET_ALL, end='')
        raise SystemExit
    except Exception as error:
        sleep(0.5)
        print(Back.BLUE + Fore.WHITE + 24 * '\n\n')
        sleep(1)
        print('''

A problem has been detected and windows has been shut down to prevent damage
to your computer

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to be sure you have adequate disk space. If a driver is
identified in the stop message, disable the driver or check
with the manufacturer for driver updates. Try changing video
adapters.

Check with your hardware vendor for any BIOS updates. Disable
BIOS memory options such as caching or shadowing. If you need
to use safe Mode to remove or disable components, you should
know this computer has no safe Mode.


Trchnical information:

    *** STOP: 0x114514MAN(0xJerry&snk, 0x754933482, 0x611739633, 0xWhatCanISay)






''')
        print("Error:", exc_info()[0], end='\n\nmore:\n')
        print_exc()
        print('\n\n正在采集错误信息...' + Style.RESET_ALL)
        sleep(randint(10,20))
        print('正在尝试重启...')
        sleep(randint(3,5))