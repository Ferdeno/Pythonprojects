# list=[]
# temp=[]
# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     for i in data:
#         list.append(i)
#         if i[1]!="temp":
#             temp.append(int(i[1]))
#
# print(list)
# print(temp)


# pandas is easy to use compared to csv
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data.condition)
# print(type(data))

# whole rows and columns are called as Dataframe in pandas
# the columns are called as Series in pandas

# dict=data.to_dict()
# #convert the dataframe to another data_structure
# print(dict)

# list=data["temp"].to_list()
#covert the series to another data_structure


# from statistics import mean
# print(mean(list))

# print(data["temp"].max())

# print(data.temp)
#RETURNS THE ROW OF THE DATAFRAME
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# print(int(monday.temp)*(9/5)+32)

n={"Ferdeno":[21,2,12,2,2,1],"mervin":[16,2,1,2,1,1]}
# creates a new dataframe and convert to csv file 
new_data=pandas.DataFrame(n)
print(new_data)
new_data.to_csv("new_data.csv")

