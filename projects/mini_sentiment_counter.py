# Mini Sentiment Counter
#input sentence
sentence = input("Enter a sentence: ").lower()
#define word lists
positive_words = ["good", "happy", "love", "great", "awesome"]
negative_words = ["bad", "sad", "hate", "terrible", "awful"]
#split sentences into words
words = sentence.split()
# .split() breaks the string into a list of words separated by spaces
#counters
pos_count = 0
neg_count = 0

# We don’t need an else here because words that are not in
# positive_words or negative_words are simply ignored (neutral).
# Only positive and negative matches affect the counts

#loop through words
for w in words:
    if w in positive_words:
        pos_count += 1
    elif w in negative_words:
        neg_count += 1
#here w checks words directly, not each letter
#result
print("Positive words:", pos_count)
print("Negative words:", neg_count)

# Decide sentiment
if pos_count == 0 and neg_count == 0:
    print("No sentiment words found.")
elif pos_count > neg_count:
    print("Overall Sentiment: Positive")
elif neg_count > pos_count:
    print("Overall Sentiment: Negative")
else:
    print("Overall Sentiment: Neutral")
