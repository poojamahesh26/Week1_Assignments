#Your task is to count the number of different words in this text

string = """
I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!
"""

# Convert text to lowercase to ensure the words match 
text = string.lower()

# Remove punctuation manually by replacing common punctuation marks with space
for char in [".", ",", "!", "?", "\n"]:
    text = text.replace(char, " ")

# Split the text into words
words = text.split()

# Get different words
unique_words = set(words)

# Count different words
print("Number of different words:", len(unique_words))
