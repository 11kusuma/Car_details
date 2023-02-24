from abc import ABC,abstractmethod
from logic import get_load,get_type,get_name

class Car(ABC):

    def __init__(self,owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):

        """
        The constructor initializes the given object attributes
        """
        self.owner=owner
        self.vehicle_name=vehicle_name
        self.vehicle_make=vehicle_make
        self.age=age
        self.kilometers_driven=kilometers_driven
        self.first_hand=first_hand
        self.second_hand=second_hand
        self.registration_number=registration_number
        self.occupation=occupation
        for k, v in self.occupation.items():
           setattr(self, k, v)
         
    @abstractmethod
    def get_vehicle_name():
        pass

    @abstractmethod
    def get_vehicle_type():
        pass

class Hatchback(Car):
    def __init__(self,owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):

        """
        inheriting the attributes from parent class(Car) using super() and initializing the value of vehicle_type attribute
        """
        super().__init__(owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation)
        self.vehicle_type="Hatchback"

    def load_data(self):
        """
        The method loads the data of object attributes into database by taking them as arguments
        params-
        owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation
        Returns-
        None
        """
        get_load(self.owner,self.vehicle_name,self.vehicle_make,self.vehicle_type,self.age,self.kilometers_driven,self.first_hand,self.second_hand,self.registration_number,self.occupation)

    def get_vehicle_name(self,vehicle_name):
        """
        The method returns the record of vehicle details when vehicle_name given is equal to the name of vehicle present in database
        param-
        vehicle_name-which needs to be checked
        Returns-
        record of details"""
        veh_name=get_name(vehicle_name)
        return veh_name

    def get_vehicle_type(self):
        """
        The method returns the record of details when vehicle_type given is equal to the type of vehicle present in the database
        param-
        vehicle_type-which needs to be checked
        Returns-
        record of details"""
        veh_type=get_type(self.vehicle_type)
        return veh_type

class Sedans(Car):
    def __init__(self,owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):
        super().__init__(owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation)
        self.vehicle_type="Sedans"

    def load_data(self):
        """
        The method loads the data of the object attributes into database by taking them as arguments
        params-
        owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation
        Returns-
        None
        """
        get_load(self.owner,self.vehicle_name,self.vehicle_make,self.vehicle_type,self.age,self.kilometers_driven,self.first_hand,self.second_hand,self.registration_number,self.occupation)

    def get_vehicle_name(self,vehicle_name):
         """
        The method returns the record of details when vehicle_name given is equal to the name of vehicle present in database
        param-
        vehicle_name-which needs to be checked
        Returns-
        record of details"""
         veh_name=get_name(vehicle_name)
         return veh_name

    def get_vehicle_type(self):
        """
        The method returns the record of details when vehicle_type given is equal to the type of vehicle present in the database
        param-
        vehicle_type-which needs to be checked
        Returns-
        record of details"""
        veh_type=get_type(self.vehicle_type)
        return veh_type

class SUV(Car):
    def __init__(self,owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):
        super().__init__(owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation)
        self.vehicle_type="SUV"

    def load_data(self):
        """
        The method loads the data of the object attributes into database by taking them as arguments
        params-
        owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation
        Returns-
        None
        """
        get_load(self.owner,self.vehicle_name,self.vehicle_make,self.vehicle_type,self.age,self.kilometers_driven,self.first_hand,self.second_hand,self.registration_number,self.occupation)    

    def get_vehicle_name(self,vehicle_name):
         """
        The method returns the record of details when vehicle_name given is equal to the name of vehicle present in database
        param-
        vehicle_name-which needs to be checked
        Returns-
        record of details"""
         veh_name=get_name(vehicle_name)
         return veh_name

    def get_vehicle_type(self):
        """
        The method returns the record of details when vehicle_type given is equal to the type of vehicle present in the database
        param-
        vehicle_type-which needs to be checked
        Returns-
        record of details"""
        veh_type=get_type(self.vehicle_type)
        return veh_type

