#http请求工具

from urllib import parse
import urllib.request

def doGet(url,headers = {}):
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html