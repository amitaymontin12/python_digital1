details_list=["amitay montin",28,"amitymon128@gmail.com",'0549087167']
print("Full name: " + details_list[0] + "\nAge: " + str(details_list[1]) + "\nMail: " + details_list[2] + "\nPhone: " + details_list[3])
ip_list=["192.168.1.1 , 195.168.5.4"]
print(ip_list)
ip_list.append("192.168.1.2")
ip_list.append("192.168.8.5")
ip_list.append("192.168.3.6")
print(ip_list)
ip_list.pop(2)
print("Ip list length is: " + str(len(ip_list)) + "\nAnd the IP list: " + str(ip_list))
