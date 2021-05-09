import pandas as pd
import time

def print_p(statement):
    print(statement)
    time.sleep(.100)

# Some lambda helper functions
get_value = lambda x,y,n :x.groupby([y])[y].count().sort_values(ascending=False).head(n).values
get_index = lambda x,y,n :x.groupby([y])[y].count().sort_values(ascending=False).head(n).index
str_cleaner = lambda x : x[8:x.find("']")]
fnum = lambda num : format(num, ",")

# Combine index = pandas.series.index and value = numpy.ndarray then print in user-friendly way
def iterate_idx_val(x,y,n, message):
    idx = get_index(x,y,n)
    val = get_value(x,y,n)
    val = map(fnum,val)
    idx_val = zip(idx, val)
    for data in idx_val:
       print_p(message.format(*data))

# Input validation functions
def y_or_n(query):
    while True:
        answer = str(input(query +'  '+'y or n ?  ')).lower()
        if answer not in('y','n'):
            print('Enter valid response: y or n')
        else:
            break
    return answer

def mon_checker(query):
    months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun']
    while True:
        mon = input(query).title()[0:3]
        if mon not in months:
            print('Enter months from Jan to Jun')
        else:
            break
    return mon

def day_checker(query):
    days = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    while True:
        day = input(query + ' ').title()[0:3]
        if day not in days:
            print('Enter a valid day')
        else:
            break
    return day

def city_checker(query):
    while True:
        city_data = { 'chicago': 'chicago.csv',
                      'new york': 'new_york_city.csv',
                      'washington': 'washington.csv' }
        city = input(query).lower()
        if city not in city_data:
            print('Invalid input: Select from: --> Chicago, New York or Washington ')
            continue
        elif city in city_data:
            city = city_data[city]
            break
    return city

def num_checker():
    while True:
        try:
            n = int(float(input('\nEnter an integer from 1 to 5\n')))
            if n > 5:
                print('Limit is 5')
                continue
            elif n < 1:
                print('1 is the minimum')
                continue
            else:
                break
        except ValueError:
                print('Please type a number')
    return n

def restart_program(query):
    restart = y_or_n(query)
    if restart == 'y':
        project()
    else:
        print("Good-Bye!")

def restart_view_data(query,df):
    restart_view_data = y_or_n(query)
    if restart_view_data == 'y':
        view_data_question(df)
    else:
        print("Proceeding to end the program")

# Filter and load DataFrame
def filter_data():
    try:
        city = city_checker('\n\nSelect a city : Chicago, New York, Washington  ')
        df = pd.read_csv(city)

        # Convert Start, End Time col. to datetime and Trip Duration to mins
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['Hour'] = df['Start Time'].dt.hour
        df['Start and End'] = df['Start Station'] + ' to ' + df['End Station']
        df['Trip Duration'] = df['Trip Duration'] // 60

        # Extract month and day of week from Start Time to create new columns
        df['Month'] = df['Start Time'].dt.strftime('%b')
        df['DOW'] = df['Start Time'].dt.strftime('%a')
        df['Hour'] = df['Start Time'].dt.strftime('%-I %p')

        # Filter by month if applicable
        mon_ans = y_or_n('Do you want to filter by month -->')
        if mon_ans == 'y':
            mon = mon_checker('What month do you want to filter? \nEnter name of month -->')
            df = df[df['Month'] == mon]
        elif mon_ans == 'n':
            mon = None
            df
        # Filter by day of week if applicable
        day_ans = y_or_n('Do you want to filter by day -->')
        if day_ans == 'y':
            day = day_checker('What day you want to filter? \nEnter name of day -->')
            df = df[df['DOW'] == day]
        elif day_ans == 'n':
            day = None
            df
    except Exception as e:
        print(e)
    df = df.copy(deep=True)
    # Returns the filtered/un-filtered DataFrame and user's inputs as tuples
    return df, mon_ans, mon, day_ans, day, city

