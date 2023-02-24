from database import get_into_dataframe,get_data_1,get_data_2

def get_load(owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occupation):
    list_of_loading_data=[]
    for k,v in occupation.items():
        """
        read key,value from occupation dictionary and assign the value of specified key to the variable
        """
        occ=occupation[k]
    if first_hand!=second_hand:
        """
        checks if first_hand is equal to second_hand and if so, it raises an exception else loads the data into database
        """
        list_of_loading_data.extend([owner,vehicle_name,vehicle_make,vehicle_type,age,kilometers_driven,first_hand,second_hand,registration_number,occ])
        get_into_dataframe(list_of_loading_data)
    else:
        raise Exception("First_hand and second_hand shouldn't be equal")

def get_name(vehicle_name):
    """
    gives the record of vehicle details if given vehicle_name is present in database
    params-
    vehicle_name 
    Return-
    returns the list of vehicle details else returns the message"""
    return_data_1=get_data_1(vehicle_name)
    return return_data_1

def get_type(vehicle_type):
    """
    gives the record of vehicle details if given vehicle_type is present in database
    params-
    vehicle_type 
    Return-
    returns the list of vehicle details"""
    return_data_2=get_data_2(vehicle_type)
    return return_data_2
