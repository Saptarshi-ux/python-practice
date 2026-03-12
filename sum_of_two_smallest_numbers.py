def sum_two_smallest_numbers(num):
  if all(isinstance(x, int) and x > 0 for x in num):
        num.sort()
        return num[0] + num[1]
  else:
        return "not all the numbers are positive"
'''
here the challenge was: Create a function that returns the sum of the two 
lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
'''
