#!/usr/bin/env python
# coding: utf-8

# In[82]:


pip install streamlit-option-menu


# In[83]:


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[84]:


state_links=["https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/astc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile"]


# In[85]:


##KERALA ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Kerala_link_route(path, num_pages):
    LINKS_KERALA = []
    ROUTE_KERALA = []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_KERALA.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_KERALA.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_KERALA, ROUTE_KERALA

# Run the function for 5 pages
LINKS_KERALA, ROUTE_KERALA = Kerala_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_KERALA)
print("Bus Route Names:", ROUTE_KERALA)

# Close the driver
driver.quit()


# In[86]:


df_k=pd.DataFrame({"Route_name":ROUTE_KERALA,"Route_link":LINKS_KERALA})
df_k


# In[87]:


path = r"D:\MSP REDBUS PROJECT\df_k.csv"

df_k.to_csv(path,index=False)


# In[88]:


##ANDHRA ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Andhra_link_route(path, num_pages):
    LINKS_ANDHRA = []
    ROUTE_ANDHRA = []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_ANDHRA.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_ANDHRA.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_ANDHRA, ROUTE_ANDHRA

# Run the function for 5 pages
LINKS_ANDHRA, ROUTE_ANDHRA = Andhra_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_ANDHRA)
print("Bus Route Names:", ROUTE_ANDHRA)

# Close the driver
driver.quit()


# In[89]:


df_A=pd.DataFrame({"Route_name":ROUTE_ANDHRA,"Route_link":LINKS_ANDHRA})
df_A


# In[90]:


path = r"D:\MSP REDBUS PROJECT\df_A.csv"
df_A.to_csv(path,index=False)


# In[91]:


##TELUGANA ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Telugana_link_route(path, num_pages):
    LINKS_TELUGANA = []
    ROUTE_TELUGANA = []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_TELUGANA.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_TELUGANA.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_TELUGANA, ROUTE_TELUGANA

# Run the function for 5 pages
LINKS_TELUGANA, ROUTE_TELUGANA = Telugana_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_TELUGANA)
print("Bus Route Names:", ROUTE_TELUGANA)

# Close the driver
driver.quit()


# In[92]:


df_T=pd.DataFrame({"Route_name":ROUTE_TELUGANA,"Route_link":LINKS_TELUGANA})
df_T


# In[93]:


path = r"D:\MSP REDBUS PROJECT\df_T.csv"
df_T.to_csv(path,index=False)


# In[94]:


##GOA
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Kadamba_link_route(path, num_pages):
    LINKS_KADAMBA = []
    ROUTE_KADAMBA = []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_KADAMBA.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_KADAMBA.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_KADAMBA, ROUTE_KADAMBA

# Run the function for 5 pages
LINKS_KADAMBA, ROUTE_KADAMBA = Kadamba_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_KADAMBA)
print("Bus Route Names:", ROUTE_KADAMBA)

# Close the driver
driver.quit()


# In[95]:


df_G=pd.DataFrame({"Route_name":ROUTE_KADAMBA,"Route_link":LINKS_KADAMBA})
df_G


# In[96]:


path = r"D:\MSP REDBUS PROJECT\df_G.csv"
df_G.to_csv(path,index=False)


# In[97]:


##RAJASTHAN ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Rajasthan_link_route(path, num_pages):
    LINKS_RAJASTHAN = []
    ROUTE_RAJASTHAN= []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_RAJASTHAN.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_RAJASTHAN.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_RAJASTHAN, ROUTE_RAJASTHAN

# Run the function for 5 pages
LINKS_RAJASTHAN, ROUTE_RAJASTHAN = Rajasthan_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_RAJASTHAN)
print("Bus Route Names:", ROUTE_RAJASTHAN)

# Close the driver
driver.quit()


# In[98]:


df_R=pd.DataFrame({"Route_name":ROUTE_RAJASTHAN,"Route_link":LINKS_RAJASTHAN})
df_R


# In[99]:


path = r"D:\MSP REDBUS PROJECT\df_R.csv"
df_R.to_csv(path,index=False)


# In[100]:


##SOUTH BENGAL ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Southbengal_link_route(path, num_pages):
    LINKS_SOUTHBENGAL = []
    ROUTE_SOUTHBENGAL= []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_SOUTHBENGAL.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_SOUTHBENGAL.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_SOUTHBENGAL, ROUTE_SOUTHBENGAL

# Run the function for 5 pages
LINKS_SOUTHBENGAL, ROUTE_SOUTHBENGAL = Southbengal_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_SOUTHBENGAL)
print("Bus Route Names:", ROUTE_SOUTHBENGAL)

# Close the driver
driver.quit()


# In[101]:


df_SB=pd.DataFrame({"Route_name":ROUTE_SOUTHBENGAL,"Route_link":LINKS_SOUTHBENGAL})
df_SB


# In[102]:


path = r"D:\MSP REDBUS PROJECT\df_SB.csv"
df_SB.to_csv(path,index=False)


