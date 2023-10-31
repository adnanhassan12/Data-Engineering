import pandas as pd
employee_data = pd.read_csv('Employee_data.csv', encoding = 'ISO-8859-1')


# Split 'Full Name' into 'First Name' and 'Last Name'
employee_data[['first_name', 'last_name']] = employee_data['full_name'].str.split(n=1, expand=True)

#employee_data= employee_data.drop(columns=['Unnamed: 5'])
#employee_data= employee_data.drop(columns=['Unnamed: 6'])


# Check for null values using isna()
null_values = employee_data.isna()
#to count null values
null_count = null_values.sum()
print("\nDataFrame with Null Value Indicators:")
print(null_values)
print("\nCount of Null Values in Each Column:")
print(null_count)

employee_data['age'] = employee_data['age'].fillna(employee_data['age'].mean())
employee_data['salary'] = employee_data['salary'].fillna(employee_data['salary'].mean())

# Check for null values using isna()
null_values = employee_data.isna()
#to count null values
null_count = null_values.sum()
print("\nDataFrame with Null Value Indicators:")
print(null_values)
print("\nCount of Null Values in Each Column:")
print(null_count)

# Round the 'Age' and 'Salary' columns to two decimal places
employee_data['age'] = employee_data['age'].round(2)
employee_data['salary'] = employee_data['salary'].round(2)

# Remove special characters from the 'City' column
employee_data['city'] = employee_data['city'].str.replace('[^a-zA-Z ]', '', regex=True)
# Change the order of columns
employee_data = employee_data[['full_name', 'first_name',  'last_name', 'age', 'salary','address', 'city']]
employee_data.to_csv('transformed_employee_data.csv', index=False)

print(employee_data)
