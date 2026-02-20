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
