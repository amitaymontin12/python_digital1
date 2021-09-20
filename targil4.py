#dictionary
my_dict={"www.google.co.il":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["5.5.5.5","6.6.6.6"]}
print(my_dict)
my_dict.update({"www.booking.com":"6.6.6.6","www.shrink.com":"6.6.3.6"})
print(my_dict)
my_dict["www.google.com"]="8.8.9.6"
print(my_dict["www.google.com"])
my_dict["www.facebook.com"]="192.168.2.1"
print(my_dict["www.facebook.com"])
print(my_dict.values())
print("8.8.9.6" in my_dict.values())
