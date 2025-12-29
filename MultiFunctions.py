class MultiFunctions():
    
    def Subfields(self):
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for subfield in Lists:
            print(subfield)

    def OddEven(self):
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
            result=num,"is Even number"
        else:
            print(num,"is Odd number")
            result=num,"is Odd number"
        return result
    
    def Elegible(self):
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender=="Male")and(Age>=21):
            print("Eligible")
            result="Eligible"
        elif(Gender=="Female")and(Age>=18):
            print("Eligible")
            result="Eligible"
        else:
            print("Not Eligible")
            result="Not Eligible"
        
        return result
    
    def percentage(self,S1,S2,S3,S4,S5):
        self.S1=S1
        self.S2=S2
        self.S3=S3
        self.S4=S4
        self.S5=S5
        Total=(self.S1+self.S2+self.S3+self.S4+self.S5)
        print(Total)
        result1=Total
        percentage=(Total/500)*100
        print(percentage)
        result2=percentage
        return result1,result2
    
    def triangle(self,a,b,x,y,z):
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        self.z=z
        Area=(self.a*self.b)/2
        print("Area of Triangle:",Area)
        result1=Area
        Perimeter=(self.x+self.y+self.z)
        print("Perimeter of Triangle:",Perimeter)
        result2=Perimeter
        return result1,result2
        