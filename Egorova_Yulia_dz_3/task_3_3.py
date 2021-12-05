def thesaurus(*name):
    names=[*name]
    dict_names={}
    for name in names:
        key=name[0]
        if key not in dict_names:
            dict_names[key]=[]
        dict_names[key].append(name)
    print(dict_names)

thesaurus('Max','Leo','Molly','Ivan')