def time_filter(df,mon_ans, mon, day_ans, day):
    """ Tailors w/c filters are applied based on
        selected filters from filter_data() function """

    mt_msg = 'Common month is '
    hr_msg = 'Common hour is '
    dow_msg ='Common day is '
    ct_msg = ' with a count of '

    month = str_cleaner(str(mt_msg + get_index(df,'Month',1) + ct_msg + fnum(int(get_value(df,'Month',1)[0]))))
    day = str_cleaner(str(dow_msg + get_index(df,'DOW',1) + ct_msg + fnum(int(get_value(df,'DOW',1)[0]))))
    hr = str_cleaner(str(hr_msg + get_index(df,'Hour',1) + ct_msg + fnum(int(get_value(df,'Hour',1)[0]))))

    print_p('\n\n***TIME Statistics***\n\n')

    # if no month and day selected print all stats
    if (mon_ans == 'n') and (day_ans == 'n'):
        print_p(month +'\n'+ day +'\n'+ hr)
    # if month is selected only print day and hour stats
    elif (mon_ans == 'y') and (day_ans == 'n'):
        print_p(day +'\n' + hr)
    # if no month is selected and day is selected only print mon and hour stats
    elif (mon_ans == 'n') and (day_ans == 'y'):
        print_p('\n' + month +'\n' + hr)
    # if both month and day is selected only print most common hour
    elif (mon_ans == 'y') and (day_ans == 'y'):
        print_p(hr)

    print_p('\n\n***End of TIME Statistics***\n\n')

def station_stats(df):
    """ `n` returns up to top5 results uses above lambda
        and iterate_idx_val functions """

    n = num_checker()
    print_p('\n\n***STATION Statistics***\n\n')

    print_p('The most common start station\n')
    iterate_idx_val(df,'Start Station',n,'{} has a count of {}')

    print_p('\n\nThe most common end station\n')
    iterate_idx_val(df,'End Station',n,'{} has a count of {}')

    print_p('\n\nThe most common start and end station\n')
    iterate_idx_val(df,'Start and End',n,'{} has a count of {}')

    print_p('\n\n***End of STATION Statistics***\n\n')

def trip_duration_stats(df):
    """ `n` returns up to top5 results uses above lambda and
        iterate_idx_val functions"""

    n = num_checker()
    print_p('\n\n***TRIP DURATION Statistics***\n\n')

    print_p('\nThe most common TRIP DURATION\n')
    iterate_idx_val(df,'Trip Duration',n,'{} mins of travel duration has a count of {}')

    print_p('\n\nThe MEAN, MODE, MIN and MAX TRAVEL TIME based on your filter(s)\n')

    print_p('Mean travel time: ' + str(round(df['Trip Duration'].mean(),2)) + ' mins')
    print_p('Most common travel time: ' + str(round(df['Trip Duration'].mode(),2)[0]) + ' mins')
    print_p('Min travel time: ' + str(round(df['Trip Duration'].min(),2)) + ' mins')
    print_p('Max travel time: ' + str(round(df['Trip Duration'].max(),2)) + ' mins')

    print_p('\n\n***End of TRIP DURATION STATION Statistics***\n\n')

def user_stats(df):
    print_p('\n\n***USER Statistics***\n\n')
    gender_ct = 2
    user_type_ct = 2

    print_p('\nThe USER TYPE COUNT\n')
    iterate_idx_val(df,'User Type',user_type_ct, '{}s have a total count of {} ')

    print_p('\nThe COUNT of RENTAL based on GENDER\n')
    iterate_idx_val(df,'Gender',gender_ct,'{}s have a total rental count of {} ')

    print_p('\nBIRTH YEAR Statistics\n')

    print_p('Most recent birth year is ' + str(int(df['Birth Year'].max())))
    print_p('Most common birth year is ' + str(int(df['Birth Year'].mode()[0])))
    print_p('Most earliest birth year is ' + str(int(df['Birth Year'].min())))

    print_p('\n\n***End of USER Statistics***\n\n')

