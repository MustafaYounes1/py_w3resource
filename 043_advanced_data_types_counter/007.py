"""

Write a python program to find the Jaccard similarity coefficient between two lists using 'Counter' objects.

Jaccard Similarity, also known as the Jaccard Index or Jaccard Coefficient, is a measure used to quantify similarity
between two sets. It's commonly employed in various fields, including data mining, information retrieval, and natural
language processing, to compare similarities between sets of elements.

For example, consider two sets:
    A = {apple, banana, orange, kiwi}
    B = {banana, kiwi, pineapple}

The intersection of A and B is {banana, kiwi}, which has a cardinality of 2.
The union of A and B is {apple, banana, orange, kiwi, pineapple}, which has a cardinality of 5.
So, the Jaccard Similarity between sets A and B is 2/5, which is 0.4.

lst1 = ['Red', 'Green', 'Blue', 'Orange']
lst2 = ['Green', 'Pink', 'Blue']

Jaccard Similarity Coefficient: 0.4

"""

from collections import Counter


def jaccard_sim(lst1: list[...], lst2: list[...]) -> float:
    if not (lst1 and lst2):
        return 0.0

    ctr1 = Counter(lst1)
    ctr2 = Counter(lst2)
    return len(ctr1 & ctr2) / len(ctr1 | ctr2)


def main():
    lst1 = ['Red', 'Green', 'Blue', 'Orange']
    lst2 = ['Green', 'Pink', 'Blue']
    print(jaccard_sim(lst1, lst2))


if __name__ == "__main__":
    main()
