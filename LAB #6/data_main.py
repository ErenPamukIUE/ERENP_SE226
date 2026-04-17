from data_package import (
    strip_whitespaces,
    remove_duplicates,
    calculate_mean,
    find_maximum,
    find_minimum
)

userInput = input('Enter a string: ')

string_list = userInput.split(',')


cleaned_strings = strip_whitespaces(string_list)

cleaned_strings = [s for s in cleaned_strings if s]

num_list = [float(num) for num in cleaned_strings]

unique_data = remove_duplicates(num_list)

print(f"Cleaned and unique data: {unique_data}")
print(f"Mean: {calculate_mean(unique_data):.2f}")
print(f"Maximum: {find_maximum(unique_data)}")
print(f"Minimum: {find_minimum(unique_data)}")