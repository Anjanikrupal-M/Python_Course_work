import Task_4 as t

function_map = {
    1: t.count_consecutive_characters,
    2: t.first_non_repeating_character,
    3: t.digital_root,
    4: t.snake_to_camel,
    5: t.longest_palindromic_substring,
    6: t.sum_of_unique_elements,
    7: t.count_palindromic_words,
    8: t.count_islands,
    9: t.remove_duplicates_in_string,
    10: t.missing_letters_to_pangram
}

while True:
    print('''
------ FUNCTION MENU ------
1. Count Consecutive Characters in a String
2. First Non-Repeating Character
3. Digital Root of a Number
4. Snake Case to Camel Case
5. Longest Palindromic Substring
6. Sum of Unique Elements in a List
7. Count Palindromic Words in a Sentence
8. Count Number of Islands
9. Remove Duplicates in a String
10. Missing Letters to Form Pangram
0. Exit
---------------------------''')

    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
