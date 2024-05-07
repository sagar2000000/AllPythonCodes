#request method 

import requests


response=requests.get("https://www.codewithharry.com/")

print(response.text)