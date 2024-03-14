import requests
resp = requests.get('https://youtube.com')
resp.raise_for_status()
print(resp.text)
ourFile= open('google.html','wb')
for data in resp.iter_content(1000):
    ourFile.write(data)
