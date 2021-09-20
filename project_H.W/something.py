import datetime
current_date=datetime.date.today().strftime('%y-%m-%d')
current_date_lst = current_date.split('-')

b_date=input('Enter birthday in yyy-mm-dd format:')
name=input('\nName of birthday legend?')
b_date=b_date.split('-')

if current_date_lst[1] == b_date[1] and current_date_lst[2] == b_date[2]:
    age=int(current_date_lst[0]) - int(b_date[0])
    ordinal_suffix= {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
    print(f" It's {name}'s {age}{ordinal_suffix} Birthday")
else:
    print("sorry, today isnt your birthday")


