import time
import pandas as pd
import numpy as np
import calendar
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
    
    c = list(CITY_DATA.keys())
    m= [m for m in calendar.month_name if m != '']
    m.append('all') 
    d = [d for d in calendar.day_name ]
    d.append('all')
    
    
    while True:
        
        try: 
            city = input('There are only three avalible cities:\n   1. chicago \n    2. new york city \n    3. washington \n Please enter the city name as it is provided \n')
        except:
             print('your input not valid, please make sure to type the names of the citis in a correct way')
             continue
        if city not in c:
            print('your input not valid, please make sure to type the names of the citis in a correct way')
            continue
            # TO DO: get user input for month (all, january, february, ... , june)
        try:    
            month =input('At which month? \n (for all months just type "all" ) or type the month name \n 1. January \n 2. Fabruary \n 3. March \n 4. April \n 5. May \n or 6.June \n')
        except:
            print('your input not valid, please make sure to type the names as provided"')
            continue
        if month not in m:
            print('your input not valid, please make sure to type the names as provided!')
            continue
        try:    
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('And which day? again please type "all" if you don\'t want a specific day. else? please type the day you want as following:\n 1. Saturday \n 2. Sunday \n 3. Monday \n 4. Tuesday \n 5.Wednesday \n 5.Thrusday \n or 7.Friday \n')
        except:
            print('your input not valid, please make sure to type the word "all" or day\'s name as provided!')
            continue
        if day not in d:
            print('your input not valid, please make sure to type the word "all" or day\'s name as provided!')
            continue
        break
            
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
   
    df =pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        m = [m for m in calendar.month_name if m !='']
        month = m.index(month) +1 
        df['month']=df[df['month']==month]
    if day != 'all':
        df['day_of_week'] = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    result1 = print('{} is the most common month'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    result2 =print('{} is the most common day of week'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    hour = df['hour'] = df['Start Time'].dt.hour
    result3 =print('{} is the most common hour'.format(hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return result1,result2,result3

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_S= df['Start Station'].mode()[0]
    result1 =print('{} is the most commonly used start station'.format(start_S))

    # TO DO: display most commonly used end station
    end_S =df['End Station'].mode()[0]
    result2 =print('{} is the most commonly used end station'.format(end_S))
    
    # TO DO: display most frequent combination of start station and end station trip
    combination =  df['Start Station'] + 'as the start station and ' + df['End Station']+ ' is the end station'
    
    result3 = print('this is the  most frequent trip which combines  {}'.format(combination.mode()[0] ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return result1,result2,result3

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['sub'] = df['End Time'] - df['Start Time']     
    result1 =print('The total travel time is {}'.format( df['sub'].sum()))

    # TO DO: display mean travel time
    result2 =print('The mean travel time is {} '.format(df['sub'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return result1, result2

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types 
    
    result = print('{} are the counts of user types'.format( df['User Type'].value_counts()))
    if 'Gender' in list(df.columns):
        # TO DO: Display counts of gender
        print('{} are the counts of gender'.format(df['Gender'].value_counts()))
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in list(df.columns):
        
        df['Birth Year'] = df['Birth Year'].fillna(0).astype('int64')
        from statistics import mode
        birth_list =[i for i in df['Birth Year'] if i !=0]   
        birth_array =np.array(birth_list)         
        result2 = print('the earliest birth year is {} , the most recent one is {} and the common on is {}'.format(birth_array.min(),birth_array.max(),mode(birth_list)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return result


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
