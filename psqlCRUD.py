# Библиотека для работы со временем
from datetime import datetime
import time
# Библиотека для работы с Postgres
from psycopg2 import connect

# Подключение в БД
conn = connect(
    dbname="ExpStud",
    user="postgres",
    host="172.17.0.2",
    port="5432",
    password="qwerty12345"
)
print("good")
#conn = psycopg2.connect(dbname='postgres', user='postgres',
                        #password='qwerty', host='localhost')

cursor = conn.cursor()

def runC(version, count):
    # Происходит запись в БД count раз
    # вернет время выполнения скрипта
    start_time = datetime.now()
    for x in range(count):
        buf = "valueV" + str(version) + "_" + str(x)
        cursor.execute("INSERT INTO test (ID) VALUES (%s)", (str(buf), ))
    return datetime.now() - start_time

def runR(version, count):
    # Происходит запись в БД count раз
    # вернет время выполнения скрипта
    start_time = datetime.now()
    for x in range(count):
        buf = "valueV" + str(version) + "_" + str(x)
        cursor.execute("SELECT ID from test WHERE ID=(%s)", (str(buf), ))
    return datetime.now() - start_time

def runU(version, count):
    # Происходит изменение значений в БД, count записей
    # вернет время выполнения скрипта
    start_time = datetime.now()
    for x in range(count):
        buf = "valueV" + str(version) + "_" + str(x)
        buf1 = "valueV" + str(version) + "_" + str(count - x)
        cursor.execute("UPDATE test SET ID=(%s) where ID=(%s)", (str(buf1), str(buf)))
    return datetime.now() - start_time

def runD(version, count):
    # Происходит удаление count записей из БД
    # вернет время выполнения скрипта
    start_time = datetime.now()
    for x in range(count):
        buf1 = "valueV" + str(version) + "_" + str(count - x)
        cursor.execute("DELETE from test WHERE ID = (%s)", (str(buf1), ))
    return datetime.now() - start_time


cursor.execute("CREATE TABLE TEST(ID TEXT)")

# выполнение С блока
print('С блок')
print(runC(1, 1000).total_seconds())
print(runC(2, 1000).total_seconds())
print(runC(3, 1000).total_seconds())
print(runC(4, 1000).total_seconds())
print(runC(5, 1000).total_seconds())
print(runC(6, 1000).total_seconds())
print(runC(7, 1000).total_seconds())
print(runC(8, 1000).total_seconds())
print(runC(9, 1000).total_seconds())
print(runC(10, 1000).total_seconds())
print(runC(11, 1000).total_seconds())
print(runC(12, 1000).total_seconds())
print(runC(13, 1000).total_seconds())
print(runC(14, 1000).total_seconds())
print(runC(15, 1000).total_seconds())
print(runC(16, 1000).total_seconds())
print(runC(17, 1000).total_seconds())
print(runC(18, 1000).total_seconds())
print(runC(19, 1000).total_seconds())
print(runC(20, 1000).total_seconds())
# Выполнение R блока
print('R блок')
print(runR(1, 1000).total_seconds())
print(runR(2, 1000).total_seconds())
print(runR(3, 1000).total_seconds())
print(runR(4, 1000).total_seconds())
print(runR(5, 1000).total_seconds())
print(runR(6, 1000).total_seconds())
print(runR(7, 1000).total_seconds())
print(runR(8, 1000).total_seconds())
print(runR(9, 1000).total_seconds())
print(runR(10, 1000).total_seconds())
print(runR(11, 1000).total_seconds())
print(runR(12, 1000).total_seconds())
print(runR(13, 1000).total_seconds())
print(runR(14, 1000).total_seconds())
print(runR(15, 1000).total_seconds())
print(runR(16, 1000).total_seconds())
print(runR(17, 1000).total_seconds())
print(runR(18, 1000).total_seconds())
print(runR(19, 1000).total_seconds())
print(runR(20, 1000).total_seconds())

# Выполнение U блока
print('U блок')
print(runU(1, 1000).total_seconds())
print(runU(2, 1000).total_seconds())
print(runU(3, 1000).total_seconds())
print(runU(4, 1000).total_seconds())
print(runU(5, 1000).total_seconds())
print(runU(6, 1000).total_seconds())
print(runU(7, 1000).total_seconds())
print(runU(8, 1000).total_seconds())
print(runU(9, 1000).total_seconds())
print(runU(10, 1000).total_seconds())
print(runU(11, 1000).total_seconds())
print(runU(12, 1000).total_seconds())
print(runU(13, 1000).total_seconds())
print(runU(14, 1000).total_seconds())
print(runU(15, 1000).total_seconds())
print(runU(16, 1000).total_seconds())
print(runU(17, 1000).total_seconds())
print(runU(18, 1000).total_seconds())
print(runU(19, 1000).total_seconds())
print(runU(20, 1000).total_seconds())

#
# # Выполнение D блока
print('D блок')
print(runD(1, 1000).total_seconds())
print(runD(2, 1000).total_seconds())
print(runD(3, 1000).total_seconds())
print(runD(4, 1000).total_seconds())
print(runD(5, 1000).total_seconds())
print(runD(6, 1000).total_seconds())
print(runD(7, 1000).total_seconds())
print(runD(8, 1000).total_seconds())
print(runD(9, 1000).total_seconds())
print(runD(10, 1000).total_seconds())
print(runD(11, 1000).total_seconds())
print(runD(12, 1000).total_seconds())
print(runD(13, 1000).total_seconds())
print(runD(14, 1000).total_seconds())
print(runD(15, 1000).total_seconds())
print(runD(16, 1000).total_seconds())
print(runD(17, 1000).total_seconds())
print(runD(18, 1000).total_seconds())
print(runD(19, 1000).total_seconds())
print(runD(20, 1000).total_seconds())

# удаление ДБ
cursor.execute("DROP TABLE test");