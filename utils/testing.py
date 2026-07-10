from data_reader_util import read_json_data
data=read_json_data("testdata/logindata.json")
print(data)
print(type(data))
print(data[0][1])
email= data[0][2]
print(email)