#Task 3: Data analysis using python (lists and data frames for managing books and members).
import pandas as pd

#Read the dataset.
data = pd.read_csv("C:/Users/CC/Downloads/motor_insure.csv/motor_data11-14lats.csv")

#Inspects its column by displaying the first 10 records.
print(data.head(10))

#Display records for 'make' and 'usage' for 'sets_num' that are more than 40.

print(data[data['SEATS_NUM'] > 40][['MAKE', 'USAGE']])

#Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes"""
import matplotlib.pyplot as plt

data['EFFECTIVE_YR'] = pd.to_numeric(data['EFFECTIVE_YR'], errors='coerce')

plt.plot(data['EFFECTIVE_YR'], data['CARRYING_CAPACITY'])
plt.ylabel('EFFECTIVE YEAR')
plt.xlabel('CARRYING  CAPACITY')
plt.title('Effective Year vs Carrying Capacity')
plt.show()