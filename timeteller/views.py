from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import requests
import bs4


def home(request):
    # #d={ 'name': 'Ranjan'}
    # names=['Ranjan','Bikalpa','biplove']
    # d={'names':names}
    # return render(request, 'index.html', d)
    # #return HttpResponse('Greetings. Welcome to the time machine.')


    page= requests.get('https://fabpedigree.com/james/mathmen.htm#top')
    soup= bs4.BeautifulSoup(page.content, 'html.parser')

    names = [li.find('a').string for li in soup.find_all('li')]
    #b= [li.find('small').string for a in soup.find_all['a']
    #names=soup.find_all(li.find('a').string)
    d={ 'names': names}
    return render(request, 'index.html', d)
# print('THE LIST OF TOP 100 MATHEMATICIAN OF ALL TIME:')

# for li in lis:
#     print(li.find('a').string)
def today(request):
    date = datetime.date.today()
    return HttpResponse("Today's date is: {}".format(date))


def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))
