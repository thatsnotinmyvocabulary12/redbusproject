#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime, timedelta


# In[2]:


##KERALA BUS DETAILS
# read the csv file
df=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_k.csv")
df


# In[3]:


#retrive the bus details
driver_k = webdriver.Chrome()
Bus_names_k = []
Bus_types_k = []
Start_Time_k = []
End_Time_k = []
Ratings_k = []
Total_Duration_k = []
Prices_k = []
Seats_Available_k = []
Route_names = []
Route_links = []

for i,r in df.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_k.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_k.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
        
    # click elements to views bus
    try:
        clicks = driver_k.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue  
    time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_k.page_source
        
        # Use ActionChains to perform a PAGE_DOWN
        ActionChains(driver_k).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_k.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_k.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_k.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_k.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_k.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_k.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_k.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_k.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_k.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_k.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_k.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_k.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_k.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_k.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_k.append(ratings.text)
    for price_elem in price:
        Prices_k.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_k.append(seats_elem.text)
        
print("Successfully Completed")
driver_k.quit()


# In[4]:


# from list to convert data frame
data = {
    'Bus_name': Bus_names_k,
    'Bus_type': Bus_types_k,
    'Start_time': Start_Time_k,
    'End_time': End_Time_k,
    'Total_duration': Total_Duration_k,
    'Price': Prices_k,
    "Seats_Available":Seats_Available_k,
    "Ratings":Ratings_k,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_1 = pd.DataFrame(data)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_1.csv"
df_buses_1.to_csv(path,index=False)


# In[5]:


df_buses_1


# In[6]:


##ANDHRA BUS DETAILS
# read the csv file
df_1=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_A.csv")
df_1


# In[7]:


#retrive the bus details
driver_A = webdriver.Chrome()
Bus_names_A = []
Bus_types_A = []
Start_Time_A = []
End_Time_A = []
Ratings_A = []
Total_Duration_A = []
Prices_A = []
Seats_Available_A = []
Route_names = []
Route_links = []

for i,r in df_1.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_A.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_A.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)

    # click elements to views bus
    try:
        clicks = driver_A.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue  
    time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_A.page_source
        
        # Use ActionChains to perform a PAGE_DOWN
        ActionChains(driver_A).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  # Adjust sleep time as needed
        
        new_page_source = driver_A.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_A.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_A.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_A.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_A.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_A.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_A.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_A.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_A.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_A.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_A.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_A.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_A.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_A.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_A.append(ratings.text)
    for price_elem in price:
        Prices_A.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_A.append(seats_elem.text)
        
print("Successfully Completed")
driver_A.quit()


# In[8]:


# from list to convert data frame
data_1 = {
    'Bus_name': Bus_names_A,
    'Bus_type': Bus_types_A,
    'Start_time': Start_Time_A,
    'End_time': End_Time_A,
    'Total_duration': Total_Duration_A,
    'Price': Prices_A,
    "Seats_Available":Seats_Available_A,
    "Ratings":Ratings_A,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_2 = pd.DataFrame(data_1)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_2.csv"
df_buses_2.to_csv(path,index=False)


# In[9]:


df_buses_2


# In[10]:


##TELUGANA BUS DETAILS
# read the csv file
df_2=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_T.csv")
df_2


# In[11]:


# retrive the bus details
driver_T = webdriver.Chrome()
Bus_names_T = []
Bus_types_T = []
Start_Time_T = []
End_Time_T = []
Ratings_T = []
Total_Duration_T = []
Prices_T = []
Seats_Available_T = []
Route_names = []
Route_links = []

for i,r in df_2.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_T.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_T.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)

    # click elements to views bus
    try:
        clicks = driver_T.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue  
    time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_T.page_source
        
        ActionChains(driver_T).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_T.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_T.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_T.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_T.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_T.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_T.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_T.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_T.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_T.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_T.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_T.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_T.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_T.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_T.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_T.append(ratings.text)
    for price_elem in price:
        Prices_T.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_T.append(seats_elem.text)
