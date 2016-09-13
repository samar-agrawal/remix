## RPN Calculator
[RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation) is a polish mathematical notation in which every operator follows all of its operands. The script will output the calculated result of a valid RPN expression as detailed in the following section.

### Problem

A library that will provide RPN calculator capabilities. Core requirements are listed below.

##### Cases
Case 1: Solving RPN expressions given as a string
```
Input               Output
"1 3 + 5 3 - *"     "8"
```
 
Case 2. Support for basic mathematical operators:

```
Input    Output
"1 3 +"    "4"
"5 3 -"    "2"
"2 4 *"    "8"
"6 2 /"    "3"
```

Case 3. Ability to define custom operators.

As an example, implement custom operator "?" that takes 3 arguments. If the first argument is true, return the second argument, otherwise return the third argument.
 
```
Input       Output
"1 2 3 ?"   "2"
"0 2 3 ?"   "3"
```
