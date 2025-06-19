#HW1
#1
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
#2
df.head(3) #Displays first 3 rows
#3
df['age'].mean() #Calculates the mean of the 'age' column
#4
df[['age', 'City']]
#5
df['Salary'] = np.random.randint(10000, 100000, size=(len(df))) #Creates a new column 'Salary' with random numbers from 10000 to 10000. and size equals to the number of rows so that it return an array of number with this length for each cell in the new column
#6
df.describe() #generates statisctics of the dataframe
#HW2
#1
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000, 6000, 7500, 8000], 'Expenses': [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)
#2
sales_and_expenses[['Sales', 'Expenses']].max()
#3
sales_and_expenses[['Sales', 'Expenses']].min()
#4
sales_and_expenses[['Sales', 'Expenses']].mean()
#HW3
#1
data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
        'January': [1200, 200, 300, 150],
        'February': [1300, 220, 320, 160],
        'March': [1400, 240, 330, 170],
        'April': [1500, 250, 350, 180]}
expenses = pd.DataFrame(data)
#2
expenses = expenses.set_index('Category') 
expenses.max(axis=1)
#3
expenses.min(axis=1)
#4
expenses.mean(axis=1)
