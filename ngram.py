from nltk import ngrams

def extract_ngrams(text, n, ignored_tokens={'and'}):
    grams = {}
    for gram in ngrams(text.split(), n):
        if not ignored_tokens.intersection(gram):
            if " ".join(gram) in grams:
                grams[" ".join(gram) ] += 1
            else:
                grams[" ".join(gram) ] = 1
    return grams
    
    
bigrams = extract_ngrams("a big dog and a big cat", 2)
assert(bigrams == {'a big': 2, 'big dog': 1, 'big cat': 1})

bigrams = extract_ngrams("a big dog and a big cat", 2, {'dog', 'cat'})
assert(bigrams == {'a big': 2, 'and a': 1})

trigrams = extract_ngrams("a big dog and a big cat", 3)
assert(trigrams == {'a big dog': 1, 'a big cat': 1})

