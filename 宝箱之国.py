# coding=utf-8
import random
import easygui as g
import datetime

'''
模块：我想查询当前金币余额
'''
def read_sum_money_now():
    global sum_money_now
    global reward
    sum_money_now = 0  # 金币总量
    reward = 0
    f = open('sum_money_now.md', 'a+')  # 判断是否有这个文件，没有则创建一个。
    # 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f = open('sum_money_now.md', 'r')
    # 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read() == '':  # 判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        # 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(0))
    else:
        pass
    f = open('sum_money_now.md', 'r')
    sum_money_now = float(f.read())  # 读取文件已经存在的数据


'''
模块：我想完成任务领取金币
'''

def small_reward():
    global sum_money_now
    global reward
    sum_money_now = 0  # 金币总量
    reward = 0
    f=open('sum_money_now.md', 'a+')#判断是否有这个文件，没有则创建一个。
    #打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f=open('sum_money_now.md', 'r')
    #以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read()=='':#判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(0))
    else:
        pass
    f=open('sum_money_now.md', 'r')
    last_money = float(f.read())#读取文件已经存在的数据
    f=open('sum_money_now.md', 'w+')#更新文件里的数据，并保存；
    #打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    reward = random.uniform(1, 5)
    sum_money_now=reward+last_money
    f.write(str(last_money+reward))
    #print(str(round(sum_money_now,1)))
    f.close()


def middle_reward():
    global sum_money_now
    global reward
    sum_money_now = 0  # 金币总量
    reward = 0
    f=open('sum_money_now.md', 'a+')#判断是否有这个文件，没有则创建一个。
    #打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f=open('sum_money_now.md', 'r')
    #以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read()=='':#判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(0))
    else:
        pass
    f=open('sum_money_now.md', 'r')
    last_money = float(f.read())#读取文件已经存在的数据
    f=open('sum_money_now.md', 'w+')#更新文件里的数据，并保存；
    #打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    reward = random.uniform(5, 10)
    sum_money_now=reward+last_money
    f.write(str(last_money+reward))
    f.close()

def super_reward():
    global sum_money_now
    global reward
    sum_money_now = 0  # 金币总量
    reward = 0
    f=open('sum_money_now.md', 'a+')#判断是否有这个文件，没有则创建一个。
    #打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f=open('sum_money_now.md', 'r')
    #以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read()=='':#判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(0))
    else:
        pass
    f=open('sum_money_now.md', 'r')
    last_money = float(f.read())#读取文件已经存在的数据
    f=open('sum_money_now.md', 'w+')#更新文件里的数据，并保存；
    #打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    reward = random.uniform(10,20)
    sum_money_now=reward+last_money
    f.write(str(last_money+reward))
    f.close()

#打开宝箱获得金币奖励模块
def complete_task():
    n=g.buttonbox(msg='大佬您又完成了什么等级的任务呀？O(∩_∩)O ', title='', choices=('初级任务：奖励1~5金币', '中级任务：奖励5~10金币', '高级任务：奖励10~20金币'))
    if n=='初级任务：奖励1~5金币':
        #sum_money_now = 0
        small_reward()
        g.msgbox(
            '恭喜您完成初级任务，您获得了{' + str(round(reward, 1)) + '}个金币~大佬，您目前的余额还有{' + str(round(sum_money_now, 1)) + '}个金币',
            ok_button="好的，朕已阅")
    elif n== '中级任务：奖励5~10金币':
        middle_reward()
        g.msgbox(
            '恭喜您完成中级任务，您获得了{' + str(round(reward, 1)) + '}个金币~大佬，您目前的余额还有{' + str(round(sum_money_now, 1)) + '}个金币',
            ok_button="好的，朕已阅")
    elif n == '高级任务：奖励10~20金币':
        super_reward()
        g.msgbox(
            '恭喜您完成高级任务，您获得了{' + str(round(reward, 1)) + '}个金币~大佬，您目前的余额还有{' + str(round(sum_money_now, 1)) + '}个金币',
            ok_button="好的，朕已阅")
    else:
        pass

'''
模块：我想消费金币开宝箱
'''

