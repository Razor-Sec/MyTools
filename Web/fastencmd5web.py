import requests, hashlib
from bs4 import BeautifulSoup

url = "http://" # put link
#proccesing
sesi = requests.session()
response = sesi.get(url)
soup = BeautifulSoup(response.content, "lxml")

str = soup.h3.string  # detecting
hashing = hashlib.md5(str.encode()).hexdigest() #hashing
 
myobj = {'hash' : hashing}
#cheking
flag = sesi.post(url, data = myobj)
print(flag.text)
print(str,hashing,myobj)
