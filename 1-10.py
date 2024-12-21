###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers

correct_answers_number = len(list(filter(bool, test_results)))
# calculates the number of incorrect answers

incorrect_answers_number = question_number - correct_answers_number

# calculates the percentage of correct answers

correct_answers_percentage = round((correct_answers_number / question_number) * 100, 2)

print('TEST STATISTICS')
print('===============')
print('Number of questions: ', question_number)
print('Number of correct answers: ', correct_answers_number)
print('Number of incorrect answers: ', incorrect_answers_number)
print('Percentage of correct answers: ', correct_answers_percentage)