def small_box():
    global sum_money_now
    global reward
    sum_money_now = 0  # 金币总量
    reward = 0
    f=open('sum_money_now.md', 'a+')#判断是否有这个文件，没有则创建一个。
    #打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f=open('sum_money_now.md', 'r')
    #以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read()=='':#判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(0))
    else:
        pass
    f=open('sum_money_now.md', 'r')
    last_money = float(f.read())#读取文件已经存在的数据
    f=open('sum_money_now.md', 'w+')#更新文件里的数据，并保存；
    #打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    reward = random.uniform(10,20)
    sum_money_now=last_money-reward
    f.write(str(last_money-reward))
    f.close()

def middle_box():
    global sum_money_now
    global reward
    sum_money_now=0
    reward=0
    f=open('sum_money_now.md', 'a+')#判断是否有这个文件，没有则创建一个。
    #打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f=open('sum_money_now.md', 'r')
    #以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read()=='':#判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(sum_money_now))
    else:
        pass
    f=open('sum_money_now.md', 'r')
    last_money = float(f.read())#读取文件已经存在的数据
    f=open('sum_money_now.md', 'w+')#更新文件里的数据，并保存；
    #打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    reward = random.uniform(20,50)
    sum_money_now=last_money-reward
    f.write(str(last_money-reward))
    f.close()

def super_box():
    global sum_money_now
    global reward
    sum_money_now = 0
    reward = 0
    f=open('sum_money_now.md', 'a+')#判断是否有这个文件，没有则创建一个。
    #打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f=open('sum_money_now.md', 'r')
    #以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read()=='':#判断文件是否为空
        f = open('sum_money_now.md', 'a+')
        #打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        f.write(str(sum_money_now))
    else:
        pass
    f=open('sum_money_now.md', 'r')
    last_money = float(f.read())#读取文件已经存在的数据
    f=open('sum_money_now.md', 'w+')#更新文件里的数据，并保存；
    #打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    reward = random.uniform(50,100)
    sum_money_now=last_money-reward
    f.write(str(sum_money_now))
    f.close()

def choujiang_small_box_contains():
    f = open('small_box_contains.md', 'r')
    small_box_contains=f.read()
    #print(f.read())
    small_box_contains_list=small_box_contains.split("，")#为方便输入要以中文的逗号分割……,将字符串以中文逗号分割成由多个子字符串组成的列表。
    choujiang=random.randint(0,len(small_box_contains_list)-1)
    f.close()
    g.msgbox('恭喜您这次开宝箱获得了{'+small_box_contains_list[choujiang]+'}作为奖励！！！',ok_button="好的，朕已阅")

def choujiang_middle_box_contains():
    f = open('middle_box_contains.md', 'r')
    middle_box_contains=f.read()
    #print(f.read())
    middle_box_contains_list=middle_box_contains.split("，")#为方便输入要以中文的逗号分割……,将字符串以中文逗号分割成由多个子字符串组成的列表。
    choujiang=random.randint(0,len(middle_box_contains_list)-1)
    f.close()
    g.msgbox('恭喜您这次开宝箱获得了{'+middle_box_contains_list[choujiang]+'}作为奖励！！！',ok_button="好的，朕已阅")


def choujiang_super_box_contains():
    f = open('super_box_contains.md', 'r')
    super_box_contains=f.read()
    #print(f.read())
    super_box_contains_list=super_box_contains.split("，")#为方便输入要以中文的逗号分割……,将字符串以中文逗号分割成由多个子字符串组成的列表。
    choujiang=random.randint(0,len(super_box_contains_list)-1)
    f.close()
    g.msgbox('恭喜您这次开宝箱获得了{'+super_box_contains_list[choujiang]+'}作为奖励！！！',ok_button="好的，朕已阅")




