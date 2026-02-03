import time 
import sys
from datetime import datetime 


# can do time.sleep to have separation in the output
def recurs (x):
   """I set a counter to ensure there is no infinite loop. I made the cutoff to be 4.i also wanted to add the 
   current date and time to match the theme of the movie. """

   # learned about f strings in my LSE class - f strings let you call functions within a print line

   # datetime is the class, now() is the funtion within thta class that returns the local date and timestemp
   print(f"did you mean groundhog day? but it's {datetime.now()} ?")  

   time.sleep(1)
   #increasing counter
   x+=1

   if x<4 :
      return  recurs(x) # for context I have some cs experience so i am familiar with recursive functions 

recurs(0) # call itself, what makes it recursive

# array example 
def testArray():
    """this is an example function for using for loop to display contents of an array"""
    example = ['meep', 'mop', 'moop']

    for name in example:

        print(name)

