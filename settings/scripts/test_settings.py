import pytest
import os,sys
sys.path.append(os.getcwd())
import page
from base.init_driver import init_driver
from base.read_yaml import read_yaml_data
from page.settings_page import SettingsPage



#读取yaml数据
def read_data():
    data = read_yaml_data('settings.yaml')
    return data.get("send_data")



class TestSettings:

    #初始化浏览器
    def setup_class(self):
        self.driver = init_driver(page.sms_app_package,page.sms_app_activity)
        self.settingspage = SettingsPage(self.driver)
    #退出浏览器
    def teardown_class(self):
        self.driver.quit()
    #业务操作
    # 点击搜索按钮
    def test_search_btn(self):
        self.settingspage.click_search()
    #点击定位输入框输入内容
    def test_input_search(self):
        self.settingspage.search_input_send()

    #输入内容
    @pytest.mark.parametrize('content',read_data())
    def test_input(self,content):
        self.settingspage.input_content(content)

    #点击返回
    def test_click_back_btn(self):
        self.settingspage.click_back_btn()
