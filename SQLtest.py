import sqlite3
from datetime import datetime
import random
import time
import Logger

max_num = 0
time_CTU = 0
num_of_rows = 0
parcel_long = 0
parcel_wide = 0
parcel_tall = 0
lowg_write_exeption = 0
time_now = datetime.now()
parcel_1_x = random.randrange (10,1300)
parcel_1_y = random.randrange (10,700)
parcel_1_z = random.randrange (10,700)


# Custom adapter for datetime
def adapt_datetime (dt):
    return dt.isoformat() # Convert datetime to ISO format string

# Register the adapter
sqlite3.register_adapter(datetime, adapt_datetime)

# connect to DB
conn = sqlite3.connect("PTU_test_db_now_parcels.db")
cursor = conn.cursor()

# create DB and keys
cursor.execute("""
    CREATE TABLE IF NOT EXISTS parcel_data (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    dimensions_x INTEGER,
    dimensions_y INTEGER,
    dimensions_z INTEGER         
    )
""")

# write data to DB
#cursor.execute("INSERT INTO parcel_data (timestamp,dimensions_x,dimensions_y,dimensions_z) VALUES (?,?,?,?)",(time_now,parcel_1_x,parcel_1_y,parcel_1_z))
# commit write
#conn.commit()

time_start = time.time()
time_end = time_start + (24 * 60 * 60)
real_time_end = datetime.fromtimestamp(time_end)
print(f"expected end time {real_time_end}")

start_time = time.perf_counter()

while time.time() < time_end:
    time_CTU += 1
    max_num += 1
    time_sleep = random.randrange(1,2)
    time_now = datetime.now()
    parcel_x = random.randrange (50,1300)
    parcel_y = random.randrange (50,650)
    parcel_z = random.randrange (50,650)

    cursor.execute("INSERT INTO parcel_data (timestamp,dimensions_x,dimensions_y,dimensions_z) VALUES (?,?,?,?)",(time_now,parcel_x,parcel_y,parcel_z))
    conn.commit()

    if parcel_x > 1200:
        parcel_long +=1
        try:
            Logger.logger(f"parcel to long, time:{time_now} length:{parcel_x}")
        except Exception as err:
            lowg_write_exeption +=1
            print (err)
    
    if parcel_y > 600:
        parcel_wide +=1
        try:
            Logger.logger(f"parcel to wide, time:{time_now} width:{parcel_y}")
        except Exception as err:
            lowg_write_exeption +=1
            print (err)

    if parcel_z > 600:
        parcel_tall +=1
        try:
            Logger.logger(f"parcel to high, time:{time_now} heigth:{parcel_z}")
        except Exception as err:
            lowg_write_exeption +=1
            print (err)

    print (f"Entrys in DB: {max_num}")
    if time_CTU >= 20:
        time_CTU = 0
        print(f"expected end time {real_time_end}")
    time.sleep(time_sleep)

end_time = time.perf_counter()


#get data from DB 

# select dataset 
cursor.execute("SELECT * FROM parcel_data")

fetchall_time_start = time.perf_counter() 

for row in cursor.fetchall():
    num_of_rows +=1
    print (row)

fetchall_time_end = time.perf_counter()



elepst_time = end_time - start_time
print("\n\n------------------------Test Time ------------------------\n")
print(f"num on entrys in to db {max_num}")
print(f"start time {start_time} end time {end_time} total time passed: {elepst_time}")

print("\n\n------------------------'Events'------------------------\n")
print(f"number of parcels to long {parcel_long}")
print(f"number of parcels to wide {parcel_wide}")
print(f"number of parcels to tall {parcel_tall}")
print(f"number of log write exeptions {lowg_write_exeption}")

fetchall_elepst_time = fetchall_time_end - fetchall_time_start
print("\n\n------------------------Fetchall Time------------------------\n")
print(f"number of rows {num_of_rows}")
print(f"fetchall start time {fetchall_time_start}")
print(f"fetchall end time {fetchall_time_end}")
print(f"elepst time {fetchall_elepst_time}")

# close DB
conn.close()