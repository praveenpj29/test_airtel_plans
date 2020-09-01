# selenium test of airtel plans page 
# generate allure reports
# excel report

## pre-requisites

### python-modules

- **selenium**
- **pytest**
- **pytest-xdist** - for running tests in parallel if there are any
- **pandas** 
- **allure-pytest** -for genearting allure reports

To install any module run command along with module name in python env
> pip install module-name

### allure
Download allure zip file and extract it any location

Add the path of allure(bin folder which contains .bat file) to system variables

## commands

> pytest -s -v testcases/airtel_plans_test.py --browser firefox

This command runs the tests in firefox and doesn't generate any allure reports
but excel file is generated

> pytest -s -v --alluredir=".//Reports/" testcases/airtel_plans_test.py --browser firefox

this command runs the tests in firefox and generate allure reports to specified location ".//Reports/"

## allure reports visualization

open command-prompt and redirect it to path which contains allure reports
command

>allure serve ".//Reports/"

## screenshots


![allure_report](.//screeshots/allure_report.png)


![excel_report](.//screenshots/excel_report.png)
