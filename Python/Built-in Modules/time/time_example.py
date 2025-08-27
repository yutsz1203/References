# Reference: https://www.youtube.com/watch?v=Qj3GlL5ckQA
import time

# convert a time expressed in seconds since epoch to a readable string
# epoch = when your computer thinks time begin (reference point)
print(time.ctime(0))

"""
time methods & functions
"""

"""
time obj format: time.struct_time(tm_year=2020, tm_mon=4, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=111, tm_isdst=-1)
"""
# Return current seconds since epoch
print(time.time())
print(time.ctime(time.time())) # current time

# time.strftime(format, timeObj): time object to string
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

utc_time_object = time.gmtime()
print(utc_time_object)
utc_time = time.strftime("%B %d %Y %H:%M:%S", utc_time_object)
print(utc_time)

# time.strptime(time_string, format): stirng to time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# time.sleep(sec)
i = 5
while i > 0: 
    time.sleep(1)
    print(i)
    i -= 1

# time.perf_counter(): measures elapsed time with high precision
def long_task():
    time.sleep(2)

start = time.perf_counter()
print(start)
long_task()
end = time.perf_counter()   
print(end)
elapsed_time = end - start

print(f"Elapsed time: {elapsed_time:.2f} seconds.")

# time.process_time(): CPU time, does not include sleep time
start = time.process_time()
result = 0
for i in range(1000000):
    result += i * i

end = time.process_time()
elapsed_time = end - start
print(f"CPU Time: {elapsed_time:.6f} seconds")

# time.asctime: convert a tuple or time obj to string; tuple format: (year, month, day, hours, minutes, secs, #day of the year, dst) 
print(time.asctime())

# time.mktime: get seconds from epoch of a time obj
print(time.mktime(time.localtime()))