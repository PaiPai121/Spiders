from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import json
import pyautogui
def wait_ran(time,driver):
    wait = WebDriverWait(driver, time + randint(1,1000)/800)
    return wait

def wait_by_time(t,randrange = 1000):
    time.sleep( t + randint(1,1000)/800)

def login():
    # 保存Cookie的文件路径
    cookie_file_path = "./cookies.json"
    if False and os.path.exists(cookie_file_path):
        with open(cookie_file_path, "r") as file:
            cookies = json.load(file)
        driver = webdriver.Chrome()
        for cookie in cookies:
            driver.add_cookie(cookie)
        # driver.get(login_url)
        # 如果需要，继续执行其他操作
        return
    # 创建一个WebDriver实例
    driver = webdriver.Chrome()
    base_url = "https://newetds.lib.tsinghua.edu.cn/qh/index"
    # 打开一个网页
    driver.get(base_url)
    # 在浏览器中执行其他操作...
    wait = wait_ran(10,driver) # WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="loginBtn cd-popup-trigger0"]')))
    # 点击元素
    element.click() # 点击登录键
    # oaauth
    # 等待元素加载（如果需要）
    wait = wait_ran(10,driver) #WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.img_Tsinghua img')))
    # 点击元素
    element.click()
    ## 此时切换入登录界面，输入账号密码
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains('login'))  # 等待页面，直到url包含login
    account = "zhangzk19"
    password = "niuniu1234"
    user_input = driver.find_element(By.ID, 'i_user')
    user_input.send_keys(account)
    wait_by_time(1)
    pass_input = driver.find_element(By.ID, 'i_pass')
    pass_input.send_keys(password)
    wait_by_time(1)
    # 点击登录
    # 定位登录按钮并点击
    login_button = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-lg.btn-primary.btn-block')
    login_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains('newetds'))  # 等待页面，直到url包含login
    
    # 保存登录后的Cookie
    cookies = driver.get_cookies()
    # 将Cookie保存到本地文件
    with open(cookie_file_path, "w") as file:
        json.dump(cookies, file)
    return driver

def search_paper(driver,paper_title= "我国人口转型特征及其对我国宏观经济运行的影响"):
    # 开始搜索
    driver.get("https://newetds.lib.tsinghua.edu.cn/qh/index")
    # 定位输入框并写入字符串
    search_string = paper_title  # 替换为你要写入输入框的字符串
    search_box = driver.find_element(By.ID, 'txtKeyword')
    search_box.send_keys(search_string)
    # 定位搜索图标并点击
    search_icon = driver.find_element(By.CSS_SELECTOR, 'i.iconfont.icon-icon.fl')
    search_icon.click()

    # 切换到新弹出的标签页
    main_window = driver.current_window_handle
    windows = driver.window_handles
    for window in windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    # 等待元素出现，设置一个合理的等待时间，比如10秒
    wait = wait_ran(10,driver)#WebDriverWait(driver, 10)

    # 使用XPath查找包含s1文本的a元素，并确保它是可点击的
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., '%s')]" % paper_title)))
    element.click()

    # 此时来到页面
    # 获取所有打开的窗口的句柄
    window_handles = driver.window_handles

    # 切换到新打开的标签页
    driver.switch_to.window(window_handles[-1])

    # 等待元素出现，设置一个合理的等待时间，比如10秒
    wait = wait_ran(2,driver)#WebDriverWait(driver, 10)

    # 使用class属性查找span元素，并确保它是可点击的
    span_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "o_name")))
    actions = ActionChains(driver)
    # 最大化浏览器窗口
    actions.send_keys(Keys.F11)  # 按下F11键
    actions.perform()

    # 点击该span元素
    span_element.click()

    # 此时打开了目标网页，关闭不必要的标签页
    # window_handles = driver.window_handles
    # for handle in window_handles[:-1]:
    #     driver.switch_to.window(handle)
    #     wait_by_time(0.5)
    #     driver.close()
    #     wait_by_time(0.1)


from pyscreeze import screenshot
import os
def get_screen_shot(driver,title):

    output_path = "./"+title+"/"
    os.makedirs(output_path, exist_ok=True)
    # 获取页面高度
    # page_height = driver.execute_script("return document.body.scrollHeight")
    # 截取屏幕快照
    # for i in range(0, page_height, 1000):  # 每次截取1000像素高度
    i = 0
    last_page = None
    actions = ActionChains(driver)
    screen_shot = screenshot().save(os.path.join(output_path, f"screenshot_{i}.png"))
    pyautogui.click(None, None)
    while i < 1000 :
        # driver.execute_script(f"window.scrollTo(0, {i});")
        # 模拟鼠标滚轮操作，例如向上滚动100个像素
        pyautogui.scroll(-13)
        # pyautogui.scroll(-100)
        screenshot().save(os.path.join(output_path, f"screenshot_{i}.png"))
        screen_shot = screenshot()
        wait_by_time(2.3)
        i += 1
        if screen_shot == last_page:
            break
        last_page = screen_shot
    # # 如果需要取消最大化，可以执行以下代码
    # driver.execute_script("window.unmaximize();")
    window_handles = driver.window_handles
    for handle in window_handles[1:]:
        driver.switch_to.window(handle)
        wait_by_time(0.5)
        driver.close()
        wait_by_time(0.1)




if __name__ == "__main__":
    # driver = login()
    # paper_title = "我国人口转型特征及其对我国宏观经济运行的影响"
    papers = ["中国剩余劳动力转移与全球劳动收入份额下降研究",
              "人口老龄化背景下的居民消费特征分析","中国的技术进步偏向性与要素收入份额",
              "中国劳动力市场性别差异研究基于教育家庭和政策视角","中国人口年龄结构对经济增长和周期波动的影响研究",
              "人口老龄化对国际贸易的影响机制研究：基于质量的分析","我国劳动力供给与劳动力资源配置效率的相关政策分析"]
    def get_paper(driver,paper_title):
        search_paper(driver=driver)
        get_screen_shot(driver,paper_title)
    for paper in papers:
        driver = login()
        try:
            get_paper(driver,paper)
            wait_by_time(2)
        except:
            print(paper)

        # 关闭浏览器
        driver.quit()
