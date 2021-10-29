height=float(input("Enter Height in mts:"))
weight=float(input("Enter Weight in kgs:"))
bmi=float(weight/(height*height));
print("wi "+str(bmi))
if(bmi>=18.5 and bmi<24.9):
    print("Normal weight")
elif(bmi<18.5):
    print("under weight")
else:
    print("Overweight")