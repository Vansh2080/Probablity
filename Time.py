# Local Solar Time Calculator
# ----------------------------
# This program calculates the approximate local solar time of a place
# using its longitude and the current UTC time.
#
# How it works:
# The Earth spins 360 degrees in 24 hours.
# So 1 degree of longitude = 4 minutes of time.
#
# Formula:
# time difference (minutes) = longitude * 4
# local solar time = UTC time + time difference
#
# East longitude = positive number
# West longitude = negative number

from datetime import datetime, timezone

print("=== Local Solar Time Calculator ===")
print("")

# get the longitude from the user
longitude = float(input("Enter the longitude (-180 to 180): "))

# get the current UTC time instead of asking the user for it
now_utc = datetime.now(timezone.utc)
utc_hour = now_utc.hour
utc_minute = now_utc.minute

# step 1: turn the UTC time into total minutes
utc_total_minutes = utc_hour * 60 + utc_minute

# step 2: work out the time difference from the longitude
# every degree = 4 minutes
time_difference = longitude * 4

# step 3: add the difference to the UTC minutes
local_total_minutes = utc_total_minutes + time_difference

# step 4: keep it inside a 24 hour range (1440 minutes in a day)
# this handles going past midnight or before midnight
local_total_minutes = local_total_minutes % 1440

# step 5: turn the total minutes back into hours and minutes
local_hour = int(local_total_minutes // 60)
local_minute = int(local_total_minutes % 60)

# check if the place is east or west of the prime meridian
if longitude > 0:
    direction = "East of the Prime Meridian"
elif longitude < 0:
    direction = "West of the Prime Meridian"
else:
    direction = "On the Prime Meridian (0 degrees)"

# print everything nicely, using zfill so single digits get a leading zero
print("")
print("--- Results ---")
print("UTC Time Now: " + str(utc_hour).zfill(2) + ":" + str(utc_minute).zfill(2))
print("Longitude:", longitude, "degrees (" + direction + ")")
print("Time Difference from UTC:", time_difference, "minutes")
print("Approximate Local Solar Time: " + str(local_hour).zfill(2) + ":" + str(local_minute).zfill(2))
