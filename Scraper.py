#web scraping tool
# a good sample is http://www.reddit.com/user/stanislavsky

import urllib.request
import re
from os import mkdir
from time import sleep

username = input("What user would you like to download from?\n>>> ")

userurl= "http://www.reddit.com/user/" + username
page = 0
images = []
while True:
    try:
        text = urllib.request.urlopen(userurl)
        sleep(2)
        code = text.read().decode('utf-8')

        pics = [n.start() for n in re.finditer("i.imgur.com/", code)]


        for pic in pics:
            if code[pic + 22] == "g":
                if not code[pic:pic + 23] in images:
                    images.append(code[pic:pic + 23])

        

        nextarray = [o.start() for o in re.finditer("&amp;after", code)] #the last will be the one I want
        j = nextarray[-1]
        while code[j] != "\"":
            j -= 1
        k = j + 1
        while code[k] != "\"":
            k += 1
        userurl = code[j + 1:k]
        print(userurl)
        page += 1
    except:
        break

i = 0
while True:
    try:
        file = open("C:/Images/" + username + "/createfolder.uff", 'w')
        file.close
    except:
        try:
            mkdir("C:/Images/" + username)
        except:
            pass
    try:
        file = open("C:/Images/" + username + "/" + username + str(i) + ".jpg", 'r')
        file.close
    except:
        break
    i += 1
for image in images:
    picurl = "http://" + str(image)).read()
    file.write(urllib.request.urlopen(picurl)
    file = open("C:/Images/" + username + "/" + username + str(i) + ".jpg", 'wb')
    file.write(urllib.request.urlopen("http://" + str(image)).read())
    file.close()
    i += 1

print(images)
print("Success!")
sleep(3)
