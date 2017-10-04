# sp_learning

Command to run all test-cases in folder

``` 
py.test src/modules/example/test/
```

Allure
1. Run all tests and store in report folder
```
py.test --alluredir=report C:\Users\Владелец\PycharmProjects\sp_learning\sp_at\test_cases\test_why_page.py
```

2. generate html report from 'report' folder to 'report-html' folder
```
allure generate -o report-html report
```
3. open reports from 'report-html' folder
```
allure open report-html
```
