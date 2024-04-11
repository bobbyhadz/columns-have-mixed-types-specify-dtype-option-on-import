# Columns have mixed types. Specify dtype option on import

import pandas as pd

dtype = {
    'first_name': str,
    'last_name': str,
    'date': str,
    'salary': str
}

df = pd.read_csv(
    'employees.csv',
    sep=',',
    encoding='utf-8',
    dtype=dtype

)

#   first_name last_name        date salary
# 0      Alice     Smith  01/21/1995   1500
# 1      Bobby      Hadz  04/14/1998    abc
# 2       Carl     Lemon  06/11/1994   3000
# 3       Dean     Berry  06/11/1996    xyz
print(df)