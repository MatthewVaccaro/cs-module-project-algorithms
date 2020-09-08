

def sliding_window_max(arr, k):
    results = []
    counter = 0

    while counter != len(arr) - k + 1:
        window = arr[counter: counter + k]
        biggest = max(window)
        results.append(biggest)
        counter += 1

    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(sliding_window_max(arr, k))

    # print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
