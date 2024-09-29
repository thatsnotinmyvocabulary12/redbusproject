#!/usr/bin/env python
# coding: utf-8

# In[485]:


# Importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time
#pip install streamlit mysql-connector-python pandas plotly streamlit-option-menu
# Load CSV data into DataFrames
# Kerala bus
lists_k = []
df_k = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_k.csv")
for i, r in df_k.iterrows():
    lists_k.append(r["Route_name"])

# Andhra bus
lists_A = []
df_A = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_A.csv")
for i, r in df_A.iterrows():
    lists_A.append(r["Route_name"])

# Telungana bus
lists_T = []
df_T = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_T.csv")
for i, r in df_T.iterrows():
    lists_T.append(r["Route_name"])

# Goa bus
lists_g = []
df_G = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_G.csv")
for i, r in df_G.iterrows():
    lists_g.append(r["Route_name"])

# Rajastan bus
lists_R = []
df_R = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_R.csv")
for i, r in df_R.iterrows():
    lists_R.append(r["Route_name"])

# South Bengal bus 
lists_SB = []
df_SB = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_SB.csv")
for i, r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

# Haryana bus
lists_H = []
df_H = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_H.csv")
for i, r in df_H.iterrows():
    lists_H.append(r["Route_name"])

# Assam bus
lists_AS = []
df_AS = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_AS.csv")
for i, r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

# UP bus
lists_UP = []
df_UP = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_UP.csv")
for i, r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

# West Bengal bus
lists_WB = []
df_WB = pd.read_csv(r"D:\MSP REDBUS PROJECT\df_WB.csv")
for i, r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])


# In[486]:


#setting up streamlit page
slt.set_page_config(layout="wide")
from streamlit_option_menu import option_menu
web = option_menu(
    menu_title="🚍ONLINE BUS TICKET BOOKING",
    options=["Home", "🌐 States and Routes "],
    icons=["house", "map"],
    orientation="horizontal"
)


# In[487]:


# Route lists
route_lists = {
    "Kerala": lists_k,
    "Andhra Pradesh": lists_A,
    "Telangana": lists_T,
    "Goa": lists_g,
    "Rajasthan": lists_R,
    "South Bengal": lists_SB,
    "Haryana": lists_H,
    "Assam": lists_AS,
    "Uttar Pradesh": lists_UP,
    "West Bengal": lists_WB,
}

# Function to query bus details based on selection
def query_bus_details(conn, route, fare_range, min_rating, bus_type):
    # Define fare range
    if fare_range == "50-700":
        fare_min, fare_max = 50, 700
    elif fare_range == "700-1000":
        fare_min, fare_max = 700, 1000
    else:
        fare_min, fare_max = 1000, 100000

    # Define bus type condition
    bus_type_condition = " OR ".join([f"Bus_type LIKE '%{bt}%'" for bt in bus_type])

    # Construct the SQL query without AC filtration
    query = f'''
        SELECT * FROM bus_details 
        WHERE Route_name = %s 
        AND Price BETWEEN %s AND %s
        AND ({bus_type_condition}) 
        AND Ratings >= %s
    '''

    try:
        # Execute the query with parameters
        params = (route, fare_min, fare_max, min_rating)
        df = pd.read_sql(query, conn, params=params)
        
        if df.empty:
            slt.warning("No data found for the given filters.")
        else:
            slt.write(df)  # Display the DataFrame if data is retrieved
    except Exception as e:
        slt.error(f"An error occurred while querying: {e}")


# In[488]:


# Custom CSS for modern attractive look
modern_css = """
<style>
    /* Background image with soft blur for subtle effect */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        backdrop-filter: blur(10px);  /* Soft blur to background */
        -webkit-backdrop-filter: blur(10px);
    }

    /* Card-like structure for the content area */
    .css-1offfwp.e1fqkh3o3 {
        background-color: rgba(255, 255, 255, 0.85);  /* Slightly transparent white background */
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);  /* Softer shadow for card effect */
        max-width: 900px;  /* Limit width for better readability */
        margin: 40px auto;  /* Center align */
    }

    /* Modern font styling for titles */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif;
        color: #333333;  /* Dark grey for professional look */
        background-color: rgba(255, 255, 255, 0.7);  /* Light background */
        padding: 10px 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);  /* Title shadow effect */
    }

    /* Paragraph and span styling */
    p, span {
        font-family: 'Open Sans', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #FFFFFF;  /* Black text for clarity */
        text-shadow: none;
        padding: 10px;
        margin-bottom: 15px;
    }

    /* Subtle button styling */
    .stButton button {
        background-color: #FF4B4B;  /* Bright color for call to action */
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    
    /* Hover effect for buttons */
    .stButton button:hover {
        background-color: #FF0000;
        box-shadow: 0px 6px 15px rgba(255, 75, 75, 0.4);
    }

    /* Add spacing between sections */
    .css-1offfwp.e1fqkh3o3 p {
        margin-bottom: 25px;
    }

    /* Footer styling */
    footer {
        text-align: center;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.1);
        font-size: 14px;
        margin-top: 40px;
    }
</style>
"""

# Apply custom CSS for enhanced layout
slt.markdown(modern_css, unsafe_allow_html=True)

# Main Content
if web == "Home":
    # Logo and title
    slt.image(r"C:\Users\91934\Desktop\MOVIES\bus logo.jpg", width=150)
    
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")

    # Subsection: Domain
    slt.subheader(":blue[Domain:]  Transportation")

    # Subsection: Objective
    slt.subheader(":blue[🎯Objective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' project automates the extraction of bus routes, schedules, prices, seat availability, and ratings from Redbus using Selenium. It presents the data in a Streamlit interface, allowing users to filter and compare options for informed travel decisions.")

    # Overview section
    slt.subheader(":blue[🔍Overview:]")
    slt.markdown("""
    **Selenium**: A tool for automated web scraping and browser interaction.
    **Pandas**: A Python library for data manipulation and analysis.
    **MySQL**: A database for storing and querying data.
    **Streamlit**: A framework for creating web applications with Python.
    """)

    # Skills section
    slt.subheader(":blue[🛠Skills-taken:]")
    slt.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, Streamlit.")

    # Developer section
    slt.subheader(":blue[👨‍💻Developed-by:]  Mugesh Surya Pradeep")

# States and Routes page setting
if web == "🌐 States and Routes ":
    state = slt.selectbox("Lists of States", list(route_lists.keys()))
    route = slt.selectbox("List of Routes", route_lists[state])
    
    # Bus Type Filter
    bus_type = slt.multiselect("Choose Bus Types", ["Sleeper", "Seater"], default=["Sleeper"])

    # Price Range Filter
    fare_range = slt.selectbox("Choose Bus Fare Range", ["50-700", "700-1000", "1000 above"])

    # Ratings Filter
    min_rating = slt.slider("Select Minimum Bus Rating", 1.0, 5.0, 3.0, step=0.1)

    # Query and display results based on selected filters
    # Make sure to create a connection to your MySQL database here
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DATA")
    query_bus_details(conn, route, fare_range, min_rating, bus_type)
    
    # Remember to close the connection after you're done
    conn.close()

