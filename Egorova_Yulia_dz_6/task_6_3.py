from itertools import zip_longest

with open('users.csv','r',encoding='utf-8') as name, open('hobby.csv','r',encoding='utf-8') as hobby:
    names=name.read().splitlines()
    hobbies=hobby.read().splitlines()

result=((names,hobbies) for names,hobbies in zip_longest(names,hobbies, fillvalue=None))

with open('result.txt','w') as file:
    for user_hobby in result:
        file.write(f'{user_hobby[0]}: {user_hobby[1]}\n')