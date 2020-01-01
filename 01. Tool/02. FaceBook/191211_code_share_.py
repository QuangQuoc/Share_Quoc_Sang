import random
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
 
def main():
    #Read data from excel
    #df = pd.read_excel('test.xlsx')
    # Your Facebook account user and password
    usr = "vinhquang13531@gmail.com"
    pwd = "Vinhquang_@13531"
    message = "https://bom.to/xK4X2U"
    chromedriver_path = "E:/05. Software/Chrome/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    # 1:allow, 2:block 
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
 
    driver = webdriver.Chrome(executable_path = chromedriver_path, chrome_options=chrome_options)
    driver.implicitly_wait(15) # seconds
 
    # Go to facebook.com
    driver.get("https://www.facebook.com/") 
    # Enter user email
    try:
        elem = driver.find_element_by_id("email")
    except:
        elem = driver.find_element_by_name("email")
    elem.send_keys(usr)
    # Enter user password
    try:
        elem = driver.find_element_by_id("pass")
    except:
        elem = driver.find_element_by_name("pass")
    elem.send_keys(pwd)
    # Login
    elem.send_keys(Keys.RETURN)
    sleep(10)
    group_links = [
        "groups/phongtrodanang/",
        "groups/chovieclamdanang/"
    ] 
    while(1):
        #for group in df['Group']:
        for group in group_links:
            try:
                print(group)
                # Go to the Facebook Group
                driver.get("https://www.facebook.com/"+str(group))
                
                try:
                    post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
                except:
                    post_box=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/li[2]/a")

                post_box.click()
                # Enter the text we want to post to Facebook
                try:
                    post_box.text = message
                except:
                    try:
                        driver.execute_script("arguments[0].value = arguments[1];", post_box, message)
                    except:     
                        ActionChains(driver).send_keys(message).perform()
                sleep(5)
                # Delete message
                ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(' ').perform()
                
                sleep(5)
                buttons = driver.find_elements_by_tag_name("button")
                sleep(5)
                for button in buttons:
                    if button.text == "Đăng":
                        button.click()
                        #random sleep 10p->15p
                        sleep(5)
                print("Share OK")
                print("------------------------")
                #random sleep 10p->15p
                x=random.randint(120,300)
                print(x)
                sleep(x)
            except:
                print("Group loi " + str(group))
                print("------------------------")
        
    # driver.close()
 
if __name__ == '__main__':
  main()