def view_data_question(df):
    """ Offers an option in how to view the data"""
    while True:
        try:
            answer = int(float(input('\n\n***Select OPTIONS to VIEW or SKIP VIEW DATA*** '
            '\n\n1 --> to view every five rows \n \n2 --> to specify the amount'
            ' of rows to return  \n \n3 --> to skip view data   ')))
            if answer not in [1, 2, 3]:
                print('\nValid options are : 1, 2, and 3')
                continue
            elif answer == 1:
                prompt_user_for_data(df)
                break
            elif answer == 2:
                view_specified_rows(df)
                break
            elif answer == 3:
                print('Skipping view options')
                break
        except ValueError:
            print('\nInvalid input. Enter only 1, 2 or 3')

def prompt_user_for_data(df):
    """ View data option 1 ---> every 5 rows? """
    print_p('\n\n***Printing FIVE ROWS consecutively***\n\n')
    print_p("I have " + str(fnum(len(df))) + " total rows available to view. ")
    start = 0
    fiverr = 5
    while fiverr < len(df)+10:
        answer = y_or_n('\n\nView every 5 rows of --> ')
        if answer == 'y':
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 800)
            pd.set_option('display.max_colwidth', None)
            print()
            print_p(df[start:fiverr])
            fiverr = fiverr + 5
            start = fiverr - 5
        elif answer == 'n':
            break

def view_specified_rows(df):
    """ View data option 2 ---> specific rows """
    while True:
        print_p('\n\n***VIEW DATA***\n\n')
        print_p("I have " + str(fnum(len(df))) + " total rows available to view. ")
        try:
            num = int(float((input("Enter from 1 up to " + str(fnum(len(df))) + " no commas ! --> "))))
            if num < 1 or num > len(df):
                print_p("\nEnter only 1 up to " + str(fnum(len(df))) + "--> ")
            else:
                print_p("\n\n***VIEWING " + str(num) + " ROWS***\n\n" )
                pd.set_option('display.max_rows', None)
                pd.set_option('display.max_columns', None)
                pd.set_option('display.width', 800)
                pd.set_option('display.max_colwidth', None)
                print_p(df.head(num))
                break
        except ValueError:
                print_p("\nInvalid. Enter only integers with *no commas* from 1 up to " + str(fnum(len(df))))
                continue

def project():
    """The driver function. Uses the returned data from the filter_data()
        and informs which filters are selected. Skips Gender stats if not available."""
    try:
        df, mon_ans, mon, day_ans, day, city = filter_data()
        row_data_message = '\n\nAggregating ' + str(fnum(len(df))) + ' rows of data'

        print_p('\n\nYou are viewing data for --> ' + city[:-4].upper() + '\n\n')

        # Statements informing user which filters are selected
        if (mon_ans == 'n') and (day_ans == 'n'):
            print_p('You selected *NO* time filters')
            print_p(row_data_message)
        elif (mon_ans == 'y') and (day_ans == 'n'):
            print_p('Your selected time filter is month --> '+ mon.upper())
            print_p(row_data_message)
        elif (mon_ans == 'n') and (day_ans == 'y'):
            print_p('Your selected time filter is day --> ' + day.upper())
            print_p(row_data_message)
        elif (mon_ans == 'y') and (day_ans == 'y'):
            print_p('Your selected time filter is month --> ' + mon.upper() +
                    ' and day --> '+ day.upper())
            print_p(row_data_message)

        # Start function calls
        time_filter(df,mon_ans, mon, day_ans, day)
        print_p('I can show you *up to Top 5* results for *some* of the next '
            'following statistics\n\n')
        station_stats(df)
        trip_duration_stats(df)
        if'Gender' not in df.columns:
            view_data_question(df)
            restart_view_data('\n\nConfirm to view data again? -->',df)
            restart_program('\n\nWould you like to RE-start this program? -->')
        else:
            user_stats(df)
            view_data_question(df)
            restart_view_data('\n\nConfirm to view data again? -->',df)
            restart_program('\n\nWould you like to RE-start this program? -->')
    except Exception as e:
            print_p(e)
project()         
