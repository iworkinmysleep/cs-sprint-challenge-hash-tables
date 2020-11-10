def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for num in a:
        # check for duplicates, positive or negative using abs
        if cache.get(abs(num)):
            # check for the negatives and add to table
            if (cache.get(abs(num))+ num) == 0:
                result.append(abs(num))
        # otherwise add to cache
        else:
            cache[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