# In[103]:


##HARYANA ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Haryana_link_route(path, num_pages):
    LINKS_HARYANA = []
    ROUTE_HARYANA= []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_HARYANA.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_HARYANA.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_HARYANA, ROUTE_HARYANA

# Run the function for 5 pages
LINKS_HARYANA, ROUTE_HARYANA = Haryana_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_HARYANA)
print("Bus Route Names:", ROUTE_HARYANA)

# Close the driver
driver.quit()


# In[104]:


df_H=pd.DataFrame({"Route_name":ROUTE_HARYANA,"Route_link":LINKS_HARYANA})
df_H


# In[105]:


path = r"D:\MSP REDBUS PROJECT\df_H.csv"
df_H.to_csv(path,index=False)


# In[106]:


##ASSAM ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/astc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Assam_link_route(path, num_pages):
    LINKS_ASSAM = []
    ROUTE_ASSAM= []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_ASSAM.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_ASSAM.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_ASSAM, ROUTE_ASSAM

# Run the function for 5 pages
LINKS_ASSAM, ROUTE_ASSAM = Assam_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_ASSAM)
print("Bus Route Names:", ROUTE_ASSAM)

# Close the driver
driver.quit()


# In[107]:


df_AS=pd.DataFrame({"Route_name":ROUTE_ASSAM,"Route_link":LINKS_ASSAM})
df_AS


# In[108]:


path = r"D:\MSP REDBUS PROJECT\df_AS.csv"
df_AS.to_csv(path,index=False)


# In[109]:


##UTTAR PRADESH ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def UP_link_route(path, num_pages):
    LINKS_UP = []
    ROUTE_UP= []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_UP.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_UP.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_UP, ROUTE_UP

# Run the function for 5 pages
LINKS_UP, ROUTE_UP = UP_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_UP)
print("Bus Route Names:", ROUTE_UP)

# Close the driver
driver.quit()


# In[110]:


df_UP=pd.DataFrame({"Route_name":ROUTE_UP,"Route_link":LINKS_UP})
df_UP


# In[111]:


path = r"D:\MSP REDBUS PROJECT\df_UP.csv"
df_UP.to_csv(path,index=False)


# In[112]:


##WEST BENGAL ROUTES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the webpage
driver.get("https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile")
driver.maximize_window()

# Set up WebDriverWait
wait = WebDriverWait(driver, 20)

def Westbengal_link_route(path, num_pages):
    LINKS_WESTBENGAL = []
    ROUTE_WESTBENGAL= []

    for page in range(1, num_pages + 1):  # Iterate over the number of pages
        print(f"Scraping page {page}")
        
        # Retrieve the route links
        paths = driver.find_elements(By.XPATH, path)
        
        # Add links to the list
        for link in paths:
            href = link.get_attribute("href")
            LINKS_WESTBENGAL.append(href)
        
        # Add names of the routes to the list
        for route in paths:
            ROUTE_WESTBENGAL.append(route.text)
        
        if page < num_pages:  # Only paginate if we have more pages to scrape
            try:
                # Wait for the pagination element to be visible
                pagination = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "DC_117_paginationTable")]')))
                
                # Find all pagination buttons
                page_tabs = pagination.find_elements(By.XPATH, '//div[contains(@class, "DC_117_pageTabs")]')
                
                if page <= len(page_tabs):
                    # Click the tab for the current page
                    tab_to_click = page_tabs[page]
                    
                    # Scroll the element into view and click it
                    driver.execute_script("arguments[0].scrollIntoView(true);", tab_to_click)
                    time.sleep(1)  # Give a short delay to ensure the button is fully in view
                    tab_to_click.click()
                    
                    # Wait for the next page to load
                    time.sleep(3)
                else:
                    print("No more pages to paginate.")
                    break
                
            except Exception as e:
                print(f"Error during pagination at page {page}: {e}")
                break
            
    return LINKS_WESTBENGAL, ROUTE_WESTBENGAL

# Run the function for 5 pages
LINKS_WESTBENGAL, ROUTE_WESTBENGAL = Westbengal_link_route("//a[@class='route']", num_pages=5)

# Print the results
print("Bus Route Links:", LINKS_WESTBENGAL)
print("Bus Route Names:", ROUTE_WESTBENGAL)

# Close the driver
driver.quit()


# In[113]:


df_WB=pd.DataFrame({"Route_name":ROUTE_WESTBENGAL,"Route_link":LINKS_WESTBENGAL})
df_WB


# In[114]:


path = r"D:\MSP REDBUS PROJECT\df_WB.csv"
df_WB.to_csv(path,index=False)


# In[115]:


# concat all the bus link and route names in one dataframe
df=pd.concat([df_k,df_A,df_T,df_G,df_R,df_H,df_SB,df_AS,df_UP,df_WB],ignore_index=True)
df


# In[151]:


# change dataframe to csv
path=r"D:\MSP REDBUS PROJECT\df_route.csv"
df.to_csv(path,index=False)


# In[ ]:




