marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 2: "))
marks3 = int(input("enter marks 3: "))
t_per =(100*(marks1 + marks2 + marks3))/300

if(t_per>=40 and marks1>=33 and marks2 >=33 and marks3 >=33):
    print("you are pass",t_per)
else:
    print("you are failed",t_per)