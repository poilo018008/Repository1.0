def filter_strings(arr):
    result = []
    for s in arr:
        if len(s) <= 3:
            result.append(s)
    return result

if __name__ == "__main__":
    initial_array = ["Hello", "2", "world", ":-)"]  # Можно изменить на ввод с клавиатуры
    filtered_array = filter_strings(initial_array)
    print(filtered_array)
