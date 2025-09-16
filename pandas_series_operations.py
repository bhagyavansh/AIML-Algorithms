import pandas as pd

values = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
series = pd.Series(values, index=months)

# Step 2: Retrieve the value for the month of 'Mar'
value_mar = series['Mar']
print(f"Value for 'Mar': {value_mar}")

# Step 3: Increase all values by 10%
series = series * 1.10
print("\nValues increased by 10%:")
print(series)

# Step 4: Filter out values greater than 50
filtered_series = series[series <= 50]
print("\nValues less than or equal to 50:")
print(filtered_series)

# Step 5: Find the index (month) corresponding to the maximum value
max_month = series.idxmax()
print(f"\nMonth with the maximum value: {max_month}")

# Step 6: Check if any values are divisible by 5
divisible_by_5 = (series % 5 == 0).any()
print(f"\nAny values divisible by 5: {divisible_by_5}")

# Step 7: Replace all values greater than 60 with the value 60
series[series > 60] = 60
print("\nValues after replacing values greater than 60 with 60:")
print(series)

# Step 8: Create a new Series showing the cumulative sum
cumulative_sum_series = series.cumsum()
print("\nCumulative sum of the values:")
print(cumulative_sum_series)
