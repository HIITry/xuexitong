#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: vhow  python3
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 输入学号
student_id = input("学号:")
# 输入密码
password = input("密码:")
chrome_options = Options()
chrome_options.add_argument('headless')
# 打开chrome浏览器
# 开启静默模式
driver = webdriver.Chrome(options=chrome_options)
print("starting..")
# get请求网址
driver.get('http://hdu.fanya.chaoxing.com/portal')
# 浏览器最大化 一定需要，否则会影响后面元素定位
driver.maximize_window()
# 设置浏览器大小
driver.set_window_size(1200, 700)

log_button = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/a')
log_button.click()

student_num = driver.find_element_by_xpath('//*[@id="un"]')
student_num.send_keys(student_id)
student_pwd = driver.find_element_by_xpath('//*[@id="pd"]')
student_pwd.send_keys(password)

# 显示等待 最多等待20s（max） 0.5s（频率）找到继续下一步  否则报出异常 nosuchelementexception
locator_1 =(By.XPATH, '//*[@id="index_login_btn"]')
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
driver.find_element_by_xpath("//*[@id='zne_kc_icon']").click()

# 定位到iframe
iframe = driver.find_element_by_id("frame_content")
# 切换到iframe
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//a[contains(@href,'214798432')]").click()

handles = driver.window_handles
driver.switch_to.window(handles[-1])

for i in range(100):  # 可自己设置循环次数
    print("第{}次运行".format(i+1))
    first_chapter = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[3]/div[1]/div[1]/h3/span[3]/a')
    first_chapter.click()
    # time.sleep(1)
    driver.back()
    time.sleep(15)  # x秒后再进行一次点击章节

time.sleep(2)
# 关闭并释放资源
driver.quit()
