__author__ = 'nickyuan'
'''
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
'''

# Write your MySQL query statement below
#159ms
# select cus.name as Customers from Customers cus left join Orders ord on cus.Id = ord.CustomerId
# where ord.CustomerId is NULL;

#163ms
# SELECT A.Name from Customers A
# WHERE A.Id NOT IN (SELECT B.CustomerId from Orders B)