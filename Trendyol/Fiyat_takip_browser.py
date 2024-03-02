from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import smtplib 

class browser:
    def __init__(self,time,count,link) :
        self.browser=webdriver.Chrome()
        self.time=time
        self.count=count
        self.link=link
        browser.TrendyolErisim(self)

    def TrendyolErisim(self):
        self.browser.get(self.link)
        browser.FiyatTakip(self)

    def FiyatTakip(self):
        for x in range(0,self.count,1):
            time.sleep(self.time)
            fiyat_element=self.browser.find_element(By.XPATH,'//*[@id="product-detail-app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[3]/div/div/span')
            fiyat_element=float(fiyat_element.text.replace("TL","").strip())

            print(fiyat_element)
            time.sleep(self.time)
            browser.MailAlert(self)
    
    def MailAlert(self):
        
        try: 
            #Create your SMTP session 
            self.smtp = smtplib.SMTP('smtp.gmail.com', 587) 
            #Use TLS to add security 
            self.smtp.starttls() 
            #User Authentication 
            self.smtp.login("ibrahim.tas@gmail.com","wdeawd5646!asad")
            #Defining The Message 
            self.message = self.FiyatTakip.fiyat_element()
            #Sending the Email
            if self.FiyatTakip.fiyat_element <= 15000:
                self.smtp.sendmail("ibrahim.tas@gmail.com", "ibrahim.tas@gmail.com",self.message) 
                #Terminating the session 
                self.smtp.quit() 
                print ("Email sent successfully!") 
        except Exception as ex: 
            print("Something went wrong....",ex)
    
        self.browser.quit()













