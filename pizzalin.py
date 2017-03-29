from math import pi

pizza_d=float()
pizza_price=float()
pizza_parameter=float()
pizza_name=str()
pizza_list=[['Ziemniaczana', 20, 12, 10], ['Margarita', 50, 35, 56.1]]      # added two positions to memory so I wont have to do it each time I test it


def pizza_calc(pizza_d,pizza_price):                        # function takes diameter and price as arguments
    area=pi*(pizza_d/2)**2
    area_price=round(area/pizza_price,2)
    print(str(area_price) + ' cm2/zl pizzy')
    return area_price                                       # and return parameter area/price


def input_diameter():
    global pizza_d
    check = False
    while check == False:
        pizza_d = float(input('Wprowadz srednice pizzy [cm]:'))
        if pizza_d > 100:
            print('Zjadlbys tyle?')
            check = False
        elif pizza_d < 10:
            print('Troche mala')
            check = False
        else:
            check = True
    return pizza_d


def input_price():
    global pizza_price
    check = False
    while check == False:
        pizza_price = float(input('Wprowadz cene pizzy [zl]:'))
        if pizza_price > 200:
            print('Nie za drogo?')
            check = False
        elif pizza_price < 5:
            print('Jakos tanio')
            check = False
        else:
            check = True
    return pizza_price


def save():
    check = False
    while check == False:
        ans2 = input('Czy chcesz zapisac? (y/n)')
        if ans2.upper() == 'Y' or ans2.upper() == 'YES':
            name = str(input('Podaj nazwe:'))
            name = name[0].upper() + name[1:]
            pizza_list.append([name, pizza_d, pizza_price, pizza_parameter])
            print('Zapisana pod nazwą %s' % name)
            check = True
        elif ans2.upper() == 'N' or ans2.upper() == 'NO':
            check = True
        else:
            print('Odpowiedź nierozpoznana')
            check = False


def new_pizza():
    global pizza_parameter
    input_diameter()
    input_price()
    pizza_parameter = pizza_calc(pizza_d,pizza_price)
    return pizza_parameter


def pizza_memory():
    for each_pizza in pizza_list:
        first_pos = each_pizza[0]
        sec_pos = each_pizza[1]
        third_pos = each_pizza[2]
        fourth_pos = each_pizza[3]
        print('\n')
        print(
            'Nazwa: %s' % first_pos + '\nŚrednica: %s cm' % sec_pos + '\nCena: %s zł' % third_pos + '\nParametr pizzy: %s cm2/zł' % fourth_pos)


def pizza_sort():
    check = False
    while check == False:
        if ans2.upper() == 'ALPHABET' or ans2.upper() == 'A' or ans2.upper == '"ALPHABET"':
            pizza_list.sort(key=lambda one_pizza: one_pizza[0])
            pizza_memory()
            check = True

        elif ans2.upper() == 'DIAMETER' or ans2.upper() == 'D' or ans2.upper == '"DIAMETER"':
            pizza_list.sort(key=lambda one_pizza: one_pizza[1], reverse=True)
            pizza_memory()
            check = True

        elif ans2.upper() == 'PRICE' or ans2.upper() == 'P' or ans2.upper == '"PRICE"':
            pizza_list.sort(key=lambda one_pizza: one_pizza[2])
            pizza_memory()
            check = True

        elif ans2.upper() == 'DEAL' or ans2.upper() == '$' or ans2.upper == '"DEAL"':
            pizza_list.sort(key=lambda one_pizza: one_pizza[3], reverse=True)
            pizza_memory()
            check = True
        else:
            print('Odpowiedź nierozpoznana')
            check = False


print('Dzien dobry!')                                                    # program start

program_stop = False

while program_stop == False:
    ans1 = input('\nAby obliczyc parametr pizzowy, wpisz "New"\nŻeby wyświetlić zapisane, wpisz "Memory"\nAby posortowac wybrane pizze, wpisz "Sort"\nJeśli chcesz wyjść, wpisz "Exit"' )

    if ans1.upper() == 'NEW' or ans1.upper() == 'N' or ans1.upper=='"NEW"':
        new_pizza()
        save()

    elif ans1.upper() =='MEMORY' or ans1.upper() == 'M' or ans1.upper() == '"MEMORY"':
        pizza_memory()

    elif ans1.upper() == 'SORT' or ans1.upper() == 'S' or ans1.upper() == '"SORT"':
        ans2 = input('\nAby posortować alfabetycznie wpisz "Alphabet"\nŻeby wyświetlić wg największej średnicy wpisz "Diameter"\nBy posortować wg najniższej ceny wpisz "Price"\nŻeby posortować wg opłacalności wpisz "Deal"')
        pizza_sort()
    elif ans1.upper() == 'EXIT' or ans1.upper() == 'E' or ans1.upper() == '"EXIT"':
        program_stop= True

    else:
        print('Odpowiedz nierozpoznana')

