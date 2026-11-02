# CSE 583 Homework 1

## Process
I loaded the bicycle count CSV using pandas, converted the date column
to datetime and the count columns to integers, and added
total count, hour, and year columns.

I then selected the 2016 data as a new data frame and found one time point with missing data. I removed that row before analysis.

I plotted bicycle counts by hour and saved the figure as counts_by_hour.png. 
I calculated the average count for each hour and identified 17:00 (5 PM) as the busiest hour.

## Bonus: Date and Time Formats

I converted the `Date` column from strings to pandas datetime dtype
using `pd.to_datetime()`. This allowed me to extract the year and hour
using `.dt.year` and `.dt.hour`.

| Type | Description |
| --- | --- |
| Python `datetime.datetime` | Represents an individual date and time using a Python object. |
| NumPy `datetime64` | Represents dates and times efficiently in arrays with a specified time unit. |
| pandas datetime | Uses `Timestamp` for individual values and typically a NumPy-backed datetime dtype for columns; supports vectorized operations and missing values (`NaT`). |

## AI Assistance
I used ChatGPT to help understand pandas codes, file paths,
function return values, and plotting, and to debug my code.
