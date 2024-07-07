#Task 1 -- Write a program that searches through reviews list and looks for keywords such as
# "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords
# then print out each review. Print out each review with the keywords in uppercase so they stand out.

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ('good', 'excellent', 'bad', 'poor', 'average')

capitalized_reviews = []

for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    capitalized_reviews.append(review)

for review in capitalized_reviews:
    print(review)


#Task 2 -- Develop a function that tallies the number of positive and negative words in each review.
# The function should return the total count of positive and negative words.

def tally_keywords(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        for word in positive_words:
            positive_count += review.lower().count(word)
        for word in negative_words:
            negative_count += review.lower().count(word)
    
    return positive_count, negative_count

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "highly recommended",
                  "impressed"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar", "didn't meet",
                  "nothing extraordinary", "wouldn't recommend"]

positive_count, negative_count = tally_keywords(reviews, positive_words, negative_words)

print(f"Positive words count: {positive_count}")
print(f"Negative words count: {negative_count}")


#Task 3 -- Implement a script that takes the first 30 characters of a review and appends "…" to create
# a summary. Ensure that the summary does not cut off in the middle of a word.

def create_summary(reviews, max_length=30):
    summaries = []
    for review in reviews:
        if len(review) <= max_length:
            summaries.append(review)
        else:
            summary = review[:max_length]
            if review[max_length] != ' ' and ' ' in summary:
                summary = summary[:summary.rfind(' ')]
            summaries.append(summary + '…')
    return summaries

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

summaries = create_summary(reviews)

for summary in summaries:
    print(summary)