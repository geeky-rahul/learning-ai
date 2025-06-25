import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()
    # print(response)
    
    if data["success"] and "data" in data:
        user_list = data["data"]["data"]
        for i in user_list:
            username = user_list[int(i)]["login"]["username"]
            country = user_list[int(i)]["location"]["country"]
        return username, country
    else:
        raise Exception("failed to fetch user data")
        
def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"Username: {username}  \ncountry: {country}")
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()





