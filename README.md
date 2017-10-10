# sp_learning

Command to run all test-cases in folder

``` 
py.test -v [path to folder]
```
or run ```py.test -v``` command in derictory with test-scripts 



Allure
1. Run all tests and store in report folder
```
py.test -v --alluredir=report [path to test-script or folder with tests]
```

2. generate html report from 'report' folder to 'report-html' folder
```
allure generate --clean -o report-html report
```
3. open reports from 'report-html' folder
```
allure open report-html
```
