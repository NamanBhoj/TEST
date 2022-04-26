import json


def read_json(data):

    f = open (data, "r")
    #read and save data in datas
    datas = json.loads(f.read())
    return(datas)




def add_json(json_file,data=None,number_times=None): #number times will be value of filecenter.json

    json_data = read_json(json_file)

    current_len = len(json_data['Unnamed: 0'])
    print(current_len) #start from this it will be new index


    
# print(read_json(r'W:\TEST\test.json'))
add_json(r'W:\TEST\test.json',[1,2,3,4],30)