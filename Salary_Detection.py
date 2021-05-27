import  joblib

#load model
model = joblib.load('model.pki')

#predict
x = model.predict([[ float(input("Enter Experience(years): ") ) ]] )

print(f"Salary { x[0] } INR")
