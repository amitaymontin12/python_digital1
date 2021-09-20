dict_names={"dudu":25000,"dodi":63000,"avi":25000,"dan":30000,"amitay":36000}
print(dict_names)
summay=dict_names["dudu"]+dict_names["amitay"]
print("my summary is: " +str(summay))
dict_names.update({"yael":summay})
print(dict_names)
print("number of entries: " + str(len(dict_names)))
print("dudu" in dict_names)
