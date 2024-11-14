# Задание №1
def dickt_form(dict_):
    for item_a in dict_:
        print (item_a,':')
        for item_b in dict_[item_a]:
            print (item_b)

with open('Receipt.txt', encoding='utf-8') as file:
    cook_book = {}
    for item in file:
        receipt = item.strip() 
        count = file.readline()
        products = []
        for prod in range(int(count)):
            rec = file.readline().strip().split('|')
            product, quantity, name = rec
            products.append({'ingredient_name': product, 'quantity': int(quantity), 'measure': name})
            cook_book[receipt] = products
        file.readline()
    dickt_form(cook_book)

#Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    in_total = {}
    for dish in dishes:
        if dish in cook_book:
            for count in cook_book[dish]:
                if count['ingredient_name'] in in_total:
                    in_total[count['ingredient_name']]['quantity'] += count['quantity'] * person_count
                else:
                    in_total[count['ingredient_name']] = {'measure': count['measure'],'quantity': (int(quantity) * person_count)}
        else:
            print('Такого блюда нет в книге')
            print(in_total)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


#Задание №3





 
    
