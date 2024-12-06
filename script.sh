# Program to print Good Morning, 
# Good Afternoon, Good Evening 
# and Good Night, according to
#  system time.


#!/bin/bash
hour=`date +%H`
if [ $hour -lt 12 ] # if hour is less than 12
then
echo "GOOD MORNING WORLD"
elif [ $hour -le 16 ] # if hour is less than equal to 16
then
echo "GOOD AFTERNOON WORLD"
elif [ $hour -le 19 ] # if hour is less than equal to 20
then
echo "GOOD EVENING WORLD"
else
echo "GOOD NIGHT WORLD"
fi