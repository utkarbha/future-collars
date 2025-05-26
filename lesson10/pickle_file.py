import pickle


warehouse = {
    "bike": {
    "price": 1000,
    "quantity": 4
},
    "computer" : {
    "price": 2000,
    "quantity": 14
},
    "bag" : {
    "price": 5000,
    "quantity": 40
}
}

with open("example", "wb") as file_stream:
    data_as_pickle = pickle.dumps(warehouse)
    # print(data_as_pickle)
    file_stream.write(data_as_pickle)



with open("example", "rb") as file_stream:
    data = pickle.load(file_stream)
print(data)