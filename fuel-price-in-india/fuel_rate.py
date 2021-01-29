#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:37:23 2019

@author: sudhir
"""
# =============================================================================
# Import library
# =============================================================================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd

# =============================================================================
# Get HistroyData
# =============================================================================
class HistoricalPrice:
    def __init__(self, till_date, file_name, city_url, **kwargs):
        self.till_date = till_date
        self.file_name = file_name
        # self.fuel = fuel
        self.city_url = city_url

    def get_table(self, browser, Data, city_name):
        " Get Table in a perticular Page"
        table = browser.find_element_by_id("BC_GV")
        # Entire Row
        rows = table.find_elements_by_tag_name("td")
        for i in range(0, (len(rows) - 1)):
            # Append Price
            Price = rows[i].find_element_by_class_name("GVPrice").text.replace("₹ ", "")
            Data["rate"].append(float(Price))
            # Append Date
            Date = re.sub("\n", "-", rows[i].find_element_by_class_name("DateDiv").text)
            Date = pd.to_datetime(Date).strftime("%Y-%m-%d")
            Data["date"].append(Date)
            # Append city_name
            Data["city"].append(city_name)
            # Append cityid
            # print(f"date: {Date} rate: {Price} city: {city_name}")

    def get_all_page(self, browser, html, city_name):
        """Get Diesel Price"""
        browser.get(html)
        pages = int(
            browser.find_element_by_xpath(
                '//*[@id="BC_GV_CustomGridPager_LabelNumberOfPages"]'
            ).text
        )
        # pages = 2
        Data = {"city": [], "date": [], "rate": []}
        for p in range(1, pages - 1):
            print(f"Page:{p} city_name: {city_name}")
            # //*[@id="BC_GV_CustomGridPager_NextButton"]
            NEXT_BUTTON_XPATH = '//input[@type="submit" and @name="ctl00$BC$GV$ctl07$CustomGridPager$NextButton" and @value=">"]'
            elem = browser.find_element_by_xpath(NEXT_BUTTON_XPATH)
            # elem.location_once_scrolled_into_view
            elem.send_keys(Keys.DOWN)
            # Data scrape
            try:
                # Data['Page'].append(p)
                self.get_table(browser, Data, city_name)
                if self.till_date in Data["date"]:
                    print("till date:", self.till_date)
                    break
                else:
                    # Go to Next Page
                    time.sleep(3)
                    elem.click()
            except:
                print("Exit may be last page")
                browser.close()
            # browser.forward()
        browser.close()
        return pd.DataFrame(Data)

    def get_old_data(self):
        # Get all data
        df_all = pd.DataFrame()
        for city_name, url in self.city_url.items():
            # browser = webdriver.Chrome('C:\\Users\\Administrator\\Documents\\SeleniumPython\\chromedriver.exe')
            browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
            df = self.get_all_page(browser, url, city_name)
            # keep data till last date mention
            # df[self.fuel] = self.fuel
            df = df.query(f'date >= "{self.till_date}"')
            df = df.sort_values(by=["city", "date"], ascending=True).reset_index(
                drop=True
            )
            # Save as csv
            file = f"dataset/{city_name}{self.file_name}"
            df.to_csv(file, index=False)

            df_all = pd.concat([df, df_all])

        # save full file
        df_all.to_csv(self.file_name, index=False)
        return df_all


if __name__ == "__main__":

    city_url = {
        "Bengaluru": "https://www.mypetrolprice.com/6/Diesel-price-in-Bengaluru?FuelType=1&LocationId=6",
        "Chennai": "https://www.mypetrolprice.com/5/Diesel-price-in-Chennai?FuelType=1&LocationId=5",
        "Mumbai": "https://www.mypetrolprice.com/3/Diesel-price-in-Mumbai?FuelType=1&LocationId=3",
        "Hyderabad": "https://www.mypetrolprice.com/8/Diesel-price-in-Hyderabad?FuelType=1&LocationId=8",
        "Delhi": "https://www.mypetrolprice.com/2/Diesel-price-in-Delhi?FuelType=1&LocationId=2",
        "Kolkata": "https://www.mypetrolprice.com/4/Diesel-price-in-Kolkata?FuelType=1&LocationId=4",
        "Coimbatore": "https://www.mypetrolprice.com/509/Diesel-price-in-Coimbatore?FuelType=1&LocationId=509",
    }
    param = {"till_date": "2021-01-01", "file_name": "tmp.csv", "city_url": city_url}

    df = HistoricalPrice(**param).get_old_data()
