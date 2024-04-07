PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_price_list = [item.split() for item in PRICE_LIST.split('\n')]
dict_price_list = dict((k, int(v.replace('р', ''))) for k, v in list_price_list)
print(dict_price_list)
