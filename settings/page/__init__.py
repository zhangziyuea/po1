#启动应用的包名和启动名
from selenium.webdriver.common.by import By

sms_app_package = "com.android.settings"
sms_app_activity = ".Settings"

#功能
# 点击搜索按钮
settings_search_btn = By.ID,"com.android.settings:id/search"
#定位搜索输入框
settings_search_input = By.ID,"android:id/search_src_text"
#点击回退按钮
settings_btn_back = By.CLASS_NAME,"android.widget.ImageButton"