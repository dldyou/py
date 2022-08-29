from ursina import *
import os

app = Ursina()

# window.borderless = False
gold = 0
clickG = 1
autoG = 0
cost_ = []
earn_ = []
cost_.append(10)
cost_.append(100)
cost_.append(1000)
cost_.append(10000)
cost_.append(100000)
earn_.append(1)
earn_.append(5)
earn_.append(50)
earn_.append(200)
earn_.append(1000)
costClick = 20



if not os.path.isfile(os.path.abspath('./savefile.txt')):
    f = open(os.path.abspath('./savefile.txt'), 'w')
    f.write('0\n')
    f.write('0\n')
    f.write('10\n')
    f.write('1\n')
    f.write('100\n')
    f.write('5\n')
    f.write('1000\n')
    f.write('50\n')
    f.write('10000\n')
    f.write('200\n')
    f.write('100000\n')
    f.write('1000\n')
    f.write('1\n')
    f.write('20\n')
    f.close()
else:
    f = open(os.path.abspath('./savefile.txt'), 'r')
    gold = int(f.readline())
    autoG = int(f.readline())
    for i in range(5):
        cost_[i] = int(f.readline())
        earn_[i] = int(f.readline())
    clickG = int(f.readline())
    costClick = int(f.readline())
    f.close()

# Text.default_font='D:\\다운로드\\글씨체 - ttf\\BMJUA_ttf'

text_gold = Text(text=f'{gold}G', x=-0.02, y=0.3, scale=2, background=False)
text_earn_gold = Text(text=f'{autoG}G/s', x=-0.04, y=-0.3, scale=2, background=False)


click = Button(text=f'G + {clickG}', x=-0.75, color=color.orange, scale=0.2)
clickUp = Button(text=f'+ {round(clickG * 1.05 + 1) - clickG}G (UP {costClick})', x = -0.75, y=-0.3, color=color.gray, scale=0.2, disabled=True, cost=costClick)
auto1 = Button(text=f'1G/s (UP {cost_[0]}G)', x=-0.45, color=color.gray, scale=0.2, disabled=True, cost=cost_[0], earn=earn_[0])
auto2 = Button(text=f'5G/s (UP {cost_[1]}G)', x=-0.15, color=color.gray, scale=0.2, disabled=True, cost=cost_[1], earn=earn_[1])
auto3 = Button(text=f'50G/s (UP {cost_[2]}G)', x=0.15, color=color.gray, scale=0.2, disabled=True, cost=cost_[2], earn=earn_[2])
auto4 = Button(text=f'200G/s (UP {cost_[3]}G)', x=0.45, color=color.gray, scale=0.2, disabled=True, cost=cost_[3], earn=earn_[3])
auto5 = Button(text=f'1000G/s (UP {cost_[4]}G)', x=0.75, color=color.gray, scale=0.2, disabled=True, cost=cost_[4], earn=earn_[4])

save = Button(text='SAVE', x=0.75, y=-0.3, color=color.black, scale=0.2)

def plus_autoG(interval=1):
    global gold, autoG
    gold += autoG

    invoke(plus_autoG, delay=interval)

def btn_click():
    global gold, clickG
    gold += clickG

def btn_clickUp():
    global gold , clickG
    if gold >= clickUp.cost:
        gold -= clickUp.cost
    clickG = round(clickG * 1.05 + 1)
    clickUp.cost = round(clickUp.cost * 1.1)
    clickUp.text = f'+ {round(clickG * 1.05 + 1) - clickG}G (UP {clickUp.cost})'
    click.text = f'G + {clickG}'
clickUp.on_click = btn_clickUp

def autoG1():
    global gold, autoG
    if gold >= auto1.cost:
        gold -= auto1.cost
    autoG += auto1.earn
    auto1.cost = round(auto1.cost * 1.1)
    auto1.text = f'{auto1.earn}G/s (UP {auto1.cost}G)'
auto1.on_click = autoG1

def autoG2():
    global gold, autoG
    if gold >= auto2.cost:
        gold -= auto2.cost
    autoG += auto2.earn
    auto2.cost = round(auto2.cost * 1.1)
    auto2.text = f'{auto2.earn}G/s (UP {auto2.cost}G)'
auto2.on_click = autoG2

def autoG3():
    global gold, autoG
    if gold >= auto3.cost:
        gold -= auto3.cost
    autoG += auto3.earn
    auto3.cost = round(auto3.cost * 1.1)
    auto3.text = f'{auto3.earn}G/s (UP {auto3.cost}G)'
auto3.on_click = autoG3

def autoG4():
    global gold, autoG
    if gold >= auto4.cost:
        gold -= auto4.cost
    autoG += auto4.earn
    auto4.cost = round(auto4.cost * 1.1)
    auto4.text = f'{auto4.earn}G/s (UP {auto4.cost}G)'
auto4.on_click = autoG4

def autoG5():
    global gold, autoG
    if gold >= auto5.cost:
        gold -= auto5.cost
    autoG += auto5.earn
    auto5.cost = round(auto5.cost * 1.1)
    auto5.text = f'{auto5.earn}G/s (UP {auto5.cost}G)'
auto5.on_click = autoG5

def save_():
    global gold, autoG
    f = open(os.path.abspath('./savefile.txt'), 'w')
    f.write(f'{gold}\n')
    f.write(f'{autoG}\n')
    f.write(f'{auto1.cost}\n')
    f.write(f'{auto1.earn}\n')
    f.write(f'{auto2.cost}\n')
    f.write(f'{auto2.earn}\n')
    f.write(f'{auto3.cost}\n')
    f.write(f'{auto3.earn}\n')
    f.write(f'{auto4.cost}\n')
    f.write(f'{auto4.earn}\n')
    f.write(f'{auto5.cost}\n')
    f.write(f'{auto5.earn}\n')
    f.write(f'{clickG}\n')
    f.write(f'{clickUp.cost}\n')
    f.close()
save.on_click = save_
click.on_click = btn_click
plus_autoG(interval=1)

def update():
    global gold
    text_gold.text = f'{gold}G'
    text_earn_gold.text = f'{autoG}G/s'

    if gold >= auto1.cost:
        auto1.disabled = False
        auto1.color = color.green
    else:
        auto1.disabled = True
        auto1.color = color.gray
    if gold >= auto2.cost:
        auto2.disabled = False
        auto2.color = color.green
    else:
        auto2.disabled = True
        auto2.color = color.gray
    if gold >= auto3.cost:
        auto3.disabled = False
        auto3.color = color.green
    else:
        auto3.disabled = True
        auto3.color = color.gray
    if gold >= auto4.cost:
        auto4.disabled = False
        auto4.color = color.green
    else:
        auto4.disabled = True
        auto4.color = color.gray
    if gold >= auto5.cost:
        auto5.disabled = False
        auto5.color = color.green
    else:
        auto5.disabled = True
        auto5.color = color.gray
    if gold >= clickUp.cost:
        clickUp.disabled = False
        clickUp.color = color.green
    else:
        clickUp.disabled = True
        clickUp.color = color.gray
app.run()
