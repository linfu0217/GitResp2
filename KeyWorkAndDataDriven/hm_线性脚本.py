#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#创建Chrome浏览器
driver = webdriver.Firefox()
driver.get("https://126.com/")
print(driver.title)
# #最大化浏览器窗口
# driver.maximize_window()
#chrome_options = Options()
#添加屏蔽 --ignore-certificate-errors提示信息的设置参数项
# chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# driver = webdriver.Chrome(chrome_options=chrome_options)
#访问126邮箱登录页
#driver.get("http://mail.126.com")
#暂停5秒，以便邮箱登录页加载完成
time.sleep(5)
assert ("126网易免费邮--你的专业电子邮" == driver.title)
print("访问126邮箱登录页成功")
#点击密码登录按钮切换页面
#driver.find_element_by_id("switchAccountLogin").click()
#driver.find_element_by_link_text("密码登录").click()
#检查tagname为iframe的iframe是否存在，存在则切换进frame控件
wait = WebDriverWait(driver,30)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,"iframe")))
#切换进frame控件
#driver.switch_to.frame("x-URS-iframe")
#因为iframe的ID是动态生成的，所以用其他方法定位到改iframe（用其上一层父元素标签的唯一识别id/iframe来定位)
#iframe = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
#driver.switch_to.frame(iframe)
#获取用户输入框
username = driver.find_element_by_xpath("//input[@name='email']")
#输入用户名
username.send_keys("lf13428104670")
#获取密码输入框
pwd = driver.find_element_by_xpath("//input[@name='password']")
#输入密码
pwd.send_keys("linfu520")
#发送一个回车键
pwd.send_keys(Keys.RETURN)
print("用户登录......")
#等待10秒，以便登录成功后的页面加载完成
time.sleep(5)
assert("网易邮箱" in driver.title)
#因为前面进入frame,此时需要退出frame
driver.switch_to.default_content()
#显示等待通讯录链接页面出现
addressBook = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='通讯录']")))
#单击“通讯录”按钮
addressBook.click()
#显示等待“联系人”按钮
newContact = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='新建联系人']")))
#单击新键联系人按钮
newContact.click()
#显示等待姓名输入框的出现
contactName = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@title='编辑详细姓名']/preceding-sibling::div/input")))
contactName.send_keys("lily")
#输入联系人电子邮箱/html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/div[1]/dl/dd/div/input
driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/div/div[1]/div/div[1]/div[1]/dl/dd/div/input").send_keys("532104418@qq.com")
driver.find_element_by_xpath("//span[text()='设为星标联系人']").click()
#输入联系人手机号码
driver.find_element_by_xpath("//*[@id='iaddress_TEL_wrap']//dd//input").send_keys("13428104670")
time.sleep(2)
#输入备注信息
driver.find_element_by_xpath("//textarea").send_keys("朋友")
time.sleep(2)
#单击“确认”按钮
driver.find_element_by_xpath("//span[text()='确 定']").click()
#driver.find_element_by_xpath("/html/body/div[9]/div[3]/div[2]/div[1]/span").click()
time.sleep(2)
assert ("532104418@qq.com" in driver.page_source)
print("添加联系人成功")
print("进入首页")
driver.find_element_by_xpath('//div[.="首页"]').click()
print("写信")
#显示等待写信链接页面元素的出现
# element = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]")))
element = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='写 信']")))
#单击写信链接
element.click()
#写入收件人地址
driver.find_element_by_xpath("//div[contains(@id,'_mail_emailinput')]/input").send_keys("532104418@qq.com")
#写入邮件主题//*[@id="1621086688662_subjectInput"]
driver.find_element_by_xpath("//div[@aria-label='邮件主题输入框，请输入邮件主题']/input").send_keys("光荣之路")
#切换进frame
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@tabindex=1]"))
editBox = driver.find_element_by_xpath("/html/body")
editBox.send_keys("发给光荣之路的一封信")
driver.switch_to.default_content()
print("写信完成")
driver.find_element_by_xpath("//header//span[text()='发送']").click()
print("开始发送邮件")
time.sleep(3)
assert ("发送成功" in driver.page_source)
print("邮件发送成功")
driver.quit()