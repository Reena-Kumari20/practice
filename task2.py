# Humne Task 1 mein scrape_top_list() function likh ke saari movies ki list nikaal li hai. 
# Iss task mein humein group_by_year naam ka ek naya function likhna hai jo ki movies ko by 
# year group karega. 

from task1 import scrapping
import json
def group_by_year(movies_list1):
    years=[]
    for i in movies_list1:
        year=i["year"]
        if year not in years:
            years.append(year)
        years.sort()
    #print(years)
    years1={}
    for i in years:
        years1[i]=[]
    for i in movies_list1:
        for j in years1:
            year=i["year"]
            if str(j)==str(year):
                years1[j].append(i)
    with open("task2.json","w") as f2:
        json.dump(years1,f2,indent=4)        
    return years1
group=group_by_year(scrapping)