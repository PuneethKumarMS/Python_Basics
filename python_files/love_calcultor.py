name_1 = input("Enter his name: ")
name_2 = input("Enter her name: ")
combine_name = name_1  +  name_2
lower_case=combine_name.lower()

t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')
true = t + r + u + e

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')
love = l + o + v + e

love_score = true + love
print(love_score)

