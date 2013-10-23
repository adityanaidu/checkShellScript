checkShellScript
================

Static Code Analysis of bash scripts

Developed on Python 2.7.3 

For Usage type

```
./checkShellScript.py -h
```

Before you use checkShellScript, use the -n and -u option on your script to 
take care of basic syntax issues

```
bash -n scriptname
bash -u scriptname
```

Unit Testing

To test the code itself run checkShellScript on test.lines
and compare the output with the expected.results file:

```
./checkShellScript.py test.lines > actual.results
diff actual.results expected.results
```

diff should not produce any output
