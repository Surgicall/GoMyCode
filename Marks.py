print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A+")
elif avg>=81 and avg<91:
    print("Your Grade is A")
elif avg>=71 and avg<81:
    print("Your Grade is B+")
elif avg>=61 and avg<71:
    print("Your Grade is B")
elif avg>=51 and avg<61:
    print("Your Grade is C+")
elif avg>=41 and avg<51:
    print("Your Grade is C")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E+")
elif avg>=0 and avg<21:
    print("Your Grade is E")
else:
    print("Invalid Input!")
