from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



locations=["New York"]
sentences=["Long term furnished co-living in ",
"Furnished vacation rentals in ",
# "Long term furnished co-living in ",
# "Summer furnished vacation rentals in ",
# "Long term housing rentals in ",
# "Seasonal furnished rentals in ",
# "Mid-term furnished rentals in ",
# "Mid-term vacation rentals in ",
# "Mid-term rental in ",
# "Mid-term rental operators in ",
# "Family vacation homes in ",
# "Family furnished vacation homes in ",
# "Family long term rentals in ",
# "Family mid-term rentals in ",
# "Luxury vacation homes in ",
# "Luxury furnished vacation homes in ",
# "Furnished beach rentals in ",
# "Furnished getaway in ",
# "Furnished condos in ",
# "Monthly vacation lodges in ",
# "Summer condo rentals in ",
# "Luxury furnished condo in ",
# "Mid-term condo rental in ",
# "Property Management",
# "Property management furnished rentals in ",
# "Long term rentals property manager in ",
# "Property manager in ",
# "Mid-term property managers in ",
# "Furnished lodge in ",
# "Furnished vacation lodges in ",
# "Monthly vacation lodges in ",
# "Mid-term lodges in ",
# "Nature lodge in ",
# "Furnished nature lodge in ",
# "Family nature lodge in ",
]


thingstobesearched=[
# "Resort",
"Apartment",
# ,"House	cabins"
# ,"Condo	Student Housing"
# ,"Bed and Breakfast	"
# ,"vacation rentals	"
# ,"Lodge	"
# ,"Vacation rentals	"
# ,"Nature lodge	"
# ,"Real Estate Company"
# ,"Corporate Housing	"
# ,"Timeshare	"
# ,"Hostel	"
# ,"Campsite Holiday Park	"
# ,"Host Management Company"
# ,"Hotel	"
]
dict1={
    "Long term furnished co-living in ":["Furnished"],
    "Furnished vacation rentals in ":["Furnished"],
    "Summer furnished vacation rentals in ":["Furnished"],
    "Long term housing rentals in ":["Furnished"],
    "Seasonal furnished rentals in ":["Furnished"],
    "Mid-term furnished rentals in ":["Furnished"],
    "Mid-term vacation rentals in ":["Furnished"],
    "Mid-term rental in ":["Furnished"],
    "Mid-term rental operators in ":["Furnished"],
    "Family vacation homes in ":["Furnished"],
    "Family furnished vacation homes in ":["Furnished"],
    "Family long term rentals in ":["Furnished"],
    "Family mid-term rentals in ":["Furnished"],
    "Luxury vacation homes in ":["Furnished"],
    "Luxury furnished vacation homes in ":["Furnished"],
    "Furnished beach rentals in ":["Furnished"],
    "Furnished getaway in ":["Furnished"],
    "Furnished condos in ":["Furnished"],
    "Monthly vacation lodges in ":["Furnished"],
    "Summer condo rentals in ":["Furnished"],
    "Luxury furnished condo in ":["Furnished"],
    "Mid-term condo rental in ":["Furnished"],
    "Property Management":["Furnished"],
    "Property management furnished rentals in ":["Furnished"],
    "Long term rentals property manager in ":["Furnished"],
    "Property manager in ":["Furnished"],
    "Mid-term property managers in ":["Furnished"],
    "Furnished lodge in ":["Furnished"],
    "Furnished vacation lodges in ":["Furnished"],
    "Mid-term lodges in ":["Furnished"],
    "Nature lodge in ":["Furnished"],
    "Furnished nature lodge in ":["Furnished"],
    "Family nature lodge in ":["Furnished"]

}

# Configure the WebDriver
def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)

# Fetch valid h3 elements and their corresponding links
# def get_valid_h3_and_links(driver):
#     h3_elements = driver.find_elements(By.TAG_NAME, "h3")
#     valid_h3_links = []
#     for h3 in h3_elements:
#         if h3.text:
#             try:
#                 # Locate the parent <a> tag for the h3 element
#                 parent_link = h3.find_element(By.XPATH, "./ancestor::a")
#                 valid_h3_links.append((h3.text, parent_link.get_attribute("href")))
#             except Exception as e:
#                 print(f"Error fetching link for h3: {h3.text}, Error: {e}")
#     return valid_h3_links

