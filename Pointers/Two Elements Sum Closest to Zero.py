def get_elements(arr: list):

    # sort integer array
    arr.sort()

    # initialize pointers
    left = 0
    right = len(arr)-1
    diff = float("inf")

    while left < right:
        a = arr[left]
        b = arr[right]
        current_total = a + b
        current_diff = abs(current_total - 0)  # closest to zero, not smallest total; target=0

        if current_diff < diff:
            diff = current_diff
            elements = [a, b]

        if current_total < 0:  # target=0
            left += 1

        else:  # current_total >= 0
            right -= 1

    return elements


if __name__ == "__main__":
    arr = [1, 60, -10, 70, -80, 85]
    print(get_elements(arr))
