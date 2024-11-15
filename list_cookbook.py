

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



with open('1.txt', 'rt', encoding='utf-8') as file_1:
    shared_file = []
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['file_1'] = count_1
        shared_file.append(line_1)
    #print(line_1)

with open('2.txt', 'rt', encoding='utf-8') as file_1:
    line_2 = {}
    count_2 = 0
    for line in file_1.readlines():
        count_2 += 1
        line_2['file_2'] = count_2
        shared_file.append(line_2)
    #print(line_2)

with open('3.txt', 'rt', encoding='utf-8') as file_1:
    line_3 = {}
    count_3 = 0
    for line in file_1.readlines():
        count_3 += 1
        line_3['file_3'] = count_3
        shared_file.append(line_3)
    #print(line_3)

sum_line = zip(line_1, line_2, line_3)
print(shared_file)
    


    





 
    
