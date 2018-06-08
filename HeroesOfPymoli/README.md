
- There are 573 Total Players, and of the total amount of players, the majority are males (82%), with a fair of amount of females (17.5%) rounding out the major portion of players.

- Largest age demographic is the 20-24 (42%) range with other notable age demographics being 15-19 (17.8%) and 25-29(15.48%).

- Like many online games with microtransactions, a small percentage of users who are willing to invest a greater deal of momey over a long period of time or "whales", are an important userbase for us and should be heavily considered when making gameplay updates. 


```python
import pandas as pd
import os
import numpy as np
```


```python
path = os.path.join("purchase_data.json")
df = pd.read_json(path)
df['Age'] = pd.to_numeric(df['Age'])
df['Item ID'] = pd.to_numeric(df['Item ID'])
df['Price'] = pd.to_numeric(df['Price'])
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Item ID2'] = df['Item ID']
df = df.loc[:, ['Gender', 'SN', 'Age', 'Price', 'Item Name', 'Item ID', 'Item ID2']]
dup_drop = df.drop_duplicates('SN')
```


```python
player_count = dup_drop['SN'].nunique()
player_count_df = pd.DataFrame({
    'Total Players': [player_count]
})
player_count_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
num_uni_items = df['Item ID'].nunique()
#num_uni_items
```


```python
avg_pur_price = df['Price'].mean()
#avg_pur_price
```


```python
tot_pur = df['Item Name'].count()
#print(tot_pur)
```


```python
tot_rev = df['Price'].sum()
#print(tot_rev)
```


```python
# Purchasing Analysis DF
pur_analysis_df = pd.DataFrame({
    'Number of Unique Items': [num_uni_items],
    'Average Price': [avg_pur_price],
    'Number of Purchases': [tot_pur],
    'Total Revenue': [tot_rev]
})
pur_analysis_df['Average Price'] = pur_analysis_df['Average Price'].map("${:,.2f}".format)
pur_analysis_df['Total Revenue'] = pur_analysis_df['Total Revenue'].map("${:,.2f}".format)
pur_analysis_df = pur_analysis_df[['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']]
pur_analysis_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
gender_series = dup_drop['Gender'].value_counts()
male_count = gender_series['Male']
print(male_count)
perMale = male_count / player_count
perMale
```

    465
    




    0.8115183246073299




```python
female_count = gender_series['Female']
print(female_count)
perFemale = female_count / player_count
print(perFemale)
```

    100
    0.17452006980802792
    


```python
other_count = player_count - male_count - female_count
print(other_count)
perOther = 1 - (perMale + perFemale)
perOther
```

    8
    




    0.013961605584642212




```python
gender = ['Male', 'Female', 'Other / Non-Disclosed']
gen_analysis_df = pd.DataFrame({
    'Percentage of Players': [perMale, perFemale, perOther],
    'Total Count': [male_count, female_count, other_count]
}, index=gender)
gen_analysis_df['Percentage of Players'] = gen_analysis_df['Percentage of Players'].map("{:.2%}".format)
gen_analysis_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
male_users = df.loc[df['Gender'] == 'Male']
female_users = df.loc[df['Gender'] == 'Female']
other_users = df.loc[df['Gender']  == 'Other / Non-Disclosed']

male_purCount = male_users['Item ID'].value_counts().sum()
female_purCount = female_users['Item ID'].value_counts().sum()
other_purCount = other_users['Item ID'].value_counts().sum()
```


```python
male_avgPrice = male_users['Price'].mean()
male_avgPrice
```




    2.9505213270142154




```python
female_avgPrice = female_users['Price'].mean()
female_avgPrice
```




    2.815514705882352




```python
other_avgPrice= other_users['Price'].mean()
other_avgPrice
```




    3.2490909090909086




```python
male_totVal = male_users['Price'].sum()
female_totVal = female_users['Price'].sum()
other_totVal = other_users['Price'].sum()
print(male_totVal)
female_totVal
```

    1867.68
    




    382.90999999999997




```python
male_sn = male_users.groupby('SN')
male_normal = male_sn['Price'].sum().mean()

female_sn = female_users.groupby('SN')
female_normal = female_sn['Price'].sum().mean()

other_sn = other_users.groupby('SN')
other_normal = other_sn['Price'].sum().mean()
```


