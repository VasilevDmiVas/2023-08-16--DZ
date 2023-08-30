# Первая задача
# someString = input('Введите слова через запятую:\n ')
# someString1 = someString.split(',')
# someString2 = []
# print(f'Из строки: {someString} - удалены повторяющиеся слова')
# for index in someString1:
#     if someString1.count(index) == 1:
#         someString2.append(index)
# print(f"Результат: {', '.join(someString2)}")
#---------------------------------------------------------------------------------------
# вторая задача
#
# import os
#
# somelists = []
#
# while True:
#     print('1 - Для записи в файл необходимо нажать единицу')
#     print('2 - Для чтения из файла необходимо нажать двойку')
#     print('3 - Для выхода из программы необходимо нажать три')
#
#     option = input('Выберите действие из списка: ')
#
#     if option == '1':
#         with open('text.txt', 'w', encoding='utf-8') as textFile:
#             newText = input('Введите текст для записи в файл: ')
#             somelists.append(newText)
#             textFile.writelines([i + '\n' for i in somelists])
#
#     elif option == '2':
#         with open('text.txt', 'r', encoding='utf-8') as textFile:
#             textRead = textFile.readlines()
#             somelists = [i.rstrip('\n') for i in textRead]
#             print(f'Содержимое файла - {somelists}')
#
#     elif option == '3':
#         break
#
# print('Вы вышли из программы \n До свидания')

# text = input('Введите предложение \n')
# index = 0
# count = 1
# text1 = len(text)
# for index in range(text1):
#     if text[index] == ' ':
#         count += 1
#     index += 1
# print(f'Количество слов в предложении = {count}')
# create database название;
# pip install mysql-connector-python
# import mysql.connector
# localhost
# user root
# password

import mysql.connector

mydb = mysql.connector.connect(
    host='MYSQL5049.site4now.net',
    user='a8ed4d_mydata',
    password='it12345678',
    database='db_a8ed4d_mydata'
)

curs = mydb.cursor()
# curs.execute('CREATE TABLE users15 (user_name varchar(25), user_age int, user_city varchar(30))')
# ---------------------------------------------------------------------------------------------------
# curs.execute('show tables')
# for x in curs:
#     print(x)
# ---------------------------------------------------------------------------------------------------
# curs.execute("insert into users15 (user_name, user_age, user_city) values ('Dmitriy', 25, 'Vitebsk')")
# mydb.commit()
# -----------------------------------------------------------------------------------------------------
# sqlQuery = "insert into users15 (user_name, user_age, user_city) values (%s, %s, %s)" --кол. столбцов в таблице %s. для создания множества строк
# sqlQuery = "insert into users15 (user_name, user_age, user_city) values (%s, %s, %s)"
# sqlValues = [
#     ('Vas', 25, 'Minsk'),
#     ('Dm', 40, 'Orsha')
# ]
# curs.executemany(sqlQuery, sqlValues)
# mydb.commit()
# -------------------------------------------------------------------------------------------------------
#
# curs.execute('select * from users15')
# # result = curs.fetchall() --или
# for i in curs:
#     print(i)
# ---------------------------------------------------------------------------------------------------------
# Workbench
# create database mydata
# create table Project (Name varchar(36), DateStart varchar(10), ManagerName varchar(30));
# create table Company (Name varchar(36), Age int, Email varchar(30))
# insert into Project (Name, DateStart, ManagerName) values ('Машины', '10.06.2023', 'Дмитрий');
# insert into Project (Name, DateStart, ManagerName) values ('Станки', '11.08.2023', 'Олег');
# insert into company (Name, Age, Email) values ('Audi', 63, 'qqqq@mail.ru');
# insert into company (Name, Age, Email) values ('Toyota', 42, 'lll@mail.ru');
# insert into company (Name, Age, Email) values ('Kia', 23, 'zzz@mail.ru');
# commit;
# select * from Project;
# select * from company;
# -----------------------------------------------------------------------------------------------------------