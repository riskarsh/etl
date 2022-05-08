## Solution 1
### Reads the test file and transformation (Capitalizing contents) is applied and the output is saved.

*Implementation below*

```bash
$ cat test.txt
hi this is a test file
to test number of words
and count of words.

$ python3 etl_1.py test.txt output.txt

$ cat output.txt 
HI THIS IS A TEST FILE
TO TEST NUMBER OF WORDS
AND COUNT OF WORDS.
```

## Solution 2

### Reads the test file and returns the occurrence of the words.

*Implementation below*

```bash 
$ cat test.txt
hi this is a test file
to test number of words
and count of words.

$ python3 etl_2.py test.txt output.txt

$ cat output.txt 
hi -> 1 
this -> 1 
is -> 1 
a -> 1 
test -> 2 
file -> 1 
to -> 1 
number -> 1 
of -> 2 
words -> 2 
and -> 1 
count -> 1