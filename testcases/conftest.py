from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox driver ........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser ........")
    else:
        driver = webdriver.Ie()
        print("Launching Internet Explorer browser ......")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# pytest HTML report

# hook to adding info in html report
# def pytest_configure(config):
#     config._metada['Project Name'] = 'Amazon.in'
#     config._metada['Tester'] = 'PJ'

# hook to remove additional info in html report
# @pytest.mark.optionalhook
# def pytest_metadata(metada):
#     metada.pop("JAVA_HOME", None)
#     metada.pop("Plugins", None)

