positive_keywords = ["good", "great", "excellent", "amazing", "happy", "love", "best", "wonderful", "satisfied", "awesome"]
negative_keywords = ["bad", "terrible", "horrible", "disappointed", "poor", "hate", "worst", "awful", "unsatisfied", "boring"]

def get_sentiment(review_text):
    review_text = review_text.lower() 
    positive_matches = sum(word in review_text for word in positive_keywords)
    negative_matches = sum(word in review_text for word in negative_keywords)

    if positive_matches > negative_matches:
        return "Positive"
    elif negative_matches > positive_matches:
        return "Negative"
    else:
        return "Neutral"

def main():
    review_list = []

    
    while True:
        user_input = input("Enter a product review (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        review_list.append(user_input)

    if len(review_list) == 0:
        print("No reviews submitted.")
        return

    positive_reviews = 0
    negative_reviews = 0
    neutral_reviews = 0

    for review in review_list:
        sentiment = get_sentiment(review)

        if sentiment == "Positive":
            positive_reviews += 1
        elif sentiment == "Negative":
            negative_reviews += 1
        else:
            neutral_reviews += 1

    print("\n--- Sentiment Summary ---")
    print(f"Total Reviews: {len(review_list)}")
    print(f"Positive Reviews: {positive_reviews}")
    print(f"Negative Reviews: {negative_reviews}")
    print(f"Neutral Reviews: {neutral_reviews}")

if __name__ == "__main__":
    main()
