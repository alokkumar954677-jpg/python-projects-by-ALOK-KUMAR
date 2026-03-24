import matplotlib.pyplot as plt 
student=['ALOK KUMAR','ABHAY KUMAR','KUNAL KUMAR','KANCHAN KUMAR']
marks=[90,91,50,40]
plt.subplot(2,2,1)
plt.bar(student,marks,color=['blue','green','pink','red'],label="2025 student")
for i in range(len(student)):
    plt.text(i,marks[i]+1,str(marks[i])+'%',ha='center')
plt.xlabel("STUDENT NAME")
plt.ylabel(" STUDENT MARKS")
plt.title("STUDENT MANAGEMENT MARKS ")
plt.tight_layout()
plt.ylim(0,100)
plt.xticks(rotation=20)
plt.legend()
#line graph
day=['mon','tue','wed','thu']
p=[60,70,80,50]
plt.subplot(2,2,2)
plt.plot(day,p,color='blue',label="2025 student",marker='o')
for i in range(len(day)):
    plt.text(i,p[i]+1,str(p[i])+'%',ha='center')
plt.xlabel("DAY NAME")
plt.ylabel("STUDENT DAY BY MARKS")
plt.legend()
plt.title("STUDENT PROGRESS")
plt.tight_layout()
plt.ylim(0,90)
plt.grid(color='blue',linestyle=":")
# pie graph
subject=['MATH','PHYSICS','PYTHON','DSA']
mark=[85,75,65,70]
plt.subplot(2,2,3)
plt.pie(mark,labels=subject,colors=['yellow','pink','blue','green'],autopct='%1.1f%%')
plt.title('STUDENT MARKS PROGRESS')
# smmrry
avg = round(sum(mark)/len(mark), 2)
topper = max(marks)
topper_name = student[marks.index(topper)]

plt.subplot(2,2,4)
plt.axis('off')
plt.text(0.1,0.6,f"AVERAGE={avg}")
plt.text(0.1,0.4,f"TOPPER={topper_name},=({topper}%)")
plt.title("SUMMERY")
plt.tight_layout()
plt.show()