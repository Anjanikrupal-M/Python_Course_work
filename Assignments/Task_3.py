def welcome():
    print("🧠 Welcome to the Python Interview Prep Quiz!")
    print("💡 Answer each question by typing a, b, c, or d.\n")


def ask_question(q_num, question_data):
    print(f"Question {q_num}: {question_data['question']}")
    print(f"a) {question_data['options']['a']}")
    print(f"b) {question_data['options']['b']}")
    print(f"c) {question_data['options']['c']}")
    print(f"d) {question_data['options']['d']}")
    answer = input("📝 Choose Your answer (a/b/c/d): ").strip().lower()
    
    if answer == question_data['answer']:
        print("✅ Correct!\n")
        return 1
    else:
        correct = question_data['options'][question_data['answer']]
        print(f"❌ Wrong! The correct answer is '{question_data['answer']}) {correct}'\n")
        return 0


def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        score += ask_question(i, q)
    return score


def show_result(score, total):
    print(f"🏁 Quiz Complete!")
    print(f"📊 Your Final Score: {score}/{total}")
    if score == total:
        print("🏆 Perfect score! You did it!")
    else:
        print("📚 Keep learning! You've got this!")

questions = [
    {
        "question": "What does the 'pass' statement do in Python?",
        "options": {
            "a": "Skips execution",
            "b": "Terminates loop",
            "c": "Acts as a placeholder",
            "d": "Throws an error"
        },
        "answer": "c"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": {
            "a": "add()",
            "b": "append()",
            "c": "insert()",
            "d": "push()"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": {
            "a": "6",
            "b": "8",
            "c": "9",
            "d": "5"
        },
        "answer": "b"
    },
    {
        "question": "Which of these is NOT a valid Python data type?",
        "options": {
            "a": "list",
            "b": "set",
            "c": "array",
            "d": "tuple"
        },
        "answer": "c"
    },
    {
        "question": "What is the result of 10 // 3?",
        "options": {
            "a": "3.33",
            "b": "3",
            "c": "4",
            "d": "Error"
        },
        "answer": "b"
    },
    {
        "question": "What does the strip() method do?",
        "options": {
            "a": "Removes characters from middle",
            "b": "Removes leading/trailing spaces",
            "c": "Changes case",
            "d": "Replaces characters"
        },
        "answer": "b"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "a": "//",
            "b": "/* */",
            "c": "#",
            "d": "<!-- -->"
        },
        "answer": "c"
    },
    {
        "question": "What will len('hello') return?",
        "options": {
            "a": "4",
            "b": "5",
            "c": "6",
            "d": "Error"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following can be a dictionary key?",
        "options": {
            "a": "list",
            "b": "set",
            "c": "tuple",
            "d": "dict"
        },
        "answer": "c"
    },
    {
        "question": "How do you raise an exception?",
        "options": {
            "a": "raise Exception('Error')",
            "b": "throw Exception('Error')",
            "c": "error()",
            "d": "panic()"
        },
        "answer": "a"
    },
    {
        "question": "Which built-in function returns the type of an object?",
        "options": {
            "a": "typeof()",
            "b": "type()",
            "c": "object_type()",
            "d": "info()"
        },
        "answer": "b"
    },
    {
        "question": "Which of these loops is not in Python?",
        "options": {
            "a": "for",
            "b": "while",
            "c": "do-while",
            "d": "None of the above"
        },
        "answer": "c"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": {
            "a": "catch",
            "b": "except",
            "c": "handle",
            "d": "trycatch"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of bool([])?",
        "options": {
            "a": "True",
            "b": "False",
            "c": "[]",
            "d": "Error"
        },
        "answer": "b"
    },
    {
        "question": "How to get all keys from a dictionary?",
        "options": {
            "a": "dict.keys()",
            "b": "dict.all()",
            "c": "dict.getkeys()",
            "d": "dict.values()"
        },
        "answer": "a"
    },
    {
        "question": "What is a correct way to open a file for writing?",
        "options": {
            "a": "open('file.txt', 'r')",
            "b": "open('file.txt')",
            "c": "open('file.txt', 'w')",
            "d": "write('file.txt')"
        },
        "answer": "c"
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": {
            "a": "function",
            "b": "def",
            "c": "class",
            "d": "struct"
        },
        "answer": "c"
    },
    {
        "question": "What does the 'is' operator check?",
        "options": {
            "a": "Equality",
            "b": "Identity",
            "c": "Type",
            "d": "None"
        },
        "answer": "b"
    },
    {
        "question": "Which of these is not a core data structure?",
        "options": {
            "a": "list",
            "b": "graph",
            "c": "tuple",
            "d": "dict"
        },
        "answer": "b"
    },
    {
        "question": "What will print(type({})) show?",
        "options": {
            "a": "<class 'set'>",
            "b": "<class 'list'>",
            "c": "<class 'dict'>",
            "d": "<class 'tuple'>"
        },
        "answer": "c"
    }
]
welcome()
score = run_quiz(questions)
show_result(score, len(questions))



