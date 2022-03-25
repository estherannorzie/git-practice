def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    all_list = set(list_a + list_b)
    return list(all_list)


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))

print(merge_lists([1, 1, 2, 2, 3, 3], [1, 2, 3, 4, 5, 5, 6]))
