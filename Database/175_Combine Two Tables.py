__author__ = 'nickyuan'
'''
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table, 
regardless if there is an address for each of those people:

FirstName, LastName, City, State
'''
#113ms
# SELECT Person.FirstName, Person.LastName, Address.City, Address.State
# from Person LEFT JOIN Address on Person.PersonId = Address.PersonId;

# SELECT FirstName, LastName, City, State
# FROM Person
# LEFT JOIN Address
# USING(PersonId);


# SELECT FirstName, LastName, City, State
# FROM Person
# NATURAL LEFT JOIN Address;

#105ms
# select p.FirstName, p.LastName, a.City, a. State
# from Person p, Address a
# where p.PersonId = a.PersonId;

#on中的条件关联，一表数据不满足条件时会显示空值。where则输出两表完全满足条件数据。
# 为什么会存在差异，这和on与where查询顺序有关。
# 我们知道标准查询关键字执行顺序为 from->where->group by->having->order by
# left join 是在from范围类所以 先on条件筛选表，然后两表再做left join。
# 而对于where来说在left join结果再次筛选。