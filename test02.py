from forex_python.converter import CurrencyRates



c = CurrencyRates()
list = ['USD', 'EUR', 'JPY', 'CHF', 'GBP', 'AUD', 'CAD']

v1 = 0
v2 = 0
r1 = 0
v3 = 0
r2 = 0

for loop_1 in list[1:]:
    v1 = c.get_rate(list[0], loop_1)
    for loop_2 in list[0:]:
        try:
            v2 = c.get_rate(loop_1, loop_2)
            r1 = v1 * v2
        except Exception:
            print("")

        for loop_3 in list[0:]:
            try:
                v3 = c.get_rate(loop_2, loop_3)
                r2 = r1 * v3
                if r2 >= 1 :
                    if loop_3 == list[0]:
                        print(list[0], loop_1, loop_2, loop_3, r2)
            except Exception:
                print("!")


