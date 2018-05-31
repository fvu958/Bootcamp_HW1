
# coding: utf-8

# In[1]:


import csv
import os
import datetime as dt


# In[2]:


# Files to load and output (Remember to change these)
emp_data = os.path.join("employee_data1.csv")
output = "employee_data_reformatted1.csv"


# In[3]:


emp_id = []
first_names = []
last_names = []
dob = []
ssn = []
states = []


# In[4]:


us_state_abbrev = {
   "Alabama": "AL",
   "Alaska": "AK",
   "Arizona": "AZ",
   "Arkansas": "AR",
   "California": "CA",
   "Colorado": "CO",
   "Connecticut": "CT",
   "Delaware": "DE",
   "Florida": "FL",
   "Georgia": "GA",
   "Hawaii": "HI",
   "Idaho": "ID",
   "Illinois": "IL",
   "Indiana": "IN",
   "Iowa": "IA",
   "Kansas": "KS",
   "Kentucky": "KY",
   "Louisiana": "LA",
   "Maine": "ME",
   "Maryland": "MD",
   "Massachusetts": "MA",
   "Michigan": "MI",
   "Minnesota": "MN",
   "Mississippi": "MS",
   "Missouri": "MO",
   "Montana": "MT",
   "Nebraska": "NE",
   "Nevada": "NV",
   "New Hampshire": "NH",
   "New Jersey": "NJ",
   "New Mexico": "NM",
   "New York": "NY",
   "North Carolina": "NC",
   "North Dakota": "ND",
   "Ohio": "OH",
   "Oklahoma": "OK",
   "Oregon": "OR",
   "Pennsylvania": "PA",
   "Rhode Island": "RI",
   "South Carolina": "SC",
   "South Dakota": "SD",
   "Tennessee": "TN",
   "Texas": "TX",
   "Utah": "UT",
   "Vermont": "VT",
   "Virginia": "VA",
   "Washington": "WA",
   "West Virginia": "WV",
   "Wisconsin": "WI",
   "Wyoming": "WY",
}


# In[5]:


emp_dict = csv.DictReader(open(emp_data))


# In[6]:


for row in emp_dict:
    emp_id = emp_id + [row["Emp ID"]]
    
    split_name = row["Name"].split(" ")
    
    first_names = first_names + [split_name[0]]
    last_names = last_names + [split_name[1]]
    
    clean_dob = dt.datetime.strptime(row["DOB"], "%Y-%m-%d")
    clean_dob = clean_dob.strftime("%m/%d/%Y")
    
    dob = dob + [clean_dob]
    
    split_ssn = list(row["SSN"])
    split_ssn[0:3] = ("*", "*", "*")
    split_ssn[4:6] = ("*", "*")
    clean_ssn = "".join(split_ssn)

    ssn = ssn + [clean_ssn]

    abbrev = us_state_abbrev[row["State"]]

    states = states + [abbrev]


# In[7]:


emp_DB = zip(emp_id, first_names, last_names, dob, ssn, states)


# In[9]:


datafile = open(output, "w", newline="")
writer = csv.writer(datafile)
writer.writerow(["Emp ID", "First Name", "Last Name",
                    "DOB", "SSN", "State"])
writer.writerows(emp_DB)

