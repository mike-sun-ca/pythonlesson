import urllib.request
with urllib.request.urlopen("https://www.python.org", data=None, cafile=None, capath=None, cadefault=False, context=None) as response:
    print(response.read())

