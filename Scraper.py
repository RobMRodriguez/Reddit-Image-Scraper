#web scraping tool
# a good sample is http://www.reddit.com/user/stanislavsky

import urllib.request
import re
from os import mkdir
from time import sleep



def find_next_url(htmlCode):
    possibleButtonArray = [o.start() for o in re.finditer(username, htmlCode)]

    startIndex = possibleButtonArray[-1] #The last value is the next button

    terminatingCharacter = chr(34)
    
    while htmlCode[startIndex] != terminatingCharacter:       
        startIndex -= 1
        
    startIndex += 1 #To remove ' " '  
    endIndex = startIndex

    while htmlCode[endIndex] != terminatingCharacter:
        endIndex += 1

    return htmlCode[startIndex:endIndex]

def get_album_image_list(url):
    print("called album")
    try:
        htmlCode = get_html_code(url)
    except:
        return []
    pics = [n.start() for n in re.finditer("imgur.com/", htmlCode)]

    imageList = []
    terminatingCharacter = chr(34)

    for index in pics:
        end = index
        while htmlCode[end] != terminatingCharacter:
            end += 1
        if not "http://" + htmlCode[index:end] in imageList:
            imageList.append("http://" + htmlCode[index:end])
    return imageList


def get_image_list(htmlCode):
    pics = [n.start() for n in re.finditer("imgur.com/", htmlCode)]

    imageList = []
    terminatingCharacter = chr(34)

    for index in pics:
        end = index
        while htmlCode[end] != terminatingCharacter:
            end += 1
        if not "http://" + htmlCode[index:end] in imageList:
            imageList.append("http://" + htmlCode[index:end])
    print(imageList)
    for image in imageList:
        if chr(47) + 'a' + chr(47) in image:
            newList = get_album_image_list(image)
            for newImage in newList:
                if not newImage in imageList:
                    imageList.append(newImage)
                imageList.remove(newImage)
    return imageList




def get_html_code(url):
    try:
        websiteDump = urllib.request.urlopen(url)
    except:
        return False
    return websiteDump.read().decode('utf-8')










def main(username):
    currentUrl= "http://www.reddit.com/user/" + username +"/submitted"
    imageUrls = []

    try:
        
        while True:
            #this loop gathers all the image urls from the profile
            htmlCode = get_html_code(currentUrl)
            if not htmlCode:
                break
            
            canidateImages = get_image_list(htmlCode)
        
            for image in canidateImages:
                if not image in imageUrls:
                    imageUrls.append(image)
        
            currentUrl = find_next_url(htmlCode)
        
        
        imageFileIndex = 0
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
                file = open("C:/Images/" + username + "/" + username + str(imageFileIndex) + ".jpg", 'r')
                file.close
            except:
                break
            imageFileIndex += 1
        for image in imageUrls:
            if image[-4] == '.':
                file = open("C:/Images/" + username + "/" + username + str(imageFileIndex) + image[-4:], 'wb')
                try:
                    file.writelines(urllib.request.urlopen(image))
                    imageFileIndex += 1
                except:
                    print("lost an image", image)
                file.close()
        
    except:
        pass
