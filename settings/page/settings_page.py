import os,sys
sys.path.append(os.getcwd())
import page
from base.base_action import BaseAction


class SettingsPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)


    #业务
    #点击搜索按钮
    def click_search(self):
        self.click_element(page.settings_search_btn)
    #定位到搜索输入框
    def search_input_send(self):
        self.click_element(page.settings_search_input)
    #输入
    def input_content(self,content):
        self.input_edit_content(page.settings_search_input,content)
     #点击返回按钮
    def click_back_btn(self):
        self.click_element(page.settings_btn_back)