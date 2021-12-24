import re
def email_parse(email):

    re_email=re.compile(r'[^@]*')
    txt=email
    result=re_email.findall(txt)
    if result[2].find('.')==-1:
        warning='Error'
        return warning
    res_dict={'username': result[0], 'domain': result[2]}
    return res_dict

print(email_parse('yulia2000_egorova@yandex.ru'))