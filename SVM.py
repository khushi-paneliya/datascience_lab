from sklearn.svm import SVC 
x=[[1],[2],[4],[5]]
y=["Fail","Fail","Pass","Pass"]

#create svm model with a simple linear boundary 
model=SVC (kernel="linear")
model.fit(x,y)

#predict for a new student
hours=[[2]]
prediction =model.predict(hours)
print(prediction)