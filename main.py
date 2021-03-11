class Student:                              #Defined a class named Student.
    def __init__(self,id,name,surname):     #Created an init func. to define my parameters that I will use in Student class.
        self.id = id                         #Self takes no argumants.
        self.name = name
        self.surname = surname


    def __str__(self):
        return self.id+" " +self.name +" "+self.surname
def file_tolist():
    my_file = open("student.txt","r")
    student_list =[]
    for line in my_file:
        line=line.strip()
        student_list.append(line)

    my_file.close()
    return student_list
def list_toobject(student_list):
    object_list = []
    for a in student_list:
        students = a.split()
        student_objects = Student(students[0],students[1],students[2])
        object_list.append(student_objects)
    return object_list


stlist=list_toobject(file_tolist())

def student_id(stlist):
    id_number=input('Please enter the ID of the student:')
    for st in stlist:
        if st.id==id_number:
            return st.name+' '+st.surname
    else:
        return 'Student not found'
uni_list = []
uni_file = open("university.txt",'r')           #Created empty list and read the university.txt file and then append
for line in uni_file:                              #the lines in uni_list.I didnt put that into a func. because I wanted to
    line = line.strip()                            #use uni_list in other functions.
    line=line.split(",")
    uni_list.append([int(line[0]),(line[1]),int(line[2]),int(line[3])])



def sortuni():
    uni_file = open("university.txt",'r')
    uni_list = []
    for line in uni_file:
        line = line.strip()
        line=line.split(",")
        uni_list.append([int(line[0]),(line[1]),int(line[2]),int(line[3])])

    basepoints_list=[]
    for k in range(len(uni_list)):
        basepoints_list.append(uni_list[k][2])
    basepoints_list.sort(reverse=True)
    for n in basepoints_list:
        for m in range(len(uni_list)):
            if n==uni_list[m][2]:
                print(uni_list[m][1]+","+str(uni_list[m][2]))

    uni_file.close()


answersfile=open("answers.txt",'r')
answer_list=[]
choices1=[]
for ans_lines in answersfile:
    ans_lines=ans_lines.strip()
    answer_list.append(ans_lines)
for lines in answer_list:
    lines=lines.split()
    choices1.append([lines[0],lines[3],lines[4],lines[5],lines[6],lines[7]])

answersfile.close()
keysfile=open("key.txt",'r')
key_list=[]
for key_lines in keysfile:
    key_lines=key_lines.strip()
    key_list.append(key_lines)
keysfile.close()
choice={}


def results():
    stu_choice_list=[]
    for k in range(len(choices1)):
        choices=[]
        for l in range(1,6):
            for u in range(len(uni_list)):
                if (int(uni_list[u][0])== int(choices1[k][l])):
                    choices.append((uni_list[u][1]))
        choice[choices1[k][0]]=choices

    results_file=open("results.txt",'w')
    for i in answer_list:
        answer_line=i.split()
        if answer_line[1]=="A":
            T_answers=0
            F_answers=0
            B_answers=0
            for i in range(len(answer_line[2])):
                if key_list[0][i]==answer_line[2][i]:
                    T_answers=T_answers+1
                elif answer_line[2][i]=="-":
                    B_answers=B_answers+1
                else:
                    F_answers=F_answers+1
            for stu_line in stlist:
                if stu_line.id==answer_line[0]:
                    dn1 = choice[str(stu_line.id)]
                    dn2="{} {} {} {} {}".format(*dn1)

                    results_file.write(str(stu_line.id) + " " + stu_line.name + " " + stu_line.surname + " " + "A"+ " " +
                    str(T_answers) + " " + str(F_answers) + " " + str(B_answers)+ " " +  str(T_answers-(F_answers/4))+" "+
                    str((T_answers-(F_answers/4))*15)+" "+dn2+"\n")

        elif answer_line[1]=="B":
            T_answers = 0
            F_answers = 0
            B_answers = 0
            for i in range(len(answer_line[2])):
                if key_list[1][i] == answer_line[2][i]:
                    T_answers = T_answers + 1
                elif answer_line[2][i] == "-":
                    B_answers = B_answers + 1
                else:
                    F_answers = F_answers + 1
            for stu_line in stlist:
                if stu_line.id == answer_line[0]:
                    dn1 = choice[str(stu_line.id)]
                    dn2 = "{} {} {} {} {}".format(*dn1)
                    results_file.write(str(stu_line.id) + " " + stu_line.name + " " + stu_line.surname + " " + "B" + " " +
                    str(T_answers) + " " + str(F_answers) + " " + str(B_answers)+" "+ str(T_answers-(F_answers/4))+" "+
                    str((T_answers-(F_answers/4))*15)+" "+dn2+"\n")

    results_file.close()
results()
def sortbyscore ():
    results()
    results_file = open('results.txt','r')
    results_list = []
    for line in results_file:
        line=line.strip()
        line=line.split()
        results_list.append([line[0],(line[1]),line[2],line[8]])

    scores=[]
    scores2=[]
    for k in range(len(results_list)):
        scores.append(results_list[k][3])
    scores.sort(reverse=True)

    for n in scores:
        for m in range(len(results_list)):
            if n == results_list[m][3] and results_list[m] not in scores2:
                scores2.append(results_list[m])
    for b in scores2:
        print(b[0],b[1],b[2],b[3])


