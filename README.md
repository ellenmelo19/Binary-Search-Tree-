# Binary-Search-Tree
BST implementation in Python

This project implements a Binary Search Tree (ABB) in Python. ABB is a data structure that organizes numbers efficiently, allowing operations such as insertion, removal, search, and other specific functionalities.

## Files:
``ABB.py``: Contains the implementation of the ABB class and the TreeNode class. The ABB class offers methods for insertion, removal, search, and ABB-specific operations, such as pre-order, in-order, post-order printing, among others.

``entrada.txt``: Input file containing a sequence of space-separated integer values. These values will be used to build ABB.

``comandos.txt``: Command file containing operations to be carried out in ABB, such as "PREORDEM" which means ''pre-order'', "EMORDEM" which means ''in order'', "POSORDEM" which means ''post order'' '', "IMPRIMEARVORE" which means ''print tree'', among others.

## How to Execute:

1. Make sure you have Python installed on your system.
2. Run the ABB.py file in your terminal or Python IDE.
bash

The program will read the ``entrada.txt`` and ``comandos.txt`` files, build the ABB based on the input values, and perform the operations specified in the commands. feel free to edit the input file or change the order of the commands.
OBS: If you need a command other than those in the command file, you will need to implement it in the code and reference it in the ``comandos.txt`` file.

## ABB Class Methods:

*insert(value)*: Inserts a value into the ABB.

*remove(value)*: Removes a value from ABB.

*pre_order()*: Returns a string with the pre-order visit sequence.

*in_order()*: Returns a string with the visit sequence in order.

*post_order()*: Returns a string with the post-order visit sequence.

*position(x)*: Returns the position occupied by element x in an in-order path.

*median()*: Returns the element that contains the median of the ABB.

*print_tree()*: Prints the tree.

## Important Notes:

* Duplicate values are not allowed at ABB.
* Attempts to remove an element that does not exist in the tree are ignored.
* ABB implementation is done without using ready-made data structures from external libraries.

## Naming Convention:

Methods starting with _ are considered private methods and are intended for internal use in the class implementation.
Contributions and Improvements:
Contributions are welcome! Feel free to open issues or pull requests to improve this project.

### License:
This code is distributed under the MIT License. See the LICENSE file for more details.
