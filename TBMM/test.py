#-*- coding: utf-8 -*-
import urllib
u  = urllib.urlopen('img.alicdn.com/imgextra/i3/687471686/TB1Sm49MXXXXXaCXVXXXXXXXXXX_!!0-tstar.jpg')
data  = u.read()
f = open('admin.jpg', 'wb')
f.write(data)
f.close()
