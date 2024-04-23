# Written by Brian Vargas, University of Utah

# Part one
user = input ("Please enter your first name: ")
print('Hello ' + user + '!')


# Weight Grade
assignments = input('Enter your assignments percentage:')

assignments = float(assignments)

midterms = input('Enter your final midterm percentage: ')

midterms = float(midterms)

quizzes = input('Enter your final quizzes percentage: ')

quizzes = float(quizzes)

labs = input('Enter your final labs percentage: ')

labs = float(labs)

ebook = input('Enter your final ebooks percentage: ')

ebook = float(ebook)

# Possible final exam outcomes
for value in range(0,120,20):
    final_scores = (assignments * 30 / 100 + midterms * 20 / 100 + quizzes * 15 / 100 + labs * 10 / 100 + ebook * 10 / 100 + value * 15 / 100)
    print(user + "," , 'if your final exam score is', value, 'your course percentage for CS 1400 will be', final_scores)





