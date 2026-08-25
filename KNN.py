from sklearn.neighbors import KNeighborsClassifier 
x=[[1],[2],[4],[5]]
y=["Fail","Fail","Pass","Pass"]

model=KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)

#predict for a new student
hours=[[2.5]]
prediction =model.predict(hours)
print(prediction)