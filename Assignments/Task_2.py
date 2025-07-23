def get_messages():
    messages = []
    n = int(input("Enter the number of messages: "))
    for _ in range(n):
        msg = input()
        messages.append(msg.strip())
    return messages


def get_user_message_dict(messages):
    user_msgs = {}
    for msg in messages:
        if ':' in msg:
            name, content = msg.split(':', 1)
            name = name.strip()
            content = content.strip()
            user_msgs.setdefault(name, []).append(content)
    return user_msgs


def count_total_messages(messages):
    print("Total messages:", len(messages))


def identify_unique_users(messages):
    users = {msg.split(':')[0].strip() for msg in messages if ':' in msg}
    print("Unique users in the chat:", users)


def count_total_words(messages):
    words = sum(len(msg.split(':', 1)[1].strip().split()) for msg in messages if ':' in msg)
    print("Total words in the chat:", words)


def average_words_per_message(messages):
    total_words = sum(len(msg.split(':', 1)[1].strip().split()) for msg in messages if ':' in msg)
    avg = total_words / len(messages)
    print("Average words per message:", round(avg, 2))


def find_longest_message(messages):
    longest = max(messages, key=lambda x: len(x.split(':', 1)[1].strip()) if ':' in x else 0)
    print("Longest message:", f'"{longest}"')


def most_active_user(user_msgs):
    user = max(user_msgs.items(), key=lambda x: len(x[1]))
    print(f"Most active user: {user[0]} ({len(user[1])} messages)")


def message_count_for_user(user_msgs):
    user = input("Input: ").strip()
    count = len(user_msgs.get(user, []))
    print(f"Messages sent by {user}: {count}")


def most_frequent_word_by_user(user_msgs):
    user = input("Input: ").strip()
    from collections import Counter
    words = []
    for msg in user_msgs.get(user, []):
        words += msg.lower().strip("?!.,").split()
    if words:
        common = Counter(words).most_common(1)[0][0]
        print(f'Most frequent word used by {user}: "{common}"')
    else:
        print(f"No messages found for {user}.")


def first_last_message_by_user(messages):
    user = input("Input: ").strip()
    user_messages = [msg for msg in messages if msg.startswith(user + ":")]
    if user_messages:
        print("First message by", user + ":", f'"{user_messages[0]}"')
        print("Last message by", user + ":", f'"{user_messages[-1]}"')
    else:
        print(f"No messages found for {user}.")


def check_user_presence(user_msgs):
    user = input("Input: ").strip()
    if user in user_msgs:
        print(f"User '{user}' is present in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")


def common_repeated_words(messages):
    from collections import Counter
    words = []
    for msg in messages:
        parts = msg.split(':', 1)
        if len(parts) == 2:
            words += parts[1].lower().strip("?!.,").split()
    common = {word for word, count in Counter(words).items() if count > 1}
    print("Common repeated words:", common)


def user_with_longest_avg_msg(user_msgs):
    user_avg = {user: sum(len(msg.split()) for msg in msgs) / len(msgs) for user, msgs in user_msgs.items()}
    user = max(user_avg.items(), key=lambda x: x[1])
    print(f"User with longest average message: {user[0]} (avg {round(user[1], 1)} words)")


def messages_mentioning_user(messages):
    user = input("Input: ").strip().lower()
    count = sum(1 for msg in messages if user in msg.split(':', 1)[1].lower())
    print(f"Messages mentioning '{user}': {count}")


def remove_duplicate_messages(messages):
    unique = list(set(messages))
    print(f"Unique messages count: {len(unique)}")
    for msg in sorted(unique):
        print(msg)


def sort_messages(messages):
    print("Messages sorted A-Z:")
    for msg in sorted(messages):
        print(msg)


def extract_questions(messages):
    questions = [msg for msg in messages if '?' in msg]
    print("Questions in chat:")
    for q in questions:
        print(q)


def reply_ratio(messages):
    user1 = input("Enter first user: ").strip()
    user2 = input("Enter second user: ").strip()
    replies = 0
    prev_user = None
    for msg in messages:
        if ':' in msg:
            current_user = msg.split(':', 1)[0].strip()
            if prev_user == user1 and current_user == user2:
                replies += 1
            prev_user = current_user
    print(f"Reply ratio from {user2} to {user1}: {replies} replies")


def check_deleted_messages(messages):
    deleted = [msg for msg in messages if "This message was deleted" in msg]
    print(f"Deleted messages found: {len(deleted)}")



