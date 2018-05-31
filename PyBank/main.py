
# coding: utf-8

# In[1]:


import csv
import os


# In[2]:


budget_CSV = os.path.join("budget_data_1.csv")
output = "budget_analysis_1.txt"


# In[3]:


tot_months = 0
prev_revenue = 0
month_change = []
rev_change_list = []
increase = ["", 0]
decrease = ["", 1000000000]
tot_revenue = 0


# In[4]:


data = csv.DictReader(open(budget_CSV))


# In[5]:


for row in data:
    tot_months = tot_months + 1
    tot_revenue = tot_revenue + int(row["Revenue"])

    revenue_change = int(row["Revenue"]) - prev_revenue
    prev_revenue = int(row["Revenue"])
    rev_change_list = rev_change_list + [revenue_change]
    month_change = month_change + [row["Date"]]

    if (revenue_change > increase[1]):
        increase[0] = row["Date"]
        increase[1] = revenue_change

    if (revenue_change < decrease[1]):
        decrease[0] = row["Date"]
        decrease[1] = revenue_change


# In[6]:


avg = sum(rev_change_list) / len(rev_change_list)


# In[7]:


analysis = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {tot_months}\n"
    f"Total Revenue: ${tot_revenue}\n"
    f"Average Revenue Change: ${avg}\n"
    f"Greatest Increase in Revenue: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Revenue: {decrease[0]} (${decrease[1]})\n")
print(analysis)


# In[11]:


datafile = open(output, "w")
datafile.write(output)

