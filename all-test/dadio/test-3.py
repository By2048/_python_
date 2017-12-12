# 2099年我几岁了？
import unittest
import datetime

# http://www.dadio.xyz/content/xyz/train

import math
def calculate_age(year_of_birth, current_year):
    str_out=''
    if year_of_birth==current_year:
        str_out=("You were born this very year!")
    if year_of_birth>current_year:
        str_out =("You will be born in {0} years.".format(year_of_birth-current_year))
    if year_of_birth<current_year:
        str_out =("You are {0} years old.".format(current_year-year_of_birth))

    if abs(year_of_birth-current_year)==1:
        str_out=str_out.replace('years','year')
    return str_out


calculate_age(2012, 2016)
calculate_age(1989, 2016)#"You are 27 years old.")
calculate_age(2000, 2090)#"You are 90 years old.")
calculate_age(2000, 1990)#"You will be born in 10 years.")
calculate_age(2000, 2000)#"You were born this very year!")
calculate_age(900, 2900)#"You are 2000 years old.")
calculate_age(2010, 1990)#"You will be born in 20 years.")
calculate_age(2010, 1500)#"You will be born in 510 years.")
calculate_age(2011, 2012)#"You are 1 year old.")
calculate_age(2000, 1999)#"You will be born in 1 year.")

'You are 4 years old.'
'You are 4 years old.'