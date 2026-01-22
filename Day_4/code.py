import json

def input_data():
    with open("app.py","r") as input_file:
        response = (input_file.readlines())
        #output_file(response)
        fun(response)
        print(type(response))

def fun(response):
    count = {
        "INFO":0,
        "ERROR":0,
        "WARNING":0
    }
    lst = response
    for l in lst:
        if "INFO" in l:
            count.update({"INFO":count["INFO"]+1})
        elif "ERROR" in l:
            count.update({"ERROR":count["ERROR"]+1})
        elif "WARNING" in l:
            count.update({"WARNING":count["WARNING"]+1})
        else:
            pass
    output_file(count)
    return count

def output_file(count):
    with open("Output_file.json","w+") as file:
        json.dump(count,file)

input_data()
#fun()