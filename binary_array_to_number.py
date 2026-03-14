# convert a binary array into a number
def binary_array_to_number(ar):
    num = 0
    n = len(ar)
    for i in range(n):
        power = (n-1)-i
        num += ar[i] * (2 ** power)   
    return num
