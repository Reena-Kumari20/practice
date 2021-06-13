# Task 2 mein humne movies ko year ke hisaab se group karne ka code toh likh liya. 
# Ab hum inn hi movies ko decade ke hisaab se group karenge. 10 saal se milakar ek decade banta hai. 
# Jaise: 1. 1960 se 1969 tak ke beech ke saare saal 1960s ke decade mein aate hain. 
# 2. 1970 se 1979 tak ke beech ke saare saal 1970s ke decade mein aate hain. 
# 3. 1980 se 1989 tak ke beech ke saare saal 1980s ke decade mein aate hain. 
# 4. 2000 se 2009 tak ke beech ke saare saal 2000s ke decade mein aate hain.

from task2 import group
import json
def sequence_of_year(movies_list):
    years_list=[]
    for index in movies_list:
        year_modules=index%10
        a=index-year_modules
        if a not in years_list:
            years_list.append(a)
    dict1={}
    for i in years_list:
        dict1[i]=[]
    for i in dict1:
        year1=i+9
        for year2 in movies_list:
            for year3 in movies_list[year2]:
                if year2<=year1 and year2>=i:
                    dict1[i].append(year3)
    with open("task3.json","a") as f2:
        json.dump(dict1,f2,indent=4)        
sequence_of_year(group)
 