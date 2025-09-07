from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a Sherdog fighter page (example: Kamaru Usman)
url = "https://www.sherdog.com/fighter/Kamaru-Usman-43447"
driver.get(url)

# Get page source
html_source = driver.page_source
print(html_source[:1000])  # print first 1000 chars to check

# Close browser
driver.quit()
