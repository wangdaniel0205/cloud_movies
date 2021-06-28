import urllib.request
import json

def save_jpg(url, file_name):
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}
    request_=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request_)# store the response
    #create a new file and write the image
    f = open('img/{}.jpg'.format(file_name),'wb')
    f.write(response.read())
    f.close()

with open('items.json') as f:
    items = json.load(f)



if __name__ == '__main__':
    for item in items:
        save_jpg(item['image_src'], item['id'])