print("Successfully Completed")
driver_T.quit()


# In[12]:


# from list to convert data frame
data_3 = {
    'Bus_name': Bus_names_T,
    'Bus_type': Bus_types_T,
    'Start_time': Start_Time_T,
    'End_time': End_Time_T,
    'Total_duration': Total_Duration_T,
    'Price': Prices_T,
    "Seats_Available":Seats_Available_T,
    "Ratings":Ratings_T,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_3 = pd.DataFrame(data_3)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_3.csv"
df_buses_3.to_csv(path,index=False)


# In[13]:


df_buses_3


# In[14]:


##GOA BUS DETAILS
# read the csv file
df_3=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_G.csv")
df_3


# In[15]:


# retrive the bus details
driver_G = webdriver.Chrome()
Bus_names_G = []
Bus_types_G = []
Start_Time_G = []
End_Time_G = []
Ratings_G = []
Total_Duration_G = []
Prices_G = []
Seats_Available_G = []
Route_names = []
Route_links = []

for i,r in df_3.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_G.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_G.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
   
    time.sleep(2)
    scrolling = True
    while scrolling:
        old_page_source = driver_G.page_source
        
        ActionChains(driver_G).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_G.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_G.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_G.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_G.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_G.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_G.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_G.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_G.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_G.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_G.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_G.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_G.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_G.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_G.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_G.append(ratings.text)
    for price_elem in price:
        Prices_G.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_G.append(seats_elem.text)
print("Successfully Completed")
driver_G.quit()


# In[16]:


# from list to convert data frame
data_4 = {
    'Bus_name': Bus_names_G,
    'Bus_type': Bus_types_G,
    'Start_time': Start_Time_G,
    'End_time': End_Time_G,
    'Total_duration': Total_Duration_G,
    'Price': Prices_G,
    "Seats_Available":Seats_Available_G,
    "Ratings":Ratings_G,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_4 = pd.DataFrame(data_4)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_4.csv"
df_buses_4.to_csv(path,index=False)


# In[17]:


df_buses_4


# In[18]:


##RAJASTHAN BUS DETAILS
# read the csv file
df_4=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_R.csv")
df_4


# In[19]:


# retrive the bus details
driver_R = webdriver.Chrome()
Bus_names_R = []
Bus_types_R = []
Start_Time_R = []
End_Time_R = []
Ratings_R = []
Total_Duration_R = []
Prices_R = []
Seats_Available_R = []
Route_names_R = []
Route_links_R = []

for i,r in df_4.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_R.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_R.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)

    scrolling = True
    while scrolling:
        old_page_source = driver_R.page_source
        
        ActionChains(driver_R).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_R.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_R.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_R.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_R.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_R.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_R.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_R.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_R.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_R.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_R.append(bus.text)
        Route_links_R.append(link)
        Route_names_R.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_R.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_R.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_R.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_R.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_R.append(ratings.text)
    for price_elem in price:
        Prices_R.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_R.append(seats_elem.text)
print("Successfully Completed")
driver_R.quit()


# In[20]:


# from list to convert data frame
data_5 = {
    'Bus_name': Bus_names_R,
    'Bus_type': Bus_types_R,
    'Start_time': Start_Time_R,
    'End_time': End_Time_R,
    'Total_duration': Total_Duration_R,
    'Price': Prices_R,
    "Seats_Available":Seats_Available_R,
    "Ratings":Ratings_R,
    'Route_link': Route_links_R,
    'Route_name': Route_names_R
}

df_buses_5 = pd.DataFrame(data_5)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_R.csv"
df_buses_5.to_csv(path,index=False)


# In[21]:


df_buses_5


# In[22]:


##SOUTH BENGAL BUS DETAILS
# read the csv file
df_5=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_SB.csv")
df_5


# In[23]:


# retrive the bus details
driver_SB = webdriver.Chrome()
Bus_names_SB = []
Bus_types_SB = []
Start_Time_SB = []
End_Time_SB = []
Ratings_SB = []
Total_Duration_SB = []
Prices_SB = []
Seats_Available_SB = []
Route_names = []
Route_links = []

for i,r in df_5.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_SB.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_SB.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_SB.page_source
        
        ActionChains(driver_SB).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_SB.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_SB.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_SB.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_SB.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_SB.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_SB.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_SB.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_SB.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_SB.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_SB.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_SB.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_SB.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_SB.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_SB.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_SB.append(ratings.text)
    for price_elem in price:
        Prices_SB.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_SB.append(seats_elem.text)
print("Successfully Completed")
driver_SB.quit()


# In[24]:


# from list to convert data frame
data_6 = {
    'Bus_name': Bus_names_SB,
    'Bus_type': Bus_types_SB,
    'Start_time': Start_Time_SB,
    'End_time': End_Time_SB,
    'Total_duration': Total_Duration_SB,
    'Price': Prices_SB,
    "Seats_Available":Seats_Available_SB,
    "Ratings":Ratings_SB,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_6 = pd.DataFrame(data_6)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_SB.csv"
df_buses_6.to_csv(path,index=False)


# In[25]:


df_buses_6


# In[26]:


##HARYANA BUS DETAILS
# read the csv file
df_6=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_H.csv")
df_6


# In[34]:


# retrive the bus details
driver_H = webdriver.Chrome()
Bus_names_H = []
Bus_types_H = []
Start_Time_H = []
End_Time_H = []
Ratings_H = []
Total_Duration_H = []
Prices_H = []
Seats_Available_H = []
Route_names_H = []
Route_links_H = []
for i,r in df_6.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_H.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_H.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
         
    scrolling = True
    while scrolling:
        old_page_source = driver_H.page_source
        
        ActionChains(driver_H).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_H.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_H.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_H.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_H.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_H.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_H.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_H.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_H.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_H.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_H.append(bus.text)
        Route_links_H.append(link)
        Route_names_H.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_H.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_H.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_H.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_H.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_H.append(ratings.text)
    for price_elem in price:
        Prices_H.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_H.append(seats_elem.text)
print("Successfully Completed")
driver_H.quit()


# In[35]:


# from list to convert data frame
data_7 = {
    'Bus_name': Bus_names_H,
    'Bus_type': Bus_types_H,
    'Start_time': Start_Time_H,
    'End_time': End_Time_H,
    'Total_duration': Total_Duration_H,
    'Price': Prices_H,
    "Seats_Available":Seats_Available_H,
    "Ratings":Ratings_H,
    'Route_link': Route_links_H,
    'Route_name': Route_names_H
}

df_buses_7 = pd.DataFrame(data_7)
#convert dataframe to csv
path=r"D:/MSP REDBUS PROJECT/df_buses_H.csv"
df_buses_7.to_csv(path,index=False)


# In[36]:


df_buses_7


# In[37]:


##ASSAM BUS DETAILS
# read the csv file
df_7=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_AS.csv")
df_7


# In[51]:


# retrive the bus details
driver_AS = webdriver.Chrome()
Bus_names_AS = []
Bus_types_AS = []
Start_Time_AS = []
End_Time_AS = []
Ratings_AS = []
Total_Duration_AS = []
Prices_AS = []
Seats_Available_AS = []
Route_names_AS = []
Route_links_AS = []
for i,r in df_7.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]
# Loop through each link
    driver_AS.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_AS.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
         
    scrolling = True
    while scrolling:
        old_page_source = driver_AS.page_source
        
        ActionChains(driver_AS).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_AS.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_AS.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_AS.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_AS.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_AS.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_AS.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_AS.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_AS.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_AS.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_AS.append(bus.text)
        Route_links_AS.append(link)
        Route_names_AS.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_AS.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_AS.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_AS.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_AS.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_AS.append(ratings.text)
    for price_elem in price:
        Prices_AS.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_AS.append(seats_elem.text)
print("Successfully Completed")
driver_AS.quit()


# In[52]:


# from list to convert data frame
data_8 = {
    'Bus_name': Bus_names_AS,
    'Bus_type': Bus_types_AS,
    'Start_time': Start_Time_AS,
    'End_time': End_Time_AS,
    'Total_duration': Total_Duration_AS,
    'Price': Prices_AS,
    "Seats_Available":Seats_Available_AS,
    "Ratings":Ratings_AS,
    'Route_link': Route_links_AS,
    'Route_name': Route_names_AS
}

df_buses_8 = pd.DataFrame(data_8)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_AS.csv"
df_buses_8.to_csv(path,index=False)


# In[53]:


df_buses_8


# In[74]:


##UTTAR PRADESH BUS DETAILS
# read the csv file
df_8=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_UP.csv")
df_8


# In[55]:


# retrive the bus details
driver_UP = webdriver.Chrome()
Bus_names_UP = []
Bus_types_UP = []
Start_Time_UP = []
End_Time_UP = []
Ratings_UP = []
Total_Duration_UP = []
Prices_UP = []
Seats_Available_UP = []
Route_names = []
Route_links = []

for i,r in df_8.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_UP.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_UP.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2) 
        
    scrolling = True
    while scrolling:
        old_page_source = driver_UP.page_source
        
        ActionChains(driver_UP).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_UP.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_UP.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_UP.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_UP.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_UP.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_UP.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_UP.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_UP.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_UP.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_UP.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_UP.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_UP.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_UP.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_UP.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_UP.append(ratings.text)
    for price_elem in price:
        Prices_UP.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_UP.append(seats_elem.text)