quota={}
def quota_of_uni(uniID):
    if (int(quota[uniID])>0):
        quota[uniID]=quota[uniID]-1
        return True
    else:
        return False

def placement():
    uniDict={}
    uni_file = open("university.txt", 'r')
    for line in uni_file:
        line = line.strip()
        line = line.split(",")
        uniDict[int(line[0])]=int(line[2]) # id ye gore puan attim

    uni_file.close()

    results_file = open('results.txt', 'r')
    results_list = []
    for line in results_file:
        line = line.strip()
        line = line.split()
        results_list.append([line[0], (line[1]), line[2], line[8]])

    scores = []
    scores2 = []
    for k in range(len(results_list)):
        scores.append(results_list[k][3])
    scores.sort(reverse=True)

    for n in scores:
        for m in range(len(results_list)):
            if n == results_list[m][3] and results_list[m] not in scores2:
                scores2.append(results_list[m])

    choice2 = {}
    for k in range(len(choices1)):
        choices = []
        for l in range(1, 6):
            for u in range(len(uni_list)):
                if (int(uni_list[u][0]) == int(choices1[k][l])):
                    choices.append((uni_list[u][0]))
        choice2[choices1[k][0]] = choices #taking the choices with student id

    for i in range(len(uni_list)):
        quota[int(uni_list[i][0])]=uni_list[i][3]

    stu_in_uni=[]
    for i in range(len(scores2)):
        for k in choice2[scores2[i][0]]:
           if uniDict[k]<= float(scores2[i][3]) and quota_of_uni(k):
               stu_in_uni.append([k,scores2[i][0],scores2[i][1],scores2[i][2],scores2[i][3]])
               break

    for uniName in range(len(uni_list)):
        print(uni_list[uniName][1])
        print(("-")*len(uni_list[uniName][1]))
        if(quota[uni_list[uniName][0]]==uni_list[uniName][3]):
            print("No Students")
        else:
            count=0
            for student in range(len(stu_in_uni)):
                if stu_in_uni[student][0]== uni_list[uniName][0]:
                    count=count+1
                    print(count,")",stu_in_uni[student][1],stu_in_uni[student][2],stu_in_uni[student][3],stu_in_uni[student][4])

def leftover():
    uniDict = {}
    uni_file = open("university.txt", 'r')
    for line in uni_file:
        line = line.strip()
        line = line.split(",")
        uniDict[int(line[0])] = int(line[2])  # id ye gore puan attim

    uni_file.close()

    results_file = open('results.txt', 'r')
    results_list = []
    for line in results_file:
        line = line.strip()
        line = line.split()
        results_list.append([line[0], (line[1]), line[2], line[8]])

    scores = []
    scores2 = []
    for k in range(len(results_list)):
        scores.append(results_list[k][3])
    scores.sort(reverse=True)

    for n in scores:
        for m in range(len(results_list)):
            if n == results_list[m][3] and results_list[m] not in scores2:
                scores2.append(results_list[m])

    choice2 = {}
    for k in range(len(choices1)):
        choices = []
        for l in range(1, 6):
            for u in range(len(uni_list)):
                if (int(uni_list[u][0]) == int(choices1[k][l])):
                    choices.append((uni_list[u][0]))
        choice2[choices1[k][0]] = choices  # Taking the choices with student ID

    for i in range(len(uni_list)):
        quota[int(uni_list[i][0])] = uni_list[i][3]

    stu_in_uni = []
    placed=[]
    for i in range(len(scores2)):
        for k in choice2[scores2[i][0]]:
            if uniDict[k] <= float(scores2[i][3]) and quota_of_uni(k):
                stu_in_uni.append([k, scores2[i][0], scores2[i][1], scores2[i][2], scores2[i][3]])
                placed.append(scores2[i][0])
                break

    print("The students who were not be able to placed anywhere")
    print('-'*20)
    left=0
    for l in scores2:
        if l[0] not in placed:
            print(l[0],l[1],l[2])
            left=left+1
    print('-'*20)
    print("Total",left)



def alldepartments():
    uni_list1=[]
    uni_file1=open('university.txt','r')
    for line in uni_file1:
        line=line.split(',')
        uni_list1.append(line)
    department_list=[]
    department_list1=[]
    for uni in uni_list1:
        a=uni[1].find("Department of")
        b=uni[1][a:]
        department_list.append(b)
    for department in department_list:
        if department not in department_list1:
            department_list1.append(department)

    for i in department_list1:
        z="*"
        print(z,i)

while True :
    print("""
        -----------------------------------------------------------
        1-Search for a student with a given ID and display his/her name and last name.
        2-List the universities and departments with a maximum base points.
        3-Create a file named 'results.txt' for each student.
        4-List the student information sorted by their score.
        5-List the students placed in every university/department.
        6-List the students who were not be able to placed anywhere.
        7-List all the departments.
        ------------------------------------------------------------
        """)
    s=input("Please enter a number to continue = ")

    if s == str(1):
        st = student_id(stlist)
        print(st)

    elif s==str(2):
        sortuni()

    elif s==str(3):
        results()
        print("saved results.txt")
    elif s==str(4):
        sortbyscore()

    elif s==str(5):
        placement()
    elif s==str(6):
        leftover()
    elif s==str(7):
        alldepartments()
    else:
        print("***Please enter valid number to continue***")

    t = input("Do you want to continue? (y)es or (n)o =")
    if t=="y":
        continue

    elif t=="n":
        break
