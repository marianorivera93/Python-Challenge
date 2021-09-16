#import budget data
import os
import csv

import statistics 

csvpath= os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print (csvreader)
    csv_header=next (csvreader)
    month= []
    revenue=[]
    revenue_change=[]
    monthly_change=[]

 #Read the header row first
    csv_header= next (csvreader)
    print (f"CSV Header: {csv_header}")

#Read each row of data after the header. Append.
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))

#Find Total # of Months, Profit, Losses, Average
    revenue_int= map(int,revenue)
    total_revenue= (sum(revenue_int)) 
    print (total_revenue)

    i=0
    for i in range (len(revenue)-1):
        profit_loss=int(revenue[i+1])- int (revenue[i])
        revenue_change.append(profit_loss)
    Total= sum(revenue_change)
    monthly_change=Total/len(revenue_change)
    print(monthly_change)

#Greatest Increase & Decrease
    profit_increase=max (revenue_change)
    profit_decrease=min (revenue_change)
    print (profit_increase)
    print (profit_decrease)
    k=revenue_change.index(profit_increase)
    j=revenue_change.index(profit_decrease)
    month_increase=month [k+1]
    month_decrease=month [j+1]

#Analysis Statements
    output_path='Financial Analysis.txt'
with open(output_path, 'w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["-----------------------------------"])
    csvwriter.writerow([f'Total Months: {len(month)}'])
    csvwriter.writerow([f'Total Profits/Losses: ${total_revenue}'])
    csvwriter.writerow([f'Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}'])
    csvwriter.writerow([f'The Greatest Increase In Profits: ${monthly_change[0]}'])
    csvwriter.writerow([f'The Greatest Decrease In Profits: ${monthly_change[len(monthly_change)-1]}'])

