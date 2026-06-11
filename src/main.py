import numpy as np

file_path = "data/Global_Cybersecurity_Threats_2015-2024.csv"

data = np.genfromtxt(
    file_path,
    delimiter=",",
    dtype=str,
    encoding="utf-8"
)

attack_types, counts= np.unique(data[1:,2], return_counts=True)


# most common attacks count 
max_counts= np.max(counts)
print("most common attacks:", max_counts)

#position of that attack 
position=np.argmax(counts)

#most common attacks
attack_name=attack_types[position] 
print("attack name:", attack_name)

#countries
countires, counts= np.unique(data[1:,0], return_counts=True)

#most common country attacked count
common_country=np.max(counts)
print("most common country attacks:",common_country)
      
#position
position2=np.argmax(counts)

#country name 
country_name=countires[position2]
print("country name:",country_name)

#industry 
industry_type, counts= np.unique(data[1:,3], return_counts=True)


#position
position1=np.argmax(counts)

#most targated industry 
industry_name=industry_type[position1]
print("industry name:",industry_name)

#industry loss 
industry_loss=np.max(counts)
print("industry incident:", industry_loss)

#financial analysis 
financial_loss=data[1:,4].astype(float)
type(financial_loss[0]) 

#highest financial loss 
highest_financial=np.max(financial_loss)
print("the biggest financial loss:",highest_financial)

#mean of financial loss 
mean=np.mean(financial_loss)
print("financil mean:", mean)

#total financial loss 
total=np.sum(financial_loss)
print("sum of the finanical loss:",total)

#security analysis 
defence_mechanism_used, counts= np.unique(data[1:,8], return_counts=True)

#position
position4=np.argmax(counts)

#best security 
mechanism=defence_mechanism_used[position4]
print("best mechanism:",mechanism)

#security vulnerbilty 
security_vulnerbilty_type , counts = np.unique(data[0:,7], return_counts= True)

#position
position5=np.argmax(counts)

#most vulnerbilty is 
vulnerbilty= security_vulnerbilty_type[position5]
print("vulnerbale spot:",vulnerbilty)