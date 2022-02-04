from Question import Question

question_prompts = [
    "what color are apples?\n(a) Red (b) Purple (c) Orange\n",
    "what color are bananas?\n(a) Red (b) Purple (c) Orange\n",
    "what color are strawberries?\n(a) Red (b) Purple (c) Orange\n",
    
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[1], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)
