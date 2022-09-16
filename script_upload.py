import mysql.connector as msql
from mysql.connector import Error
import pandas as pd



# #############################################################################################
#                                       TABLE CIRCUITS 
# #############################################################################################

empdata = pd.read_csv('./Datasets/circuits.csv', index_col=False, delimiter = ',')

try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')#give ur username, password

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        #
        cursor.execute('DROP TABLE IF EXISTS `circuits`;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `circuits` (
            `circuitId`		INTEGER NOT NULL,
            `circuitRef` 		VARCHAR(50),
            `name`			VARCHAR(50) COLLATE utf8mb4_spanish_ci NOT NULL,
            `location`		VARCHAR(50) COLLATE utf8mb4_spanish_ci NOT NULL,
            `country`			VARCHAR(50) COLLATE utf8mb4_spanish_ci NOT NULL,
            `lat`				VARCHAR(8) NOT NULL,
            `lng`				VARCHAR(9) NOT NULL,
            `alt`				VARCHAR(4) NOT NULL,
            `url`				VARCHAR(80),
            PRIMARY KEY (`circuitId`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO pidb.circuits VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)


# ######################################################################################
#                                       TABLE RACES
# ######################################################################################            

empdata = pd.read_csv('./Datasets/races.csv', index_col=False, delimiter = ',')
            
try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        # CREATING DATABASE
        cursor.execute('DROP TABLE IF EXISTS `races`;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS `races` (
            `raceId`		INT,
            `year` 			VARCHAR(4),
            `round`			VARCHAR(2),
            `circuitId`		INT,
            `name`			VARCHAR(50),
            `date`			DATE,
            `time`			VARCHAR(8),
            `url`			VARCHAR(70),
            PRIMARY KEY (`raceId`),
            FOREIGN KEY(`circuitId`) REFERENCES `circuits`(`circuitId`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO pidb.races VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)


######################################################################################
#                                    TABLE DRIVERS
######################################################################################

empdata = pd.read_json('./Datasets/drivers.json', lines=True)
empdata.to_csv('./Datasets/drivers.csv',index=False)
empdata = pd.read_csv('./Datasets/drivers.csv')

try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        # CREATING DATABASE
        cursor.execute('DROP TABLE IF EXISTS `drivers`;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `drivers` (
            `driverId`		INT,
            `driverRef`		VARCHAR(50),
            `number`		VARCHAR(10),
            `code`			VARCHAR(3),
            `name`			VARCHAR(100),
            `dob`			VARCHAR(10),
            `nationality`	VARCHAR(20),
            `url`			VARCHAR(100),
            PRIMARY KEY(`driverId`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO pidb.drivers VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)



# ######################################################################################
#                                     TABLE CONSTRUCTORS
# ######################################################################################

empdata = pd.read_json('./Datasets/constructors.json', lines=True)
empdata.to_csv('./Datasets/constructors.csv',index=False)
empdata = pd.read_csv('./Datasets/constructors.csv')

try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        # CREATING DATABASE
        cursor.execute('DROP TABLE IF EXISTS `constructors`;')
        print('Creating table....')
        # in the below line please pass the create table statement which you want #to create
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `constructors` (
            `constructorId`			INT,
            `constructorRef`		VARCHAR(100),
            `name`					VARCHAR(50),
            `nationality`			VARCHAR(20),
            `url`					VARCHAR(100),
            PRIMARY KEY (`constructorId`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO pidb.constructors VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL. Please check out :)", e)


# ######################################################################################
#                                     TABLE PIT_STOPS
# ######################################################################################


empdata = pd.read_json('./Datasets/pit_stops.json')
empdata.to_csv('./Datasets/pit_stops.csv',index=False)
empdata = pd.read_csv('./Datasets/pit_stops.csv')

try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        # CREATING DATABASE
        cursor.execute('DROP TABLE IF EXISTS `pit_stops`;')
        print('Creating table....')
        # in the below line please pass the create table statement which you want #to create
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `pit_stops` (
            `raceId`			INT,
            `driverId`			INT,
            `stop`				VARCHAR(1),
            `lap`				VARCHAR(2),
            `time`				VARCHAR(8),
            `duration`			VARCHAR(18),
            `milliseconds`		VARCHAR(7),
            FOREIGN KEY (`raceId`) REFERENCES races(`raceId`),
            FOREIGN KEY (`driverId`) REFERENCES drivers(`driverId`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO pidb.pit_stops VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted",i)
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL. Please check out :)", e)


# ######################################################################################
#                                     RESULTS
# ######################################################################################

empdata = pd.read_json('./Datasets/results.json', lines=True)
empdata.to_csv('./Datasets/results.csv',index=False)
empdata = pd.read_csv('./Datasets/results.csv')

try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        # CREATING DATABASE
        cursor.execute('DROP TABLE IF EXISTS `results`;')
        print('Creating table....')
        # in the below line please pass the create table statement which you want #to create
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `results` (
            `resultId`		INT,
            `raceId`		INT,
            `driverId`		INT,
            `constructorId`	INT,
            `number`		VARCHAR(3),
            `grid`			VARCHAR(2),
            `position`		VARCHAR(2),
            `positionText`	VARCHAR(2),
            `positionOrder`	VARCHAR(2),
            `points`		VARCHAR(4),
            `laps`			VARCHAR(3),
            `time`			VARCHAR(11),
            `milliseconds`	VARCHAR(8),
            `fastestLap`	VARCHAR(2),
            `rank`			VARCHAR(2),
            `fastestLapTime`VARCHAR(8),
            `fastestLapSpeed`VARCHAR(7),
            `statusId`		VARCHAR(3),
            PRIMARY KEY(`resultId`),
            FOREIGN KEY(`raceId`) REFERENCES races(`raceId`),
            FOREIGN KEY(`driverId`) REFERENCES drivers(`driverId`),
            FOREIGN KEY(`constructorId`) REFERENCES constructors(`constructorId`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO pidb.results VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted",i)
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL. Please check out :)", e)



# ######################################################################################
#                                     QUALIFY
# ######################################################################################

data1 = pd.read_json('./Datasets/Qualifying/qualifying_split_1.json')
data2 = pd.read_json('./Datasets/Qualifying/qualifying_split_2.json')
empdata = pd.concat([data1,data2], ignore_index=True)
# DATA CLEANING FILL NULL VALUES WITH NAN
for i in empdata.columns[6:]:
    empdata[i].replace("",'0', inplace = True)
    empdata[i].replace(r"NAN",'0', inplace = True)
    empdata[i].replace(r'\NAN','0', inplace = True)
    empdata[i].replace(r'\N','0', inplace = True)
    empdata[i].replace(r'\\N','0', inplace = True)
    empdata[i].replace(r'\\NAN','0', inplace = True)

empdata.to_csv('./Datasets/Qualifying/qualify.csv',index=False)
empdata = pd.read_csv('./Datasets/Qualifying/qualify.csv')

try:
    conn = msql.connect(
        host='localhost',
        user='root', 
        password='73538862')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pidb;")
        cursor.execute("USE pidb;")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS `qualify`;')
        print('Creating table....')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `qualify` (
            `qualifyId`			INT,
            `raceId`			INT,
            `driverId`			INT,
            `constructorId`		INT,
            `number`			VARCHAR(2),
            `position`			VARCHAR(2),
            `q1`				VARCHAR(9),
            `q2`				VARCHAR(9),
            `q3`				VARCHAR(9),
            PRIMARY KEY (`qualifyId`),
            FOREIGN KEY (`raceId`) REFERENCES races(`raceId`),
            FOREIGN KEY (`driverId`) REFERENCES drivers(`driverId`),
            FOREIGN KEY (`constructorId`) REFERENCES constructors(`constructorId`)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
        """)
        print(f"Table is created....")
        for i,row in empdata.iterrows():
            sql = ("INSERT INTO pidb.qualify VALUES (%s,%s,%s,%s,%s,%s,%s, %s,%s)")
            cursor.execute(sql, tuple(row))
            print("Record inserted", i)
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL. Please check out :( ", e)



################################################################################
# FUNCIONES QUE SE HAN USADO EN LA INGESTA DE DATOS PARA UNA EXPLORACION PREVIA
################################################################################

# import pandas as pd
# import numpy as np
# def max_vars(df):
#     listaColumnas = list(data.columns)
#     lista = []
#     for x in listaColumnas:
#         maximo = np.max(np.array([len(str(i)) for i in df.loc[:][x].values if i != ' ']))
#         lista.append({x:maximo})
#     return lista
# max_vars(data)