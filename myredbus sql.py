#!/usr/bin/env python
# coding: utf-8

# In[253]:


#importing libraries
import pandas as pd
import mysql.connector
import numpy as np
import streamlit as slt  # Make sure you have streamlit installed

# Load CSV data into DataFrames
file_paths = [
    r"D:\MSP REDBUS PROJECT\df_buses_1.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_2.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_3.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_4.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_R.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_SB.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_H.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_AS.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_9.csv",
    r"D:\MSP REDBUS PROJECT\df_buses_10.csv"
]

# Read CSV files into DataFrames
dataframes = []
for path in file_paths:
    try:
        df = pd.read_csv(path)
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {path}: {e}")

# Concatenate DataFrames
Final_df = pd.concat(dataframes, ignore_index=True)

# Check if Final_df is empty
if Final_df.empty:
    print("Final_df is empty. Please check your CSV files.")
else:
    print(Final_df.head())  # Check the first few rows
    print(Final_df.info())  # Check the structure and data types

    # Convert prices to numeric, handling errors
    Final_df["Price"] = Final_df["Price"].str.replace("INR", "", regex=False).astype(float, errors='ignore')

    # Filter prices below or equal to 7000
    Final_df = Final_df[Final_df["Price"] <= 7000]

    # Fill NaN values in Price column with 0
    Final_df["Price"] = Final_df["Price"].fillna(0)

    # Replace NaN values with None for database compatibility
    Final_df = Final_df.where(pd.notnull(Final_df), None)

    # Save to CSV for backup or later use
    path = r"D:\MSP REDBUS PROJECT\Final_busdetails_df.csv"
    Final_df.to_csv(path, index=False)

    # Database connection
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="RED_BUS_DATA")
        my_cursor = conn.cursor()

        # Table Creation
        my_cursor.execute('''CREATE TABLE IF NOT EXISTS bus_details (
                              ID INT AUTO_INCREMENT PRIMARY KEY,
                              Bus_name VARCHAR(255) NOT NULL,
                              Bus_type VARCHAR(255) NOT NULL,
                              Start_time VARCHAR(255) NOT NULL,
                              End_time VARCHAR(255) NOT NULL,
                              Total_duration VARCHAR(255) NOT NULL,
                              Price FLOAT NULL,
                              Seats_Available VARCHAR(255) NOT NULL,
                              Ratings FLOAT NULL,
                              Route_link VARCHAR(255) NULL,
                              Route_name VARCHAR(255) NULL)''')

        print("Table Created successfully")

        # SQL query to insert data into bus_details table
        insert_query = '''INSERT INTO bus_details(
                            Bus_name,
                            Bus_type,
                            Start_time,
                            End_time,
                            Total_duration,
                            Price,
                            Seats_Available,
                            Ratings,
                            Route_link,
                            Route_name)
                          VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        data = Final_df.values.tolist()

        # Inserting data into the database
        my_cursor.executemany(insert_query, data)
        conn.commit()
        print("Values inserted successfully")

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the cursor and connection
        if my_cursor:
            my_cursor.close()
        if conn:
            conn.close()


# In[ ]:




