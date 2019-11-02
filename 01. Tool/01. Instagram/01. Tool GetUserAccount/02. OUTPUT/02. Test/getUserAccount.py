from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas

chromedriver_path = "E:/05. Software/Chrome/chromedriver.exe"
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
tagname = username.tag_name
username.send_keys("quang_quoc")
password = webdriver.find_element_by_name("password")
password.send_keys("quoc@12345")

button_loggin = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
button_loggin.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()

hashtag_list = ['tuicoi', 'depcoi']
prev_user_list = []
liked_user_list = []
#prev_user_list = pandas.read_csv('_users_followed_list.csv', delimiter=',')
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)    
    listRowTopPost = webdriver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div')
    for r in range(1, len(listRowTopPost) + 1):
        pathRow = '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[' + str(r) + ']/div'
        listItemInRow = webdriver.find_elements_by_xpath(pathRow)
        for itemIndex in range(1, len(listItemInRow) + 1):
            pathItem = pathRow + '[' + str(itemIndex) + ']/a/div'
            item = webdriver.find_element_by_xpath(pathItem)
            item.click()
            sleep(randint(1, 2))
            try:
                pathLikeButton = "//section[contains(@class,'EDfFK ygqzn')]//button[1]"
                pathSpanLikeButton = "//section[contains(@class,'EDfFK ygqzn')]//button[1]/span"
                elementSpanLikeButton = webdriver.find_element_by_xpath(pathSpanLikeButton)
                numberOfUsersLiked = elementSpanLikeButton.text
                elementLikeButton = webdriver.find_element_by_xpath(pathLikeButton)               
                elementLikeButton.click()
                likedUsers_Xpath = "//body/div[contains(@class,'')]/div[contains(@class,'')]/div[contains(@class,'')]/div/div/div"
                likedUsers_Elements = webdriver.find_elements_by_xpath(likedUsers_Xpath)
                for likedUserIndex in range(1, int(numberOfUsersLiked) + 1):
                    try:
                        userNamePath = "//body//div[contains(@class,'')]//div[contains(@class,'')]//div[contains(@class,'')]//div["+ str(likedUserIndex) +"]//div[2]//div[1]//div[1]//a[1]"
                        userNameElement = webdriver.find_element_by_xpath(userNamePath)
                        userName = userNameElement.get_attribute("title")
                        liked_user_list.append(userName)
                        sleep(randint(1, 2))
                    except:
                        continue
                sleep(randint(1, 2))
                pathCloseLike = "//button[contains(@class,'wpO6b')]//*[contains(@class,'_8-yf5')]"
                closeLikeButton = webdriver.find_element_by_xpath(pathCloseLike)
                closeLikeButton.click()
                sleep(randint(1, 2))
                pathClose = '/html/body/div[3]/button[1]'
                closeButton = webdriver.find_element_by_xpath(pathClose)
                closeButton.click()
                sleep(randint(1, 2))
                #likenumber = elementLikeButton
            except:
                pathClose = '/html/body/div[3]/button[1]'
                closeButton = webdriver.find_element_by_xpath(pathClose)
                closeButton.click()
                sleep(randint(1, 2))
                continue



    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]')
    first_thumbnail.click()
    sleep(randint(1, 2))
    try:
        for x in range(1, 200):
            username = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            if username not in prev_user_list:
                webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                new_followed.append(username)
                followed += 1

                #liking the picture
                button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                button_like.click()
                likes += 1
                sleep(randint(18,25))

                #comments and tracker
                comm_prob = randint(1, 10)
                print('{}_{}: {}'.format(hashtag, x, comm_prob))
                if comm_prob > 7:
                    comments += 1
                    webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                    comment_box = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                    if (comm_prob < 7):
                        comment_box.send_keys('Really cool!')
                        sleep(1)
                    elif  (comm_prob > 6) and (comm_prob < 9):
                        comment_box.send_keys('Nice work :)')
                        sleep(1)
                    elif comm_prob == 9:
                        comment_box.send_keys('Nice')
                    elif comm_prob == 10:
                        comment_box.send_keys('So cool! :)')
                        sleep(1)
                    comment_box.send_keys(Keys.ENTER)
                    sleep(randint(22,28))
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(25, 29))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(20,26))
    except:
        continue

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

updateUserdf = pandas.DataFrame(prev_user_list)
updateUserdf.to_csv(strftime("%Y%m%d-%H%M%S") + "__users_followed_list.csv")
