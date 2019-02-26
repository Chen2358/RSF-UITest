# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep,ctime

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
'''
#一 控制浏览器操作
# （1）控制浏览器前进后退
first_url = 'https://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)
sleep(10)

# （2）设置浏览器大小，参数数字为像素点
driver.set_window_size(480, 800)
# 最大化
driver.maximize_window()

second_url = 'http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)
sleep(10)

# （3）返回
print("back to %s" %(first_url))
driver.back()
sleep(10)

# （4）前进
print("forward to %s" %(second_url))
driver.forward()
sleep(10)

# （5）刷新
driver.refresh()
sleep(10)

#二 常用方法
# （1）点击,输入,提交
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
driver.find_element_by_id("su").submit()
sleep(10)

# （2）其他方法
#获得元素尺寸
size = driver.find_element_by_id("kw").size
print(size)
#返回文本
text = driver.find_element_by_id("cp").text
print(text)
#返回元素属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)
#放回元素的结果是否可见
result = driver.find_element_by_id("kw").is_displayed()

# 三 鼠标事件
# 需引入ActionChains模块
# perform():执行所有ActionChains中存储的行为；
# context_click():右击
# double_click():双击
# drag_and_drop():拖动
# move_to_element()：鼠标悬停

#鼠标悬停
above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()
sleep(3)

# 四 键盘事件
# 需引入Keys模块
driver.find_element_by_id("kw").send_keys("seleniumm")
sleep(3)
# Backspace
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(3)
#space
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
sleep(3)
driver.find_element_by_id("kw").send_keys("aaa")
sleep(3)
# ctrl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
sleep(3)
# ctrl+x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
sleep(3)
# ctrl+v
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
sleep(3)
driver.find_element_by_id("su").send_keys(Keys.ENTER)
sleep(3)

# 五 获取断言信息
#title,current_url,text
print("Before search=======")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)

print("After search========")

title = driver.title
print(title)

now_url = driver.current_url
print(now_url)

nums = driver.find_element_by_class_name('nums').text
print(nums)

# 六 设置元素等待
# (1)显示等待：等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
# WebDriverWait类：是web Driver提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常；一般与until()或until_not()配合使用。
# 格式：WebDriverWait(driver, timeout, poll_frequency=0.5, ignore_exceptions=None)
# 浏览器驱动；最长超时时间，默认单位秒；检测的间隔（步长）时间，默认0.5s；超时后的异常信息，默认抛出NoSuchElementException异常
element = WebDriverWait(driver, 5, 0.5).until(
	EC.presence_of_element_located((By.ID, "kw"))
	)
element.send_keys('selenium')

# (2)隐式等待:implicitly_wait()，默认设置为0
# 1>设置的时间不是一个固定时间，并不影响脚本的执行速度；
# 2>并不针对页面商的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；如果元素定位不到，则将以轮询的方式不断地判断元素是否被定位到。若超出设置时长，则抛出异常。
# 设置隐式等待10s 
driver.implicitly_wait(10)
try:
	print(ctime())
	driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
	print(e)
finally:
	print(ctime())
	driver.quit()

# 七 定位一组元素
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_class_name()
# find_elements_by_tag_name()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_xpath()
# find_elements_by_css_selector()

# 八多表单切换
# switch_to.iframe():默认可以直接取表单的id，或name,也可通过xpath定位
xf = driver.find_elements_by_xpath('//*[@id="x-URS-iframe"]')
driver.switch_to.iframe(xf)
...
driver.switch_to.parent_frame()
#跳回到最外层的页面
driver.switch_to.default_content()

# 九 多窗口切换
# switch_to.window()

# 获得百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.find_elements_by_link_text('登录').click()
driver.find_elements_by_link_text('立即注册').click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

#进入注册窗口
for handle in all_handles:
	if handle != search_windows:
		driver.switch_to.window(handle)
		print('now register window!')
		driver.find_element_by_name("account").send_keys('username')
		driver.find_element_by_name("password").send_keys('password')
		time.sleep(2)

# 十 警告框处理
# text：返回 alert/confirm/prompt 中的文字信息。
# accept()：接受现有警告框。
# dismiss()：解散现有警告框。
# send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。
link = driver.find_elements_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

driver.find_elements_by_link_text("搜索设置").click()

driver.find_element_by_name("prefpanelgo").click()
sleep(2)

#接受警告框
driver.switch_to.alert.accept()

# 十一 下拉框
#(1) 使用Select类
sel = driver.find_elements_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')
# index从 0 开始
# value是option标签的一个属性值，并不是显示在下拉框中的值
# visible_text是在option标签中间的值，是显示在下拉框的值
select_by_index(index)
select_by_value(value)
select_by_visible_text(text)
#(2) 反选（deselect）
deselect_by_index(index)
deselect_by_value(value)
deselect_by_visible_text(text)
deselect_all()
#(3) 信息查看Select提供了三个属性方法给我们必要的信息： 
options ——提供所有的选项的列表，其中都是选项的WebElement元素 
all_selected_options ——提供所有被选中的选项的列表，其中也均为选项的WebElement元素 
first_selected_option ——提供第一个被选中的选项，也是下拉框的默认值
# 十二 文件上传/下载
# (1)input 标签，绝对路径
driver.find_elements_by_name("file").send_keys('D:\\upload_file.txt')
# (2) 非input 上传文件
http://blog.csdn.net/huilan_same/article/details/52439546
# 下载
http://blog.csdn.net/huilan_same/article/details/52789954

# 十三 cookie操作
# get_cookies()： 获得所有cookie信息。
# get_cookie(name)： 返回字典的key为“name”的cookie信息。
# add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。
# delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
# delete_all_cookies()： 删除所有cookie信息。
driver.get("https://www.youdao.com")

cookie = driver.get_cookies()
print(cookie)

driver.add_cookie({'name': 'key-aaaaa', 'value': 'value-aaaa'})

for cookie in driver.get_cookies():
	print("%s -> %s" %(cookie['name'], cookie['value']))

# Selenium添加访问cookie实现自动登录
#(1) 登录并保存cookie
# 前面部分代码用于填写登录信息并登录

# 获取cookie并通过json模块将dict转化成str
dictCookies = self.browser.get_cookies()
jsonCookies = json.dumps(dictCookies)
#登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)

#(2) 读取cookie实现免登录访问
# 初次建立连接，随后方可修改cookie
self.browser.get('http://xxxx.com')
# 删除第一次建立连接时的cookie
self.browser.delete_all_cookies()
# 读取登录时存储到本地的cookie
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    self.browser.add_cookie({
        'domain': '.xxxx.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })
# 再次访问页面，便可实现免登陆访问
self.browser.get('http://xxx.com')
# 十四 调用Javascript
# 一 操作滚动条
http://blog.csdn.net/huilan_same/article/details/52387102
# execute_script()
# (1) 纵向滑动
js = "window.scrollTo(100, 450);"
driver.execute_script(js)

# (2) 横向滑动
#移动到最右边
js5 = "window.scrollTo(document.body.scrollWidth,0)"
#移动到最左边
js6 = "window.scrollTo(0,0)"
#移动到向右移动200像素
js7 = "window.scrollTo(200,0)"

# (3)操作内嵌滚动条
# 内嵌滚动条，一般嵌在一个iframe 里面，先切到要操作滚动条所在的iframe里面即可
driver.get("http://sahitest.com/demo/iframesTest.htm")
sleep(2)
driver.switch_to.frame(1)
js5 = "window.scrollTo(0,200)"
driver.execute_script(js5)  #向下移动200像素
#(4)总结
# 1)使用window.scrollTo(x,y) 这一语句，可以实现所有的纵向或横向滑动滚动条。其中x为横坐标，y为纵坐标，想纵向滚动200像素，就window.scrollTo(0,200)
# 2)获取当前窗口的高度和宽度
document.body.scrollWidth
document.body.scrollHeight
# 3)滑动到指定元素位置
arguments[0].scrollIntoView() ，arguments[0] 是指第一个传参

# 二 修改元素属性
http://blog.csdn.net/duzilonglove/article/details/78273546

# 十五 窗口截图
# get_screenshot_as_file()
# 截取当前窗口并指定截图图片的保存位置
driver.get_screenshot_as_file("C:\\Users\\sogaa001\\Desktop\\baidu_test.jgp")

# 十六 操作输入框
ele = driver.find_element_by_id('kw')
#获得输入框的值
ele.get_property('value')
#获得name属性值
ele.get_attribute('name')
#输入框是否可见
ele.is_displayed()
#输入框是否可用
ele.is_enabled()
#输入框是否被选中
ele.is_selected()

# 操作表格
# (1) 取某个单元格中的值像普通元素一样定位
# (2) 打印表格所有值
思路：
1、先定位页面中表格对象元素
2、在该表格中，通过tag name = ‘tr’ 找所有行
3、在第一行中，通过tag name = ‘td’ 找所有列
driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/tableTest.htm')

table = driver.find_element_by_xpath('/html/body/table[1]')
rows = table.find_elements_by_tag_name('tr')
cols = rows[0].find_elements_by_tag_name('td')

for i in range(len(rows)):
    for j in range(len(cols)):
        cell = rows[i].find_elements_by_tag_name('td')[j]
        print(cell.text)

# 十七 操作日期时间控件
# js = "document.getElementById('c-date1').removeAttribute('readonly')" # 1.原生js，移除属性
# js = "$('input[id=c-date1]').removeAttr('readonly')"  # 2.jQuery，移除属性
# js = "$('input[id=c-date1]').attr('readonly',false)"  # 3.jQuery，设置为false
js = "$('input[id=c-date1]').attr('readonly','')"  # 4.jQuery，设置为空（同3）

# 十八 Selenium之定制Chrome的选项（Options）
# 一 chromeoptions
chromeoptions 是一个方便控制 chrome 启动时属性的类。通过 selenium 的源码，可以看到，chromeoptions 主要提供如下的功能：
（1）设置 chrome 二进制文件位置 (binary_location)
（2）添加启动参数 (add_argument)
（3）添加扩展应用 (add_extension, add_encoded_extension)
（4）添加实验性质的设置参数 (add_experimental_option)
（5）设置调试器地址 (debugger_address)
# 二 定制启动选项
(1)添加chrome启动参数
# 启动时设置默认语言为中文 UTF-8
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
driver = webdriver.Chrome(chrome_options = options)

最常用的应用场景是设置user-agent以用来模拟移动设备，比如模拟 iphone6
options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')

（2）修改chrome设置
# 禁止图片加载
from selenium import webdriver
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)
driver.get("http://www.baidu.com/")
（3）添加扩展应用
from selenium import webdriver
options = webdriver.ChromeOptions()
extension_path = '/extension/path'
options.add_extension(extension_path)
driver = webdriver.Chrome(chrome_options = options)

（4）附赠添加代理方法
from selenium import webdriver
PROXY = "proxy_host:proxy:port"
options = webdriver.ChromeOptions()
desired_capabilities = options.to_capabilities()
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}
driver = webdriver.Chrome(desired_capabilities = desired_capabilities)

（5）启动浏览器，最大化
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

（6）指定driver地址
from selenium import webdriver

driver = webdriver.Chrome(executable_path='..drivers\chromedriver.exe')
这个地方的executable_path，可以是一个相对路径或一个绝对路径
'''

driver.quit()    #关闭所有窗口
driver.close()	 #关闭单个窗口

