from selenium import webdriver
from Page import PerPage

class PerZuoPin:
    def __init__(self, url, path = './'):
        self.url = url
        wb=webdriver.Firefox(executable_path="./geckodriver.exe")
        wb.get(url)
        self.wb = wb
        self.path = path

    def DownLoad(self, ):
        url = self.wb.current_url
        url = str(url)
        hostnames = url.split('/')
        hostname = hostnames[0] + '//' + hostnames[2]
        a_elements = self.wb.find_elements_by_xpath('//*[@id="permalink"]/div[4]/ul//a')
        llll = []    
        for i in range(len(a_elements) - 4, len(a_elements)):
            uHref = a_elements[i].get_attribute('href')
            href = str(uHref)
            sub_url = href
            llll.append(sub_url)
        
        # llll.append(str(a_elements[0].get_attribute('href')))
            
        self.wb.close()

        for u in llll:
            ppp = PerPage(u, self.path)
            ppp.DownLoad()

        
        

if __name__ == '__main__':
    # a = PerZuoPin('http://www.hhimm.com/manhua/17334.html', './hentai/')
    a = PerZuoPin('http://www.hhimm.com/manhua/27411.html', './hentai/')
    a.DownLoad()