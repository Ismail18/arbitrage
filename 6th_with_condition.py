from forex_python.converter import CurrencyRates


c = CurrencyRates()
list = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD']


v1 = 0
v2 = 0
v4 = 0
v6 = 0

loop_num_1 = 0
loop_num_2 = 0
loop_num_3 = 0
loop_num_4 = 0

for user_choice in list[0:]:
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
                        except Exception:
                            print("")
                        for loop_3 in list[0:]:
                            loop_num_3 = loop_3
                            if user_choice != loop_3:
                                if loop_num_1 != loop_3:
                                    if loop_num_2 != loop_3:
                                        try:
                                            v4 = c.get_rate(loop_2, loop_3)
                                        except Exception:
                                            print("")
                                        for loop_4 in list[0:]:
                                            loop_num_4 = loop_4
                                            if user_choice != loop_4:
                                                if loop_num_1 != loop_4:
                                                    if loop_num_2 != loop_4:
                                                        if loop_num_3 != loop_4:
                                                            try:
                                                                v6 = c.get_rate(loop_3, loop_4)
                                                            except Exception:
                                                                print("")

                                                            for loop_5 in list[0:]:
                                                                loop_num_5 = loop_5
                                                                if user_choice != loop_5:
                                                                    if loop_num_1 != loop_5:
                                                                        if loop_num_2 != loop_5:
                                                                            if loop_num_3 != loop_5:
                                                                                if loop_num_4 != loop_5:
                                                                                    try:
                                                                                        v8 = c.get_rate(loop_4, loop_5)
                                                                                        if loop_5 != user_choice:
                                                                                            v9 = c.get_rate(loop_5,
                                                                                                            user_choice)
                                                                                            r7 = v1 * v2 * v4 * v6 * v8 * v9
                                                                                            if r7 > 1:
                                                                                                # print(user_choice, loop_1, loop_2,loop_3, user_choice, r4)
                                                                                                print(user_choice, loop_1,
                                                                                                      '->', v1, loop_1,
                                                                                                      loop_2,
                                                                                                      '->', v2,
                                                                                                      loop_2, loop_3, '->',
                                                                                                      v4,
                                                                                                      loop_3, loop_4, '->',
                                                                                                      v6,
                                                                                                      loop_4, loop_5, '->',
                                                                                                      v8,
                                                                                                      loop_5, user_choice,
                                                                                                      '->', v9,
                                                                                                      " =  %0.7f" % r7)

                                                                                    except Exception:
                                                                                        print("------------------------------------------------------------------------------------------------------------------------------")



