E-Commerce Advisor
Introduction
E-Commerce Advisor is a simple product search and comparison system built using Python and Streamlit.
The main idea behind this project is to make product searching easier. Instead of checking multiple websites and comparing products manually, this system allows users to search products in one place and view useful information like prices, price changes, and review patterns.
This project is a small simulation of how an e-commerce assistant could work using structured product data.

What This Project Does
This application allows users to:
Search products by category (for example: smartwatch)


Search by product model name (for example: FitPro X1)


Search using both category and model together


Compare prices from Amazon and Flipkart


Check whether the product price has increased or decreased


Detect duplicate reviews in the dataset


View product features and summary


The product information is stored in a products.json file, and the interface is created using Streamlit.

How the Search Works
When a user enters a search query:
The system reads the product data from the JSON file.


It converts the search text into keywords.


It checks whether those keywords match:


Product name


Category


Feature tags


If a match is found, the product is displayed on the screen.


This allows flexible searching. For example:
Typing smartwatch shows all smartwatches.


Typing FitPro shows that specific model.


Typing smartwatch FitPro shows matching results.



Technologies Used
Python


Streamlit


JSON


Collections module (for checking duplicate reviews)



Project Files
E-Commerce-Advisor/
│
├── abc.py
├── products.json
└── README.md
abc.py contains the main application code.


products.json contains all product data.


Both files must be in the same folder.

How to Run the Project.
Step 1: Run the Application
Run this command:
python -m streamlit run abc.py
After running it, you will see something like:
Local URL: http://localhost:8501

Step 2: Open the Interface
Copy that Local URL and paste it into your browser.
The application will open, and you can start searching for products.

