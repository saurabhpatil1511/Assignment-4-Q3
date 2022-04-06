# Program to square the elements of a a list using map function
def square_num(n):
    return n * n
nums = [4, 5, 2, 9]
result = map(square_num, nums)
print("Square the elements of the said list is:")
print(list(result))
