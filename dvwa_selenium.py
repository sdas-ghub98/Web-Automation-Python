import time,sys,getopt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless=True
driver = webdriver.Firefox(options=options, executable_path='/root/Documents/Web_Automation/geckodriver')

url = ''
username = ''
password = ''
argv = sys.argv[1:]

try:
    opts,args = getopt.getopt(argv,"u:l:p:",["url=","username=","password="])
except getopt.GetoptError:
    print('dvwa_selenium.py -url <Login URL> -l <username> -p <password>')
    sys.exit(2)
# print(opts)
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

# print('URL = ',url)
# print('Username = ',username)
# print('Password = ',password)

if(url==''):
    print('URL has not been entered!')
    sys.exit()
if(username==''):
    print('Username has not been entered!')
    sys.exit()
if(password==''):
    print('Password has not been entered!')
    sys.exit()

driver.get(url)
a = driver.find_element_by_name('username')
a.send_keys(username)

a = driver.find_element_by_name('password')
a.send_keys(password)

driver.find_element_by_name('Login').click()

time.sleep(2)
message = driver.find_element_by_xpath('//div[@class="message"]').text

print(message)
driver.quit()
