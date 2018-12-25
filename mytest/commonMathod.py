# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.select import Select


class CreateDriver():
    def __init__(self,brower): #初始化浏览器
        if brower == 'Firefox' or brower == 'firefox' :
            driver = webdriver.Firefox()
        elif brower == 'Chrome' or brower =='chrome' :
            driver = webdriver.Chrome()
        elif brower == 'IE' or brower == 'ie' :
            driver = webdriver.Ie()
        elif brower == 'Opera' or brower == 'opera' :
            driver = webdriver.Opera()
        elif brower == 'Safari' or brower == 'safari' :
            driver = webdriver.Safari()
        else :
            raise NameError('只支持Firefox、chrome、ie、opera、safari浏览器')
        self.driver = driver

    def make_maxwindow(self):  # 最大化浏览器
        self.driver.maximize_window()

    def make_sizewindow(self,width,height): #设置浏览器窗口宽、高
        self.set_window_size(width,height)


    def element(self,way,value):  #定位元素
        if way == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif way == 'id':
            element = self.driver.find_element_by_id(value)
        elif way == 'name':
            element = self.driver.find_element_by_name(value)
        elif way == 'class_name':
            element = self.driver.find_element_by_class_name(value)
        elif way == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif way == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif way == 'tag':
            element = self.driver.find_element_by_tag_name(value)
        elif way == 'pa_link_text':
            element = self.driver.find_elements_by_partial_link_text(value)
        else:
            raise NameError("Please enter element local_way,like xpath/id/name/class_name/css/link_text/tag/pa_link_text")
        return element

    def elements(self,way,value):  #定位元素组
        if way == 'xpath':
            elements = self.driver.find_elements_by_xpath(value)
        elif way == 'id':
            elements = self.driver.find_elements_by_id(value)
        elif way == 'name':
            elements = self.driver.find_elements_by_name(value)
        elif way == 'class_name':
            elements = self.driver.find_elements_by_class_name(value)
        elif way == 'css':
            elements = self.driver.find_elements_by_css_selector(value)
        elif way == 'link_text':
            elements = self.driver.find_elements_by_link_text(value)
        elif way == 'tag':
            elements = self.driver.find_elements_by_tag_name(value)
        elif way == 'pa_link_text':
            elements = self.driver.find_elements_by_partial_link_text(value)
        else:
            raise NameError("Please enter element local_way,like xpath/id/name/class_name/css/link_text/tag/pa_link_text")
        return elements

    def element_wait(self,way,value,wait=5): #显式等待
        if way == 'xpath':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif way == 'id':
            WebDriverWait(self.driver,wait,1).until(EC.presence_of_element_located((By.ID,value)))
        elif way == 'name':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif way == 'class_name':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif way == 'css':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif way == 'link_text':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif way == 'tag':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.TAG_NAME, value)))
        elif way == 'pa_link_text':
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        else:
            raise NameError("Please enter element local_way,like xpath/id/name/class_name/css/link_text/tag/pa_link_text")

    def implicitly_wait(self,wait_time): #隐性等待
        self.driver.implicitly_wait(wait_time)

    def sleep(self,sleep_time): #休眠
        sleep(sleep_time)



    def click(self,way,value): #点击事件
        self.element_wait(way,value)
        el = self.element(way,value)
        el.click()


    def clear(self,way,value): #清除事件
        self.element_wait(way,value)
        el = self.element(way,value)
        el.clear()


    def send_keys(self,way,value,str): #键盘输入
        el = self.element(way,value)
        el.clear()
        el.send_keys(str)

    def open(self,url):
        self.driver.get(url)

    def forward(self): #前进
        self.driver.forward()

    def back(self): #后退
        self.driver.back()

    def right_click(self,way,value): #鼠标右击
        self.element_wait(way,value)
        el = self.element(way,value)
        ActionChains(self.driver).context_click(el).perform()

    def double_click(self,way,value): #鼠标双击
        self.element_wait(way,value)
        el = self.element(way,value)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self,sway,svalue,tway,tvalue):
        el_s = self.element(sway,svalue)
        el_t = self.element(tway,tvalue)
        ActionChains(self.driver).drag_and_drop(el_s,el_t)

    def move_to_element(self,way,value):
        self.element_wait(way,value)
        el = self.element(way,value)
        ActionChains(self.driver).move_to_element(el)

    def switch_to_frame(self,way,value): #表单切换
        toframe = self.element(way,value)
        self.driver.switch_to.frame(toframe)

    def switch_to_window(self,handle): #窗口切换
        self.driver.switch_to.window(handle)

    def f5(self): #刷新
        self.driver.refresh()

    def quit(self): #退出
        self.driver.quit()

    def close(self): #关闭
        self.driver.close()

    def js(self,script,way,value): #执行js
        if way == '' and value == '':
            self.driver.execute_script(script)
        elif way != '':
            el = self.element(way,value)
            self.driver.execute_script(script,el)
        else:
            raise NameError("Error")

    def get_arribute(self,way,value,arribute): #获取元素属性
        self.element_wait(way,value)
        el = self.element(way,value)
        return el.get_attribute(arribute)

    def get_text(self,way,value): #获取元素文本信息
        self.element_wait(way,value)
        el = self.element(way,value)
        return el.text

    def is_display(self,way,value): #元素是否显式
        self.element_wait(way,value)
        el = self.element(way,value)
        return el.is_displayed()

    def get_title(self):
        return self.driver.title

    def get_screen(self,file_path): #截屏保存到file_path路径下
        return self.driver.get_screenshot_as_file(file_path)

    def get_img(self):  #   截屏已base64方式保存
        return  self.driver.get_screenshot_as_base64()

    def add_img(self,file_path):
        return  self.driver.get_screenshot_as_base64() # 获取当前窗口的截图保存为一个base64编码的字符串。

    def accept(self): #提醒中的同意/允许/确认
        self.driver.switch_to.alert.accept()

    def dismiss(self): #提醒中的取消
        self.driver.switch_to.alert.dismiss()

    def submit(self,way,value): #提交
        self.element_wait(way,value)
        el = self.element(way,value)
        el.submit()

    def select(self,way,value,sel_way,sel_value):
        self.element_wait(way,value)
        el = self.element(way,value)
        if sel_way == 'index':
            Select(el).select_by_index(sel_value)
        elif sel_way == 'value':
            Select(el).select_by_value(sel_value)
        elif sel_way == 'text':
            Select(el).select_by_visible_text(sel_value)
        else:
            raise NameError("please enter arg_way,such as:index/value/text")