# def get_valid_h3_and_links(driver):
#     h3_elements = driver.find_elements(By.TAG_NAME, "h3")
#     valid_h3_links = []
#     for h3 in h3_elements:
#         if not h3.text.strip() or "Map" in h3.text or "More places" in h3.text:
#             continue
#         try:
#             parent_link = h3.find_element(By.XPATH, "./ancestor::a")
#             valid_h3_links.append((h3.text, parent_link.get_attribute("href")))
#         except Exception as e:
#             print(f"Error fetching link for h3: {h3.text}, Error: {e}")
#     return valid_h3_links
def get_valid_h3_and_links(driver):
    h3_elements = driver.find_elements(By.TAG_NAME, "h3")
    valid_h3_links = []
    for h3 in h3_elements:
        # Skip headings with known non-link text or those without meaningful content
        if not h3.text.strip() or "Map" in h3.text or "More places" in h3.text or "More businesses" in h3.text:
            continue
        try:
            # Locate the parent <a> tag only if it exists
            parent_link = h3.find_element(By.XPATH, "./ancestor::a")
            link_href = parent_link.get_attribute("href")
            if link_href:  # Ensure the link has a valid href attribute
                valid_h3_links.append((h3.text, link_href))
        except Exception as e:
            print(f"Error fetching link for h3: {h3.text}, Error: {e}")
    return valid_h3_links


def main():
    driver = setup_driver()
    try:
        driver.get("https://www.google.com/")
        time.sleep(10)
        finalbestsites = []
        mainindex=0
        mainindex2= 0

        for i in range(len(sentences)):
            query = sentences[i]
            for location in locations:
                for term in thingstobesearched:
                    full_query = f"{query} {location} {term}"
                    print(f"Searching for: {full_query}")

                    # search_box = WebDriverWait(driver, 10).until(
                    #     EC.element_to_be_clickable(
                    #         (By.XPATH, "/html/body/div[2]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div[2]/textarea")
                    #     )
                    # )

                    if i==0 and location==locations[0] and term==thingstobesearched[0]:
                        search_box = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
                            )
                        )
                        search_box.clear()
                        search_box.send_keys(full_query)
                        search_box.send_keys(Keys.ENTER)
                    else:
                        search_box = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, "/html/body/div[2]/div[2]/form/div[1]/div[1]/div[2]/div[1]/div[2]/textarea")
                            )
                        )
                        search_box.clear()
                        search_box.send_keys(full_query)
                        search_box.send_keys(Keys.ENTER)



                    WebDriverWait(driver, 40).until(
                        EC.presence_of_all_elements_located((By.TAG_NAME, "h3"))
                    )

                    h3_and_links = get_valid_h3_and_links(driver)
                    print(f"Found {len(h3_and_links)} valid links for query: {full_query}")

                    for h3_text, link_href in h3_and_links:
                        try:
                            print(f"Attempting to click link for: {h3_text}")
                            link = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, f"//a[@href='{link_href}']"))
                            )
                            driver.execute_script("arguments[0].scrollIntoView(true);", link)

                            if link.is_displayed() and link.is_enabled():
                                print(f"Link is clickable: {h3_text}")
                                driver.execute_script("arguments[0].click();", link)
                                time.sleep(10)
                            else:
                                print(f"Link is not clickable: {h3_text}")

                            isperfect = True
                            checkinglist = dict1.get(query, []) + [term]

                            for word in checkinglist:
                                if word in driver.page_source:
                                    print(f"Found the word on the page: {word}")
                                else:
                                    isperfect = False
                                    print(f"Page did not match criteria: {driver.current_url}")
                                    break

                            if isperfect:
                                print("Found one of the useful sites")
                                finalbestsites.append(driver.current_url)
                                print(finalbestsites, " newer form")
                            else:
                                print(finalbestsites, " should be the same as old")

                            driver.back()
                            time.sleep(10)
                            # break

                        except Exception as e:
                            print(f"Error interacting with link for h3: {h3_text}, Error: {e}")
                    # Open a file in append mode ('a')
                    with open('example.txt', 'a') as file:
                        file.write(f"This is the result of the sites for the search command {full_query}\n")
                        while mainindex<len(finalbestsites):
                            file.write(finalbestsites[mainindex])
                            file.write("\n")
                            mainindex+=1
                    with open('links.txt', 'a') as file:
                        # file.write(f"This is the result of the sites for the search command {full_query}\n")
                        while mainindex2<len(finalbestsites):
                            file.write(finalbestsites[mainindex])
                            file.write("\n")
                            mainindex2+=1
    finally:
        driver.quit()

