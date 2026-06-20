# Understanding Floor Division (`//`)

Floor division (using the `//` symbol) is like regular division, but it **always rounds down to the next smaller whole number**. Imagine it as asking: *"How many full, complete times does this number fit into the other?"*

Here are the three best examples to understand how it works, starting simple and ending with the tricky part!

## 1. The Clean Cut (No Remainder)
If a number divides perfectly, floor division gives the exact same result as normal division, just as an integer instead of a decimal.

* **Normal:** `10 / 5` is `2.0`
* **Floor:** `10 // 5` is `2`

## 2. The Leftovers (Positive Numbers)
If there is a decimal, floor division simply chops it off. It drops down to the nearest whole integer.

* **Normal:** `11 / 5` is `2.2`
* **Floor:** `11 // 5` is `2` 

> *(5 goes into 11 exactly 2 whole times. We ignore the leftovers).*

## 3. The Tricky Part (Negative Numbers)
This is where people get caught in interviews or tests! Floor division always rounds **down** (to the left on a number line), it does not just chop off the decimal towards zero.

* **Normal:** `-11 / 5` is `-2.2`
* **Floor:** `-11 // 5` is `-3` 

> *(Because -3 is mathematically smaller/lower than -2.2, the "floor" pulls it further down the negative number line. It does NOT become -2!).*

---
*Here is an interactive calculator so you can test how different numbers behave. Try putting negative numbers in to see how the "floor" behaves on the number line!*
