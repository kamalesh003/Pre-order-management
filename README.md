# Efficient Pre-Order Management System

This project leverages Celery for distributed task processing to create an efficient pre-order management system for e-commerce businesses. It integrates **Celery**, **Flask**, **Streamlit**, and **Redis** to streamline the handling of pre-orders and provide real-time updates on order status.

## Key Features

- **Order Placement:** Customers place pre-orders through a user-friendly interface built with Streamlit.
- **Order Processing:** Flask serves as the backend, handling incoming pre-orders and interfacing with Celery for task distribution.
- **Task Distribution:** Celery distributes order processing tasks across multiple nodes, ensuring efficient handling of large volumes.
- **Real-time Updates:** Redis is used to store order data, providing fast access for real-time updates on order status.
- **Fulfillment:** Once products are available, Celery coordinates the fulfillment process, ensuring quick and accurate delivery.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python]
- [Redis]
- [Celery]
- [Flask]
- [Streamlit]

### Running the System

To run the pre-order management system, open a terminal for each of the commands below:

1. **Start Redis Server:**

   ```bash
   redis-server

2. **Start Celery Worker:**
   ```bash
   celery -A celery_tasks.tasks worker --loglevel=info --concurrency=4 --pool=solo

3. **Start Flask Backend:**
   ```bash
   python backend.py

5. **Start Publisher Interface:**
   ```bash
   streamlit run publisher.py
   
6. **Start Customer Interface:**
   ```bash
    streamlit run app.py
   
**Technical Architecture:**
Flask serves as the main backend server.
Streamlit provides the front-end interfaces for both publishers and customers.
Celery handles task distribution across multiple workers, enabling efficient order processing.
Redis is used for caching and storing order data, ensuring real-time updates.
