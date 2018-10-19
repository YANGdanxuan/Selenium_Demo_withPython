# coding:UTF-8
#_*_coding:utf-8_*_
from selenium import webdriver
import unittest
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#通过关键字as把excepted_conditiont预期条件判断类重命名为EC，则可以在之后使用EC代替excepted_condition
from selenium.webdriver.support import excepted_condition as EC
from time import sleep, ctime
import os

if sys.getdefaultencoding()!='utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')

#选择元素
class DemoAboutSelect(unittest.testcase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.base_url = 'http://baidu.com'

	def test(self):
		driver = self.driver
		driver.get(self.base_url)
		
		#可以通过元素的id来定位，id是HTML页面中元素的唯一的属性，适合用来定位
		driver.find_element_by_id('')
		
		#可以通过元素的name来定位，name在HTML中不唯一
		driver.find_element_by_name('')
		
		#可以通过元素的class来定位，class在HTML中不唯一
		driver.find_element_by_class_name('')
		
		#可以通过元素的标签名来定位，tag_name在HTML中不唯一
		driver.find_element_by_tag_name('')
		
		#可以通过元素标签对之间的文本信息来定位,文本信息在HTML中有可能是唯一的
		driver.find_element_by_link_text('')

		#可以通过元素标签对之间的一部分文本信息来定位，在HTML中有可能并不唯一
		driver.find_element_by_partial_link_text('')
		
		#可以通过XPATH方式来定位(可以通过FF、Chrome、Edge调试工具快速生成xpath)
		#可以传入在HTML中的绝对定位、元素属性、运算符driver.find_element_by_xpath('')
		
		#XPATH可以通过绝对路径方式来定位
		driver.find_element_by_xpath('/html/body/div/div[3]/div/imput')
		
		#xpath可以利用元素属性方式来定位
		#元素属性方式：'//' + '标签名或*通配符' + '[@' + '要使用的元素属性' + '=' + '要定位元素属性的值'
		driver.find_element_by_xpath("//input[@id='su']")
		
		#xpath可以同时使用元素属性方式+绝对路径方式来定位，通过属性较多的父级找到子级
		driver.find_element_by_xpath("//input[@id='su']/input")
		
		#xpath可以使用逻辑运算符+元素属性+路径方式来定位，适合一个属性不能唯一定位元素的情况下 
		driver.find_element_by_xpath("//input[@name='su' and @class='btclass']/div/input")
		
		#可以通过CSS方式来定位元素[.class, #id, *, tag_name, 层级, [属性='值']] 等组合定位
		driver.find_element_by_css_selector('')
		
		#可以通过By方式来定位元素,find_element(By.定位方式, 定位相关参数)
		#使用前要导入By类:from selenium.webdriver.common.by import By
		#定位方式：ID,NAME,CLASS_NAME,TAG_NAME,LINK_TEXT,PARTIAL_LINK_TEXT,XPATH,CSS_SELECTOR
		driver.find_element(By.ID,'kw')
		
		
		#定位一组元素，通常用于以下场景：1.批量操作元素；2.先获取一组元素，再从这组对象中过滤出需要操作的元素
		#在这里其实是有点问题的，比如id，这个东西在一个HTML里面是唯一的不能有id重复的元素，定位出来永远只有一个，用find_elements_by_id()其实有点违背了HTML的规则了，除非有些特殊情况下是想以一个数组形式来获取一个元素，但这是很浪费资源的一件事，目前想不出来什么情况下可以用到
		driver.find_elements_by_id('kw')
		driver.find_elements_by_name('su')
		driver.find_elements_by_class_name('su')
		driver.find_elements_by_tag_name('kw')
		driver.find_elements_by_link_text('kw')
		driver.find_elements_by_partial_link_text('su')
		driver.find_elements_by_xpath('su')
		driver.find_elements_by_css_selector('su')
		#可从里面使用pop()指定某一个元素来操作
		driver.find_elements_by_class_name('class').pop(-1).click()


	def teatDown(self):
		self.driver.quit()

#操作类
class DemoAboutOperate(unittest.testcase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.base_url = 'http://baidu.com'
	
	
	#操作窗口、浏览器（改变窗口大小，浏览器前进、后退、刷新）
	def testOperateWithWindow(self):
		driver = self.driver
		driver.get(self.base_url)
		
	#控制浏览器window
		#控制浏览器大小set_window_size(width, height)，用于自适应移动端时可以设置
		driver.set_window_size(480, 720)
		
		#用于PC端一般希望全屏显示可以使用maximize_window(),不需要参数
		driver.maximize_window()
		
		#控制浏览器后退，back()
		driver.back()
		
		#控制浏览器前进
		driver.forward()
		
		#控制浏览器刷新
		driver.refresh()
		
		#获取当前所有打开的窗口的句柄，返回数组形式，window_handle 
		handle2 = driver.window_handles
		
		#获取当前/焦点窗口的句柄，current_window_handle
		handle1 = driver.current_window_handle

		#切换到指定窗口句柄的窗口，switch_to.window(handle)
		driver.switch_to.window(handle1)
	
	
	#操作元素
	def testOperateWithElement(self):
		driver = self.driver
		driver.get(self.base_url)
		
		
	#简单元素操作（清除内容、发送写入内容、点击、提交）
		#清空内容，用于避免文本输入框中输入造成与默认提示语拼接
		driver.find_element(By.ID, 'kw').clear()
		
		#模拟按键输入，模拟键盘向输入框输入内容，发送键盘按键，模拟文件上传
		driver.find_element(By.ID, 'kw').send_keys('value')
		
		#模拟单击，用于可以被单击的对象，可以包括按钮，文字/图片链接，复选框，单选框，下拉框等
		driver.find_element(By.ID, 'su').click()
		
		#模拟提交操作，可以用于搜索框模拟搜索按钮效果，提交一个按钮，有时可以和click方法交互使用
		driver.find_element(By.ID, 'kw').submit()
		
		
	#WebElement接口其他常用方法（获得元素尺寸、元素文本内容、属性的值、返回是否可见）
		#可返回元素的尺寸{'width':value1, 'height':value2} size没有()
		driver.find_element(By.ID, 'kw').size
		
		#可返回元素的文本内容,text没有()
		driver.find_element(By.ID, 'kw').text
		
		#可返回元素的属性
		driver.find_element(By.ID, 'kw').get_attribute('type')
		
		#可返回该元素是否用户可见 true/false
		driver.find_element(By.ID, 'kw').is_displayed()
		
		
	#鼠标事件（模拟单击、悬停、双击、拖放、提交）
		#使用前要导入 ActionChains 类:from selenium.webdriver.common.action_chains import ActionChains
		#调用 ActionChains 需要把浏览器驱动作为参数传入 
		#格式：ActionChains (浏览器驱动).操作(元素)
		
		#变量化元素（个人添加步骤，避免以下例子代码过长，才变量化，非必要）
		element1 = driver.find_element(By.ID, 'kw')
		element2 = driver.find_element(By.ID, 'su')
		
		#模拟鼠标右键操作，context_click()需要传入点击的元素
		ActionChains(driver).context_click(element1)
		
		#模拟鼠标悬停,move_to_element()
		ActionChains(driver).move_to_element(element1)
		
		#模拟鼠标双击操作
		ActionChains(driver).double_click(element1)
		
		#模拟鼠标拖放操作 drag_and_drop(source, target) 拖动的源元素，释放到目标元素上
		ActionChains(driver).drag_and_drop(element1, element2)
		
		#perform() 执行 ActionChains 中存储的行为，可以理解为对整个操作的提交动作
		ActionChains(driver).context_click(element1).perform()
		
		
	#键盘事件（键盘按下操作，可单键可组合键）
		#使用键盘上按键前要导入 Keys 类：from selenium.webdriver.common.keys import Keys
		#send_keys(Keys.yourself_keyboard [,'组合键'])
		#BACK_SPACE删除\SPACE空格\TAB制表\ESCAPE回退键\ENTER回车键\CONTROL控制键\F1\F2...\组合键
		#输入删除键
		element1.send_keys(Keys.BACK_SPACE)
		#输入空格键
		element1.send_keys(Keys.SPACE)
		#输入Tab键（制表）
		element1.send_keys(Keys.TAB)
		#输入回退键
		element1.send_keys(Keys.ESCAPE)
		#输入回车键
		element1.send_keys(Keys.ENTER)
		#输入组合键Ctrl+a
		element1.send_keys(Keys.CONTROL, 'a')
		#输入F1键
		element1.send_keys(Keys.F1)
		
		
	#获得验证信息
		#来验证是否符合预期结果，可以从title、URL、text来验证执行结果的对错
		#获取当前页面的标题，title
		title1 = driver.title
		#获取当前页面的URL，current_url
		now_url1 = driver.current_url
		#获取元素的文本，text
		now_text = driver.text
		
		
	#设置元素等待
		#显示等待： WebDriverWait().until() 某个条件成立时继续，否则在达到最大时长时抛出超时异常TimeoutException
		#使用前需要导入WebDriverWait：from selenium.webdriver.support.ui import WebDriverWait
		#WebDriverWait(driver, timeout, check_per_secondtime, ignored_exceptions=None)
		#ignored_exceptions超时后抛出的异常，默认抛出NoSuchElementException异常
		#WebDriverWait通常会搭配until(method, value) /until_not(method, value)使用
		element3 = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
		# EC excepted_condition类提供的预期条件判断方法
		#{title_is:判断当前页面的标题是否等于预期, title_contains:判断当前页面的标题是否包含预期字符串, presence_of_element_located:判断元素是否被加在DOM树里，包含不可见元素, visibility_of_element_located:判断元素的定位是否非隐藏且宽高不为0（参数是定位）, visibility_of:判断元素是否非隐藏且宽高不为0（参数是定位好的元素）, presence_of_all_element_located:判断至少有一个元素存在于DOM树中, text_to_be_present_in_element:判断元素中的text是否包含预期字符串, text_to_be_present_in_element_value:判断元素的value属性是否包含预期字符串, frame_to_be_available_and_switch_to_it:判断该表单是否可以切换进去，可以则切换并返回True, invisibility_of_element_located:判断元素是否不存在于DOM树或不可见, element_to_be_clickable:判断元素是否可见且可点击, staleness_of:等到一个元素从DOM树中移除, element_to_be_selected:判断元素是否被选中（下拉列表）, element_selection_state_to_be:判断元素的选中状态是否符合预期, element_located_selection_state_to_be:判断元素的定位的选中状态是否符合预期, alert_is_present:判断页面上是否存在alert} is_displayed()元素是否可见
		
		#隐式等待：implicitly_wait()设置全局固定等待时长s，找不到时才等待，超出时长报异常
		driver.implicitly_wait(10)
		
		#sleep休眠方法：设置某一次等待的固定时长，然后继续，单位为秒
		#使用前需要导入sleep： from time import sleep
		sleep(8)
		
		
	#表单操作(切换表单、跳出表单、切回主文档)
		#frame/iframe表单嵌套页面时使用，需要切换iframe和frame两个页面
		#switch_to.frame() 可以传入id\name，也可以传入定位对象，或者传入frame的下标index从0开始
		#传入id\name此处有问题，和HTML有关，同一个HTML文档中id和name可以相同，这样传参会出现问题，建议还是传入定位对象
		#传入定位对象
		element4 = driver.fine_element_by_xpath('/html/body/div/li/frame')
		driver.switch_to.frame(element4)
		#传入id/name
		driver.switch_to.frame('if')
		#传入下标index
		driver.switch_to.frame(2)
		
		#switch_to.parent_content() 跳出当前一级的表单，默认是匹配最近的 switch_to.frame()方法，该方法有可能不可用
		driver.switch_to.parent_content()
		
		#切到父frame，有多层frame时有用，但一般这种嵌套多层的frame是有影响到性能的问题的，可以让开发改进
		driver.switch_to.parent_frame()
		
		#切换到主文档，或者理解为最外层的页面
		driver.switch_to.default_content()
		
		
	#switch_to家族的其他（切到当前焦点元素、切到当前alert、confirm、prompt框、切到某个浏览器窗口）
		#driver.switch_to.active_element.send_keys('selenium') 返回当前取得焦点的webdriver对象，然后操作
		#driver.switch_to.alert.send_keys()  返回浏览器的alert对象，可对浏览器alert、confirm、prompt框操作
		#driver.switch_to.window(window_name)  切到某个浏览器窗口
		
		
	#警告框的处理 先使用switch_to.alert()定位到警告框 包括 alert\confirm\prompt
		#accept() 接受现有警告框
		driver.switch_to.alert().accept()
		
		#dismiss() 解散现有警告框
		driver.switch_to.alert().dismiss()
		#也可以定位到警告框之后，返回警告框的文本信息 text , 或者发送文本信息 send_keys(message)
	
	
	#如果要使用本地的HTML文档进行测试，get的时候传入文件地址
	def testWithLocalhostHTMLFile(self):
		driver = self.driver
		
		#使用本地文件进行测试
		#在当前py同个路径时使用'file:///' + os.path.abspath('xxx.html')
		#使用非当前路径的文件时'file:///' + 文件的绝对路径如'F:\doc\find.html'
		#os.path.abspath('file.html')用于获取当前路径下的文件，需要提前导入os类
		#import os
		file_path = 'file:///' + os.path.abspath('result.html')
		driver.get(file_path)
	
	
	#上传文件
	def testWithUploadFile(self):
		driver = self.driver
		driver.get(self.base_url)
		
		#send_keys方法完成，传入文件的绝对路径，适用input标签，可以避免操作windows控件
		driver.find_element_by_id('su').send_keys('E:\\disk\file.txt')
		#Autolt方法实现
		#执行autoit的脚本来实现
	
	
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	testunit = unittest.TestSuite()
	testunit.addTest(DemoAboutSelect('test'))