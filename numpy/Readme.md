# NumPy (Numerical Python)

## What is NumPy?

**NumPy (Numerical Python)** is a powerful open-source Python library used for **numerical computing and scientific calculations**.

It provides support for working with large, multi-dimensional arrays and matrices along with a collection of mathematical functions to perform operations efficiently.

---

## Why use NumPy?

Python lists are flexible but can become slow when handling large amounts of numerical data.

NumPy solves this problem by providing:

- Faster numerical computations
- Memory-efficient data storage
- Powerful mathematical operations
- Support for multi-dimensional arrays
- Tools for linear algebra and statistics

---

## Core Concept: NumPy Array

The main object in NumPy is the **ndarray (N-dimensional array)**.

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

Output:

```text
[1 2 3 4 5]
```

Unlike Python lists, NumPy arrays store data in a structured way that allows faster calculations.

---

## Creating Arrays

### 1D Array

```python
import numpy as np

a = np.array([10, 20, 30])
```

### 2D Array (Matrix)

```python
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

---

## Important NumPy Operations

### Mathematical Operations

```python
import numpy as np

a = np.array([1,2,3])

print(a + 5)
```

Output:

```text
[6 7 8]
```

NumPy performs operations element-wise.

---

## Array Properties

```python
arr.shape
```

Returns the dimensions of the array.

Example:

```text
(2,3)
```

means:

2 rows and 3 columns.


```python
arr.ndim
```

Returns the number of dimensions.


```python
arr.size
```

Returns total number of elements.

---

## Statistical Functions

NumPy provides built-in statistical operations:

```python
np.mean(data)
np.median(data)
np.std(data)
np.sum(data)
np.min(data)
np.max(data)
```

Example:

```python
import numpy as np

data = np.array([10,20,30])

print(np.mean(data))
```

Output:

```text
20
```

---

## Random Number Generation

NumPy can generate random values:

```python
np.random.randint(1,100,5)
```

Example output:

```text
[34 72 11 89 45]
```

---

## Linear Algebra Support

NumPy is widely used for matrix operations:

```python
np.dot(a,b)
```

It supports:

- Matrix multiplication
- Determinants
- Eigenvalues
- Matrix inversion

---

## NumPy in Data Science

NumPy is the foundation of many Python data science libraries:

- Pandas
- Matplotlib
- Scikit-learn
- SciPy

It is commonly used in:

- Data analysis
- Machine learning
- Scientific computing
- Financial modelling

---

## Installation

Install NumPy using pip:

```bash
pip install numpy
```

Import in Python:

```python
import numpy as np
```

---

## Summary

| Feature | Description |
|---|---|
| Library | Numerical Python |
| Main Object | ndarray |
| Purpose | Numerical computing |
| Advantage | Fast array operations |
| Used In | Data Science, ML, AI |

NumPy provides the foundation for efficient numerical computation in Python.
