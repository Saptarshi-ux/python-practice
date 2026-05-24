#Character frequency in a string

def char_fn(text):
  freq={}
  for i in text.lower():
    freq[i]=freq.get(i,0)+1
  return freq


# core logic:

"""req[i] = freq.get(i, 0) + 1 is the powerhouse of the function.

The .get(i, 0) command asks the dictionary: Do we already have a count for the character i?
If the character is already in the dictionary, it returns the current number.

If the character is not in the dictionary yet, it safely returns 0 (instead of crashing with a KeyError).

It then adds 1 to whatever number it got back, and assigns that new total to freq[i]"""
