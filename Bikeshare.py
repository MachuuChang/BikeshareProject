import time
import pandas as pd
import numpy as np

# Definiting each data set
CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}

DEFINE_CITY = ['Chicago', 'New York City', 'Washington']

DEFINE_MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

DEFINE_DAY_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in DEFINE_CITY:
        print("Please enter which city you would like to filter to: Chicago, New York City, Washington. "
              "Please answer with the full city name.")
#get users input for particular city      
        city = input().title()
        if city not in DEFINE_CITY:
            print('This is not a valid input, please ensure you are entering the full city name. Let us try again!')

    print('You have selected ' + city.title())

    month = ''
    while month not in DEFINE_MONTH:
        print("Please enter which month you would like to filter to: January, February, March, April, May, June.Please "
              "answer with the full month name. If you do not require any filters, please enter All")
#get users if they would like to filter for a particular month
        month = input().title()
        if month not in DEFINE_MONTH:
            print('This is not a valid input, please ensure you are entering the full month name. Let us try again!')
    print('You have selected ' + month.title())

    day = ''
    while day not in DEFINE_DAY_OF_WEEK:
        print(
            'Please enter which day you would like to filter to: Monday, Tuesday, Wednesday, Thursday, Friday, '
            'Saturday, Sunday.Please answer with the full month name. If you do not require any filters, please enter '
            'All')
#get users if they would like to filter for a particular day of the week            
        day = input().title()
        if day not in DEFINE_DAY_OF_WEEK:
            print('This is not a valid input, please ensure you are entering the full name of the specific day')
    print('You have selected ' + day.title())
    return city, month, day

#Load data using the particular fields mentioned above   
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day'] = pd.to_datetime(df['Start Time']).dt.day_name()

    if month != 'All':
        df = df[df['month'] == DEFINE_MONTH.index(month) + 1]
    if day != 'All':
        df = df[df['day'] == day.title()]
    return df

#Generate statistics around popular month/day of the week/hour
def time_stat(df):
    start_time = time.time()
    popular_month_1 = df['month'].mode()[0]
    popular_month_2 = DEFINE_MONTH[popular_month_1 - 1]
    print('Most Common Month is: ', popular_month_2)

    popular_day = df['day'].mode()[0]
    print('Most Common Day is: ', popular_day)

    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Generate statistics around most popular stations
def station_stats(df):
    start_time = time.time()
    most_used_start_station = df['Start Station'].mode()[0]
    print('Most used start station:', most_used_start_station)

    most_used_end_station = df['End Station'].mode()[0]
    print('Most used end station:', most_used_end_station)

    df['Combination'] = df['Start Station'] + ' to ' + df['End Station']
    combination = df['Combination'].mode()[0]
    print('Most common trip :', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Generate statistics around trip duration
def trip_duration_stats(df):
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is ' + str(total_travel_time) + ' seconds')
    total_days_travelled = round(total_travel_time / 86400, 1)
    print('The total travel time in days is ' + str(total_days_travelled) + ' days')

    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ' + str(mean_travel_time) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Generate statistic on the customers details
def user_stats(df):
    start_time = time.time()

    print(str(df['User Type'].value_counts()))
    try:
        print(str(df['Gender'].value_counts()))
    except:
        print('There is no gender data for this input')

    try:
        print('Earliest Birth Year is ' + str(int(df['Birth Year'].min())))
        print('Most Recent Birth Year is ' + str(int(df['Birth Year'].max())))
        print('Most Frequent Birth Year is ' + str(int(df['Birth Year'].mode()[0])))
    except:
        print('There is no birth year data for this input')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

#Provide user option to view raw data
def display_data(df):
    top_row = 0
    bottom_row = 5
    maximum_row = int(df.shape[0])
    answer = input('Would you like to see some raw data? Please enter "Yes" or "No"\n').title()

    while answer in 'Yes' and bottom_row < maximum_row:
        print(df.iloc[top_row:bottom_row, 1:8])
        top_row += 5
        bottom_row += 5
        answer = input('Would you like to see another 5 rows? Please enter "Yes" or "No"\n').title()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stat(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        redo = input('Would you like to restart the program? Enter "Yes" or "No"\n')
        if redo.title() != 'Yes':
            break


if __name__ == "__main__":
    main()
