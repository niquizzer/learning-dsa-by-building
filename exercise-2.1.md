Exercise 2.1. The List method add all(i, c) inserts all elements of the Collection c into the list at position i. (The add(i,x) method is a special case
where c = {x}.) Explain why, for the data structures in this chapter, it is
not efficient to implement add all(i, c) by repeated calls to add(i,x). Design and implement a more efficient implementation.

- Arrays can't expand or shrink, and since we are increasing the # of elements, we need to create a new array, and copy all the elements from the old one.
    This is mad inefficient yo

Solution:
    