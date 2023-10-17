import pandas as pd
import numpy as np


class EmployerDataPreparation():
 
         
    def zero_one_encoding_employer(self, x):
        if x == "0":
            return 0
        elif pd.isnull(x):
            return np.nan
        else:
            return 1
        

class SalaryAccountDataPreparation():

   
    def zero_one_encoding_salary_account(self, x):
        if x == "0":
            return 0
        
        elif pd.isnull(x):
            return np.nan
        else:
            return 1


class CityDataPreparation:
    
    #(source https://statisticstimes.com/demographics/country/india-cities-population.php)
    
    def __init__(self, data):
        self.most_comm_city = list(data["City"].value_counts()[:10].index)
        # over 10 mln people
        self.big_cities = ['Delhi', 'Mumbai', 'Kolkata', 'Bengaluru', 'Chennai', 'Hyderabad']  
        
        # from 2 to 10 mln people
        self.medium_cities = ['Ahmadabad', 'Surat', 'Pune', 'Jaipur', 'Lucknow', 'Kozhikode', 'Malappuram', 'Thrissur', 
                     'Kochi', 'Kanpur',  'Indore', 'Nagpur', 'Coimbatore', 'Thiruvananthapuram', 'Patna', 
                     'Bhopal', 'Agra', 'Vadodara', 'Kannur', 'Visakhapatnam', 'Nashik', 'Vijayawada'] 
         

    def big_medium_small_city_groupping(self, x):
        if x in self.big_cities:
            x = 'big_city'
            return x
        elif x in self.medium_cities:
            x = 'medium_city'
            return x
        elif pd.isnull(x):
            return np.nan
        else:
            x = 'small_city'
            return x


class AgeDataPreparation:
    
    
    def __init__(self, data):
        self.data = data
    
    def age_counter(self):
        self.data['DOB'] = pd.to_datetime(self.data['DOB'], format='%d-%b-%y')
        self.data['Lead_Creation_Date'] = pd.to_datetime(self.data['Lead_Creation_Date'], format='%d-%b-%y')
        self.data["DOB"] = self.data["DOB"].apply(lambda x: x - pd.DateOffset(years=100) if x.year > 2010 else x)
        self.data["Age"]= (self.data['Lead_Creation_Date'] - self.data["DOB"]).apply(lambda x: round(x.days/365, 0))
        return self.data["Age"]


class OtherSimpleEncoding:
    
    
    def __init__(self, data):
        self.data = data
    
    def mobile_verified_encoding(self):
        """Encoding 
        N = 0
        Y = 1
        """
        self.data["Mobile_Verified"] = self.data["Mobile_Verified"].replace({"N": 0, "Y": 1})
        return self.data["Mobile_Verified"]
        
    def filled_form_encoding(self):
        """Encoding 
        N = 0
        Y = 1
        """
        self.data["Filled_Form"] = self.data["Filled_Form"].replace({"N": 0, "Y": 1})
        return self.data["Filled_Form"]
        
    def gender_encoding(self):
        """Encoding 
        Male = 0
        Female = 1
        """
        self.data["Gender"] = self.data["Gender"].replace({"Male": 0, "Female": 1})
        return self.data["Gender"]
    
    
    def device_encoding(self):
        """Encoding 
        Web-browser = 0
        Mobile = 1
        """
        self.data["Device_Type"] = self.data["Device_Type"].replace({"Web-browser": 0, "Mobile": 1})
        return self.data["Device_Type"]
