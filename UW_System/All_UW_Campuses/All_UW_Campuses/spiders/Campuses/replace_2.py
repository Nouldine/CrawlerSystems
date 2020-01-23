
import pandas as pd



data = [['Austria', 'Germany', 'hob', 'Australia'],
        ['Spain', 'France', 'Italy', 'Mexico']]

df = pd.DataFrame(data, columns = ['A','B','C','D'])

# Values to find and their replacements
findL = ['Australia', 'Mexico', 'United States', 'hob']
replaceL = ['Kangaroo', 'Spider Monkey', 'Eagle', 'Test']

# Select column (can be A,B,C,D)
col = 'C';

# Find and replace values in the selected column
df[col] = df[col].replace(findL, replaceL)

print df 
