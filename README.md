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
Products.json:
[
  {
    "product_id": "SW001",
    "name": "FitPro X1",
    "category": "Smartwatch",
    "price": 3999,
    "price_history": [4599, 3999],
    "features_tags": ["fitness", "heart-rate", "bluetooth"],
    "review_summary": "Affordable fitness smartwatch",
    "reviews": ["Good fitness tracking", "Good fitness tracking", "Battery life is great"],
    "platform_prices": {"Amazon": 3999, "Flipkart": 3799}
  },
  {
    "product_id": "SW002",
    "name": " thMHealaxPro",
    "category": "Smartwatch",
    "price": 6999,
    "price_history": [7499, 6999],
    "features_tags": ["amoled", "fitness", "spo2"],
    "review_summary": "Premium health tracking features",
    "reviews": ["Excellent display", "Excellent display", "Good battery backup"],
    "platform_prices": {"Amazon": 6999, "Flipkart": 6799}
  },


  {
    "product_id": "HP001",
    "name": "BassCore ANC",
    "category": "Headphones",
    "price": 5499,
    "price_history": [5999, 5499],
    "features_tags": ["anc", "wireless"],
    "review_summary": "Strong ANC performance",
    "reviews": ["Amazing sound quality", "Amazing sound quality", "Very comfortable"],
    "platform_prices": {"Amazon": 5499, "Flipkart": 5299}
  },
  {
    "product_id": "HP002",
    "name": "SoundMax 500",
    "category": "Headphones",
    "price": 3999,
    "price_history": [4499, 3999],
    "features_tags": ["wireless", "bass"],
    "review_summary": "Deep bass headphones",
    "reviews": ["Bass is powerful", "Bass is powerful", "Battery backup is good"],
    "platform_prices": {"Amazon": 3999, "Flipkart": 3799}
  },


  {
    "product_id": "AP001",
    "name": "AirTune Lite",
    "category": "AirPods",
    "price": 2999,
    "price_history": [3499, 2999],
    "features_tags": ["wireless", "budget"],
    "review_summary": "Affordable earbuds",
    "reviews": ["Good sound", "Good sound", "Value for money"],
    "platform_prices": {"Amazon": 2999, "Flipkart": 2799}
  },
  {
    "product_id": "AP002",
    "name": "AirTune Pro",
    "category": "AirPods",
    "price": 6999,
    "price_history": [7499, 6999],
    "features_tags": ["anc", "premium"],
    "review_summary": "Premium ANC earbuds",
    "reviews": ["Amazing ANC", "Amazing ANC", "Premium feel"],
    "platform_prices": {"Amazon": 6999, "Flipkart": 6799}
  }
]

main.py:
import json
from collections import Counter


with open("products.json", "r") as file:
    products = json.load(file)


def fake_review_score(product):
    reviews = product["reviews"]
    count = Counter(reviews)
    duplicates = sum(1 for review in count if count[review] > 1)
    return round(duplicates / len(reviews), 2)


def sentiment_score(product):
    positive_words = ["amazing", "great", "good", "excellent", "comfortable", "premium"]
    negative_words = ["bad", "poor", "worst", "cheap"]


    score = 0
    for review in product["reviews"]:
        review_lower = review.lower()
        for word in positive_words:
            if word in review_lower:
                score += 1
        for word in negative_words:
            if word in review_lower:
                score -= 1


    return round(score / len(product["reviews"]), 2)


def check_price_drop(product):
    if product["price_history"][-1] < product["price_history"][0]:
        return "Price Dropped"
    else:
        return "No Price Drop"


def compare_across_platforms(product):
    prices = product["platform_prices"]
    best_platform = min(prices, key=prices.get)
    print("Platform Prices:")
    for platform, price in prices.items():
        print(platform + ":", price)
    print("Best Deal:", best_platform, prices[best_platform])


def calculate_final_score(product, query_features):
    feature_match = len(set(product["features_tags"]) & set(query_features))
    sentiment = sentiment_score(product)
    fake_penalty = fake_review_score(product)


    avg_price = sum(product["platform_prices"].values()) / len(product["platform_prices"])
    price_score = 10000 / avg_price


    final_score = feature_match + sentiment + price_score - fake_penalty
    return round(final_score, 2)


def smart_search(query):
    query_words = query.lower().split()
    matched_products = []


    for product in products:
        searchable_text = product["name"].lower() + " " + " ".join(product["features_tags"]).lower()


        if any(word in searchable_text for word in query_words):
            score = calculate_final_score(product, query_words)
            matched_products.append((product, score))


    ranked = sorted(matched_products, key=lambda x: x[1], reverse=True)
    return ranked


def show_results(query):
    results = smart_search(query)


    if not results:
        print("No products found")
        return


    print("\nSearch Results for:", query)


    for i, (product, score) in enumerate(results, 1):
        print("\nRank", i)
        print("Product:", product["name"])
        print("Category:", product["category"])
        print("Price:", product["price"])
        print("Final Score:", score)
        print("Sentiment Score:", sentiment_score(product))
        print("Fake Review Score:", fake_review_score(product))
        print("Price Status:", check_price_drop(product))
        compare_across_platforms(product)


if __name__ == "__main__":
    user_query = input("Enter product search: ")
    show_results(user_query)

abc.py


import json
from collections import Counter


with open("products.json", "r") as file:
    products = json.load(file)


def fake_review_score(product):
    reviews = product["reviews"]
    count = Counter(reviews)
    duplicates = sum(1 for review in count if count[review] > 1)
    return round(duplicates / len(reviews), 2)


def check_price_drop(product):
    if product["price_history"][-1] < product["price_history"][0]:
        return "Price Dropped"
    return "No Price Drop"


def smart_search(query):
    query = query.lower().strip()
    if not query:
        return []


    query_words = query.split()
    matched_products = []


    for product in products:
        name = product["name"].lower()
        category = product["category"].lower()
        features = " ".join(product["features_tags"]).lower()


        searchable_text = name + " " + category + " " + features


        score = 0


        if query == name:
            score += 10


        for word in query_words:
            if word in searchable_text:
                score += 1


        if score > 0:
            matched_products.append((product, score))


    matched_products.sort(key=lambda x: x[1], reverse=True)


    return [item[0] for item in matched_products]


st.title("AI Product Advisor")


query = st.text_input("Search by product name, category, or feature")


if st.button("Search"):
    results = smart_search(query)


    if not results:
        st.warning("No products found")
    else:
        for product in results:
            st.subheader(product["name"])
            st.write("Category:", product["category"])
            st.write("Price:", product["price"])
            st.write("Fake Review Score:", fake_review_score(product))
            st.write("Price Status:", check_price_drop(product))
            st.write("Platform Prices:", product["platform_prices"])
            st.markdown("---")












