from bs4 import BeautifulSoup
import requests

#news
url = [
    'https://www.theguardian.com/football/2022/feb/10/chelsea-braced-for-kepa-arrizabalaga-bids-and-open-to-summer-exit',
    
]

# cnn
# url = 'https://edition.cnn.com/2022/02/10/politics/donald-trump-gop-incumbents-impeach-votes/index.html' 

# bbc
# url ='https://www.bbc.com/news/av/60334905'

#ratopati
# url ='https://www.ratopati.com/story/220582/2022/2/10/congress'

#kathmandu post ----> error occured
# url = 'https://kathmandupost.com/national/2022/02/10/will-people-from-kalapani-region-get-to-exercise-their-franchise'

#nepalnews -----> yesma paragraph lina sakena ----> didnt catch the p tag
# url = 'https://nepalnews.com.np/s/nation/mohp-records-1-369-new-covid-cases-12-deaths-on-thursday'

#online khabar
# url = 'https://www.onlinekhabar.com/2022/02/1077033'

#nytimes
# url = 'https://www.nytimes.com/2022/02/10/us/politics/jan-6-trump-calls.html'

#foxnews
# url = 'https://www.foxnews.com/politics/democrats-scramble-reverse-course-covid-restrictions-midterms'

#nbcnews ----> error occured
# url = 'https://www.nbcnews.com/news/world/u-s-intel-nine-probable-russian-routes-ukraine-full-scale-n1288922'

#gaurdians news
# url = 'https://www.theguardian.com/football/2022/feb/10/chelsea-braced-for-kepa-arrizabalaga-bids-and-open-to-summer-exit'

#abc news
# url = 'https://abcnews.go.com/Politics/pressure-builds-biden-democrats-move-past-covid/story?id=82754983'

# url = 'https://edition.cnn.com/2022/02/10/politics/biden-ukraine-things-could-crazy/index.html'


def getUrl(url): #get the response 
    pageContent = requests.get(url)
    print(pageContent)
    return pageContent

def parse(pagecontent):
    data = []
    if pagecontent.status_code != 200: #beside response 200 for all response show page not found
        print('Page not found')
        return 0
    coup = BeautifulSoup(pagecontent.content, 'html.parser') #Parse the content using bs4
    try:
        if coup.find('article') is not None: #if news article is in article tag
            print('article')
            contentParse = coup.find('article')

        

        elif coup.find('div') is not None: #if news article is in div tag
            print("div")
            #searching for the right div is left here
            contentParses = coup.find_all('div')
            # print(len(contentParses))
        
            flag = 0
            for contentParse in contentParses:
                if contentParse.find('h1') is not None:
                    headline = contentParse.find('h1').text
                    # print(f'Title: {headline}')
                    break
                flag +=1
            count = 0
            newsArticles = contentParses[flag].find_all('p')
            for newsArticle in newsArticles:
                if count == 5:
                    break
                # print(newsArticle.text, end=' ')
                data.append(newsArticle.text)
                count +=1
            data.insert(0, headline)
            data = ' '.join(data)
            dictt = {
            # 'title': headline,
            'article': data
        }
            print(dictt)
            return dictt # to process only the article which is in div tag
        else:
            errormessage = 'No content found'
            print(errormessage)
        
    
# to process the article which is in article tag
        headline = contentParse.find('h1').text
        # print(f"Title: {headline}")

        newsArticles = contentParse.find_all('p')
    # print(len(newsArticles))

        for newsArticle in newsArticles:
            # print(newsArticle.text, end=' ')
            data.append(newsArticle.text)
        # dictt = {
        #     'title': headline,
        #     'article': data
        # }
        data.insert(0, headline)
        data = ' '.join(data)
        dictt = {
            'title': headline,
            'content': data
        }

        print(dictt)
        return dictt

    except: #any error occured during the process 
        print("Error Occured")

import csv
fieldnames = ['title','content']
with open('news.csv', 'a', newline='') as csv_file:
    
    # csv_writer = csv.writer(csv_file)
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # csv_writer.writeheader()   #---> for setting up the header for the csv file &&&& also uncomment this line after first execution of the script
    for lin in url:
        news = parse(getUrl(lin))
    # print()
    # print('printing for csv file: {}'.format(news['title']))
    # print()
    # print('printing for csv file: {}'.format(news['content']))
        csv_writer.writerow(news)