print("Successfully Completed")
driver_UP.quit()


# In[56]:


# from list to convert data frame
data_9 = {
    'Bus_name': Bus_names_UP,
    'Bus_type': Bus_types_UP,
    'Start_time': Start_Time_UP,
    'End_time': End_Time_UP,
    'Total_duration': Total_Duration_UP,
    'Price': Prices_UP,
    "Seats_Available":Seats_Available_UP,
    "Ratings":Ratings_UP,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_9 = pd.DataFrame(data_9)
#convert dataframe to csv
path=r"D:\MSP REDBUS PROJECT/df_buses_9.csv"
df_buses_9.to_csv(path,index=False)


# In[57]:


df_buses_9


# In[58]:


##WEST BENGAL BUS DETAILS
# read the csv file
df_9=pd.read_csv(r"D:\MSP REDBUS PROJECT\df_WB.csv")
df_9


# In[59]:


# retrive the bus details
driver_WB = webdriver.Chrome()
Bus_names_WB = []
Bus_types_WB = []
Start_Time_WB = []
End_Time_WB = []
Ratings_WB = []
Total_Duration_WB = []
Prices_WB = []
Seats_Available_WB = []
Route_names = []
Route_links = []

for i,r in df_9.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]
# Loop through each link
    driver_WB.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_WB.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2) 
        
    scrolling = True
    while scrolling:
        old_page_source = driver_WB.page_source
        
        ActionChains(driver_WB).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_WB.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_WB.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_WB.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_WB.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_WB.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_WB.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_WB.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_WB.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_WB.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_WB.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_WB.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_WB.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_WB.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_WB.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_WB.append(ratings.text)
    for price_elem in price:
        Prices_WB.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_WB.append(seats_elem.text)
print("Successfully Completed")
driver_WB.quit()


# In[60]:


# from list to convert data frame
data_10 = {
    'Bus_name': Bus_names_WB,
    'Bus_type': Bus_types_WB,
    'Start_time': Start_Time_WB,
    'End_time': End_Time_WB,
    'Total_duration': Total_Duration_WB,
    'Price': Prices_WB,
    "Seats_Available":Seats_Available_WB,
    "Ratings":Ratings_WB,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_10 = pd.DataFrame(data_10)
#convert dataframe to csv
path=r"D:MSP REDBUS PROJECT/df_buses_10.csv"
df_buses_10.to_csv(path,index=False)


# In[61]:


df_buses_10


# In[ ]:




