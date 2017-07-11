__author__ = 'nickyuan'
'''
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+
For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
'''

# Write your MySQL query statement below

#121ms
# select wt1.Id from Weather wt1, Weather wt2
# where wt1.Temperature > wt2.Temperature
# AND
# To_DAYS(wt1.DATE)-TO_DAYS(wt2.DATE)=1;

#90ms
# select wt1.Id from Weather wt1, Weather wt2
# where wt1.Temperature > wt2.Temperature
# AND
# wt1.DATE-wt2.DATE=1;