```python
gen_pur_analysis_df = pd.DataFrame({
    'Purchase Count': [male_purCount, female_purCount, other_purCount],
    'Average Purchase Price': [male_avgPrice, female_avgPrice, other_avgPrice],
    'Total Purchase Value': [male_totVal, female_totVal, other_totVal],
    'Normalized Totals': [male_normal, female_normal, other_normal]
}, index=gender)

gen_pur_analysis_df['Average Purchase Price'] = gen_pur_analysis_df['Average Purchase Price'].map("${:,.2f}".format)
gen_pur_analysis_df['Normalized Totals'] = gen_pur_analysis_df['Normalized Totals'].map("${:,.2f}".format)
gen_pur_analysis_df['Total Purchase Value'] = gen_pur_analysis_df['Total Purchase Value'].map("${:,.2f}".format)
gen_pur_analysis_df[['Purchase Count','Average Purchase Price','Total Purchase Value', 'Normalized Totals']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 1000]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
df['Age Ranges'] = pd.cut(dup_drop['Age'], bins, labels=group_names)
age_counts = df['Age Ranges'].value_counts()
agePer = age_counts / player_count * 100
age_demo_df = pd.DataFrame({
    'Percentage of Players': agePer,
    'Total Count': age_counts
})
age_demo_df.sort_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.315881</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.013962</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.452007</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.200698</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.183246</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.202443</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.712042</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.919721</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df with all purchases of all users regardless of duplicates
df['Age Ranges'] = pd.cut(df['Age'], bins, labels=group_names)
# df
```


```python
age_pur_tot = df.groupby('Age Ranges').sum()['Price']
age_pur_count = df.groupby('Age Ranges').count()['Price']
age_pur_avg = df.groupby('Age Ranges').mean()['Price']
age_norm_tot = age_pur_tot / age_demo_df['Total Count']

age_pur_analysis_df = pd.DataFrame({
    'Purchase Count': age_pur_count,
    'Average Purchase Price': age_pur_avg,
    'Total Purchase Value': age_pur_tot,
    'Normalized Totals': age_norm_tot
})

age_pur_analysis_df['Average Purchase Price'] = age_pur_analysis_df['Average Purchase Price'].map("${:,.2f}".format)
age_pur_analysis_df['Total Purchase Value'] = age_pur_analysis_df['Total Purchase Value'].map("${:,.2f}".format)
age_pur_analysis_df['Normalized Totals'] = age_pur_analysis_df['Normalized Totals'].map("${:,.2f}".format)
age_pur_analysis_df = age_pur_analysis_df[['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals']]
age_pur_analysis_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.20</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Spenders
big_ballas = df.pivot_table(index='SN', values='Price', aggfunc=np.sum).sort_values(by='Price', ascending=False)
big_ballas['Purchase Count'] = df['SN'].value_counts()
big_ballas = big_ballas.rename(columns={'Price': 'Total Purchase Value'})
big_ballas['Average Purchase Price'] = big_ballas['Total Purchase Value'] / big_ballas['Purchase Count']
big_ballas['Total Purchase Value'] = big_ballas['Total Purchase Value'].map("${:,.2f}".format)
big_ballas['Average Purchase Price'] = big_ballas['Average Purchase Price'].map("${:,.2f}".format)
big_ballas = big_ballas[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value']]
big_ballas.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Popular Items
pop_count_df = df.pivot_table(index=['Item ID', 'Item Name'], values=['Item ID2'],
                              aggfunc={'Item ID2': len})
tpv_df = df.pivot_table(index=['Item ID', 'Item Name'], values=['Price'],
                        aggfunc={'Price': np.sum})
pop_item_df = pd.merge(pop_count_df, tpv_df, left_index=True, right_index=True).sort_values(by='Item ID2', ascending=False)
pop_item_df = pop_item_df.rename(columns={
    'Item ID2': 'Purchase Count',
    'Price': 'Total Purchase Value'
})
pop_item_df['Price'] = pop_item_df['Total Purchase Value'] / pop_item_df['Purchase Count']
pop_item_df['Total Purchase Value'] = pop_item_df['Total Purchase Value'].map("${:,.2f}".format)
pop_item_df['Price'] = pop_item_df['Price'].map("${:,.2f}".format)
pop_item_df = pop_item_df[['Purchase Count','Price','Total Purchase Value']]
pop_item_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Profitable Items
profitable_df = df.pivot_table(index=['Item ID', 'Item Name'], values='Price', aggfunc=np.sum)
profitable_df.head()
most_profitable_df = pd.merge(profitable_df, pop_count_df, left_index=True, right_index=True).sort_values(by='Item ID2', ascending=False)
most_profitable_df = most_profitable_df.rename(columns={
    'Item ID2': 'Purchase Count',
    'Price': 'Total Purchase Value'
})
most_profitable_df['Price'] = most_profitable_df['Total Purchase Value'] / most_profitable_df['Purchase Count']
most_profitable_df['Total Purchase Value'] = most_profitable_df['Total Purchase Value']
most_profitable_df['Price'] = most_profitable_df['Price'].map("${:,.2f}".format)
most_profitable_df = most_profitable_df.sort_values('Total Purchase Value', ascending=False)
most_profitable_df = most_profitable_df[['Purchase Count', 'Price', 'Total Purchase Value']]
most_profitable_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


