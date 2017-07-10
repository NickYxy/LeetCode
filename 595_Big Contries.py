__author__ = 'nickyuan'
'''
There is a table World

+-----------------+------------+------------+--------------+---------------+
| name            | continent  | area       | population   | gdp           |
+-----------------+------------+------------+--------------+---------------+
| Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
| Albania         | Europe     | 28748      | 2831741      | 12960000      |
| Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
| Andorra         | Europe     | 468        | 78115        | 3712000       |
| Angola          | Africa     | 1246700    | 20609294     | 100990000     |
+-----------------+------------+------------+--------------+---------------+
A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.

Write a SQL solution to output big countries' name, population and area.

For example, according to the above table, we should output:

+--------------+-------------+--------------+
| name         | population  | area         |
+--------------+-------------+--------------+
| Afghanistan  | 25500100    | 652230       |
| Algeria      | 37100000    | 2381741      |
+--------------+-------------+--------------+
'''

# Write your MySQL query statement below

#1、这应该是最糟糕的写法 392ms
#select name,population,area from World where population >= 25000000 or area >= 3000000

#2、想一想哪里可以优化
#如果把等号去掉，134ms

#3再想想哪里可以优化 118ms 用union
#select name, population, area
# from World
# where area > 3000000
# Union distinct
# select name, population, area
# from World
# where population > 25000000;

'''
1 union简介
    UNION属于集合运算符（set operator）允许我们把多个表表达式组合到一个复合表表达式中，
    它把一个表表达式的结果放在另一个表表达式的下面,在mysql数据库中提供了UNION和UNION ALL关键字,
    列于每个SELECT语句的对应位置的被选择的列应具有相同的类型。在第一个SELECT语句中被使用的列名称也被用于结果的列名称。
    从效率上说，UNION ALL 要比UNION快很多。
    DISTINCT关键词是一个自选词，不起任何作用，但是根据SQL标准的要求，在语法中允许采用。
    UNION ALL只是简单的将两个结果合并后就返回。
    这样，如果返回的两个结果集中有重复的数据，那么返回的结果集就会包含重复的数据了。
    UNION在进行表链接后会筛选掉重复的记录，所以在表链接后会对所产生的结果集进行排序运算，删除重复的记录再返回结果。
    如果可以确认合并的两个结果集中不包含重复的数据的话，那么就使用UNION ALL。
'''