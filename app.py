# app.py
import streamlit as st
import requests
import json
import redis
import time
from datetime import datetime

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Function to get product details by ID
def get_product_by_id(product_id):
    product_json = redis_client.get(f"product:{product_id}")
    return json.loads(product_json) if product_json else None

# Streamlit app for pre-order
st.title("Pre-order Products")

# Input fields
product_id = st.text_input("Enter Product ID")
product = None
if product_id:
    product = get_product_by_id(product_id)
    if product:
        st.write(f"Product Name: {product['name']}")
        st.write(f"Product Price: ${product['price']}")
        availability_datetime = datetime.fromtimestamp(product['availability_timestamp'])
        st.write(f"Available on: {availability_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.warning("Product not found.")

user_name = st.text_input("Your Name")
user_email = st.text_input("Your Email")

# Submit pre-order
if st.button("Submit Pre-order"):
    if product and user_name and user_email:
        response = requests.post("http://localhost:5000/preorder", json={
            "product_id": product_id,
            "name": user_name,
            "email": user_email
        })
        
        if response.status_code == 200:
            task_id = response.json().get("task_id")
            st.success("Pre-order submitted successfully!")
            
            # Check task status
            status = "Pending"
            while status == "Pending":
                task_response = requests.get(f"http://localhost:5000/task_status/{task_id}")
                if task_response.status_code == 200:
                    task_status = task_response.json().get("status")
                    st.info(f"Task Status: {task_status}")
                    if task_status in ["success", "failure"]:
                        status = task_status.capitalize()
                    time.sleep(5)
                else:
                    st.error("Failed to check task status.")
        else:
            st.error("Failed to submit pre-order.")
    else:
        st.warning("Please fill out all fields.")
