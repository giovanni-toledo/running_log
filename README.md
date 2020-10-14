# Running Log
Script I wrote to keep track of how many miles I've run this year.
Edit main.py to use.
dependencies: _**matplotlib**_

## USAGE EXAMPLE: 

Create a Month object for july which has 31 days 
```python
jul = Month("JULY", 31)
```
Call *Month.add_multiple_miles(self, chunk)* which parses through a multiline string in format:
 ```
 """
 {day}, {miles}
 {day}, {miles} 
 ... 
 """
 ```
and adds the value of *miles* to the corresponding *Day* object stored in *Month.days*
```python
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
```
individual days can also be logged as:
```python
jul.add_miles(30, 2)
```
adding miles to a day by either function more than once **adds to the previous value**. 

create plot object
Plot class takes a Month or list of Month objects as argument and plots their data 
```python
plot = Plot([jul, aug, sep])
```
to display the plot:
```python
plot.display()
```
