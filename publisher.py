# publisher.py
import streamlit as st
import redis
import json
from datetime import datetime

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Streamlit form for adding products
st.title("Add Products for Pre-order")

product_id = st.text_input("Product ID")
product_name = st.text_input("Product Name")
product_price = st.number_input("Product Price", min_value=0.0, step=0.01)
availability_date = st.date_input("Availability Date")
availability_time = st.time_input("Availability Time")



if st.button("Add Product"):
    if product_id and product_name:
        # Combine date and time into a single datetime object
        availability_datetime = datetime.combine(availability_date, availability_time)
        
        product = {
            "id": product_id,
            "name": product_name,
            "price": product_price,
            "availability_timestamp": availability_datetime.timestamp()
        }
        
        # Store product in Redis
        redis_client.set(f"product:{product_id}", json.dumps(product))
        st.success(f"Product '{product_name}' added successfully!")
    else:
        st.warning("Please fill out all fields.")
