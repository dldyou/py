# pip install webdriver-manager
# pip install selenium
# chromedriver 검색, 크롬에서 ... > 도움말 > Chrome 정보 에서 버전확인 후 알맞은 버전으로 다운

from email import message
from optparse import Values
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller as chrome
from selenium.webdriver.common.by import By
from ctypes import sizeof
import time
import os

root = Tk()

title = "Auto Ecampus"
width, height = 300, 95
x, y = round((root.winfo_screenwidth() - width)  / 2), round((root.winfo_screenheight() - height) / 2 - 100)

# 값 불러오기

# 크롬 

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
chrome.install()

# .exe 창 크기 및 위치

root.title(title)
root.geometry("{}x{}+{}+{}".format(width, height, x, y))
root.resizable(0, 0)

# 인터페이스

# 로그인 관련 인터페이스 

LoginEntWidth = 18

labelLogin = Label(root, text = "○ LMS 로그인")
labelLogin.place(x=0, y=0)

labelID = Label(root, text = "ID")
labelID.place(x=0, y=20)
entID = Entry(root, width=LoginEntWidth)
entID.place(x=25, y=20)

labelPW = Label(root, text = "PW")
labelPW.place(x=0, y=40)
entPW = Entry(root, width=LoginEntWidth, show="*")
entPW.place(x=25, y=40)

# 대학 eCampus 주소 관련 인터페이스 

labelCampus = Label(root, text = "대학교")
labelCampus.place(relx=0.7, y=0)

# 리스트

campus = ["건국대", "고려대", "서울대", "연세대", "인하대", "중앙대", "한양대(에리카)"]
campus.sort()
comboboxCampus = Combobox(root, height=5, values=campus, state="readonly", width=15)
comboboxCampus.place(relx=0.55, y=20)
comboboxCampus.current(0)

if os.path.isfile(os.path.abspath('./login.txt')):
    f = open(os.path.abspath('./login.txt'), 'r', encoding='utf-8')
    entID.insert(0, f.readline().rstrip())
    entPW.insert(0, f.readline().rstrip())
    lastCampus = f.readline().rstrip()

    for i in range(len(campus)):
        if(lastCampus == campus[i]):
            comboboxCampus.current(i)
    f.close()

def start():
    f = open(os.path.abspath('./login.txt'), 'w', encoding='utf-8')
    f.write(entID.get()+'\n')
    f.write(entPW.get()+'\n')
    f.write(comboboxCampus.get()+'\n')
    f.close()

    campusName = comboboxCampus.get()

    if(campusName == "건국대"):
        Konkuk()
    elif(campusName == "고려대"):
        Korea()
    elif(campusName == "서울대"):
        Seoul()
    elif(campusName == "연세대"):
        Yonsei()
    elif(campusName == "인하대"):
        Inha()
    elif(campusName == "중앙대"):
        Chungang()
    elif(campusName == "한양대(에리카)"):
        Hanyang_ERICA()

def Konkuk():
    driver = webdriver.Chrome(options=options)
    url1 = "https://ecampus.konkuk.ac.kr/ilos/main/member/login_form.acl"
    tabs = driver.window_handles
    driver.switch_to_window(tabs[0])
    driver.get(url1)
    actoin = ActionChains(driver)
    driver.implicitly_wait(10)
    print("웹 실행 중...")
    driver.set_window_size(1400, 600)
    driver.set_window_position(0, 0)
    print("창 크기 및 위치 조절...")
    driver.implicitly_wait(10)
    driver.find_element_by_id("usr_id").send_keys(entID.get())
    print("아이디 입력")
    driver.implicitly_wait(10)
    driver.find_element_by_id("usr_pwd").send_keys(entPW.get())
    print("비밀번호 입력")
    driver.implicitly_wait(10)
    driver.find_element_by_id("login_btn").click()
    print("로그인 중...")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//div[@title="Todo List"]').click()
    print("ToDo List 열기")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//div[@data="lecture_weeks"]').click()
    print("온라인 강의 확인...")
    driver.implicitly_wait(10)
    while True:
        lecture_cnt = driver.find_element_by_class_name("cate_cnt").text
        driver.implicitly_wait(10)
        if lecture_cnt == '0':
            print(lecture_cnt)
            print("남은 강의가 없습니다")
            break;
        driver.find_elements_by_xpath('//div[@class="todo_list"]/div[@class="todo_wrap on"]')[0].click()
        driver.implicitly_wait(10)
        btn = driver.find_elements(By.CSS_SELECTOR, "img[src='/ilos/images/ko/btn_start_learning.gif'")
        f = False
        for video in btn:
            video.click()
            driver.implicitly_wait(10)
            if f == False:
                print("2차 인증 중...")
                driver.find_element_by_xpath('//*[@id="secondary_auth_way_wrap"]/div[1]/div[1]').click()
                driver.implicitly_wait(10)
                driver.find_element_by_xpath('//*[@id="secondary_auth_sub_list_wrap"]/div[1]/div/div[2]/div[1]').click()
                driver.implicitly_wait(10)
                driver.find_element_by_xpath('//*[@id="btnConfirmSecondaryAuth"]').click()
                driver.implicitly_wait(10)
                time.sleep(3)
                f = True
            print(driver.current_url)
            while True:
                pass

def Korea():
    messagebox.showwarning("Not in this version", "아직 서비스를 하지 않고 있습니다!\n다음 버전을 기다려주세요.")
def Seoul():
    messagebox.showwarning("Not in this version", "아직 서비스를 하지 않고 있습니다!\n다음 버전을 기다려주세요.")
def Yonsei():
    messagebox.showwarning("Not in this version", "아직 서비스를 하지 않고 있습니다!\n다음 버전을 기다려주세요.")
def Inha():
    messagebox.showwarning("Not in this version", "아직 서비스를 하지 않고 있습니다!\n다음 버전을 기다려주세요.")
def Chungang():
    messagebox.showwarning("Not in this version", "아직 서비스를 하지 않고 있습니다!\n다음 버전을 기다려주세요.")
def Hanyang_ERICA():
    messagebox.showwarning("Not in this version", "아직 서비스를 하지 않고 있습니다!\n다음 버전을 기다려주세요.")
# 버튼 

buttonStart = Button(root, width=40, text="시작하기", command=start)
buttonStart.place(x=7, y=65)

# main

root.mainloop()


