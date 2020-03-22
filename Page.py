from selenium import webdriver
import time
import requests

class PerPage:
    def __init__(self, url, path='./'):
        self.url = url
        # options=webdriver.ChromeOptions()
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--allow-running-insecure-content')
        # wb=webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
        wb=webdriver.Firefox(executable_path="./geckodriver.exe")
        wb.get(url)
        self.wb = wb
        self.path = path
    
    def PageInfo(self):
        ss = self.wb.find_element_by_xpath('/html/body/div[1]/div[1]/b').get_attribute('textContent')
        s = str(ss)
        print(type(s))
        sArray = s.split('/')
        sArray[0] = sArray[0].strip()
        sArray[1] = sArray[1].strip()
        res = [int(sArray[0]), int(sArray[1])]
        return res
    
    def NextPage(self):
        self.wb.find_element_by_xpath('//*[@id="btnPageNext2"]').click()
        time.sleep(2)
    

    def DownLoad(self):
        pageIF = self.PageInfo()
        fileNames = self.wb.title.split(' ')
        fileName = self.path + fileNames[0] + '_' + fileNames[1]
        print('begin download: 1 page')

        uImg_src = self.wb.find_element_by_xpath('//*[@id="iBody"]/img').get_attribute('src')
        img_src = str(uImg_src)
        with open(fileName + '.txt', 'wb') as f:
            f.writelines(img_src)

        while pageIF[0] != pageIF[1]:            
            self.NextPage()

            uImg_src = self.wb.find_element_by_xpath('//*[@id="iBody"]/img').get_attribute('src')
            img_src = str(uImg_src)
            print(img_src)
            with open(fileName + '.txt', 'ab') as f:
                f.writelines('\r\n')
                f.writelines(img_src)
            pageIF = self.PageInfo()
        self.wb.close()
        

if __name__ == '__main__':
    a = PerPage('http://www.hhimm.com/cool200862/1.html?s=10')
    a.DownLoad()

    