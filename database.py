import pandas as pd
import numpy as np
import csv
info=[]
def get_into_dataframe(l1):
    """
    loads the data of attributes to the database
    params-
    takes list of attributes as argument
    Returns-
    None
    """
    info.append(l1)
    df=pd.DataFrame(info,columns=['owner','vehicle_name','vehicle_make','vehicle_type','age','kilometers_driven','1st_hand','2nd_hand','registration_number','occupation'])
    df.to_csv("C:\\Users\\hp\\OneDrive\\Desktop\\data.csv",index=False,header=True)
    new_df=pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\data.csv")
    #print(new_df)

def get_data_1(vehicle_name):
    """
    checks if vehicle_name given is present in database
    params-
    vehicle_name
    Returns-
    list of records if given value is present in database else shows the message
    """
    with open("C:\\Users\\hp\\OneDrive\\Desktop\\data.csv") as file_obj:
        reader_obj = csv.DictReader(file_obj)
        list_1=[]
        for row in reader_obj:
             if row["vehicle_name"]==vehicle_name:
                 list_1.append(row)
        if len(list_1)==0:
            return "No match for the given vehicle_name"
        else:
          return list_1

def get_data_2(vehicle_type):
    """
    gives the record of vehicle details when specific vehicle_type is passed
    params-
    vehicle_type
    Returns-
    list of records with given vehicle_type
    """
    with open("C:\\Users\\hp\\OneDrive\\Desktop\\data.csv") as file_obj:
        reader_obj = csv.DictReader(file_obj)
        list_2=[]
        for row in reader_obj:
             if row["vehicle_type"]==vehicle_type:
                list_2.append(row)
        return list_2