# Main function
# def main():
#     driver = setup_driver()
#     driver.get("https://www.google.com/")
#     time.sleep(10)
#     finalbestsites = []
#
#     for i in range(0,len(sentences)):
#         str1 = ""
#         str1+=sentences[i]
#         for j in range(0,len(locations)):
#             str2=""
#             str2+=str1
#             str2+=locations[j]
#             for k in range(0,len(thingstobesearched)):
#                 str3=""
#                 str3+=str2
#                 str3+=" "
#                 str3+=thingstobesearched[k]
#                 query=str3
#                 try:
#                     # Locate search input
#                     search_box = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable(
#                             (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea"))
#                     )
#                     if search_box:
#                         # Enter query and search
#                         search_box.clear()
#                         search_box.send_keys(query)
#                         search_box.send_keys(Keys.ENTER)
#                         time.sleep(40)  # Allow results to load
#                     else:
#                         print("Search box not found!")
#                         return
#
#                     # Fetch initial list of links
#                     h3_and_links = get_valid_h3_and_links(driver)
#                     print(f"Found {len(h3_and_links)} valid h3 elements and links for query: {query}")
#
#                     for h3_text, link_href in h3_and_links:
#                         try:
#                             print(f"Attempting to click link for: {h3_text}")
#
#                             # Re-fetch the link dynamically to avoid stale references
#                             link = WebDriverWait(driver, 10).until(
#                                 EC.presence_of_element_located((By.XPATH, f"//a[@href='{link_href}']"))
#                             )
#                             driver.execute_script("arguments[0].scrollIntoView(true);", link)
#
#                             # Check clickability dynamically
#                             if link.is_displayed() and link.is_enabled():
#                                 print(f"Link is clickable: {h3_text}")
#                                 driver.execute_script("arguments[0].click();", link)
#                                 time.sleep(10)  # Wait for navigation
#                             else:
#                                 print(f"Link is not clickable: {h3_text}")
#
#                             isperfect=True
#
#                             checkinglist=dict1[sentences[i]]
#                             checkinglist.append(thingstobesearched[k])
#
#                             # Validate page content
#                             for words in range(0,len(checkinglist)):
#                                 if checkinglist[words] in driver.page_source:
#                                     print(f"Found the word on the page {checkinglist[words]}")
#                                 else:
#                                     isperfect=False
#                                     print(f"Page did not match criteria: {driver.current_url}")
#                                     break
#
#                             if isperfect:
#                                 print("Found one of the useful sites")
#                                 finalbestsites.append(driver.current_url)
#                                 print(finalbestsites," newer form")
#                             else:
#                                 print(finalbestsites," should be the same as old")
#
#
#                             # Navigate back to results
#                             driver.back()
#                             time.sleep(10)  # Wait for results to reload
#
#                         except Exception as e:
#                             print(f"Error interacting with link for h3: {h3_text}, Error: {e}")
#
#                 finally:
#                     driver.quit()



    # query = "Long term furnished co-living in New York Furnished"
    #
    # try:
    #     # Locate search input
    #     search_box = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea"))
    #     )
    #     if search_box:
    #         # Enter query and search
    #         search_box.clear()
    #         search_box.send_keys(query)
    #         search_box.send_keys(Keys.ENTER)
    #         time.sleep(40)  # Allow results to load
    #     else:
    #         print("Search box not found!")
    #         return
    #
    #     # Fetch initial list of links
    #     h3_and_links = get_valid_h3_and_links(driver)
    #     print(f"Found {len(h3_and_links)} valid h3 elements and links for query: {query}")
    #
    #     for h3_text, link_href in h3_and_links:
    #         try:
    #             print(f"Attempting to click link for: {h3_text}")
    #
    #             # Re-fetch the link dynamically to avoid stale references
    #             link = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, f"//a[@href='{link_href}']"))
    #             )
    #             driver.execute_script("arguments[0].scrollIntoView(true);", link)
    #
    #             # Check clickability dynamically
    #             if link.is_displayed() and link.is_enabled():
    #                 print(f"Link is clickable: {h3_text}")
    #                 driver.execute_script("arguments[0].click();", link)
    #                 time.sleep(10)  # Wait for navigation
    #             else:
    #                 print(f"Link is not clickable: {h3_text}")
    #
    #             # Validate page content
    #             if "Furnished" in driver.page_source:
    #                 print(f"Matching page found: {driver.current_url}")
    #             else:
    #                 print(f"Page did not match criteria: {driver.current_url}")
    #
    #             # Navigate back to results
    #             driver.back()
    #             time.sleep(10)  # Wait for results to reload
    #
    #         except Exception as e:
    #             print(f"Error interacting with link for h3: {h3_text}, Error: {e}")
    #
    # finally:
    #     driver.quit()

if __name__ == "__main__":
    main()
