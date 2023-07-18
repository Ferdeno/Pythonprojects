import pandas

count_data={"Gray":[0],"Cinnamon":[0],"Black":[0],"Other":[0]}
csv_data=pandas.DataFrame(count_data)
squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
for i in squirrel_data["Primary Fur Color"]:
    if i == "Gray":
        # count_data["Gray"][0]+=1
        csv_data.Gray[0]+=1
    elif i == "Cinnamon":
        # count_data["Cinnamon"][0]+=1
        csv_data.Cinnamon[0]+=1
    elif i == "Black":
        # count_data["Black"][0]+=1
        csv_data.Black[0]+=1
    else :
        # count_data["Other"][0]+=1
        csv_data.Other[0]+=1

csv_data.to_csv("squirrel_color.csv")