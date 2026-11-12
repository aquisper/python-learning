"""Small utility functions."""

def clean_text(text):
    """lowercase and strip punctuation from a string"""
    import string
    return text.lower().strip(string.punctuation + " ")

def word_count(text):
    """Return a dict of word → count."""
    words = clean_text(text).split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def top_n(counts, n=10):
    """Return the top n items from a count dict."""
    return sorted(counts.items(), key=lambda  kv:kv[1], reverse=True)[:n]