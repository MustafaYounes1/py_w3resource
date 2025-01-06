"""

Write a Python program to retrieve the value of the nested key indicated by the given selector list from a
dictionary or list.

users = {
  'freddy': {
    'name': {
      'first': 'Fateh',
      'last': 'Harwood'
    },
    'postIds': [1, 2, 3]
  }
}

['freddy', 'name', 'last']      =>  Harwood
['freddy', 'postIds', 1]        =>  2

"""

from functools import reduce
from operator import getitem, itemgetter


def main():
    users = {
        'freddy': {
            'name': {
                'first': 'Fateh',
                'last': 'Harwood'
            },
            'postIds': [1, 2, 3]
        }
    }

    # using itemgetter which returns a callable that fetched elements from its operand itemgetter(item)(operand)
    # each iteration of reduce gives: v1, v2 (where v1 is the accumulated value) => itemgetter(v2)(v1)  =>  v1[v2]
    lst = ['freddy', 'name', 'last']
    print(reduce(lambda v1, v2: itemgetter(v2)(v1), lst, users))

    # or simply using getitem(a)(b) which is equivalent to a[b]
    # each iteration of reduce gives: v1, v2 (where v1 is the accumulated value) => getitem(v1, v2)     =>  v1[v2]
    lst = ['freddy', 'postIds', 1]
    print(reduce(getitem, lst, users))


if __name__ == "__main__":
    main()
