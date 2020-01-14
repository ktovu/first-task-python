# -*- coding: utf-8 -*-

def create_list_dict(list):
    products = []
    for i in range(len(list)):
        stringText = list[i].split(' *')
        products.append({
            'product': stringText[0],
            'provider': stringText[1],
            'measure': stringText[2],
            'price': float(stringText[3]),
            'count': int(stringText[4])
        })
        products[i].update({'total_value': float(products[i]['price'] * products[i]['count'])})
    return products

def show_on_screen(products):
    colums = len(products[0])
    print('==========================================================================================')
    print('Товар                Поставщик         Ед. измерения     Цена       Кол-во       Стоимость')
    print('==========================================================================================')
    for i in range(len(products)):
        print('{product:20} {provider:22} {measure:11} {price} {count:9} {total_value:17}'.format(
            **products[i]))


def sort_by_provider(prod,k=0):
    for i in range(len(prod)):
        for j in range(len(prod) - 1):
            if (prod[i]['provider'] > prod[j + 1]['provider'] and k == 0):  # по возрастанию
                prod[i], prod[j] = prod[j], prod[i]
            if (prod[i]['provider'] < prod[j + 1]['provider'] and k == 1):  # по убыванию
                prod[i], prod[j] = prod[j], prod[i]


def total_sum(product):
    sum = 0
    for i in range(len(product)):
        sum += product[i]['total_value']
    return sum

def sum_by_provider(product, list):
    sum = 0
    for i in range(len(product)):
        if list ==product[i]['provider']:
            sum += product[i]['total_value']
    return sum


f = open('file.txt', 'r', encoding='utf-8') # открываем файл для получения данных
list = f.readlines() # записываем все строки в список
f.close() # закрываем файл

products = create_list_dict(list) # вызываем функцию create_lis_dict() для создания списка словарей
sort_by_provider(products, 1) #сортируем
show_on_screen(products)
print('\nИтоговая сумма')
print('==============')
print(str(total_sum(products)) + '\n')


providers = []
providers.append(products[0]['provider'])
temp = products[0]['provider']

for i in range(1, len(products)):
    if temp != products[i]['provider']:
        temp = products[i]['provider']
        providers.append(products[i]['provider'])

f = open('new_file.txt', 'w', encoding='utf-8')
for i in range(len(providers)):
    print(str(providers[i]) + '\n==============\n' + str(sum_by_provider(products, providers[i]))+'\n')
    f.write(str(providers[i]) + ' ' + str(sum_by_provider(products, providers[i]))+'\n')

f.close()