class Premium_suv(Car):
    def __init__(self,owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):
        super().__init__(owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation)
        self.vehicle_type="Premium SUV"

    def load_data(self):
        """
        The method loads the data of the object attributes into database by taking them as arguments
        params-
        owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation
        Returns-
        None
        """
        get_load(self.owner,self.vehicle_name,self.vehicle_make,self.vehicle_type,self.age,self.kilometers_driven,self.first_hand,self.second_hand,self.registration_number,self.occupation)    

    def get_vehicle_name(self,vehicle_name):
         """
        The method returns the record of details when vehicle_name given is equal to the name of vehicle present in database
        param-
        vehicle_name-which needs to be checked
        Returns-
        record of details"""
         veh_name=get_name(vehicle_name)
         return veh_name

    def get_vehicle_type(self):
        """
        The method returns the record of details when vehicle_type given is equal to the type of vehicle present in the database
        param-
        vehicle_type-which needs to be checked
        Returns-
        record of details"""
        veh_type=get_type(self.vehicle_type)
        return veh_type

class Crossover(Car):
    def __init__(self,owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):
        super().__init__(owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation)
        self.vehicle_type="Crossovers"

    def load_data(self):
        """
        The method loads the data of the object attributes into database by taking them as arguments
        params-
        owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation
        Returns-
        None
        """
        get_load(self.owner,self.vehicle_name,self.vehicle_make,self.vehicle_type,self.age,self.kilometers_driven,self.first_hand,self.second_hand,self.registration_number,self.occupation)   

    def get_vehicle_name(self,vehicle_name):
         """
        The method returns the record of details when vehicle_name given is equal to the name of vehicle present in database
        param-
        vehicle_name-which needs to be checked
        Returns-
        record of details"""
         veh_name=get_name(vehicle_name)
         return veh_name

    def get_vehicle_type(self):
        """
        The method returns the record of details when vehicle_type given is equal to the type of vehicle present in the database
        param-
        vehicle_type-which needs to be checked
        Returns-
        record of details"""
        veh_type=get_type(self.vehicle_type)
        return veh_type

class Limousine(Car):
    def __init__(self,owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):
        super().__init__(owner,vehicle_name,vehicle_make,age,kilometers_driven,first_hand,second_hand,registration_number,occupation)
        self.vehicle_type="Limousine"

    def load_data(self):
        """
        The method loads the data of the object attributes into database by taking them as arguments
        params-
        owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation
        Returns-
        None
        """
        get_load(self.owner,self.vehicle_name,self.vehicle_make,self.vehicle_type,self.age,self.kilometers_driven,self.first_hand,self.second_hand,self.registration_number,self.occupation)   

    def get_vehicle_name(self,vehicle_name):
         """
        The method returns the record of details when vehicle_name given is equal to the name of vehicle present in database
        param-
        vehicle_name-which needs to be checked
        Returns-
        record of details"""
         veh_name=get_name(vehicle_name)
         return veh_name

    def get_vehicle_type(self):
        """
        The method returns the record of details when vehicle_type given is equal to the type of vehicle present in the database
        param-
        vehicle_type-which needs to be checked
        Returns-
        record of details"""
        veh_type=get_type(self.vehicle_type)
        return veh_type

