import os
import random
import re
import sys
from numpy.random import choice

DAMPING = 0.85
SAMPLES = 10000
proximity = 0.001

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    result = dict.fromkeys(corpus.keys(), 0)
    n = len(corpus[page])
    buff = 0
    if not corpus[page]:
        buff = damping_factor / len(result)
    for i in corpus[page]:
        result[i] += damping_factor / n
    for i in result:
        result[i] += int(100-damping_factor * 100)/(100 * len(result)) + buff
    return result


def sample_pagerank(corpus, damping_factor, n):
    webpages = list(corpus.keys())
    rates = dict.fromkeys(webpages, 0)
    cur_page = random.choice(webpages)
    for i in range(n):
        weights = transition_model(corpus, cur_page, damping_factor)
        rates[cur_page] += 1/n
        cur_page = choice(webpages, 1, p=list(weights.values()))[0]
    return rates


def difference_of_two_arrays(previous, current):
    for i in range(len(previous)):
        if abs(previous[i] - current[i]) >= proximity:
            return True
    return False


def iterate_pagerank(corpus, damping_factor):
    n = len(corpus)
    webpages = list(corpus.keys())
    rates = dict.fromkeys(webpages, 1)
    rates1 = dict.fromkeys(webpages, 1/n)
    while difference_of_two_arrays(list(rates.values()), list(rates1.values())):
        rates = rates1
        for i in rates1:
            rates1[i] = (1 - damping_factor) / n
            sm = 0
            for j in corpus:
                if i in corpus[j]:
                    sm += rates[j] / len(corpus[j])
            rates1[i] += damping_factor * sm
    return rates1


if __name__ == "__main__":
    main()
