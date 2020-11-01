from urllib import request
#import urllib
#import urllib.request
try:
    #site = request.urlopen('https://www.netflix.com/browse')
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('deu erro arrombado')
else:
    print('funfou legal')
    print(site.read())