def open_box():
    read_sum_money_now()#方便显示当前余额
    if float(sum_money_now)>0:
        yourchoice=g.buttonbox(msg='大佬您想开什么宝箱呢？开宝箱可是要花费金币的噢，O(∩_∩)O ，您当前余额为'+str(round(sum_money_now,1))+'个金币！', choices=('初级宝箱：消耗10~20金币', '中级宝箱：消耗20~50金币', '高级宝箱：消耗50~100金币'))
        if yourchoice=='初级宝箱：消耗10~20金币':
            small_box()
            f = open('small_box_contains.md', 'a+')
            f = open('small_box_contains.md', 'r')
            small_box_contains = f.read()
            f.close()
            g.msgbox('初级宝箱里面的奖励现在有\n\n{' + small_box_contains+'}', ok_button="好的，朕已阅")
            choujiang_small_box_contains()
            g.msgbox('您这次消费了：' + str(round(reward, 1)) + '个金币,大佬，您目前的余额还有' + str(round(sum_money_now, 1)) + '个金币',
                     ok_button="好的，朕已阅")
        elif yourchoice== '中级宝箱：消耗20~50金币':
            middle_box()
            f = open('middle_box_contains.md', 'a+')
            f = open('middle_box_contains.md', 'r')
            middle_box_contains = f.read()
            f.close()
            g.msgbox('中级宝箱里面的奖励现在有\n\n{' + middle_box_contains + '}', ok_button="好的，朕已阅")
            choujiang_middle_box_contains()
            g.msgbox('您这次消费了：' + str(round(reward, 1)) + '个金币,大佬，您目前的余额还有' + str(round(sum_money_now, 1)) + '个金币',
                     ok_button="好的，朕已阅")
        elif yourchoice== '高级宝箱：消耗50~100金币':
            super_box()
            f = open('super_box_contains.md', 'a+')
            f = open('super_box_contains.md', 'r')
            super_box_contains = f.read()
            f.close()
            g.msgbox('初级宝箱里面的奖励现在有\n\n{' + super_box_contains + '}', ok_button="好的，朕已阅")
            choujiang_super_box_contains()
            g.msgbox('您这次消费了：' + str(round(reward, 1)) + '个金币,大佬，您目前的余额还有' + str(round(sum_money_now, 1)) + '个金币',
                     ok_button="好的，朕已阅")
        else:
            pass
    else:
        g.msgbox('您当前余额为'+str(round(sum_money_now,1))+',无法再开宝箱，该去做任务攒金币了！', ok_button="好的，朕已阅")
        pass

'''
模块：我想修改宝箱里的奖励
'''

def add_small_box_contains():
    f = open('small_box_contains.md', 'w')
    small_box_contains=g.enterbox(msg='请输入你想往初级宝箱里面放的奖励,每个奖励以中文逗号“，”分隔开。示例输入：苹果一个，香蕉两只，可乐一瓶', title=' ', default='', strip=True, image=None, root=None)
    if small_box_contains==None:
        g.msgbox("您选择了Cancel，相当于重置了该宝箱里的所有奖励！")
    else:
        f.write(small_box_contains)
        f.close()

def add_middle_box_contains():
    f = open('middle_box_contains.md', 'w')
    middle_box_contains=g.enterbox(msg='请输入你想往中级宝箱里面放的奖励,每个奖励以中文逗号“，”分隔开。示例输入：苹果一个，香蕉两只，可乐一瓶', title=' ', default='', strip=True, image=None, root=None)
    if middle_box_contains==None:
        g.msgbox("您选择了Cancel，相当于重置了该宝箱里的所有奖励！")
    else:
        f.write(middle_box_contains)
        f.close()

def add_super_box_contains():
    f = open('super_box_contains.md', 'w')
    super_box_contains=g.enterbox(msg='请输入你想往超级宝箱里面放的奖励,每个奖励以中文逗号“，”分隔开。示例输入：苹果一个，香蕉两只，可乐一瓶', title=' ', default='', strip=True, image=None, root=None)
    if super_box_contains==None:
        g.msgbox("您选择了Cancel，相当于重置了该宝箱里的所有奖励！")
    else:
        f.write(super_box_contains)
        f.close()


def change_box_contains():
    remind=g.buttonbox(msg='您确定要修改宝箱内容吗？这将会重置宝箱内容！？', choices=('我要修改', '算了不修改了'))
    if remind=="我要修改":
        yourchoice=g.buttonbox(msg='那么大佬您想往以下哪种宝箱里重新放置奖励呢？', choices=('初级宝箱', '中级宝箱', '高级宝箱'))
        if yourchoice=='初级宝箱':
            add_small_box_contains()
            f = open('small_box_contains.md', 'r')
            small_box_contains=f.read()
            f.close()
            g.msgbox('您这次修改了{' + yourchoice + '}里的内容！'+'里面的奖励现在是：\n\n'+small_box_contains, ok_button="好的，朕已阅")
        elif yourchoice== '中级宝箱':
            add_middle_box_contains()
            f = open('middle_box_contains.md', 'r')
            middle_box_contains = f.read()
            f.close()
            g.msgbox('您这次修改了{' + yourchoice + '}里的内容！' + '里面的奖励现在是：\n\n' + middle_box_contains, ok_button="好的，朕已阅")
        elif yourchoice== '高级宝箱':
            add_super_box_contains()
            f = open('super_box_contains.md', 'r')
            super_box_contains = f.read()
            f.close()
            g.msgbox('您这次修改了{' + yourchoice + '}里的内容！' + '里面的奖励现在是：\n\n' + super_box_contains, ok_button="好的，朕已阅")
        else:
            pass
    else:
        pass


