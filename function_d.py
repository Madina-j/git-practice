def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    # Luqi
    max_num = 0
    
    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num




if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
