from selenium import webdriver
# 拿到driver
driver = webdriver.Firefox()
# 打开网页
driver.get("http://www.baidu.com")
# 获取网页的title
print(driver.title)
# 获取网页当前的地址
print(driver.current_url)
# 选中输入框，输入内容点击百度一下按钮
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()