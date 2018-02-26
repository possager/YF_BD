#_*_coding:utf-8_*_
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium import webdriver

logindriver=webdriver.Chrome()

logindriver.get(url='https://twitter.com/login')
username_div=logindriver.find_element_by_xpath('//div[@id="page-container"]//div[@class="signin-wrapper"]//input[@name="session[username_or_email]"]')#//div[@id="page-container"]//div[@class="signin-wrapper"]//input[@name="session[username_or_email]"]
password_div=logindriver.find_element_by_xpath('//div[@id="page-container"]//div[@class="signin-wrapper"]//input[@name="session[password]"]')
username_div.click()
username_div.send_keys('mio1650392zhi@163.com')

password_div.click()
password_div.send_keys('ww13552')

loginButton=logindriver.find_element_by_xpath('//button[@class="submit EdgeButton EdgeButton--primary EdgeButtom--medium"]')
loginButton.click()

#增加一个针对帖子来评论，以此来生成对应的gid等cookie
forum1=logindriver.find_element_by_xpath('//div[@id="page-container"]//div[@role="main"]//div[@class="stream"]//ol/li[2]/div/div[@class="content"]//span[@class="Icon Icon--medium Icon--reply"]')
forum1.click()


Actioncharis1=ActionChains(logindriver)
action1=Actioncharis1.send_keys('mark')
endterkey=Keys.ENTER
action1.send_keys(endterkey)
action1.click()
action1.perform()
