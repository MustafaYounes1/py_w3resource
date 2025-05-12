"""

Write a Python program to sort unsorted numbers using patience sorting.

From Wikipedia: In computer science, patience sorting is a sorting algorithm inspired by, and named after, the card
game patience. A variant of the algorithm efficiently computes the length of the longest increasing subsequence in a
given array.

The algorithm's name derives from a simplified variant of the patience card game. The game begins with a shuffled deck
of cards. The cards are dealt one by one into a sequence of piles on the table, according to the following rules:
1. Initially, there are no piles. The first card dealt forms a new pile consisting of the single card.

2. Each subsequent card is placed on the leftmost existing pile whose top card has a value greater than or equal to
    the new card's value, or to the right of all of the existing piles, thus forming a new pile.

3. When there are no more cards remaining to deal, the game ends.

Goal is to form as much as few piles possible.

Note: In order to find the longest increasing subsequence:
    Whenever a card is placed on top of a pile, put a back-pointer to the top card in the previous pile (that, by
    assumption, has a lower value than the new card has).

A good illustration of the algorithm can be found in this YouTube Tutorial: https://www.youtube.com/watch?v=22s1xxRvy28

Worst Time Complexity:  O(n log(n))
Best Time Complexity:   O(n)    occurs when the input is pre-sorted.

[14, 46, 43, 27, 57, 41, 45, 21, 70]

Ascending order:    [14, 21, 27, 41, 43, 45, 46, 57, 70]
Descending order:   [70, 57, 46, 45, 43, 41, 27, 21, 14]

"""

from dataclasses import dataclass
from functools import total_ordering
from heapq import merge
from typing import Self


@dataclass
class Card:
    """A pile item"""
    val: ...  # the card value
    previous: Self | None = None # once this card has been added to a pile, this pointer would point to the top
    # card in the pile to the left of this card's pile (used to get the longest increasing/decreasing subsequence)

    def __repr__(self) -> str:
        return f"{self.val} <- {self.previous}"


@total_ordering
class Pile:
    """A class that represents a pile of cards"""
    def __init__(self, cards: list[Card] = None):
        self.__cards: list[Card] = cards if cards else []

    def append(self, card: Card) -> None:
        """add a card"""
        self.__cards.append(card)

    @property
    def top(self) -> Card | None:
        """get the top card"""
        if self:
            return self.__cards[-1]
        else:
            return None

    def values(self, reverse: bool = False) -> list[...]:
        """get the values of the cards in the pile"""
        if reverse:
            return [card.val for card in self.__cards[::-1]]
        else:
            return [card.val for card in self.__cards]

    def __len__(self):
        return len(self.__cards)

    def __repr__(self) -> str:
        return " | ".join(map(str, self.__cards))

    def __lt__(self, other):
        """A pile is less than another pile if its top card is less than the other one's top card"""
        if self and other:
            return self.top.val < other.top.val

        else:
            raise ValueError("called with empty pile(s)")

    def __eq__(self, other):
        """A pile is less than another pile if its top card equals to the other one's top card"""
        if self and other:
            return self.top.val == other.top.val

        elif self or other:
            return False

        else:
            raise True


def bisect_right(lst: list[...], item: ..., reverse: bool = False):
    """An alternative to Python's bisect.bisect_right that supports locating the insertion point for 'item' in 'lst'
    while maintaining sorted order. The gist here: 'lst' can be sorted in descending order.
    Using binary search, this function returns an insertion point which comes after (to the right of) any existing
    entries of 'item' in 'lst'
    :param lst: the sorted list
    :param item: the item to be inserted
    :param reverse: False -> the list is sorted in ascending order
                    True -> the list is sorted in descending order
    :return the index of 'item' in 'lst' such that when inserted, 'lst' would maintain its ordering"""

    s, e = 0, len(lst) - 1

    while s <= e:
        mid = s + (e - s) // 2

        if [item < lst[mid], item > lst[mid]][reverse]:
            e = mid - 1

        else:
            s = mid + 1

    return s


def patience_sort(lst: list[...], reverse: bool = False) -> tuple[list[...], list[...]]:
    """An implementation of patience sort
    :param lst: the input list
    :param reverse: False: sort in ascending order and extract the longest increasing subsequence.
                    True: sort in descending order and extract the longest decreasing subsequence.
    :return a tuple having: the sorted list, and the extracted longest increasing/decreasing subsequence
    """
    piles: list[Pile] = []  # would store a list of piles with cards sorted in decreasing order when the list has to
    # be sorted in ascending order, and vice versa.

    for item in lst:
        card = Card(item)
        new_pile = Pile([card])

        # Locate the insertion point (index of the pile) for the new card while maintaining the order of the list of
        # piles, i.e:
        # In the ascending order -> the card can be placed in a pile if its top card has a bigger value
        # In the descending order -> the card can be placed in a pile if its top card has a smaller value
        idx = bisect_right(piles, new_pile, reverse)

        if idx == len(piles):
            # all previous piles have a top item that is smaller_acs/bigger_desc than the current item
            piles.append(new_pile)  # add the current item to a new pile on the right

        else:
            # found a pile with a top element that is bigger_asc/smaller_desc than the current item
            piles[idx].append(card)  # add the current item on top of the found pile

        # add a back-pointer of the current card to the top card in the left pile (used to extract the longest
        # increasing_asc/decreasing_desc subsequence
        if idx > 0:
            piles[idx].top.previous = piles[idx - 1].top

    ls = []  # would store the longest increasing/decreasing subsequence in the input list

    # extract the LIS/LDS in the input list
    if piles:
        curr = piles[-1].top
        ls.append(curr.val)

        while curr.previous is not None:
            curr = curr.previous
            ls.append(curr.val)

    ls.reverse()

    # merge the piles in the required order
    res = merge(*(pile.values(reverse=True) for pile in piles), reverse=reverse)

    return list(res), ls


def main():
    lst = [14, 46, 43, 27, 57, 41, 45, 21, 70]

    print(patience_sort(lst, False))
    print(patience_sort(lst, True))


if __name__ == "__main__":
    main()
