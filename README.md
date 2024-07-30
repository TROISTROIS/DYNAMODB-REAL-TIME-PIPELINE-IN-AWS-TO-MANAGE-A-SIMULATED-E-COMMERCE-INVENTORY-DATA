# REAL-TIME-DATA-PIPELINE-IN-AWS-TO-MANAGE-A-SIMULATED-E-COMMERCE-INVENTORY-DATA-WITH-DYNAMODB
## Objective: 
Design and implement a real-time data processing pipeline in AWS to manage a simulated e-commerce platform's inventory data.
</br>
## Problem Statement:
My e-commerce platform needs to track real-time inventory changes for its products. Every time a product is added, removed, or its quantity changes, an event is generated. My task is to design a real-time processing system that will capture these events, process them, and update a real-time inventory system.
</br>
## Requirements:
- **Data Source:** A mock script I will design will simulate inventory events by generating and publishing them to an AWS Kinesis stream.
- **Event Processing:** Use AWS EventBridge to capture events from the Kinesis stream and forward them for processing.
- **Data Transformation and Storage:**
  - Process the real-time stream of data to calculate the latest inventory state for each product.
  - Store the processed data in DynamoDB, ensuring that inventory counts remain consistent and accurate.
- **Inventory Events Include:**
  - Product added to inventory.
  - Product removed from inventory.
  - Product quantity changes (increment or decrement).
## Steps:
1. Create a Kinesis stream to capture real-time inventory events.</br>
2. Design a mock script that simulates the inventory events and publishes them to the Kinesis stream in real-time.</br>
3. Set up AWS EventBridge to capture the events from the Kinesis stream.</br>
4. Process the real-time events, and according to the event type, update the product's state in DynamoDB.</br>
5. Ensure DynamoDB maintains the latest inventory state for all products and handles high-velocity updates reliably.</br>
