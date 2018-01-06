import requests

file_urls="http://www.7-zip.org/a/7z1604-x64.exe"




request=requests.get(file_urls,stream=True)
with open("7z1604-x64.exe","wb") as zs:
    for chunk in request.iter_content(chunk_size=1024):
        if chunk:
            zs.write(chunk)