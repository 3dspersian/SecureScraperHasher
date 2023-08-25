from pwn import *
import requests
from bs4 import BeautifulSoup
import hashlib

context.log_level = 'debug'
url = 'http://157.245.37.125:30647'
cookies = {'PHPSESSID': '13kjomj7hrep7036lhodldcr26'}

response = requests.get(url, cookies=cookies)

while 'HTB' not in response.text:
    extracted = BeautifulSoup(response.text, features="lxml").h3.contents[0]
    debug('extracted: %s', extracted)

    hashed = hashlib.md5(extracted.encode()).hexdigest()
    debug('hash: %s', hashed)

    response = requests.post(url, data={'hash': hashed}, cookies=cookies)

extracted = BeautifulSoup(response.text, features="lxml").p.contents[0]
warn(extracted)
