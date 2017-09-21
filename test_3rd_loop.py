from forex_python.converter import CurrencyRates


c = CurrencyRates()
list = ['USD', 'EUR', 'JPY', 'CHF', 'GBP', 'AUD', 'CAD']

user_choice = list[0]



r1 = 0
r3 = 0
r5 = 0

v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0

loop_num_1 = 0
loop_num_2 = 0
loop_num_3 = 0
loop_num_4 = 0


for loop_1 in list[0:]:
    loop_num_1 = loop_1
    if user_choice != loop_1:
        try:
            v1 = c.get_rate(user_choice, loop_1)
        except Exception:
            print('')
        for loop_2 in list[0:]:
            loop_num_2 = loop_2
            if user_choice != loop_2:
                if loop_1 != loop_2:
                    try:
                        v2 = c.get_rate(loop_1, loop_2)
                        if loop_2 != user_choice:
                            v3 = c.get_rate(loop_2, user_choice)
                            r1 = v1 * v2
                            r2 = r1 * v3
                            if r2 > 1.00001:
                                #print(user_choice, loop_1,'->',v1, loop_2,user_choice, r2)

                                print(user_choice, loop_1, '->', v1 ,loop_1, loop_2, '->', v2 ,loop_2, user_choice,'->', v3 , "-----------------------------------------  =  %0.5f" % r2)

                    except Exception:
                        print("")

                    for loop_3 in list[0:]:
                        loop_num_3 = loop_3
                        if user_choice != loop_3:
                            if loop_num_1 != loop_3:
                                if loop_num_2 != loop_3:
                                    try:
                                        v4 = c.get_rate(loop_2, loop_3)
                                        if loop_3 != user_choice:
                                            v5 = c.get_rate(loop_3, user_choice)
                                            r3 = v4 * v5
                                            r4 = r1 * r3
                                            if r4 > 1.00001:
                                                #print(user_choice, loop_1, loop_2,loop_3, user_choice, r4)
                                                print(user_choice, loop_1, '->', v1, loop_1, loop_2, '->', v2,
                                                      loop_2, loop_3, '->', v4,
                                                     loop_3, user_choice, '->', v5, "-------------------- =  %0.5f" % r4)

                                    except Exception:
                                        print("")




