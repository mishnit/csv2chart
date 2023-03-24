import pandas as pd 
import numpy as np 
import plotly.express as pex

#Banners Revenue
df = pd.read_csv('Growth_Tech-Revenue_Data_Jan22-Nov22_Banners.csv')
df = df[["Adv Name", "Industry", "Total Revenue", "Month"]]
df = pd.DataFrame(data=(df.groupby(["Adv Name", "Industry", "Month"])["Total Revenue"].sum().reset_index()))
fig = pex.sunburst(df , path = ["Industry", "Adv Name", "Month"], values = "Total Revenue")
#fig.show()
fig.write_html('Banners.html')
