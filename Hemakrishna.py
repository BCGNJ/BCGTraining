import pandas as pd
import matplotlib.pyplot as mp

c_d, = pd.read_html("https://github.com/jennybc/gapminder/blob/master/data-raw/01_pop.tsv")


# to get  number of rows, columns
print(c_d.shape)

# to print top 100 rows, bottom 100 rows
print(c_d.head(100))
print(c_d.tail(100))



# saving to a file

c_d.to_csv("con_pop.csv", index=False)


# to read the file and take only required columns
c_p = pd.read_csv("con_pop.csv", usecols=['country', 'year', 'pop'])

# to get total population by year
p = c_p.groupby(by=['year'])['pop'].sum()
print(p)
# to plot the year and total population
mp.show(p.plot(x='Year', kind='bar'))


# p1 = c_p.groupby(by=['country'])['pop'].sum()
# print(p1)

# print(p)
# p1 = p.tolist()
# # print(p1)
# p2 = c_p.year.unique()
# # print(p2)
#
# p3 = [c_p.year.unique(), p.tolist()]
# # print(p3)
#
# p.to_csv("tot_pop.csv", index=False)
# c_p2 = pd.read_csv("tot_pop.csv")
# # print(c_p2)
# mp.plot(c_p.year.unique(), p.tolist())
# mp.axis([1950, 2018, 0, 100000])
# mp.show()
# # print(p[0], p[1])


# import csv
# import numpy as np
#
# a = open("D:\Today\work2.csv")
# read = csv.reader(a)
# for row in read:
#     b = row
#     print(b)
#
# c = np.array(b)
# print(c)

# cd = pd.read_html("https://github.com/jennybc/gapminder/blob/master/data-raw/01_pop.tsv")
# print(cd)



# print(c_d)
# calls_df.to_csv("calls.csv", index=False)
# c_d.columns = c_d.iloc[0]
# c_d = c_d.reindex(c_d.index.drop(1))

