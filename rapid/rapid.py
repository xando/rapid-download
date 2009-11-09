#!/usr/bin/python

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                     Version 2, December 2004

#  Copyright (C) 2009 xando
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#   0. You just DO WHAT THE FUCK YOU WANT TO. 

import pycurl
import re
import os
import urllib
import sys
from cStringIO import StringIO

COOKIE = 'cookie.txt'
VERBOSE = False

def login(login,password):
    curl = pycurl.Curl()
    curl.setopt(pycurl.VERBOSE, VERBOSE)
    curl.setopt(pycurl.COOKIEJAR, COOKIE)
    curl.setopt(pycurl.COOKIEFILE, COOKIE)
    curl.setopt(pycurl.POST, 1) 
    curl.setopt(pycurl.URL, "http://rapidshare.com/cgi-bin/premium.cgi")
    curl.setopt(pycurl.POSTFIELDS, urllib.urlencode( {'accountid' : login ,
                                                      'password' : password , 
                                                      'premiumlogin' : '1' 
                                                      }))
    buffer = StringIO()
    curl.setopt(curl.WRITEFUNCTION, buffer.write)
    curl.perform()
    curl.close()

def logout():
    os.remove(COOKIE)

def get_file(link,login,passwd):
    print link
    file = re.search('/files/.+/.*',link).group(0).strip('/').split('/')
    
    fileid = file[1]
    filename = file[2]
    
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, link)
    curl.setopt(pycurl.FOLLOWLOCATION, True)
    curl.setopt(pycurl.COOKIEJAR, COOKIE)
    curl.setopt(pycurl.COOKIEFILE, COOKIE)
    curl.setopt(pycurl.POSTFIELDS, urllib.urlencode( {'l' : login ,
                                                      'p' : passwd }))
    
    buffer = StringIO()
    curl.setopt(curl.WRITEFUNCTION, buffer.write)
    curl.perform()
    curl.close()

    file = open(filename, 'w')
    file.write(buffer.getvalue())
    file.close()
    print "DONE"
    
def main():
    
    if len(sys.argv) is not 4:
        print "Usage:\n\trapid userid password filelist"
        sys.exit()
    
    user = sys.argv[1]
    password = sys.argv[2]
    file = open(sys.argv[3], 'r')
    login(user , password)    
        
    try:
        line = file.readline().strip('\n')
        while line:
            get_file(line,user,password)
            line = file.readline().strip('\n')
    finally:
        logout()

if __name__ == "__main__":
    main()
