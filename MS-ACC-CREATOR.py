import ctypes
import warnings
from selenium import webdriver
from requests.exceptions import ProxyError
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import os, json, string, random
from selenium.common.exceptions import NoSuchElementException

def randomString(length=16):
    base_Str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''
    for i in range(length):
        random_str += base_Str[random.randint(0, (len(base_Str) - 1))]
    return random_str


# 前置操作
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = False
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_argument('--inprivate')
edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
driver = webdriver.Edge('S:\Programs\AutoXGP\msedgedriver.exe', options=edge_options)
wait = WebDriverWait(driver, 30)

os.system("cls || clear")
print("微软账户注册工具 - Kawakaze || 白洲アズサ")


# 创建Edge浏览器对象
print("这是一个自动创建MS账号的小程序 使用selenium执行 请确认相关依赖和msedgedriver.exe已经正确设置")
print("作者:白洲アズサ || Kawakaze")
print("𝓔𝓽 𝓸𝓷𝓶𝓲𝓪 𝓥𝓪𝓷𝓲𝓽𝓪𝓼")
print("更新地址:https://github.com/XokoukioX/AutoMSACC")
amount = 1
while True:
    try:
        amount = int(input("你想要创建多少个账号？\n> "))
        if amount > 0: break
        print("请检查你的输入")
    except ValueError:
        print("请检查你的输入")
        pass


for x in range(amount):
    email = randomString(10)
    for y in range(5):
        b = random.randint(0, 3)
    if b == 0:
        password = randomString(8)
    elif b == 1:
        password = randomString(5) + "!" + randomString(1)
    else:
        password = randomString(3) + "A" + randomString(2) + "!" + randomString(1)
    driver.get("https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1605407946&rver=7.0.6738.0&wp=MBI_SSL&wreply=https:%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin%3Fru%3Dhttps%253A%252F%252Faccount.microsoft.com%252F%253Frefp%253Dsignedout-index&lc=1033&id=292666&lw=1&fl=easi2&mkt=en-CN")
    time.sleep(2)
    try:
        driver.find_element(By.XPATH,'//*[@id="iSignupAction"]').click()
    except NoSuchElementException:
        pass
    driver.find_element(By.XPATH,'//*[@id="MemberName"]').send_keys('a' + email + '@outlook.com')
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="iSignupAction"]').click()
    WebDriverWait(driver,200).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="PasswordInput"]'))).click()
    driver.find_element(By.XPATH,'//*[@id="PasswordInput"]').send_keys('b' + password)
    driver.find_element(By.XPATH,'//*[@id="iSignupAction"]').click()
    WebDriverWait(driver,200).until((EC.visibility_of_element_located((By.ID,"Country")))).click()
    Select(driver.find_element(By.ID, "Country")).select_by_value("US")
    Select(driver.find_element(By.ID, "BirthMonth")).select_by_value("1")
    Select(driver.find_element(By.ID, "BirthDay")).select_by_value("1")
    driver.find_element(By.ID, "BirthYear").send_keys("1984")
    driver.find_element(By.ID, "iSignupAction").click()
    WebDriverWait(driver,20000).until(EC.visibility_of_element_located((By.ID,"enforcementFrame"))).click()
    print("请通过人机验证")
    WebDriverWait(driver,2000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="id__0"]'))).click()
    try:
        driver.find_element(By.XPATH, '//*[@id="id__0"]').click()
    except NoSuchElementException:
        pass
    WebDriverWait(driver,2000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="idSIButton9"]'))).click()
    print("Your Account is: " + 'a' + email + '@outlook.com')
    print("Your password is: " + 'b' + password)
    email=str(email)
    with open("accounts.txt", "a") as f:
        f.write(f"{'a' + email + '@outlook.com'}----{'b' + password}\n")
