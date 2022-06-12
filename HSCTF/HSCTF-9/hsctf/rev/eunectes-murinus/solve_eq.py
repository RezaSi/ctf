import requests

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

my_vars = [f"x{i}" for i in range(57, -1, -1)]

possibles = {}
for v in my_vars:
    possibles[v] = [i for i in range(40, 150)]

eqs = requests.get("https://bigir.ir/cdn/5dcd3c8ae06e41f3b5bc6fd7a/eq.json").json()

for eq, value in eqs.items():
    print(eq, value)
    included_vars = []
    for var in my_vars:
        for splited in eq.split(' '):
            splited.strip()
            splited = splited.replace('(', '')
            if var == splited:
                included_vars.append(var)
    possibles_0 = []
    possibles_1 = []
    possibles_2 = []
    for possible_0 in possibles[included_vars[0]]:
        for possible_1 in possibles[included_vars[1]]:
            for possible_2 in possibles[included_vars[2]]:
                temp_eq = eq.replace(included_vars[0], str(possible_0))
                temp_eq = temp_eq.replace(included_vars[1], str(possible_1))
                temp_eq = temp_eq.replace(included_vars[2], str(possible_2))
                if eval(temp_eq) == value:
                    possibles_0.append(possible_0)
                    possibles_1.append(possible_1)
                    possibles_2.append(possible_2)
    possibles[included_vars[0]] = intersection(possibles[included_vars[0]], possibles_0)
    possibles[included_vars[1]] = intersection(possibles[included_vars[1]], possibles_1)
    possibles[included_vars[2]] = intersection(possibles[included_vars[2]], possibles_2)

res = ''
for k,v in possibles.items():
    if len(v) == 1:
        res += chr(v[0])
    else:
        res += 'X'

print(res[::-1])