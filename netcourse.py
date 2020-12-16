#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: vhow  python3
'''
注意！！！
本代码在chrome浏览器上自动测试
运行此代码需要selenium库和chromedriver
chromedriver版本为chrome的版本
本代码用的版本是 87.0.4280.88
通过下面的链接下载和你chrome版本相同的driver并放置于python.exe所在同级文件夹下
http://npm.taobao.org/mirrors/chromedriver/
代码跑起来后可最小化后台运行，或者开启静默模式不显示浏览器
'''
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
# import getpass  # 暂时没使用 用于隐式输入密码
# username =input('uarname:')
# password =getpass.getpass('password:')
# from selenium.webdriver.chrome.options import Options
#
# chrome_options=Options()
# chrome_options.add_argument('headless')
# # 开启静默模式
# browser = webdriver.Chrome(options=chrome_options)
# browser.get()

# 输入学号
student_id = input("学号:")
# 输入密码
password = input("密码:")  # 密码可以隐式输入，这里由于是在IDE中调试，用不了隐式输入getpass
# 如果觉得输入密码学号麻烦，可更改代码student_num.send_keys(student_num) student_pwd.send_keys(password) 固定密码学号
# 打开chrome浏览器
driver = webdriver.Chrome()
# get请求网址
driver.get('http://hdu.fanya.chaoxing.com/portal')
# 浏览器最大化 一定需要，否则会影响后面元素定位
driver.maximize_window()
# 设置浏览器大小
driver.set_window_size(1200, 700)

log_button = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/a')
log_button.click()

locat = (By.XPATH, '//*[@id="un"]')
WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located(locat))
student_num = driver.find_element_by_xpath('//*[@id="un"]')
student_num.send_keys(student_id)
student_pwd = driver.find_element_by_xpath('//*[@id="pd"]')
student_pwd.send_keys(password)

# 显示等待 最多等待20s（max） 0.5s（频率）找到继续下一步  否则报出异常 nosuchelementexception
# WebDriverWait(driver, 20, 0.5).until(lambda el: driver.find_element_by_xpath('//*[@id="index_login_btn"]'))
locator_1 = (By.XPATH, '//*[@id="index_login_btn"]')
WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located(locator_1))
log_button2 = driver.find_element_by_xpath('//*[@id="index_login_btn"]')
log_button2.click()
# 显示等待写法
locator = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/a')
WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located(locator))
study_space_button = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/a')
study_space_button.click()

# 当前句柄
currentWin = driver.current_window_handle
# 切换到最新打开的标签页
handles = driver.window_handles
driver.switch_to.window(handles[-1])

locator2 = (By.XPATH, "//*[@id='zne_kc_icon']")
WebDriverWait(driver, 20, 0.5).until(ec.presence_of_element_located(locator2))
driver.find_element_by_xpath("//*[@id='zne_kc_icon']").click()
# 定位到iframe
iframe = driver.find_element_by_id("frame_content")
# 切换到iframe
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//a[contains(@href,'200162231')]").click()

handles = driver.window_handles
driver.switch_to.window(handles[-1])

for i in range(600):  # 可自己设置循环次数
    print("第{}次运行".format(i+1))
    first_ep = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[3]/div[1]/div/h3/span[3]/a')
    first_ep.click()
    # time.sleep(5)  # 章节里面停留时间 (这里可以不用停留,应该是总的时间和大于一个数值即可+1）
    driver.back()
    time.sleep(15)  # x秒后再进行一次点击章节

time.sleep(2)
# 关闭并释放资源
driver.quit()  # 关闭所有释放chromedriver资源


# 一些常用功能
# # 刷新
# driver.refresh()
# # 返回
# driver.back()
# # 前进
# driver.forward()
# # 截图
# driver.get_screenshot_as_file('C:\\Users\\12559\\Desktop\\shot.jpg')
# # 获得当前url
# print(driver.current_url)
# # 获取页面源码
# print(driver.page_source)
# # 获取标题
# print(driver.title)
# driver.close() 关闭当前
