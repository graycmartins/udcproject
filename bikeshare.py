import time
import pandas as pd
import numpy as np
from datetime import datetime
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def select_city():
    """
    Asks user to specify a city

    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = [ 'chicago', 'new york city', 'washington' ]
    print( '\nSelect your city by typing one of the options:', valid_cities )
    city = str.lower( input() )
    while city not in valid_cities:
        print( 'Please type one of the cities below:', valid_cities )
        city = str.lower( input() )
    return city


def get_filters():
    """
    Asks user to specify a month and day to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june']
    print( '\nPlease, type a month from January to June' )
    month = str.lower( input() )
    while month not in valid_months:
        print( 'Please type one of the months below:', valid_months )
        month = str.lower( input() )

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print( '\nPlease, type a week day' )
    day = str.lower( input() )
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in week_days:
        print( 'Please type one valid week day:' )
        day = str.lower( input() )
           
    print('\n\n -- Your options were:', city, ' - ', month, ' - ', day )

    print('-'*40)
    return month, day


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
    df = pd.read_csv( CITY_DATA[city] )   
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] =  df['Start Time'].apply( lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ) )

    # TO DO: display the most common month
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['month'] = df['Start Time'].apply( lambda x: x.month )
    print('the most common month is:', calendar.month_name[df.month.mode()[0]])

    # TO DO: display the most common day of week
    df['day_of_week'] = df['day_of_week'] = df['Start Time'].apply( lambda x: x.weekday() )
    print('the most common day of week is:', calendar.day_name[df.day_of_week.mode()[0]] )
   
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].apply( lambda x: x.hour )
    print('the most common start hour:', df.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].mode()[0] )


    # TO DO: display most commonly used end station
    print('The most commonly used end station is:', df['End Station'].mode()[0] )


    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip:', df[['Start Station', 'End Station']].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time:', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('mean travel time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types', df['User Type'].value_counts())

    
    # TO DO: Display counts of gender
    # Check if dataset has Gender info
    if 'Gender' in df.columns:
        print('counts of gender', df['Gender'].value_counts())
    else:
        print('This data does not have gender info')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('earliest year of birth:', int(df['Birth Year'].min()) )
        print('most recent year of birth:',int(df['Birth Year'].max()) )
        print('most common year of birth:', int(df['Birth Year'].mode()[0]) )
    else:
        print('This data does not have birth year info')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
     """
        Display raw data to the user on request
     """
     print('Would you like to see five lines of data? Yes or No')
     show_data = str.lower( input() )
     line = 0
        
     # Check if user type a valid choice
     if show_data not in ['yes', 'no']:
         print('Invalid choice. Please, type Yes or No')
        
     while show_data == 'yes':
         if line <= df.shape[0]:
             print(df[line : line + 5])
             print('Would you like to see five more? Yes or No')
             show_data = str.lower( input() )
             line += 5
         else:
             print('No more data to see')      
             show_data = 'No'
    

def main():
    while True:
        city = select_city()
        month = 'all' 
        day = 'all'
        
        print('You can filter your data by month and week day. Would you like to apply filters? Yes or No')
        apply_filter = str.lower( input() )
        if apply_filter == 'yes':
            month, day = get_filters()
        
        print('Loading data accorting to defined options...\n')
        df = load_data(city, month, day)
        
        # Display data
        display_data(df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()