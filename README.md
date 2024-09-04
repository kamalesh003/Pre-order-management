***Efficient pre-order management system leveraging Celery for distributed task processing***

It involves two parts: 
Publisher site (to let publsiher to sell pre-order products using avaialblity data)
Customer Site (to place pre-order)

**Our solution integrates Celery, Flask, Streamlit, and Redis to streamline pre-order management for e-commerce businesses**. 
Here's how it works:

**Order Placement:** Customers place pre-orders through a user-friendly interface built with Streamlit.

**Order Processing:** Flask serves as the backend, handling incoming pre-orders and interfacing with Celery for task distribution.

**Task Distribution:** Celery distributes order processing tasks across multiple nodes, ensuring efficient handling of large volumes.

**Real-time Updates:** Redis is used to store order data, providing fast access for real-time updates on order status.

**Fulfillment:** Once products are available, Celery coordinates the fulfillment process, ensuring quick and accurate delivery.
