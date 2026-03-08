import random
name = ""
random_question=("Am i gonna be successful?:")
answer_number=random.randint(1,9)

if answer_number==1:
  answer="Yes Definitely"
elif answer_number ==2:
  answer="It is decidedly so"
elif answer_number==3:
  answer="Without a doubt"
elif answer_number==4:
  answer="Reply hazy,try again"
elif answer_number==5:
  answer="ask again later"
elif answer_number==6:
  answer="Better not tell you now"
elif answer_number==7:
  answer="my sources say no"
elif answer_number==8:
  answer="Outlook not so good"
elif answer_number==9:
  answer="Very doubtful"
else:
  print("Error!")

print(str(name)+ "Question : "+ random_question )
print("Magic 8-Ball's answer: " + answer)
