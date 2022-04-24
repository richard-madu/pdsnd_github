import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',

'new york city': 'new_york_city.csv',

'washington': 'washington.csv' }

months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}

days = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}
def get_filters():
   
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in CITY_DATA:
        city = input("\nPlease enter the city name of your choice from either chicago, new york city or washington\n")
    if city.lower() in CITY_DATA:
        city_name = CITY_DATA[city.lower()]
        print ('You entered {} as your preffered city'.format(city))
    else:
        print("please enter a valid output\n")
    # get user input for month (all, january, february, ... , june)
    month = ''
    while month not in months.keys():
        month = input('\nWhich month do you want to analyze? January, February, March, April, May, or June?\nYou can also specify all if you want to analyse all the months\n').lower()
        if month not in months.keys():
            print('Sorry, I do not understand your input. Please type in a month between January and June\n')
        else:
            month_name = months[month]
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in days.keys():
        day = input('\nWhich day do you want to analyze? monday, tuesday, wednesday, friday, saturday, sunday?\nYou can also specify all if you want to analyse all the days of the week\n').lower()
        if day not in days.keys():
            print('please enter a valid weekday\n')
        else:
            day_name = days[day]
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'january':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'monday':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    if month != 'january':
        print('No mode available when month is specified.')
    else:
        df['Month'] = df['Start Time'].dt.month
        popular_month = df['Month'].mode()[0]
        print('Most common month (january = 1...): ', popular_month)
    # TO DO: display the most common day of week
    if day != 'monday':
        print('No mode available when day is specified.')
    else:
        df['Day'] = df['Start Time'].dt.weekday
        popular_day = df['Day'].mode()[0]
        print('Most common day (monday = 0, sunday = 6: ', popular_day)
    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Start Hour'].mode()[0]
    print('The Most common start hour: ', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most popular start station is: ', popular_start)
    
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most popular end station is: ', popular_end) 
    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End'] = df['Start Station'] + df['End Station']
    popular_combo = df['Start and End'].mode()[0]
    print('The most popular start and end station combination is: ', popular_combo)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time spent traveling is: ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time is: ', mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print('No gender information available')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        latest = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest birth year is: ', int(earliest))
        print('The latest birth year is: ', int(latest))
        print('The most common birth year is: ', int(most_common))
    else:
        print('No birth year information available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw(df):
    iloc_start = 0
    while True:
        raw_input = input('Do you want to see 5 lines of raw data? (y/n): ').lower()
        if raw_input != 'y':
            print('Alright!')
            break
        else:
            print(df.iloc[iloc_start:iloc_start+5])
            iloc_start += 5
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)
           
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
<<<<<<< HEAD
<<<<<<< HEAD
            print("Thank you for your time")
||||||| parent of 63a275f... Rephrase the last message
=======
||||||| parent of 431b22d... Added A Concluding Message
=======
            print("Thanks for your time")
>>>>>>> 431b22d... Added A Concluding Message

>>>>>>> 63a275f... Rephrase the last message
            break
if __name__ == "__main__":
	main()
