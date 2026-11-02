import pandas as pd
def load_data():
    df = pd.read_csv("bicycle_data.csv")
    return df

def check_column_change_type(df):
    print(df.columns)
    print(df.head())
    print(df.dtypes)

# Date: date and time of each hourly observation; should be datetime.
# Fremont Bridge Sidewalks, south of N 34th St Total: total bicycle count across both sidewalks; should be an integer.
# Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk: bicycle count on the west sidewalk; should be an integer.
# Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk: bicycle count on the east sidewalk; should be an integer.
# Use nullable Int64 for counts to preserve missing values.

    df["Date"] = pd.to_datetime(
    df["Date"], format="%m/%d/%Y %I:%M:%S %p"
    )
    count_columns = df.columns[1:]
    df[count_columns] = df[count_columns].astype("Int64")
    print(df.head()) 
    return df

def add_column(df):
    df["total_count"] = (
    df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]
    + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"])

    df["hour"] = df["Date"].dt.hour
    df["year"] = df["Date"].dt.year
    return False

def create_df(df):
    df_2016 = df[df["year"] == 2016].copy()
    return df_2016

def count_missing(df_2016):
    missing_points = df_2016.isna().any(axis=1).sum()
    print(missing_points)
    print(df_2016[df_2016.isna().any(axis=1)])
    # Number of missing data: one missing data at 2016-03-13 02:00:00.
    # Remove rows with missing total counts before analysis.
    df_2016 = df_2016.dropna()
    return df_2016

def make_plot(df_2016):
    import matplotlib.pyplot as plt
    hourly_counts = df_2016.groupby("hour")["total_count"].sum()
    plt.bar(hourly_counts.index, hourly_counts.values,
            color="skyblue", width=0.6)

    plt.title("Fremont Bridge Bicycle Counts by Hour, 2016")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Total daily counts")
    plt.xticks(range(24))

    plt.tight_layout()
    plt.savefig("counts_by_hour.png")
    plt.close()      # Set to not pop up the plot
    return hourly_counts

def busiest_hour(df_2016, hourly_counts):
    days_per_hour = df_2016.groupby("hour")["total_count"].count()
    hourly_average = hourly_counts / days_per_hour
    busiest_hour = hourly_average.idxmax()
    print("busiest hour is: ", busiest_hour)
    # The busiest hour on average is 17:00 (5 PM).
    return busiest_hour


if __name__ == "__main__":
    df = load_data()
    check_column_change_type(df)
    add_column(df)
    df_2016= create_df(df)
    df_2016 = count_missing(df_2016)
    hourly_counts = make_plot(df_2016)
    make_plot(df_2016)
    busiest_hour(df_2016, hourly_counts)


