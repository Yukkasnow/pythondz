from requests import get, utils
def currency_rates(char_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_dict = {}
    for code in content.split('</Value>'):
        i = code.split('</CharCode>')[0][-3:]
        # print(i)
        # print(code[-7:])
        currency_dict[i] = code[-7:]
    char_code = char_code.upper()
    if currency_dict.setdefault(char_code) == None:
        print('Код валюты введен неверно')
    else:
        price = currency_dict[char_code]
        print(f'{char_code} = {price}')

currency_rates(input('Введите код валюты '))
