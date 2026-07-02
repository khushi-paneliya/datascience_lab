import pandas as pd
stu_data={"roll no.": [1,2,3,4,5],
          "name":["Khushi","Pari","Snehaa","Prit","Siddh"],
          "Gender": ["female","female","female","male","male"],
          "course":["BscIt","BBA","BCA","BscIT","CA"],
          "marks":[87,88,78,90,95]}
df=pd.DataFrame(stu_data)
print("Student data")
print(df)
print("\n student info :")
print(df.info())
print("\n student describe :")
print(df.describe()) 



import pandas as pd
emp_data={"EmployeeID":[1,2,3,4,5],
          "Name":["khushi","mahi","prince","yatri","jiyu"],
          "department":["IT","HR","Sales","Marketing","HR"],
          "salary":[50000,25000,15000,35000,25000],
          "experience":["5 years","3 years","2 years","6 years","2 years"]}

df=pd.DataFrame(emp_data)
print("Employee data")
print(df)


import pandas as pd
car_data={"carID":[1256,2867,3907,4235,5674],
          "brandName":["BMW","Mahindra","Tata","ferrari","porsche"],
          "salary":[8000000,2500000,650000,8800000,9000000],
          "fuel type":["diesal","cng","","petrol","diesal"],
          "mileage":[90,88,67,82,89]}

df=pd.DataFrame(car_data)
print("car data")
print(df)

import pandas as pd
patient_data={"patientID":[10,25,36,44,56],
          "Name":["raj","jay","kay","mayo","prox"],
          "age":[50,42,46,78,34]
          "Gender": ["male","male","male","male","male"],
          "disease name":["fever","headche","BP","sugar","thoyrod"],
          "doctor name":["dr patel","dr mehta","dr hemto","dr raj","dr mehul"]}

df=pd.DataFrame(patient_data)
print("patient data")
print(df)