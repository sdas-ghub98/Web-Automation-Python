import time,sys,getopt
from robobrowser import RoboBrowser
import re
from bs4 import BeautifulSoup

url = ''
username = ''
password = ''
argv = sys.argv[1:]

try:
    opts,args = getopt.getopt(argv,"u:l:p:",["url=","username=","password="])
except getopt.GetoptError:
    print('dvwa_selenium.py -url <Login URL> -l <username> -p <password>')
    sys.exit(2)
for opt,arg in opts:
    if(opt == '-h'):
        print('dvwa_selenium.py -url <Login URL> -l <username> -p <password>')
        sys.exit(2)
    elif opt in("-u","--url"):
        url=arg
    elif opt in("-l","--login"):
        username=arg
    elif opt in("-p","--password"):
        password=arg


if(url==''):
    print('URL has not been entered!')
    sys.exit()
if(username==''):
    print('Username has not been entered!')
    sys.exit()
if(password==''):
    print('Password has not been entered!')
    sys.exit()

br = RoboBrowser()
br.open(url)
form = br.get_form()
form['username']=username
form['password']=password
br.submit_form(form)

src = str(br.parsed())
soup = BeautifulSoup(src,'html.parser')
message = soup.find("div",class_="message")
print(message.text)