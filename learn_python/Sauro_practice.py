import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### Intro to panda dataframes! (pandas works a lot like R dataframes)


# df = pd.read_csv("alkirempi/MPI_national.csv", header = True) #read from data file
# header describes whether or not there are variable/columns names at top of data

# if the columns have no names and you want to give them names, use the optional parameter
# names = ['Var1', 'Var2', ...]

example_data = {'Day':[1,2,3,4,5,6],
                'Visitors':[43, 53, 34, 45, 64, 34],
                'Bounce_rate':[65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(example_data)

#print (data)
print ("\ngetting variables\n")
vars = list(df) # gets list of variables in data
print (vars)


## Getting columns of data

#single column
#print(df['Visitors']) # same as below
print ("\nsingle columns\n")
print (df.Visitors) # extracts a column of data (all observations of given variable ISO)
print (df.Visitors.tolist()) # gives list of data instead

#multiple columns
print ("\nmultiple columns\n")
print(df[['Visitors', 'Bounce_rate']])
print(np.array(df[['Visitors', 'Bounce_rate']])) # extracting multiple columns into array

print ("\nData.Head()\n")
print (df.head())  # prints FIRST few observations; give glimpse of what table looks like
print ("\nData.Tail()\n")
print (df.tail(3)) # prints LAST 3 observations; gives a glimpse of what table looks like

## indexes in pandas dataframe;
# allows us to organize our data to extract specific observations. i.e. before when I had
# no index,to extract an observation I had to know what row of the data table it was in
# Now, I just need to know the Day the observation occurred on to collect that info.
print ("\nSetting an Index\n")
df2 = df.set_index('Day')
print (df2)
# to set it while reading file in, use optional parameter index_col = int in read_csv.


# change variables names
print("\nchanging variable names\n")
# only include column names you want to change; old_name : new_name
# inplace=True is the same as df = df.rename(...)
df.rename(columns= {'Bounce_rate': 'losers'}, inplace=True)
print(df.head())


# combining several data frames
print("\ncombining several data frames\n")
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

concat = pd.concat([df1, df2]) # this essentially just adds on extra rows of observations
print (concat)

#concat2 = pd.concat([df1,df2,df3])
#print(concat2)
# notice how it creates extra rows at the bottom rather than just combining this information
# with the already existing data (as it is compatible in this case)

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year': [2001, 2002, 2003, 2004]})

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                   'Year' : [2005, 2006, 2007, 2008]})

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year': [2001, 2002, 2003, 2004]}
                   )

merged = pd.merge(df1, df3, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print (merged)

#joined = df1.join(df2)
#joined.set_index('Year', inplace=True)
#print (joined)






### Intro to Seaborn: data visualization made easy
sns.set()
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", row="time", col = "sex",
            hue="smoker", style="smoker", size="size", kind= "scatter",
            data=tips)

plt.show()
# x,y are variables within the data set.

# col/row = BLANK splits the data into different groups based on the value
# each observation has in the BLANK variable, and plots them
# separately. i.e. in the example above, the data is split by the
# time of the meal: Lunch or Dinner.
# row = BLANK separates each value of BLANK along rows

# size = how to weight our observations. i.e. if we are plotting a scatterplot, we
# can change the weight of the dots based on a third variable (a different one than
# x and y) Changes size of data points

# hue = Variable; each data point receives a color based on its value of the given variable

# style = Variable; each data point receives a different styled marker (i.e. star vs
# cross vs dot) based on its value of the given variable

# kind = what type of plot to make (Scatter, Line, etc)






### Testing Tellurium
import tellurium as te
import roadrunner
import antimony

r = te.loada('''
model feedback()
  // Reactions:
  J0: Nan1 + Mol -> Nan1Mol; (K1*Nan1*Mol);
  J1: Nan1Mol -> Nan1 + Mol; (K_1*Nan1Mol); 
  J2: Nan1Mol + Nan2 -> Nan1MolNan2; (K2*Nan1Mol*Nan2)
  J3: Nan1MolNan2 + GeneOff -> GeneOn; (K3*Nan1MolNan2*GeneOff);
  //J4: GeneOn -> Nan1MolNan2 + GeneOff; (K_3*GeneOn);
  
  // Species initializations:
  Nan1 = 0.0001692; 
  Mol = 0.0001692/2; 
  Nan2 = 0.0001692; 
  Nan1Mol = 0;
  Nan1MolNan2 = 0; 
  GeneOff = 5*10^-5; 
  GeneOn = 0;
  
  // Variable initialization:
  const K1, K_1, K2, K3, K_3;
  K1 = 6.1*10^5; 
  K_1 = 8*10^-5; 
  K2 = 3.3*10^5; 
  K3 = 1*10^5; 
  K_3 = 0;
  
end''')

result = r.simulate(0, .5, 1000)
plt.plot(result)
plt.show()