from sklearn.neural_network import MLPClassifier
x=[[1],[2],[4],[5]]
y=["Fail","Fail","Pass","Pass"]

#Create and rain the model
model=MLPClassifier(hidden_layer_sizes=(2,),max_iter=5000,random_state=42)
model.fit(x,y)

#give new input
hours=[[3]]

#predict result
prediction=model.predict(hours)

print(prediction)