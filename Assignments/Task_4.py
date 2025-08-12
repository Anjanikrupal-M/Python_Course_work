def count_consecutive_characters():
    print("💡 Program: Count Consecutive Characters in a String\n")

    print("📜 Code:")
    print('''\
def count_consecutive(s):
    count = 1
    result = []
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append((s[i-1], count))
            count = 1
    result.append((s[-1], count))
    return result

s = input("Enter a string: ")
print(count_consecutive(s))
''')

    print("🧾 Test Cases:")
    print("Input: aaabbcaa → Output: [('a', 3), ('b', 2), ('c', 1), ('a', 2)]")
    print("Input: xxxxyy → Output: [('x', 4), ('y', 2)]")

    print("\n🗒️ Explanation:")
    print("We iterate over the string, counting how many times each character repeats consecutively, and store the character with its count.")


def first_non_repeating_character():
    print("💡 Program: Find the First Non-Repeating Character in a String\n")

    print("📜 Code:")
    print('''\
def first_non_repeating(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

s = input("Enter a string: ")
result = first_non_repeating(s)
print("First non-repeating character:", result if result else "None")
''')

    print("🧾 Test Cases:")
    print("Input: swiss → Output: w")
    print("Input: aabb → Output: None")

    print("\n🗒️ Explanation:")
    print("We check each character in order and return the first one that appears exactly once in the string.")


def digital_root():
    print("💡 Program: Find the Digital Root of a Number\n")

    print("📜 Code:")
    print('''\
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

num = int(input("Enter a number: "))
print("Digital Root:", digital_root(num))
''')

    print("🧾 Test Cases:")
    print("Input: 942 → Output: 6")
    print("Input: 132189 → Output: 6")

    print("\n🗒️ Explanation:")
    print("The digital root is obtained by summing the digits repeatedly until a single-digit number remains.")


def snake_to_camel():
    print("💡 Program: Convert Snake Case to Camel Case\n")

    print("📜 Code:")
    print('''\
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

snake = input("Enter snake_case string: ")
print("CamelCase:", snake_to_camel(snake))
''')

    print("🧾 Test Cases:")
    print("Input: hello_world → Output: helloWorld")
    print("Input: my_name_is → Output: myNameIs")

    print("\n🗒️ Explanation:")
    print("We split the string by underscores and capitalize the first letter of each subsequent word.")


def longest_palindromic_substring():
    print("💡 Program: Find the Longest Palindromic Substring\n")

    print("📜 Code:")
    print('''\
def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

s = input("Enter a string: ")
print("Longest Palindromic Substring:", longest_palindrome(s))
''')

    print("🧾 Test Cases:")
    print("Input: babad → Output: bab (or aba)")
    print("Input: cbbd → Output: bb")

    print("\n🗒️ Explanation:")
    print("We check all substrings to see if they are palindromes and keep track of the longest one found.")


def sum_of_unique_elements():
    print("💡 Program: Sum of Unique Elements in a List\n")

    print("📜 Code:")
    print('''\
def sum_unique(lst):
    return sum(x for x in lst if lst.count(x) == 1)

lst = list(map(int, input("Enter numbers: ").split()))
print("Sum of unique elements:", sum_unique(lst))
''')

    print("🧾 Test Cases:")
    print("Input: 1 2 3 2 → Output: 4 (1 + 3)")
    print("Input: 4 4 5 6 → Output: 11 (5 + 6)")

    print("\n🗒️ Explanation:")
    print("We sum the elements that appear exactly once in the list.")


def count_palindromic_words():
    print("💡 Program: Count Palindromic Words in a Sentence\n")

    print("📜 Code:")
    print('''\
def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(sentence):
    words = sentence.split()
    return sum(1 for w in words if is_palindrome(w.lower()))

sentence = input("Enter a sentence: ")
print("Count of palindromic words:", count_palindromes(sentence))
''')

    print("🧾 Test Cases:")
    print("Input: madam speaks level words → Output: 2")
    print("Input: hello world → Output: 0")

    print("\n🗒️ Explanation:")
    print("We split the sentence into words and count how many are palindromes.")


def count_islands():
    print("💡 Program: Count Number of Islands in a Grid\n")

    print("📜 Code:")
    print('''\
def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return
    grid[i][j] = '0'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

def num_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)
    return count

grid = [
    ['1','1','0','0'],
    ['1','0','0','1'],
    ['0','0','1','1']
]
print("Number of islands:", num_islands(grid))
''')

    print("🧾 Test Cases:")
    print("Input: [['1','1','0','0'], ['1','0','0','1'], ['0','0','1','1']] → Output: 3")
    print("Input: [['1','0'], ['0','1']] → Output: 2")

    print("\n🗒️ Explanation:")
    print("We use DFS to mark connected land ('1') as visited and count how many disconnected groups exist.")


def remove_duplicates_in_string():
    print("💡 Program: Remove Duplicates in a String\n")

    print("📜 Code:")
    print('''\
def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result

s = input("Enter a string: ")
print("String without duplicates:", remove_duplicates(s))
''')

    print("🧾 Test Cases:")
    print("Input: programming → Output: progamin")
    print("Input: hello → Output: helo")

    print("\n🗒️ Explanation:")
    print("We iterate through the string, adding characters to the result only if they haven't been added before.")


def missing_letters_to_pangram():
    print("💡 Program: Missing Letters to Form a Pangram\n")

    print("📜 Code:")
    print('''\
import string

def missing_letters(s):
    alphabet = set(string.ascii_lowercase)
    s = set(s.lower())
    return ''.join(sorted(alphabet - s))

text = input("Enter text: ")
print("Missing letters:", missing_letters(text))
''')

    print("🧾 Test Cases:")
    print("Input: The quick brown fox jumps over the lazy dog → Output: '' (empty string)")
    print("Input: hello world → Output: abcfgijkmnpqstuvxyz")

    print("\n🗒️ Explanation:")
    print("We compare the letters in the input text to the full alphabet to find which letters are missing.")
