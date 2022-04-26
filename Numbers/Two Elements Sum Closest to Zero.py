def get_elements(arr: list):
    # sort integer array
    arr.sort()

    # initialize pointers
    left = 0
    right = len(arr)-1
    total = arr[left] + arr[right]
    elements = [arr[left], arr[right]]

    while left < right:
        current_total = arr[left] + arr[right]

        if current_total < 0:
            left += 1

        else:  # current_total >= 0
            right -= 1

        if abs(current_total) < total:  # closest to zero, not smallest total
            total = current_total
            elements = [arr[left], arr[right]]

    return elements


if __name__ == "__main__":
    arr = [1, 60, -10, 70, -80, 85]
    print(get_elements(arr))
