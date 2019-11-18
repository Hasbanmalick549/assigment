sub1 = int(input("maths"));
sub2 = int(input("physics"));
sub3 = int(input("chemestry"));
sub4 = int(input("urdu"));
sub5 = int(input("english"));
all_subject = (sub1+sub2+sub3+sub4+sub5)/5 
if all_subject >= 80 and all_subject <= 100 :
    print("Percentage")
    print(all_subject)
    print("Grade A+")
elif all_subject >= 70 and all_subject <= 80 :
    print("Percentage")
    print(all_subject)
    print("Grade A")
elif all_subject >= 60 and all_subject <= 70 :
    print("Percentage")
    print(all_subject)
    print("Grade B")
elif all_subject >= 50 and all_subject <= 60 :
    print("Percentage")
    print(all_subject)
    print("Grade C")
elif all_subject >= 40 and all_subject <= 60 :
    print("Percentage")
    print(all_subject)
    print("Grade E")
elif all_subject > 33 and all_subject <= 40 :
    print("Percentage")
    print(all_subject)
    print("Only Pass")
elif all_subject < 33 :
    print("Percentage")
    print(all_subject)
    print("Fail")
else :
    print("you are given improper result")

