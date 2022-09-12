file = "Prob2.txt"
file2 = "Prob2result.txt"

openfile = open(file,"r")
name = openfile.readline()

openfile.readline()
q1 = openfile.readline()
q2 = openfile.readline()
q3 = openfile.readline()
q4 = openfile.readline()

openfile.readline()
a1=openfile.readline()
a2=openfile.readline()

openfile.readline()
e=openfile.readline()

Qa = (int(q1)+int(q2)+int(q3)+int(q4))/4
Aa = (int(a1)+int(a2))/2
grade = (int(Qa)+int(Aa)+int(e))/3

openfile.close()

if grade >= 75:
    remarks = "Passed"
else:
    remarks = "Failed"

openfile2 = open(file2,"w")
openfile2.write("Name : " + name +"\n")
openfile2.write("Average Quiz : {0:.2f} \n\n".format(Qa))
openfile2.write("Average Assignment :  {0:.0f} \n\n".format(Aa))
openfile2.write("Grade : {0:.0f} \n\n".format(grade))
openfile2.write("Remarks : {0} \n\n".format(remarks))
openfile2.close()