messages = get_messages()
user_msgs = get_user_message_dict(messages)

while True:
    print("\nChoose an option:")
    print("1. Count total messages")
    print("2. Identify unique users")
    print("3. Count total words")
    print("4. Calculate average words per message")
    print("5. Find longest message")
    print("6. Most active user")
    print("7. Message count for a user")
    print("8. Most frequent word by user")
    print("9. First and last message by user")
    print("10. Check user presence")
    print("11. Common repeated words")
    print("13. User with longest average message")
    print("14. Count messages mentioning user")
    print("15. Remove duplicate messages")
    print("16. Sort messages A-Z")
    print("17. Extract all questions")
    print("18. Reply ratio between two users")
    print("19. Check for deleted messages")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '1':
        count_total_messages(messages)
    elif choice == '2':
        identify_unique_users(messages)
    elif choice == '3':
        count_total_words(messages)
    elif choice == '4':
        average_words_per_message(messages)
    elif choice == '5':
        find_longest_message(messages)
    elif choice == '6':
        most_active_user(user_msgs)
    elif choice == '7':
        message_count_for_user(user_msgs)
    elif choice == '8':
        most_frequent_word_by_user(user_msgs)
    elif choice == '9':
        first_last_message_by_user(messages)
    elif choice == '10':
        check_user_presence(user_msgs)
    elif choice == '11':
        common_repeated_words(messages)
    elif choice == '13':
        user_with_longest_avg_msg(user_msgs)
    elif choice == '14':
        messages_mentioning_user(messages)
    elif choice == '15':
        remove_duplicate_messages(messages)
    elif choice == '16':
        sort_messages(messages)
    elif choice == '17':
        extract_questions(messages)
    elif choice == '18':
        reply_ratio(messages)
    elif choice == '19':
        check_deleted_messages(messages)
    elif choice == '0':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


# Enter the number of messages: 6
# Alice: Good morning!
# Bob: Morning Alice!
# Charlie: Morning everyone!
# Alice: Hope you all have a great day.
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend.

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 1
# Total messages: 6

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 2
# Unique users in the chat: {'Bob', 'Charlie', 'Alice'}

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 3
# Total words in the chat: 22

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 4
# Average words per message: 3.67

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 5
# Longest message: "Charlie: Let's plan something fun this weekend."

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 6
# Most active user: Alice (2 messages)

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 7
# Input: charlie 
# Messages sent by charlie: 0

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 8
# Input: alice 
# No messages found for alice.

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 9
# Input: bob
# No messages found for bob.

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 10
# Input: alice
# User 'alice' not found in the chat.

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 11
# Common repeated words: {'you', 'morning', 'alice'}

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 12
# Invalid option. Try again.

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 13
# User with longest average message: Alice (avg 4.5 words)

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 14
# Input: bob
# Messages mentioning 'bob': 0

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 15
# Unique messages count: 6
# Alice: Good morning!
# Alice: Hope you all have a great day.
# Bob: Morning Alice!
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend.
# Charlie: Morning everyone!

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 15
# Unique messages count: 6
# Alice: Good morning!
# Alice: Hope you all have a great day.
# Bob: Morning Alice!
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend.
# Charlie: Morning everyone!

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 16
# Messages sorted A-Z:
# Alice: Good morning!
# Alice: Hope you all have a great day.
# Bob: Morning Alice!
# Bob: You too, Alice!
# Charlie: Let's plan something fun this weekend.
# Charlie: Morning everyone!

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 17
# Questions in chat:

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 18
# Enter first user: alice
# Enter second user: bob
# Reply ratio from bob to alice: 0 replies

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 19
# Deleted messages found: 0

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 19
# Deleted messages found: 0

# Choose an option:
# 1. Count total messages
# 2. Identify unique users
# 3. Count total words
# 4. Calculate average words per message
# 5. Find longest message
# 6. Most active user
# 7. Message count for a user
# 8. Most frequent word by user
# 9. First and last message by user
# 10. Check user presence
# 11. Common repeated words
# 13. User with longest average message
# 14. Count messages mentioning user
# 15. Remove duplicate messages
# 16. Sort messages A-Z
# 17. Extract all questions
# 18. Reply ratio between two users
# 19. Check for deleted messages
# 0. Exit
# Enter your choice: 0
# Exiting. Goodbye!

