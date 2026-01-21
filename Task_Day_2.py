import requests
import json
def main():
    url = "https://api.artic.edu/api/v1/artworks?limit=5"
    response = requests.get(url=url)
    # print(type(response.json()))
    # print(response.json().keys())
    # print(response.json().values())

    data = response.json()["data"]
    info = response.json()["info"]
    # for i in data:
    #     print(i)
    print(type(data))

    lst = []
    for i in data:
        for key,value in i.items():
            if key == "title":
                lst.append(value)
                print(value)
    print(lst)

    # count=0
    # for i in data:
    #     if(i.keys()):
    #         count = count+1
    #         print(i.keys())
    #         print(count)

    with open("Output_file.json","w+") as json_file:
        json.dump(lst,json_file)

main()