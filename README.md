# Python_weakly_works

#Data structure and algorithms using python

################################## Week 2 Programming Assingment########################

1) Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

  >>> intreverse(783)
  387
  >>> intreverse(242789)
  987242
  >>> intreverse(3)
  3

2) Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.

 
  >>> matched("zb%78")
  True
  >>> matched("(7)(a")
  False
  >>> matched("a)*(?")
  False
  >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
  True
  
3) Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

  >>> sumprimes([3,3,1,13])
  19
  >>> sumprimes([2,4,6,9,11])
  13
  >>> sumprimes([-3,1,6])
  0

###################### W e a k 3 Q u e s t i o n s #########################################

1). Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it. For instance:

  >>> descending([])
  True

  >>> descending([4,4,3])
  True

  >>> descending([19,17,18,7])
  False
  
2). A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

  >>> valley([3,2,1,2,3])
  True

  >>> valley([3,2,1])
  False

  >>> valley([3,3,2,1,2])
  False
  
3). A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

  1  2  3
  4  5  6 
would be represented as [[1, 2, 3], [4, 5, 6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

  1  4  
  2  5
  3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

  >>> transpose([[1,4,9]])
  [[1], [4], [9]]

  >>> transpose([[1,3,5],[2,4,6]])
  [[1, 2], [3, 4], [5, 6]]

  >>> transpose([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
