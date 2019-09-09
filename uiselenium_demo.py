from selenium import webdriver
import time
import  unittest


#打开百度，然后搜索python关键字。 配合unittest、点击第二条搜索结果，查看打开页面的标题。
#chromedriver 对应的下载地址： http://npm.taobao.org/mirrors/chromedriver
class BaiBu(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.baidu.com")
        time.sleep(5)

    def tearDown(self):
        self.browser.quit()

    def test_search(self):
        self.browser.find_element_by_id("kw").send_keys("python")
        self.browser.find_element_by_id("su").click()
        self.browser.maximize_window()
        self.browser.find_element_by_xpath(".//*[@id='2']/h3/a").click()
        time.sleep(5)
        
        print (self.browser.title)
        self.assertIn("python", self.browser.title)

if __name__=="__main__":
    unittest.main()

