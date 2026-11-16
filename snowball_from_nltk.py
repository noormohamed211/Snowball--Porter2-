import nltk
from nltk.stem.snowball import SnowballStemmer

def stemming_demo():
    
    # Initialize stemmer for English
    stemmer = SnowballStemmer('english')
    
    # Test words with different morphological patterns
    test_words = [
        'running', 'runs', 'ran',           # Verb variations
        'caring', 'cared', 'careful',       # Different suffixes  
        'university', 'universities',       # Plural forms
        'fairly', 'unfairly',               # Adverbs with prefixes
        'singing', 'singer', 'song'         # Related but different stems
    ]
    
    print("Basic Stemming Results:")
    print("-" * 30)
    
    for word in test_words:
        stem = stemmer.stem(word)
        print(f"{word:12} → {stem}")

stemming_demo()