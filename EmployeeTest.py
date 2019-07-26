class Employee:
    def __init__(self, name, gender, emailid):
        self.name = name;
        self.gender = gender;
        self.emailid = emailid;

def main():
    emp1 = Employee('abc','Male','abc@gmail.com')
    print ("Employe details are : ",emp1.name,emp1.gender,emp1.emailid)
    print('%s is %d years old' % ('Joe', 42))

if __name__ =="__main__":
    main()

