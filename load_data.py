from app.models import Dataset
import pandas as pd

df = pd.read_csv("D:\\Real_Estate_Price_Prediction\Backend\mysite\Datasets.csv") # Enter path of csv file

locality_name = list(df[df.columns[0]])
bhks = list(df[df.columns[1]])
per_sq_ft_area = list(df[df.columns[2]])
price_per_sq_ft_area = list(df[df.columns[3]])
construction_status = list(df[df.columns[4]])
price = list(df[df.columns[5]])
appt_name = list(df[df.columns[6]])
appt_link = list(df[df.columns[7]])

for i in range(len(bhks)): #from here press shift+enter
    Dataset.objects.create(locality_name=locality_name[i],bhks=bhks[i],per_sq_ft_area=per_sq_ft_area[i],price_per_sq_ft_area=price_per_sq_ft_area[i],construction_status=construction_status[i],price=price[i],appt_name=appt_name[i],appt_link=appt_link[i])#press tab before writing this line