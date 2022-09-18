betyg=int(input("Hur manga poang av 100 har du fat i provet?? "))
if betyg<=100 and betyg>=90:
    print("Poang \t Betyg")
    print("==============")
    print(betyg, "\t A")
elif betyg<90 and betyg>=80:
    print("Poang \t Betyg")
    print("==============")
    print(betyg, "\t B")
elif betyg<80 and betyg>=70:
    print("Poang \t Betyg")
    print("==============")
    print(betyg, "\t C")
elif betyg<70 and betyg>=60:
    print("Poang \t Betyg")
    print("==============")
    print(betyg, "\t D")
elif betyg<60 and betyg>=50:
    print("Poang \t Betyg")
    print("==============")
    print(betyg, "\t E")
else:
    print("Poang \t Betyg")
    print("==============")
    print(betyg, "\t F")
