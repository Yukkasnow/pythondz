my_list_1=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list_2=[]
for element in my_list_1:
    if element.isdigit() ==True and int(element)<10 :
        my_list_2.append('"')
        element = f'0{element}'
        my_list_2.append(element)
        my_list_2.append('"')
    elif element[0]=='+':
        my_list_2.append('"')
        element = f'+0{element[-1]}'
        my_list_2.append(element)
        my_list_2.append('"')

    elif element.isdigit() ==True :
        my_list_2.append('"')
        my_list_2.append(element)
        my_list_2.append('"')
    else:
        my_list_2.append(element)
print(my_list_2)
message=' '.join(my_list_2)
print(message)