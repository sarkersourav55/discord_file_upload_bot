from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


ls=[
"https://discord.com/channels/694878834926813246/694945396119699557",

]
class bot:
    def __init__(self,email,password):
        self.driver = webdriver.Chrome(executable_path="D:\Sourav (softwares)\chromedriver.exe")
        self.email=email
        self.password=password
    def login(self):
        driver=self.driver
        driver.get("https://discordapp.com/channels/@me")
        time.sleep(10)
        email=driver.find_element_by_xpath("//input[contains(@name,'email')]")
        email.send_keys(self.email)
        password=driver.find_element_by_xpath("//input[contains(@name,'password')]")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
    def send_file(self,ls,location,messeage_with_picture):
        
        driver=self.driver
        for channels in ls:
            driver.get(channels)
            time.sleep(10)
            #pop=driver.find_element_by_xpath("//button[@type='button'][contains(.,'Continue')]")
            #pop.click()
            img=driver.find_element_by_xpath("//input[contains(@class,'file-input')]")
            #chat.send_keys("How is it going(test)")
            #chat.send_keys(Keys.RETURN)

            loc="H://Sourav/"+str(location)
            time.sleep(2)
            img.send_keys(loc)
            time.sleep(2)
            upload_button=driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Upload')]")
            msg=driver.find_element_by_xpath("//div[contains(@class,'markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP textAreaWithoutAttachmentButton-qiaiTB')]")
            msg.send_keys(messeage_with_picture)
            upload_button.click()
            time.sleep(2)
            print("File Uploaded in server")
    def write(self,messeage):
        for channels in ls:
            driver.get(channels)
            time.sleep(10)
            chat=driver.find_element_by_xpath("//div[contains(@data-slate-object,'block')]")
            chat.send_keys(messeage)
            chat.send_keys(Keys.RETURN)


email=input("Enter Your Email(Discord):")
password=input("Enter Your password(Discord):")
a=input("Select a command('run':to initiate uploading):")
if a == "run":
    sourav= bot(email,password)
    time.sleep(8)
    location= input("Enter File name(with extension):")
    messeage_with_picture=input("Enter a messeage:")
    sourav.login()
    sourav.send_file(ls,location,messeage_with_picture)
#sourav= bot()
#sourav.login()
#sourav.join(ls)
#sourav.write(messeage)