'''
#模块，我想查询一下当前宝箱里有哪些奖励
'''


def query_box_contains():
    yourchoice = g.buttonbox(msg='那么大佬您想查看哪种宝箱里的奖励？', choices=('初级宝箱', '中级宝箱', '高级宝箱'))
    if yourchoice == '初级宝箱':
        f = open('small_box_contains.md', 'a+')
        f = open('small_box_contains.md', 'r')
        small_box_contains = f.read()
        f.close()
        g.msgbox('里面的奖励现在是：\n\n' + small_box_contains, ok_button="好的，朕已阅")
    elif yourchoice == '中级宝箱':
        f = open('middle_box_contains.md', 'a+')
        f = open('middle_box_contains.md', 'r')
        middle_box_contains = f.read()
        f.close()
        g.msgbox('里面的奖励现在是：\n\n' + middle_box_contains, ok_button="好的，朕已阅")
    elif yourchoice == '高级宝箱':
        f = open('super_box_contains.md', 'a+')
        f = open('super_box_contains.md', 'r')
        super_box_contains = f.read()
        f.close()
        g.msgbox('里面的奖励现在是：\n\n' + super_box_contains, ok_button="好的，朕已阅")
    else:
        pass


'''
称号模块
'''

def honor():
    f = open('start_time.md', 'a+')  # 判断是否有这个文件，没有则创建一个。
    # 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f = open('start_time.md', 'r')
    # 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    if f.read() == '':  # 判断文件是否为空
        f = open('start_time.md', 'a+')
        # 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        start_time = datetime.datetime.now().strftime('%j')
        #print(start_time)
        f.write(start_time)
    else:
        pass
    f = open('start_time.md', 'r')
    start_time = int(f.read())  # 读取文件已经存在的数据
    f.close()
    now_time=int(datetime.datetime.now().strftime('%j'))#%j 十进制表示的每年的第几天
    sum_time=abs(now_time-start_time)+1
    if sum_time<=1:
        g.msgbox('您已累计登录{'+str(sum_time)+'}天，您当前称号为{自律之星}', ok_button="好的，朕已阅")
    elif 2<=sum_time<5:
        g.msgbox('您已累计登录{' + str(sum_time) + '}天，您当前称号为{自律之灵}', ok_button="好的，朕已阅")
    elif 5 <= sum_time < 10:
        g.msgbox('您已累计登录{' + str(sum_time) + '}天，您当前称号为{自律之王}', ok_button="好的，朕已阅")
    elif 10<=sum_time<20:
        g.msgbox('您已累计登录{' + str(sum_time) + '}天，您当前称号为{自律之皇}', ok_button="好的，朕已阅")
    elif 20<=sum_time<30:
        g.msgbox('您已累计登录{' + str(sum_time) + '}天，您当前称号为{自律之尊}', ok_button="好的，朕已阅")
    elif 30<=sum_time<60:
        g.msgbox('您已累计登录{' + str(sum_time) + '}天，您当前称号为{自律之圣}', ok_button="好的，朕已阅")
    elif sum_time>=60:
        g.msgbox('您已累计登录{' + str(sum_time) + '}天，您当前称号为{自律之帝}', ok_button="好的，朕已阅")
'''
模块：游戏简介
'''


