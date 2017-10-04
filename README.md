# sp_learning

Command to run all test-cases in folder

``` 
py.test src/modules/example/test/
```

Allure
1. Run all tests and store in report folder
```
py.test --alluredir=report [path to test-script or folder with tests]
```

2. generate html report from 'report' folder to 'report-html' folder
```
allure generate -o report-html report
```
3. open reports from 'report-html' folder
```
allure open report-html
```
