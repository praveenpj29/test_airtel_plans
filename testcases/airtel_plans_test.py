from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
import pandas as pd
import time


class Test_1:

    def test_airtel_links(self):
        driver = webdriver.Firefox()
        driver.get("https://www.airtel.in")
        time.sleep(10)
        # driver.find_element_by_class_name("moe-btn moe-btn-block").click()
        action = ActionChains(driver)
        prepaid = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[1]/div[1]/div[1]/h3")
        action.move_to_element(prepaid).perform()
        plans = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[1]/div[1]/div[1]/ul/li[3]/a")
        action.move_to_element(plans).perform()
        plans.click()
        plans_xpath = "//*[@class='clear pack-detail-wrap first-padding']"
        plans = driver.find_elements_by_xpath(plans_xpath)
        df = {
            "S.no": [],
            "plan_rate": [],
            "validation": []
        }
        count = 1
        for i in range(1, len(plans) + 1):
            plans_1_xpath = plans_xpath + "[{}]".format(i) + "//*[@class='pack-detail-row']"
            plans_1 = driver.find_elements_by_xpath(plans_1_xpath)
            for j in range(1, len(plans_1) + 1):
                plans_2_xpath = plans_1_xpath + "[{}]".format(j) + "//*[@class='btn-circle icn-rupee']"
                plans_2 = driver.find_element_by_xpath(plans_2_xpath)
                df["plan_rate"].append(plans_2.text)
                try:
                    plans_2.click()
                    df["S.no"].append(count)
                    time.sleep(5)
                except ElementNotInteractableException as e:
                    df["validation"].append(e)
                else:
                    if driver.title == "Online Mobile Recharge, Prepaid New Mobile Recharge - Airtel":
                        driver.back()
                        time.sleep(5)
                        if driver.title == "Best Prepaid Plans, Data Recharge Online - Airtel":
                            df["validation"].append("passed")
                        else:
                            df["validation"].append("failed")
                finally:
                    count += 1
        driver.close()
        Data = pd.DataFrame(df)
        output = pd.ExcelWriter(".//Reports/airtel_plans.xlsx")
        Data.to_excel(output)
        output.save()

        if "failed" not in df["validation"]:
            assert True
        else:
            assert False