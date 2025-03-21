from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure the WebDriver
def setup_driver():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        raise

try:
    driver = setup_driver()
except Exception as e:
    print("Could not initialize the driver. Exiting.")
    exit(1)

# List of URLs to check
list1 = ["https://www.google.com/", "https://www.youtube.com/"]

# Keywords to validate per site
dict1 = {
    "https://www.google.com/": ["Google"],
    "https://www.youtube.com/": ["YouTube"],
}

finalbestsites = []

for url in list1:
    try:
        print(f"Visiting: {url}")
        driver.get(url)
        time.sleep(10)  # Allow the page to load completely

        isperfect = True
        checkinglist = dict1.get(url, [])

        if not checkinglist:
            print(f"No keywords provided for {url}. Skipping.")
            continue

        for word in checkinglist:
            if word in driver.page_source:
                print(f"Found the word on the page: {word}")
            else:
                isperfect = False
                print(f"Page did not match criteria: {url}. Missing: {word}")
                break

        if isperfect:
            print("Found one of the useful sites")
            finalbestsites.append(url)
        else:
            print(f"{url} did not meet the criteria.")

    except Exception as e:
        print(f"Error processing URL {url}: {e}")

    time.sleep(10)  # Small delay before the next site

print("\nThese are the correct sites which have everything in them:")
for site in finalbestsites:
    print(site)

# Clean up the WebDriver
driver.quit()
