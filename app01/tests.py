# from django.test import TestCase

# Create your tests here.
import requests

# response_type = code &
# client_id = Va5yQRHlA4Fq4eR3LT0vuXV4 &
# redirect_uri = http % 3
# A % 2
# F % 2
# Fwww.example.com % 2
# Foauth_redirect &
# scope = email &
# display = popup

payload = {
    'response_type': 'code',
    'client_id': 'asejKO13L8RYtwwEZua6zw3E',
    'redirect_uri':'oob',

}

r = requests.get('https://openapi.baidu.com/oauth/2.0/authorize',params=payload)
print(r.status_code)
print(r.encoding)

html=r.content
html_doc=str(html,'utf-8')
with open('log.html','w') as f:
    f.write(html_doc)
# print(r.text)
# print(r.json())