# def func1(require = [], go = False):
#     if go:
#         require.append(20)
#         return require
        
#     add = func1(go = True)
#     require += add
#     return require

# add = 10

# def therealreal(update):
#     def modify(require = []):
#         require += update()
#         # print(require)
        
#         global add
#         require.append(add)
#         add += 10
#         return require
    
#     return modify
    
# use = therealreal(func1)
upto = 213

# calc = use()
# for _ in range(1, upto+1):
#     calc = use(calc)

print(20 * (2 ** (upto + 3) - ((upto + 2) * 2 + 2)) + (10 * ((upto + 1) * (upto + 2)) // 2))
# 2106245833371143733958360553673408646377901908010982225086219772130