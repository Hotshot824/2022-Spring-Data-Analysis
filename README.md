# DataAnalysis Homework 3

Use Python codes and execution results to answer the questions. Any other forms are also acceptable. Answer the questions as concise as possible. Put the answer in this docx file.

## (1).	What are "module" and "package" for Python?

* Module : A single pythonfile.
* Package : A set of module sebpackage and otherfile in a **directory** structrue.
  * including `__init__.py`

## How to run Python

1. CMD. python
2. Idle, Idlex
3. `Jupyder`(AI), `Pycham, Spyder`(Project)
4. Clone online
5. direct execution

## (2).	What is "namespace" in Python and it’s purpose? Give an example in Python and daily life.

* When imported, namespace should be specified.'

```
import numpy as np # numerical computation
numpy.__version__ # namespace
```

## (3).	Use examples to explain the difference among "list", "tuple" and "dictionary".

* List : Lists are used to store multiple items in a single variable.

`['A', 10, True, 20, 'C', 'Peter']`
* Tuple : Tuples are used to store multiple items in a single variable.

`(10, 20, 30, 40, 50)`
* dictionary : Dictionaries are used to store data values in key:value pairs. Like JSON datastruct.

`thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 }`

## (4).	Parse and name the objects.
```Python
myobj = {"name":"John", "age":30.5, "cars":{'1':["Frd",22], 2:["BMW",24]}, 2.3:[{15,16},(77,88,"77")]}
```

* Is a dictionary 
```
  Key : 'name' value : "John"
  Key : 'age' value : "30.5"
  Key : 'cars' value : is a Dict {'1':["Frd",22], 2:["BMW",24]}
  Key : '2.3' value : is a List [{15, 16},(77, 88, "77")] {15, 16} is a Set
```

## (5).	For indexing `lst[i]` and slicing `lst[a:b:s]`, what are the ranges of i and a, b, and s? What are the default values of a, b, and s? Use slicing to reverse a list.

```
```


## (6).	What is the main difference between "list" and "ndarray"?

## (7).	Show the print results.
```
lst = [1,2,3]
nda = np.array([1, 2, 3])
print(type(lst)) #
print(type(nda)) #
print(lst*3)     #
print(nda*3)     #
```

## (8).	What is the difference of “alias copy”, “shallow copy”, and “deep copy” for both list and ndarray? What is these mechanism for?

## (9).	What are the 3 looping mechanisms for programming languages. Claim when to use. What we have in Python?

## (10).	Write a subroutine 【lst = fibon(m, n)】 to output a "list" of Fibonancci numbers between m and n (n not included). Use simple code to call the subroutine.
```
input:  m, n (integers)
output: lst  (list)
Give comments for the code and explain your reults are correct.
Fibonancci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
Example: lst = fibon(6, 34) # lst is [8, 13, 21]
```

## Python's design philosophy emphasizes code readability with use of significant indentation. 


