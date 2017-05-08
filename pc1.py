#!/user/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
a = response.read()
print(a)
fileObjec = open('./baidu.html','wb')
fileObjec .write(a)
fileObjec.close()