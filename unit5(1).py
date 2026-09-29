#step1: Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier

#step2:read csv dataset
data=pd.read_csv("unit5.csv")
print(data)

#step3:seperate Input (x) and output(y)
x=data[["study_hours"]]
y=data["status"]

#step4:Divide data into Training and Testing data 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=32)

print("x Testing Data")
print(x_test)
print("y Testing Data")
print(y_test)

#step5:create Decision Tree model
model=DecisionTreeClassifier()


#step6:Test the model
model.fit(x,y)

#step7:Test the model
accuracy=model.score(x_test,y_test)
print("Accuracy :",accuracy)

#step8:Give new input
#new student input
hours=pd.DataFrame({"study_hours":[3.5]})
prediction=model.predict(hours)
print('prediction',prediction)