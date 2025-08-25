# numpy and pandas are libraries that are very useful for doing data analysis
# np.random.seed() is a special function that allows us to reproduce the same random data every time we run the code
# we generate 100 years of experience with a uniform distribution between 0.5 and 10 years
# we add 30000 to the years of experience and add a random number between 0 and 4000 to get the salaries
# we round the salaries to 2 decimal places
# we create a pandas DataFrame which is a 2D table with columns and rows
# we save the DataFrame to a csv file which is a file that can be read by computers and humans
# print a message to let the user know that the data has been saved

import numpy as np
import pandas as pd

np.random.seed(42) #by seed tutorial and my random data is same

years=np.random.uniform(0.5,10,100).round(2)

salaries=(30000 + years*6000 + np.random.normal(0,4000,size=100)).round(2)

df=pd.DataFrame({
    "yearsExperience":years,
    "salaries":salaries
})

df.to_csv("./data/salaries.csv",index=False)
print("data saved in file")