def introduce():
    game_introduce = '''
    《宝箱之国》游戏简介
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    这起初是写给自己用的一个小工具，或者说一个小游戏，现在在这里分享出来。
    希望它能让大家的日常学习生活、工作生活多一些游戏色彩，变得更有趣一些。

    一、称号解释（借鉴了小说《斗破苍穹》）
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    累积登录天数=1,获得称号“自律之星”；
    累积登录天数>2,获得称号“自律之灵”；
    累积登录天数>5,获得称号“自律之王”；
    累积登录天数>10,获得称号“自律之皇”；
    累积登录天数>20,获得称号“自律之尊”；
    累积登录天数>30,获得称号“自律之圣”；
    累积登录天数>60,获得称号“自律之帝”；

    二、任务难度分级
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    现实里玩家完成了相应的任务，可以选择完成任务领取金币，金币可以用来开宝箱。
    不同难度的任务奖励金币的数量是不一样的，而且同一难度的任务每次提交时，奖励也是在相应范围内随机波动的。
    奖励给玩家的金币会保存到本地，不会随着程序关闭而清零；

    初级任务：应当是难度不大，并且能在一小时之内完成的任务。
    中级任务：应当是具有挑战性，并且能在1小时~2天之内完成的任务。
    高级任务：应当是非常具有挑战性，并且花费时间在2天以上的任务。

    示例情景一：小明花了半小时修改好了一个Bug，他熟悉任务难度分级，明白这是初级任务。
    于是他就点击按钮“我想完成任务领取金币”，去领取了初级任务的金币奖励；

    示例情景二：小明花了一周终于做完了一个小项目，这妥妥地属于高级任务了。
    于是他提交了高级任务，领取到了一大笔丰厚的金币奖励。
    然后去开了一个高级宝箱，非常幸运地得到了自己想要的奖励。

    三、宝箱奖励完全自定义
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    注意事项1;三种宝箱里的奖励初始为空，需要玩家自己去选择按钮"我想修改宝箱里的奖励"，然后自行添加；
    每次添加都是将宝箱里的内容重置，并不是在原有内容上追加，这需要留意；

    注意事项2：还需要留意的是，输入宝箱内容时，每个奖励内容之间需要用中文逗号“，”隔开，否则将被识别为属于同一奖励内容。

    玩家可以根据自己的个人爱好自定义每个宝箱的内容，比如作者自己设置的每个宝箱内容如下：

    初级宝箱：看一集动漫，看一局羽毛球比赛视频，逛半小时煎蛋网，玩半小时手游
    中级宝箱：打一小时台球，打一小时羽毛球，盐花生一袋，苹果两斤，香蕉两斤，苏梨两斤，一小瓶木糖醇
    高级宝箱：新短袖，新运动鞋，一罐蛋白粉，None，None，None

    Tips：
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1.奖励可以任意多个，注意用中文逗号隔开即可；
    2.当奖励内容过多时，建议先在其他地方想清楚，罗列好，然后直接复制到对话框，奖励一经添加，会保存到本地，下次再打开程序不用重新输入奖励；
    3.可调整特定奖励的概率：比如你特别想要打台球，那就多输入几次打台球，这样就能提升抽中它的概率了；
    4.为了寻求刺激，你还可以在内容里设置None的选项，意思是有一定概率得不到任何奖励2333，比如上文中我设置的高级宝箱里的内容就是如此；
    5.建议设置的奖励应该是自己非常想要的，符合底层本能，符合自己当前经济实力，能够靠自己立刻得到的东西，比如以下这些奖励就有些不靠谱：

    #奖励自己做50个俯卧撑；
    #奖励自己1千万现金；
    #奖励自己多刷一套试卷；

    补充：
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1.双击exe文件后，等待时间有些长，大概要过上15s才会出现交互界面；

    联系方式：
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    作者：大野
    Wechat：why277855
    博客：www.iohaoyu.com

    '''
    g.textbox(msg='《宝箱之国》游戏简介', title='点击右侧OK，进入下一步 ', text=game_introduce, codebox=False)

'''
首页
'''

#g.msgbox("嗨，欢迎来到宝箱之国")
g.buttonbox('~欢迎来到宝箱之国~', image='cat2.png', choices=('哇'))
while 1:
    choice = g.buttonbox(msg='请问这位客官有何贵干？', title="宝箱之国",image='cat.png', choices=("余额称号查询以及游戏简介", "我想完成任务领取金币", "我想消费金币开宝箱", "我想查看宝箱里的奖励","我想修改宝箱里的奖励","退出"))
    if choice=="余额称号查询以及游戏简介":
        read_sum_money_now()
        g.msgbox('大佬，您目前的余额还有{' + str(round(sum_money_now, 1)) + '}个金币', ok_button="好的，朕已阅")
        honor()
        introduce()
    elif choice=="我想完成任务领取金币":
        complete_task()
    elif choice=="我想消费金币开宝箱":
        open_box()
    elif choice=="我想查看宝箱里的奖励":
        query_box_contains()
    elif choice=="我想修改宝箱里的奖励":
        change_box_contains()
    elif choice == "退出":
        break
    else:
        break

