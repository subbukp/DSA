import requests

response = requests.get('https://brightdata.com/blog/web-data/python-requests-guide')
print(dir(response))
print(response.status_code)
print(response.headers)
print(response.text)
#print(response.json())
print(response.content)
print(response.url)
print(response.history)
#print(type(response))
#print(help(response))
