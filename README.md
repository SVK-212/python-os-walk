# python-os-walk
This code represents directories in tree format.

How to use:

1) Download this library.
2) Import the library in your main code.
3) Call the makeTree(path), where path is the root path of the desired final tree.

Attributes supported by makeTree:
1) dir_sep - Either / or \ used to separate directory names in any file path. Default value: "\\".
2) line_start - [For formatting purpose] Used to decide the start of each printed line except the very first. Default value: "|".
3) line_sep - [For formatting purpose] Used to decide the distinguishing indicator for every folder or file level. Default value: "-".

Taking line_sep as "\t" and line_start as "" is also a good choice.

E.g.
Script:
import pythonOsWalk
pythonOsWalk.makeTree("C:\\root folder")
Output: (View output in RAW mode)
C:
|-root folder

|--:FILES:0
|--first_one
|---:FILES:0
|---second_one_one
|----:FILES:0
|----third_one_one_one
|-----:FILES:3
|------fourth_one_one_one_one.txt
|------fourth_one_one_one_three.txt
|------fourth_one_one_one_two.txt
|----third_one_one_three
|-----:FILES:1
|------fourth_one_one_three_one.txt
|----third_one_one_two
|-----:FILES:0
|---second_one_three
|----:FILES:0
|---second_one_two
|----:FILES:0
|--first_three
|---:FILES:0
|--first_two
|---:FILES:0
|---second_two_one
|----:FILES:0
|---second_two_three
|----:FILES:0
|---second_two_two
|----:FILES:0

 
