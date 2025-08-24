
def new_game():
    guesses =[]
    correct_guess =0
    question_num = 0

    for key in question:
         print('#------------------------------#')
         print(key)
         print(options[question_num])
         answer = str(input('your answer A , B or C:')).upper()
         guesses.append(answer)
         correct_guess += check_answer(question.get(key),answer)
         question_num += 1
    check_score(guesses ,correct_guess)


def check_score(guesses , score):
 print("___________________")
 print('correct answer :')
 for i in question:
      print(question.get(i) + " " ,end='')


 print("guesses : " ,end=" ")
 for i in guesses:
      print(i + " ",end='')
 print()

 print('your score : ',score ,  "" + 'out of 3' )
 percentage = int((score /len(question))*100)
 print(str(percentage) + "%")

 again = input("Do you want to play again? (y/n): ").lower()
 if again == 'y':
      play_again()
 else:
      print("Goodbye")

def check_answer(trueanswer ,guessanswer ):
           if trueanswer ==guessanswer:
                print("Correct!")
                return 1
           else:
                print("Wrong!")
                return 0

def play_again():
     new_game()


question = {"who created python : "  : "A" ,
            "when was python introduced :" : "C" ,
            "is Earth round ?" : "A"}

options = [ ["A.Guido van Rossum" , "B.rahul" , "C.chan"] ,
            ['A.1992' , "B.1993" , "C.1991"] ,
            ['A.yes' , 'B.no' , 'C.maybe']]

new_game()