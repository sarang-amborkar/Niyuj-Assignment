print('hello world') # valid python 2 not in python 3
print ('hello world') # valid python 3 and later versions of python 2


print((5 / 2)) # in python 2 result is 2 in python 3 result is 2.5




import urllib.request, urllib.error, urllib.parse

try:
    x = urllib.request.urlopen("http://pythonprogramming.net").read()
    print(x)
except Exception as e:
    print(str(e))


