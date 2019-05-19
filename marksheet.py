Urdu=int(input('enter your urdu marks out of 200: '))
Islamiat=int(input('enter your islamiat marks out of 50: '))
English=int(input('enter your English marks out of 200: '))
Physics=int(input('enter your Physics marks out of 200: '))
ChEMISTRY=int(input('enter your Chemistry marks out of 200: '))
Mathematics=int(input("enter your Mathematics marks out of 200: "))
Pak_Studies=int(input('enter your Pakistan Studies marks out of 50: '))
sum=Urdu+Islamiat+English+Physics+ChEMISTRY+Mathematics+Pak_Studies
print("your total marks are: ", sum)
percentage=int((sum/1150)*100)
print("Hello!! your percentage is" , percentage)
if percentage>80:
    print('Welldone!!...Your Grade is A-one')
elif percentage>70 :
    print("Your Grade is A")
elif percentage>60 :
    print("your grade is B")
elif percentage>50:
    print("Your Grade is C")
elif percentage>40 :
    print("Your Grade is D")
