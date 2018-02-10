#-*-coding:utf-8-*-
import os
import re
import sys
import time
import random
import pandas
import pyquery
import requests
import StringIO
import traceback
import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from sklearn.externals import joblib
from in2mysql import MySQL_API

httplib = requests.Session()
httplib.trust_env = False

class crack_picture(object):
	def __init__(self, img_url1, img_url2):
		self.img1, self.img2 = self.picture_get(img_url1, img_url2)
		# print "crack_picture..."

	def picture_get(self, img_url1, img_url2):
		hd = {"Host": "static.geetest.com",
			  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
		img1 = StringIO.StringIO(self.repeat(img_url1, hd).content)
		img2 = StringIO.StringIO(self.repeat(img_url2, hd).content)
		# print "picture_get..."
		return img1, img2


	def repeat(self, url, hd):
		times = 10
		while times > 0:
			try:
				ans = httplib.get(url, headers=hd, timeout=5)
				return ans
			except Exception as e:
				# print "repeat:", e
				times -= 1


	def pictures_recover(self, ypos):
		xpos = self.judge(self.picture_recover(self.img1, 'screenshots/img1.jpg'), self.picture_recover(self.img2, 'screenshots/img2.jpg')) - 6
		# print "xpos=%d" %xpos
		# print "ypos=%d" %ypos
		# print "pictures_recover"
		return self.darbra_track(xpos, ypos)


	def picture_recover(self, img, name):
		a = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
		im = Image.open(img)
		im_new = Image.new("RGB", (260, 116))
		for row in range(2):
			for column in range(26):
				right = a[row*26+column] % 26 * 12 + 1
				down = 58 if a[row*26+column] > 25 else 0
				for w in range(10):
					for h in range(58):
						ht = 58 * row + h
						wd = 10 * column + w
						im_new.putpixel((wd, ht), im.getpixel((w + right, h + down)))
		im_new.save(name)
		return im_new


	def darbra_track(self, xpos, ypos):
		list = []
		x = 5

		while xpos - x >= 10:
			t = random.randint(1, 2) / 20.0
			y_offset = random.randint(1, 2)
			list.append([x, ypos + y_offset, t])
			xpos = xpos - x
			x = random.randint(10, 30)

		while xpos - x >= 5:
			t = random.randint(1, 2) / 10.0
			y_offset = random.randint(1, 2)
			list.append([x, ypos+y_offset ,t])
			xpos = xpos - x
			x = random.randint(3, 10)

		while xpos > 0:
			x = random.randint(1, 2)
			# x = 1
			if xpos == 1:x = 1
			t = random.randint(3, 5) / 10.0
			list.append([x, ypos+y_offset, t])
			xpos = xpos - x
		# print "darbra_track"
		return list


	def diff(self, img1, img2, wd, ht):
		rgb1 = img1.getpixel((wd, ht))
		rgb2 = img2.getpixel((wd, ht))
		tmp = reduce(lambda x, y: x+y, map(lambda x: abs(x[0]-x[1]), zip(rgb1, rgb2)))
		return True if tmp >= 200 else False

		
	def col(self, img1, img2, cl):
		for i in range(img2.size[1]):
			if self.diff(img1, img2, cl, i):
				return True
		return False


	def judge(self, img1, img2):
		for i in range(img2.size[0]):
			if self.col(img1, img2, i):
				return i
		return -1


class gsxt(object):
	def __init__(self, br_name="chrome", timeout=60):

		# self.set_proxy()
		self.disable_proxy()

		self.br = self.get_webdriver(br_name)
		self.wait = WebDriverWait(self.br, timeout=timeout, poll_frequency=1.0)
		self.br.set_page_load_timeout(timeout)
		self.br.set_script_timeout(timeout)
		# self.br.maximize_window()
		self.br.set_window_position(0, 3000)

	def set_proxy(self):
		proxy = webdriver.Proxy()
		proxy.proxy_type = ProxyType.MANUAL
		proxy.http_proxy = "127.0.0.1:1080"
		proxy.socks_proxy = "127.0.0.1:1080"
		self.capabilities = webdriver.DesiredCapabilities.CHROME
		proxy.add_to_capabilities(self.capabilities)

	def set_proxy_system(self):
		proxy = webdriver.Proxy()
		proxy.proxy_type = ProxyType.SYSTEM
		self.capabilities = webdriver.DesiredCapabilities.CHROME
		proxy.add_to_capabilities(self.capabilities)

	def disable_proxy(self):
		proxy = webdriver.Proxy()
		proxy.proxy_type = ProxyType.DIRECT
		self.capabilities = webdriver.DesiredCapabilities.CHROME
		proxy.add_to_capabilities(self.capabilities)

	def input_params(self, name):
		self.br.get("http://www.gsxt.gov.cn/corp-query-homepage.html")
		element = self.wait_for(By.ID, "keyword")
		element.send_keys(name)
		time.sleep(1.0)
		element = self.wait_for(By.ID, "btn_query")
		element.click()
		# print "btn_query"
		time.sleep(2.0)
		# if u"请输入更详细的查询条件" in self.br.page_source:
		# 	print u"请输入更详细的查询条件"
		# 	return False
		return True


	def drag_pic(self):
		# print "drag_pic"
		return (self.find_img_url(self.wait_for(By.CLASS_NAME, "gt_cut_fullbg_slice")),
			   self.find_img_url(self.wait_for(By.CLASS_NAME, "gt_cut_bg_slice")))
		
	
	def wait_for(self, by1, by2):
		# print "wait_for:", by1, by2
		return self.wait.until(EC.presence_of_element_located((by1, by2)))


	def find_img_url(self, element):
		# print "find_img_url:", element
		try:
			return re.findall('url\("(.*?)"\)', element.get_attribute('style'))[0].replace("webp", "jpg")
		except Exception as e:
			# print "find_img_url:", e
			return re.findall('url\((.*?)\)', element.get_attribute('style'))[0].replace("webp", "jpg")


	def emulate_track(self, tracks):
		# print "emulate_track"
		element = self.br.find_element_by_class_name("gt_slider_knob")
		ActionChains(self.br).click_and_hold(on_element=element).perform()
		for x, y, t in tracks:
			# print x, y ,t
			ActionChains(self.br).move_to_element_with_offset(
						to_element=element,
						xoffset=x+22,
						yoffset=y+22).perform()
			ActionChains(self.br).click_and_hold().perform()
			time.sleep(t)
			
		time.sleep(0.24)
		ActionChains(self.br).release(on_element=element).perform()
		time.sleep(0.8)
		element = self.wait_for(By.CLASS_NAME, "gt_info_text")
		ans = element.text
		# print ans
		return ans


	def run(self, company_list=[u'信息技术'], log_state=False, paging=True):
		from_index = 0
		dat_file = "from_index.dat"
		# if os.path.exists(dat_file):
		#	from_index = joblib.load(dat_file)
		
		np.random.shuffle(company_list)
		for index, company_name in enumerate(company_list):
			if log_state and index <= from_index:
				continue
			try:
				self.hack_geetest(company_name, paging=paging)
			except Exception as e:
				# print e
				# print traceback.print_exc()
				# raw_input("Quit?")
				self.quit_webdriver()
				sys.exit(1)

			if log_state:
				joblib.dump(index, dat_file, compress=3)

			time.sleep(1)

	def hack_geetest(self, company=u"信息技术", paging=True, retry=2):
		flag = True
		ret = self.input_params(company)
		if not ret:
			return False

		self.wait_for(By.CLASS_NAME, "gt_slider_knob")
		element = self.br.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")
		# print "find_element_by_xpath"
		location = element.location
		y = location['y']

		info_list = []

		while (flag and retry):
			# print "hack_geetest..."
			img_url1, img_url2 = self.drag_pic()
			tracks = crack_picture(img_url1, img_url2).pictures_recover(y)
			tsb = self.emulate_track(tracks)
			# print tsb
			if u'通过' in tsb:
				print "=" * 40
				print tsb
				time.sleep(2)
				info_list += self.parse_html()
				if paging:
					info_list += self.click_next_page()
				break
			elif u'吃' in tsb:
				time.sleep(4)
			else:
				self.input_params(company)
			retry = retry - 1

		for info in info_list:
			company_name, url = info
			ret = self.get_html_data_by_url(company_name, url)


	def click_next_page(self):
		info_list = []
		for i in range(2, 5 + 1):
			try:
				next_page = self.br.find_element_by_link_text(u"下一页")
				next_page.click()
				info_list += self.parse_html()
				time.sleep(1)
			except Exception as e:
				# if "NoSuchElementException" in e:
				break
		return info_list

	def get_html_data_by_url(self, company_name, url, retry=5):
		file_name = "html/%s.html" % (company_name.encode("gbk"))
		if os.path.exists(file_name):
			print company_name.encode("gbk"), "exists"
			return True
		try:
			self.br.get(url)
		except Exception as e:
			# print e
			# print traceback.print_exc()
			time.sleep(2)
			return self.get_html_data_by_url(company_name, url, retry=retry)

		self.br.execute_script("""
			var script = document.createElement('script');
			script.type='text/javascript';
			script.innerHTML = "var delay=0;var timeOut;function scrollToBottom(){delay++;if(delay>50){};window.scrollBy(0, 200);timeOut=setTimeout('scrollToBottom()', 200);}";
			document.body.appendChild(script);
			scrollToBottom();
		""")

		self.br.execute_script("scrollToBottom();")

		# time.sleep(0.2*10*5)

		company_html = self.br.page_source.encode("utf8")
		if "返回首页重新操作" in company_html or "国家企业信用信息公示系统" not in company_html or "营业执照信息" not in company_html:
			if retry >= 0:
				time.sleep(2)
				return self.get_html_data_by_url(company_name, url, retry=retry-1)
			else:
				print u"由于您操作过于频繁/由于您长时间未操作，请稍后返回首页重新操作".encode("gbk")
				sys.exit(1)

		company_html = company_html.replace('href="/css/', 'href="css/')
		# company_html = company_html.replace('src="/js/', 'src="js/')
		company_html = company_html.replace('\r\n', ' ENTERENTERENTER ')
		company_html = re.sub("<script.+?</script>", "", company_html)
		company_html = company_html.replace(' ENTERENTERENTER ', '\r\n')

		with open(file_name, "w") as f:
			f.write(company_html)
			f.close()

		print company_name.encode("gbk"), "+++++"

		return True

	def parse_html(self):
		html = self.br.page_source
		data = html.split('<div class="container">', 1)[-1]
		data = data.split('<div class="footer3"')[0]

		dom = pyquery.PyQuery(data)
		search_list_items = dom("a.search_list_item")

		info_list = []
		for i in range(len(search_list_items)):
			text = search_list_items.eq(i).text().encode("utf8")
			href = search_list_items.eq(i).attr("href")
			href = "http://www.gsxt.gov.cn" + href

			ele = pyquery.PyQuery(search_list_items.eq(i).html())
			company_name = ele("h1").eq(0).text()
			company_name = company_name.replace(u"(", u"（")
			company_name = company_name.replace(u")", u"）")
			company_name = company_name.replace(u" ", u"")
			info_list.append((company_name, href))
			try:
				print company_name.encode("gbk")
			except:
				pass

		return info_list

	def quit_webdriver(self):
		self.br.quit()

	def get_webdriver(self, name):
		if name.lower() == "phantomjs":
			dcap = dict(DesiredCapabilities.PHANTOMJS)
			dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36")
			return webdriver.PhantomJS(desired_capabilities=dcap)

		elif name.lower() == "chrome":
			# return webdriver.Chrome()
			return webdriver.Chrome(desired_capabilities=self.capabilities)


def crawl_by_keywords():
	data = pandas.read_csv("keywords.csv", header=0)
	keywords = data.keyword.tolist()
	keywords = [keyword.decode("utf8") for keyword in keywords if len(keyword.decode("utf8")) >= 2]
	keywords = list(set(keywords))

	browser = gsxt("chrome")
	browser.run(company_list=keywords, log_state=True)
	browser.quit_webdriver()

def crawl_by_company():
	browser = gsxt("chrome")
	mysql = MySQL_API()
	
	sql = "select id, name from company where crawled = 0 order by id"
	result = mysql.query(sql)
	for row in result:
		id, company_name = row
		try:
			time.sleep(2)
			# ret = browser.hack_geetest(company_name.decode("utf8"), paging=False)
			ret = browser.hack_geetest(company_name.decode("utf8"), paging=True)
			sql_update = "update company set crawled = 1 where id = %d" % id
			mysql.query(sql_update)
			mysql.commit()
		except Exception as e:
			pass
			# print e
			# print traceback.print_exc()

	browser.quit_webdriver()

if __name__ == "__main__":
	crawl_by_keywords()
	# crawl_by_company()