h_1=Hatchback("john","Swift","Maruti","Hatchback",4,780,"yes","no","AP21TX2003",{"businessman":"BUSINESSMAN"})
h_2=Hatchback("Alex","i20","Maruti","Hatchback",5,5430,"yes","no","TN09WS3456",{"teacher":"TEACHER"})
h_3=Hatchback("James","i10","Maruti","Hatchback",5,5400,"no","yes","TN19XS3486",{"doctor":"DOCTOR"})
h_4=Hatchback("Thomas","Baleno","Maruti","Hatchback",2,1764,"yes","no","TS09WS3496",{"professor":"PROFESSOR"})
h_5=Hatchback("Miller","Wagon","Maruti","Hatchback",4,1435,"yes","no","TS39AS3056",{"actor":"ACTOR"})
s_1=Sedans("Anderson","Verna","Hyundai","Sedans",2,3450,"no","yes","KL34ET8790",{"businessman":"BUSINESSMAN"})
s_2=Sedans("Smith","Virtus","Volkswagen","Sedans",4,454,"yes","no","AP05TY6701",{"professor":"PROFESSOR"})
s_3=Sedans("Arun","skoda slavia","Volkswagen","Sedans",2,6218,"yes","no","RJ02TR2341",{"doctor":"DOCTOR"})
s_4=Sedans("Jones","Audi","Volkswagen","Sedans",3,2336,"no","yes","AP03YT6571",{"teacher":"TEACHER"})
s_5=Sedans("Taylor","BMW","BMW","Sedans",1,2036,"yes","no","TS04WA2300",{"actor":"ACTOR"})
suv_1=SUV("Martin","Scorpio","Mahindra","SUV",4,892,"yes","no","AP08TY567",{"teacher":"TEACHER"})
suv_2=SUV("James","Thar","Mahindra","SUV",1,9023,"yes","no","AP01RW0001",{"businessman":"BUSINESSMAN"})
suv_3=SUV("Nelson","Creta","Hyundai","SUV",3,6700,"no","yes","TS32QE4321",{"businessman":"BUSINESSMAN"})
suv_4=SUV("Allen","XUV 700","Mahindra","SUV",2,5660,"no","yes","TN76EW2135",{"doctor":"DOCTOR"})
suv_5=SUV("Robert","Fortuner","Toyota","SUV",2,907,"yes","no","KA43UI0872",{"professor":"PROFESSOR"})
p_1=Premium_suv("Stewart","MG","SAIC Motor","Premium SUV",3,3444,"yes","no","TS32RE4567",{"actor":"ACTOR"})
p_2=Premium_suv("Morris","BMW X5","BMW","Premium SUV",5,778,"no","yes","AP98YU6709",{"teacher":"TEACHER"})
p_3=Premium_suv("Morgan","Volvo XC60","Geely","Premium SUV",2,5661,"yes","no","TS45VB760",{"businessman":"BUSINESSMAN"})
p_4=Premium_suv("Peter","Nissan","Renault","Premium SUV",4,2345,"yes","no","KL65TY4321",{"doctor":"DOCTOR"})
p_5=Premium_suv("Cook","BMW X7","BMW","Premium SUV",5,778,"no","yes","AP78YU6329",{"doctor":"DOCTOR"})
c_1=Crossover("Ross","Renault kwid","Renault","Crossovers",2,5665,"yes","no","DL65TY3241",{"teacher":"TEACHER"})
c_2=Crossover("Scott","Ford","Nissan","Crossovers",2,605,"no","yes","KL65TY3241",{"businessman":"BUSINESSMAN"})
c_3=Crossover("Hill","Maruti suzuki","Suzuki","Crossovers",4,7165,"yes","no","KA43TY3241",{"professor":"PROFESSOR"})
c_4=Crossover("Evans","Tata Tiago NRG","Tata","Crossovers",3,980,"no","yes","AP15TY3841",{"doctor":"DOCTOR"})
c_5=Crossover("Rogers","Ford","Ford","Crossovers",4,1651,"no","yes","KA55XY3041",{"teacher":"TEACHER"})
li_1=Limousine("Julia","Bentley Mulsanne","Bentley","Limousine",6,655,"yes","no","KA45HK8731",{"student":"STUDENT"})
li_2=Limousine("Bell","Cadillac XTS","General motors","Limousine",3,561,"no","yes","TS09UT4321",{"professor":"PROFESSOR"})
li_3=Limousine("Ward","Porsche Cayenne","Volkswagen","Limousine",2,8767,"yes","no","AP65YT3421",{"businessman":"BUSINESSMAN"})
li_4=Limousine("Richard","Hyundai Equus","Hyundai","Limousine",2,1877,"yes","no","TS65YT3421",{"doctor":"DOCTOR"})
li_5=Limousine("Ben","Mercedes Benz","Daimler AG","Limousine",5,9789,"no","yes","TN03RD8421",{"teacher":"TEACHER"})
li_5.load_data()
li_4.load_data()
li_3.load_data()
li_2.load_data()
li_1.load_data()
h_1.load_data()
h_2.load_data()
h_3.load_data()
h_4.load_data()
h_5.load_data()
s_1.load_data()
s_2.load_data()
s_3.load_data()
s_4.load_data()
s_5.load_data()
p_1.load_data()
p_2.load_data()
p_3.load_data()
p_4.load_data()
p_5.load_data()
suv_1.load_data()
suv_2.load_data()
suv_3.load_data()
suv_4.load_data()
suv_5.load_data()
c_1.load_data()
c_2.load_data()
c_3.load_data()
c_4.load_data()
c_5.load_data()

print(li_1.get_vehicle_name("XTS")) 
print("-----------------------------------------------------------")    #prints no match for the vehicle_name given
result=c_1.get_vehicle_name("Ford")
for i in result:
    print(i,end="\n\n")                                                #prints the record of vehicle details with name="Ford"
print("-----------------------------------------------------------")
r=c_1.get_vehicle_type()                                        
for i in r:
    print(i,end="\n\n")                                           #prints the list of vehicle details with specified vehicle_type