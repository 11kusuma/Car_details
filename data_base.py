import pandas as pd
import numpy as np
import csv

def get_data(vehicle_name,vehicle_type):
    with open("C:\\Users\\hp\\OneDrive\\Desktop\\data.csv") as file_obj:
      
        reader_obj = csv.DictReader(file_obj)
        for row in reader_obj:
       # print(row)
             if row["vehicle_name"]==vehicle_name and row["vehicle_type"]==vehicle_type:
                 return row
    
"""info=[["john","Swift","Maruti","Hatchback",34,78,"yes","no","AP21TX2003"],
      ["Alex","i20","Maruti","Hatchback",45,543,"yes","no","TN09WS3456"],
      ["James","i10","Maruti","Hatchback",55,54,"no","yes","TN19XS3486"],
      ["Thomas","Baleno","Maruti","Hatchback",25,176,"yes","no","TS09WS3496"],
      ["Miller","Wagon","Maruti","Hatchback",49,143,"yes","no","TS39AS3056"],
      ["Anderson","Verna","Hyundai","Sedans",23,345,"no","yes","KL34ET8790"],
      ["Smith","Virtus","Volkswagen","Sedans",45,45,"yes","no","AP05TY6701"],
      ["Arun","skoda slavia","Volkswagen","Sedans",52,621,"yes","no","RJ02TR2341"],
      ["Jones","Audi","Volkswagen","Sedans",32,233,"no","yes","AP03YT6571"],
      ["Taylor","BMW","BMW","Sedans",21,203,"yes","no","TS04WA2300"],
      ["Martin","Scorpio","Mahindra","SUV",45,89,"yes","no","AP08TY567"],
      ["James","Thar","Mahindra","SUV",21,90,"yes","no","AP01RW0001"],
      ["Nelson","Creta","Hyundai","SUV",43,67,"no","yes","TS32QE4321"],
      ["Allen","XUV 700","Mahindra","SUV",32,566,"no","yes","TN76EW2135"],
      ["Robert","Fortuner","Toyota","SUV",22,90,"yes","no","KA43UI0872"],
      ["Stewart","MG","SAIC Motor","Premium SUV",43,344,"yes","no","TS32RE4567"],
      ["Morris","BMW X5","BMW","Premium SUV",45,778,"no","yes","AP98YU6709"],
      ["Morgan","Volvo XC60","Geely","Premium SUV",23,566,"yes","no","TS45VB760"],
      ["Peter","Nissan","Renault","Premium SUV",43,234,"yes","no","KL65TY4321"],
      ["Cook","BMW X7","BMW","Premium SUV",45,778,"no","yes","AP78YU6329"],
      ["Ross","Renault kwid","Renault","Crossovers",24,65,"yes","no","DL65TY3241"],
      ["Scott","Datsun","Nissan","Crossovers",25,605,"no","yes","KL65TY3241"],
      ["Hill","Maruti suzuki","Suzuki","Crossovers",34,165,"yes","no","KA43TY3241"],
      ["Evans","Tata Tiago NRG","Tata","Crossovers",43,98,"no","yes","AP15TY3841"],
      ["Rogers","Ford","Ford","Crossovers",44,165,"no","yes","KA55XY3041"],
      ["Bell","Cadillac XTS","General motors","Limousine",43,561,"no","yes","TS09UT4321"],
      ["Ward","Porsche Cayenne","Volkswagen","Limousine",42,87,"yes","no","AP65YT3421"],
      ["Richard","Hyundai Equus","Hyundai","Limousine",22,187,"yes","no","TS65YT3421"],
      ["Ben","Mercedes Benz","Daimler AG","Limousine",52,97,"no","yes","TN03RD8421"],
      ["Julia","Bentley Mulsanne","Bentley","Limousine",36,65,"yes","no","KA45HK8731"]
]"""

