class Day:
    """Object to keep track of miles run on a given day"""
    def __init__(self, day_num, miles= 0):
        self.day_num = day_num
        self.miles = miles

    def __str__(self):
        #format and return string  
        s = f"{self.day_num} - {self.miles}\n"
        return s 

class Month:
    """Object to represent a month, store a number of Day objects"""
    def __init__(self, month_name, length):
        """Example usage: Month("JANUARY", 31)"""
        self.month_name = month_name
        self.length = length
        self.days = []
        self.populate()
    
    def get_mileage(self):
        """get total sum of miles"""
        m = 0
        for day in self.days:
            m += day.miles
        return round(m, 2)


    def populate(self):
        """This function is called on creation and recursively populates Month.days list with Day objects."""
        #for every day in the month
        for day in range(1, self.length+1):
            #create a Day object with sequential Day.day_num and default 0 Day.miles
            self.days.append(Day(day))
    
    def add_miles(self, day, miles_run):
        """log miles on a given day""" 
        #offset for 0 index
        #adds the value of miles_run to Day.miles which by default is 0
        self.days[day-1].miles += miles_run
    
    def add_multiple_miles(self, chunk):
        """parse a multiline string in format "{day}, {miles}" separated by a new line"""
        #iter through each line in chunk
        for line in chunk.splitlines():
            #confirm line length and comma separated format
            if len(line) > 2 and "," in line:
                #separate day, miles_run values
                l = line.split(",")
                day = int(l[0])
                miles_run = float(l[1])
                #offset for 0 index 
                #adds miles_run value to Day.miles current value which by default is 0
                self.days[day-1].miles += miles_run

    def to_string(self, show_skipped_days=False):
        #month name as header 
        s = f"\n{self.month_name.upper()} - {self.get_mileage()} miles\n\n"
        #iter through Day objects
        for day in self.days:
            #if show_skipped_days is set to False and Day.miles is also 0
            if show_skipped_days == day.miles and day.miles < 1:
                #hide that day
                pass
            else:
                s += str(day)
        s += "\n"
        return s


# USAGE EXAMPLE: 

# Create a Month object for july which has 31 days 
jul = Month("JULY", 31)
# Call Month.add_multiple_miles(self, chunk) which parses through a multiline string in format:
# 
# {day}, {miles} \n
# {day}, {miles} \n
# ... 
# 
# and adds the value of miles to the corresponding Day object stored in Month.days  
jul.add_multiple_miles("""
3, 6.04
5, 7.04
7, 6.62
13, 7.0
17, 6.55
19, 7.08
21, 7.14
24, 8.0
26, 8.0
30, 4.25
""")
# individual days can also be logged as:
jul.add_miles(30, 2)
# adding miles to a day by either function more than once adds to the previous value 

# print the name of the month, the total miles run in that month and days and miles logged
# days with no activity are skipped by default 
# to show them set the show_skipped_days argument to True
print(jul.to_string())
