import requests
import json

def input_url():
    url = "https://api.artic.edu/api/v1/artworks?limit=5" #API containing the data of some artistic structure.
    try:
        response = requests.get(url=url)
        data = response.json()["data"]
        fun(data)
        #print(data)
    except KeyError:
        print("Unexpected API Error Detected!")
    except requests.exceptions.RequestException:
        print("Unable to fetch data from the API!")

def fun(data):
    lst = []
    for i in data:
        for key,value in i.items():
            if key == "title":
                lst.append(value)
                print(value)
    print(lst)
    output_file(lst)

def output_file(lst):
    try:
        with open("Output_json.json","w+") as Output_File:
            json.dump(lst,Output_File)
    except IOError:
        print("ERROR:File Not Found!")
input_url()