
num = int(input("Enter a number for table: "))
for i in range (1,11):
    print(num ,"x", i,'=',num*i )



# Number of rows in the pattern
rows = 5

# Outer loop handles the rows
for i in range(rows,0,- 1):
    # Inner loop handles the columns (stars per row)
    for j in range(i,0,- 1):
        print("*", end=" ")  # end=" " keeps printing on the same line
    print()  # Moves to the next line after finishing the row

print("\n")

#while loop pattern
rows = 5
i = 1

# Outer loop for rows
while i <= rows:
    j = 1
    # Inner loop for columns
    while j <= i:
        print("*", end=" ")
        j += 1
    print()  # Moves to the next line
    i += 1


#numpy array
import sys
import numpy as np
arr1=np.array([10,20,30,40,50])
print(arr1)

#multi numpy array
import sys

arr=np.array([[10,20,30,40],[5,6,7,8]])
print(arr)
print(arr[0,0])
print(arr[0,1])
print(arr[0,2])
print(arr[0,3])


print(arr[1,0])
print(arr[1,1])
print(arr[1,2])
print(arr[1,3])

#pandas series
import pandas as pd
stu_name=pd.Series(["Khushi","pari","jiyu","snehaa"])
print("student name")
print(stu_name)


import pandas as pd
stu_Rollno=pd.Series([12,15,10,11])
print("student Rollno")
print(stu_Rollno)


import pandas as pd
stu_course=pd.Series(["B.Sc.IT","BCA","CFA","BBA"])
print("student course")
print(stu_course)

#pandas datafream

import pandas as pd 
emp_data={"EmployeeID":[1,2,3,4,5],
          "Name":["khushi","mahi","prince","yatri","jiyu"],
          "department":["IT","HR","Sales","Marketing","HR"],
          "salary":[50000,25000,15000,35000,25000],
          "experience":["5 years","3 years","2 years","6 years","2 years"]}

df=pd.DataFrame(emp_data)
print("Employee data")
print(df)

#matplotlib (bar chart)
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("sales_data.csv")
plt.bar(df["Month"],df["Sales"],color="#37D6E8")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

#pie
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.pie(df["Sales"],
labels=df["Month"],
autopct='%1.1f%%',
colors=["#ABCBDD","#8FACBD","#7698C8","#76B1DCFF","#6DAEC8","#089CCD","#0381DC","#658FBC","#4F9EB4","#96D7F5"])

plt.title("Monthly Sales Distribution")

plt.show()

#pre
import pandas as pd
stu_marks=pd.Series([50,20,40,36,45],index=['abhi','cdo','zye','mars','sara'])
print(stu_marks)

