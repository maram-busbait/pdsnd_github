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
    while True:
           try:
            city = input("Enter the city you are interested in to analyze chicago, new york or washington:").lower()
            if city in CITY_DATA:
             break   
           except:
             print("not except")
        
           print("try again")
    # TO DO: get user input for month (all, january, february, ... , june) 
    while True:
           months=['january', 'february', 'march', 'april', 'may', 'june']
           try:
              month = input("Enter the month you are interested in month january, february, march, april, may, june:").lower()
              if month in months:
               break
           except:
             print("not except")

           print("try again")
    # TO DO: get user input for day 
    while True:
           daies= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
           try:
              day = input("enter day sunday, monday, tuesday, wednesday, thursday, friday, saturday:").lower()
              if day in daies:
                break
           except:
             print("not except")

           print("try again")
        
          
               
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
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
  
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('most common month:',popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('most common day of week:',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("the most commonly used start station:",popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("the most commonly used end station:",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start and end station : {}"\
            .format(popular_start_end_station[0] ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

              
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n",user_counts)

    # TO DO: Display counts of gender
    if "Gender" in df:
      gender_counts = df['Gender'].value_counts()
      print("Counts of user types:\n",gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:

     birth_year = df['Birth Year']
     earliest_year = birth_year.min()
     print("The most earliest year of birth:", earliest_year)
    
     most_recent = birth_year.max()
     print("The most recent year of birth:", most_recent)

     popular_year = birth_year.value_counts().idxmax()
     print("The most common year of birth:", popular_year)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
