from time import sleep
import datetime
print("Now the program will show date and time......")
sleep(3)
x=datetime.datetime.now()
print(x)
print("\nNow the program will show list and changed list....")
sleep(3)
list=['red','green','white','black','pink','yellow']
print(list)
print("\nNow will be a changes in the list........")
sleep(3)
list.pop(5)
list.pop(4)
list.pop(0)
print(list)

