 
#import 
import csv 
import os
from sqlite3 import Row
  
#Declare file
budget_data_csv =os.path.join('Resources','budget_data.csv')
print(budget_data_csv)

#declar variables
total_months =1
totalProfit =[]
totalLost =[]
revenueChange_list=[]
revenueChange  = []
totalrevenue = 0
prevoiusRevanu = 0
Month_change =[]
great_increase =["",10000]
great_decreace =["",0]
with open("FinancialAnalysis.txt",'w') as outs:
    outs.write("Financial Analysis" + "\n")
    outs.write(".................." + "\n")
#print the output into  txt file 


# open the csv file to read
with open(budget_data_csv,'r') as file:
    csvreader = csv.reader(file)
    #read header 
    next(csvreader)
    #skip first row of data
    first_row = next(csvreader)
    #set prev revenue to equal first row's profit/loss
    prevoiusRevanu = int(first_row[1])
    totalrevenue += prevoiusRevanu
    
    for row in csvreader:
        print(row)
# find the total months
        total_months  +=1
        totalrevenue = totalrevenue + int(row[1])    
        
        #calculate average change in Revenue 
        revenueChange = int(row[1]) - prevoiusRevanu
        prevoiusRevanu = int(row[1])
        revenueChange_list = revenueChange_list + [revenueChange]
        
        
# # increase in revenue  btween date and amounts in the entire perit 
        if revenueChange > great_increase[1]:
            great_increase[1] = revenueChange 
            great_increase[0] = row[0]
    
# #Decrease in revenue 
        if revenueChange<great_decreace[1]:
            great_decreace[1] =revenueChange
            great_decreace[0] = row[0]
            
avrege_revenue = sum(revenueChange_list) / len(revenueChange_list)
print("Avrg_change:" +"$" + str(avrege_revenue ))


print("Total Revenue: %d"% totalrevenue)

print(great_decreace)
print(great_increase)
        
# Create an output file
output_file = os.path.join('output',"pybank_ result.txt")
with open(output_file,"w") as output_file:
     output_file.write("Financial Analysis" + "\n")
     output_file.write("----------------------------\n")
     output_file.write(f'Total Months: {total_months}\n')
     output_file.write(f'Total  : {totalrevenue}\n')
     output_file.write(f'Avrage:{avrege_revenue}\n')
     output_file.write(f'Greatest Increase: {great_increase}\n')
     output_file.write(f'greatest Deceace: {great_decreace}\n')
     
# Show the output in terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total Revenue: {totalrevenue}')
print(f'Avrage:{avrege_revenue}')
print(f'Total Increase: {great_increase}')
print(f'Total Decreas: {great_decreace}')


