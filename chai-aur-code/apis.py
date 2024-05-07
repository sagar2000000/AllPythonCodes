import requests
def fetch_random_user():
  url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
  response=requests.get(url)
  wholedata=response.json()
  if "data" in wholedata:
    user_data=wholedata["data"]
    user_name=user_data["login"]["username"]
    country=user_data["location"]["country"]
    return user_name,country
  else:
     raise Exception("failed to fetch userddata")

def main():
   try:
       username,country=fetch_random_user() 
       print(f"username:{username}\n country:{country}")  
   except Exception as e:
       print(str(e)) 


if __name__=="__main__":
    main()
 