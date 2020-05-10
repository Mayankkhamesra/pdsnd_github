import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please input city name: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "City name is invalid or there is no data for this city! Please enter either Chicago, New york City or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please input month name(January, February, March, April, May, June or All): ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please input day of week(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All): ").lower()
    
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
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    # Cleansing and expanding date and time data within the DataFrame
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    
    # Processing DataFrame for the selected month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]

    # Processing DataFrame for selected day
    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: {}".format(
        str(df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("Most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0].title()))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("Most common starting hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common starting station: {} ".format(
        df['Start Station'].mode().values[0])
    )

    # TO DO: display most commonly used end station
    print("Most common ending station: {}".format(
        df['End Station'].mode().values[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+ "   To   " + df['End Station']
    print("Most frequent route taken: {}".format(
        df['route'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: {}".format(
        str(df['Trip Duration'].sum()))
    )

    # TO DO: display mean travel time
    print("Average travel time: {}".format(
        str(df['Trip Duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types Counts: ")
    print(df['User Type'].value_counts())

    if city != 'washington':
        # TO DO: Display counts of gender
        print("\nGender Counts:")
        print(df['Gender'].value_counts())


        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nEarliest birth year: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("Latest birth year: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("Most common birth year: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        # Displaying raw data
        start_loc = 0
        end_loc = 5

        display_active = input("Would you like to see 5 rows of raw data?(Yes/No): ").lower()
    
        if display_active == 'yes':
            while end_loc <= df.shape[0] - 1:
                print(df[start_loc:end_loc])
                start_loc += 5
                end_loc += 5
                end_display = input("Would you like to see 5 more rows of raw data?(Yes/No): ").lower()
                if end_display == 'no':
                    break

        
        restart = input('\nDo you want to run the program again?(Yes/No): ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
