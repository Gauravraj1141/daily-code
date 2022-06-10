
# """
# #n! = n*n-1*n-2*n-3.....
# # jse 5! = 5*4*3*2*1 = 120 to ase hi factorial ka program banan h
#
#
#         :parameter  n: Integer lena
#         :return: n * n-1 * n-2 * n-3.......1 value ye ani chiye
#     """
#
# def factorial_itirative(n): # ye itirative se h
#     gau = 1
#     for i in range(n):
#         gau = gau * (i+1)
#     return gau # ye hmne for loop se bhr ake return kiya
# number = int(input("number"))
# print("it is itirative method",factorial_itirative(number))
#
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial_itirative(n-1)
# print("it is a recursive method",factorial_recursive(number))
#
# """logic recursive
#   #   5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1 = 120
# """


#0 1 1 2 3 5  8  13 .....
def fibonachi(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else :
        return fibonachi(n-1)+fibonachi(n-2)
number = int(input("kkdkd"))
print(fibonachi(number))
