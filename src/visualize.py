import matplotlib.pyplot as plt
from collections import Counter

def plot_top_words(texts):
    words = " ".join(texts).split()
    counter = Counter(words).most_common(10)

    labels, values = zip(*counter)
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.title("Top Words")
    plt.show()