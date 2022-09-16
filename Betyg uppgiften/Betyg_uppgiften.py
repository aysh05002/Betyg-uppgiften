betyg=int(input("Hur manga poang av 100 har du fat i provet?? "))
if betyg<=100 and betyg>=90:
    print("Du har fat A i betyg")
elif betyg<90 and betyg>=80:
    print("Du har fat B i betyg")
elif betyg<80 and betyg>=70:
    print("Du har fat C i betyg")
elif betyg<70 and betyg>=60:
    print("Du har fat D i betyg")
elif betyg<60 and betyg>=50:
    print("Du har fat E i betyg")
else:
    print("Du har fat F i betyg")