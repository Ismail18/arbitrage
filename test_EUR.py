from forex_python.converter import CurrencyRates



c = CurrencyRates()

list = ['USD', 'EUR', 'JPY', 'CHF', 'GBP', 'AUD', 'CAD']

user_choice = list[0]


for loop_1 in list[0:]:
    if user_choice != loop_1:
        try:
            v1 = c.get_rate(user_choice, loop_1)
        except Exception:
            print('     ----------      ')
        for loop_2 in list[0:]:
            if user_choice != loop_2:
                try:
                    if loop_1 != loop_2:
                        v2 = c.get_rate(loop_1, loop_2)
                        r1 = v1 * v2
                        if r1 >= 1:
                            if loop_2 == user_choice:
                                print(user_choice,loop_1, loop_2,r1)
                except Exception:
                    print("     ----------      ")

        for loop_3 in list[0:]:
            if loop_2 != loop_3:
                try:
                    if loop_3 != loop_2:
                        v3 = c.get_rate(loop_2, loop_3)
                        r2 = r1 * v3
                        if r2 >= 1:
                            if loop_3 == user_choice:
                                print(user_choice, loop_1, loop_2, loop_3, r2)
                except Exception:
                    print("     ----------      ")




