# import sys
# inp = input()
# sol = ""
# def toeight(inp):
#     upper = 0
#     sum = 0
#     for i in inp[::-1]:
#         sum += int(i) * (2 ** upper)
#         upper += 1
#     return str(sum)

# for _ in range(len(inp) // 3):
#     sol = toeight(inp[len(inp) - 3:]) + sol
#     inp = inp[0:len(inp) - 3]
# if inp == "":
#     print(sol)
# else:
#     sol = toeight(inp) + sol
#     print(sol)
print(oct(int(input(),2))[2:])