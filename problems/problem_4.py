def max_n_digit_number(n):
    return int("9" * n)

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def largest_palindrome_product_of_n_digit_numbers(n):
    palindromes = []
    for i in range(max_n_digit_number(n), 0, -1):
        for k in range(max_n_digit_number(n), 0, -1):
            if is_palindrome(i * k):
                palindromes.append(i * k)
    return max(palindromes)

print(largest_palindrome_product_of_n_digit_numbers(3))
