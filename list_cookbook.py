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


# Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    in_total = {}
    for dish in dishes:
        if dish in cook_book:
            for prod in cook_book[dish]:
                if prod['ingredient_name'] in in_total:
                    in_total[prod['ingredient_name']]['quantity'] += prod['quantity'] * person_count
                else:
                    in_total[prod['ingredient_name']] = {'measure': prod['measure'],'quantity': (int(prod['quantity']) * person_count)}
            else:
                print(in_total)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



# Задание №3
shatered_file ={}
sum_line = {}
with open('1.txt', 'rt', encoding='utf-8') as file_1:
    sum_line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        sum_line_1['file_1'] = count_1
        print()

with open('2.txt', 'rt',  encoding='utf-8') as file_2:
    sum_line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        sum_line_2['file_2'] = count_2
   

with open('3.txt','rt',  encoding='utf-8') as file_3:
    sum_line_3 = {}
    count_3 = 0
    for line in file_3.readlines():
        count_3 += 1
        sum_line_3['file_3'] = count_3
    
    sum_line = zip(sum_line_1, sum_line_2, sum_line_3)
    
    dicts = [sum_line_1, sum_line_2, sum_line_3]
    shatered_file = {}
    for dict in dicts:
        shatered_file.update(dict)
    shatered_file_sorted = sorted(shatered_file.items(), key=lambda item: item[1])   
    print(shatered_file_sorted)
       
with open('shared_file.txt', 'w') as fp:
    fp.write('\n'.join('%s %s' % x for x in shatered_file_sorted))


    
