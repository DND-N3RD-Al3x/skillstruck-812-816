my_list = [str(n) for n in input("please give me 5 words: ").split()]

action1 =my_list[0]
action2 = my_list[4]

final = "Some animals {} and some {}"

print(final.format(action1,action2))