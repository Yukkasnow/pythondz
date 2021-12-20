with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    request_list=[]
    for line in file:
        adress= line[:line.find(' ')]
        request_type=line[line.find('"')+1:line.find('/d')-1]
        request_resourse=line[line.find('/d'):line.find('HTTP')-1]
        result=(adress, request_type, request_resourse)
        request_list.append(result)
    print(request_list)