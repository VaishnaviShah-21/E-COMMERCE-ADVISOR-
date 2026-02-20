
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











