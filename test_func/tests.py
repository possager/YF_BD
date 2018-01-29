from selenium import webdriver
import time
import pickle




driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.find_element_by_xpath('//div[@id="u1"]/a[@name="tj_login"]').click()
time.sleep(3)
driver.find_element_by_xpath('//p[@class="tang-pass-footerBarULogin"]').click()
time.sleep(3)
input_name=driver.find_element_by_xpath('//input[@class="pass-text-input pass-text-input-userName"]')
input_name.send_keys('somepython')

input_pwd=driver.find_element_by_xpath('//input[@id="TANGRAM__PSP_10__password"]')
input_pwd.send_keys('ll13629056300')
driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()
time.sleep(10)
driver.find_element_by_xpath('//input[@class="pass-button pass-button-submit"]').click()
driver.get(url='https://tieba.baidu.com/index.html?traceid=')
cookies=driver.get_cookies()
print cookies


driver.get(url='https://tieba.baidu.com/p/5526240215')

# one_post=driver.find_element_by_xpath('//li[@fid]//div[@class="thread-name-wraper"]/a')
# one_post.click()
print 'end'


pass


script='''
var a=function(){var t = {};
                    window._BSK.a("omzVouOACqkNljzDbdOB", {
                        IN: {tbs:"1796da2383a8d7601516771376"},
                        OUT: t
                    }); return t.data};
                    
                    a();
'''


print driver.execute_script(script)



with open('cookies/baidu_lognin_driver','w+') as f:
    try:
        pickle.dump(obj=driver,file=f)
    except Exception as e:
        print e




print 'end'