import requests
import datetime as datetime

PIXEL_ENDPOINTS="https://pixe.la/v1/users"

USERNAME="ferdeno1012"
TOKEN="ferdenoo"



user_parameter={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=PIXEL_ENDPOINTS,json=user_parameter)
# print(response.text)

graph_endpoint=f"{PIXEL_ENDPOINTS}/{USERNAME}/graphs"
graph_id="graph1"
graph_config={
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ichou"
}

#this is used to hidden the token in search bar that is passed in the browser 
headers={
    "X-USER-TOKEN":TOKEN
}

# reponse=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# #this header is passed to hide the token number or encrypt data in the address bar
# print(reponse.text)

today=datetime.datetime(year=2023,month=7,day=11)
print(today.strftime("%Y%m%d"))
#strftime will format the date according to our needs

update_data_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"15.3"
}
# update_data_endpoint=f"{PIXEL_ENDPOINTS}/{USERNAME}/graphs/{graph_id}"
# reponse=requests.post(url=update_data_endpoint,json=update_data_config,headers=headers)
# print(reponse.text)

put_config={
    "quantity":"34.5"
}

# put_endpoints=f"{PIXEL_ENDPOINTS}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
# reponse=requests.put(url=put_endpoints,json=put_config,headers=headers)
# print(reponse.text)


delete_endpoints=f"{PIXEL_ENDPOINTS}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
reponse=requests.delete(url=delete_endpoints,headers=headers)
print(reponse.text)