###
''' 🧠 Welcome to the Python Interview Prep Quiz!
💡 Answer each question by typing a, b, c, or d.

Question 1: What does the 'pass' statement do in Python?
a) Skips execution
b) Terminates loop
c) Acts as a placeholder
d) Throws an error
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 2: Which method is used to add an item to a list?
a) add()
b) append()
c) insert()
d) push()
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 3: What is the output of: print(2 ** 3)?
a) 6
b) 8
c) 9
d) 5
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 4: Which of these is NOT a valid Python data type?
a) list
b) set
c) array
d) tuple
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 5: What is the result of 10 // 3?
a) 3.33
b) 3
c) 4
d) Error
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 6: What does the strip() method do?
a) Removes characters from middle
b) Removes leading/trailing spaces
c) Changes case
d) Replaces characters
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 7: Which symbol is used for comments in Python?
a) //
b) /* */
c) #
d) <!-- -->
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 8: What will len('hello') return?
a) 4
b) 5
c) 6
d) Error
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 9: Which of the following can be a dictionary key?
a) list
b) set
c) tuple
d) dict
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 10: How do you raise an exception?
a) raise Exception('Error')
b) throw Exception('Error')
c) error()
d) panic()
📝 Choose Your answer (a/b/c/d): a
✅ Correct!

Question 11: Which built-in function returns the type of an object?
a) typeof()
b) type()
c) object_type()
d) info()
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 12: Which of these loops is not in Python?
a) for
b) while
c) do-while
d) None of the above
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 13: Which keyword is used to handle exceptions?
a) catch
b) except
c) handle
d) trycatch
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 14: What is the output of bool([])?
a) True
b) False
c) []
d) Error
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 15: How to get all keys from a dictionary?
a) dict.keys()
b) dict.all()
c) dict.getkeys()
d) dict.values()
📝 Choose Your answer (a/b/c/d): a
✅ Correct!

Question 16: What is a correct way to open a file for writing?
a) open('file.txt', 'r')
b) open('file.txt')
c) open('file.txt', 'w')
d) write('file.txt')
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 17: Which keyword is used to create a class in Python?
a) function
b) def
c) class
d) struct
📝 Choose Your answer (a/b/c/d): c
✅ Correct!

Question 18: What does the 'is' operator check?
a) Equality
b) Identity
c) Type
d) None
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 19: Which of these is not a core data structure?
a) list
b) graph
c) tuple
d) dict
📝 Choose Your answer (a/b/c/d): b
✅ Correct!

Question 20: What will print(type({})) show?
a) <class 'set'>
b) <class 'list'>
c) <class 'dict'>
d) <class 'tuple'>
📝 Choose Your answer (a/b/c/d): a
❌ Wrong! The correct answer is 'c) <class 'dict'>'

🏁 Quiz Complete!
📊 Your Final Score: 19/20
📚 Keep learning! You've got this!'''
