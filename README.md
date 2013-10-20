checkShellScript
================

Static Code Analysis of bash scripts

Developed on Python 2.7.3 

For Usage type

```
./checkShellScript.py -h
```

Unit Testing
To test the code itself run checkShellScript on test.lines
and compare the output with the expected.results file:

```
./checkShellScript.py test.lines > actual.results
diff actual.results expected.results
```

diff should not produce any output
