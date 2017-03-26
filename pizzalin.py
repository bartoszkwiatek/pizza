from math import pi


def pizza_calc(d,price):                        # function takes diameter and price as arguments
    area=pi*(d/2)**2
    area_price=round(area/price,2)
    print(str(area_price) + ' cm2/zl pizzy')
    return area_price                           # and return parameter area/price

print('Dzien dobry!')
pizza_list=[['Ziemniaczana', 20, 12, 10], ['Margarita', 50, 35, 8]]      # added two positions to memory so I wont have to do it each time I test it
program_stop = False
while program_stop == False:
    ans1 = input('\nAby obliczyc parametr pizzowy, wpisz "New"\nŻeby wyświetlić zapisane, wpisz "Memory"\nAby porownac wybrane pizze, wpisz "Compare"\nJeśli chcesz wyjść, wpisz "Exit"' )
    if ans1.upper() == 'NEW' or ans1.upper() == 'N' or ans1.upper=='"NEW"':
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

        pizza_parameter = pizza_calc(pizza_d, pizza_price)
        check = False
        while check == False:
            ans2 = input('Czy chcesz zapisac? (y/n)')
            if ans2.upper() == 'Y' or ans2.upper() == 'YES':
                name = str(input('Podaj nazwe:'))
                pizza_list.append([name,pizza_d,pizza_price,pizza_parameter])
                print('Zapisana pod nazwą %s' % name)
                check = True
            elif ans2.upper() == 'N' or ans2.upper() == 'NO':
                check = True
            else:
                print('Odpowiedź nierozpoznana')
                check = False

    elif ans1.upper() =='MEMORY' or ans1.upper() == 'M' or ans1.upper() == '"MEMORY"':
        for each_pizza in pizza_list:
            first_pos = each_pizza[0]
            sec_pos = each_pizza[1]
            third_pos = each_pizza[2]
            fourth_pos = each_pizza[3]
            print('\n')
            print('Nazwa: %s' %first_pos + '\nŚrednica: %s cm' %sec_pos + '\nCena: %s zł' %third_pos + '\nParametr pizzy: %s cm2/zł' %fourth_pos)

    elif ans1.upper() == 'EXIT' or ans1.upper() == 'E' or ans1.upper() == '"EXIT"':
        program_stop= True

    else:
        print('Odpowiedz nierozpoznana')

