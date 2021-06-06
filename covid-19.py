import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "3dadbc7c58msh37667a52e98f576p19efe9jsnfbd8ec27d80b",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()
def search_by_city(city_name):
    for each in response['state_wise']:
        if int(response['state_wise'][each]['active']) != 0:
            for city in response['state_wise'][each]['district']:
                if city.lower() == city_name.lower():
                   return response['state_wise'][each]['district'][city]['active']

flag = 1
while flag != 0:
    city_name = input("Enter the city: ")
    if city_name == "0":
        break
    cases = search_by_city(city_name)
    print("Total numbers of cases in "+city_name+" is: ",cases)