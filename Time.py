from datetime import datetime, timezone
print("Local Solar Time Calculator")
longitude = float(input("Enter the longitude (-180 to 180): "))
now_utc = datetime.now(timezone.utc)
utc_hour = now_utc.hour
utc_minute = now_utc.minute
utc_total_minutes = utc_hour * 60 + utc_minute
time_difference = longitude * 4
local_total_minutes = utc_total_minutes + time_difference
local_total_minutes = local_total_minutes % 1440
local_hour = int(local_total_minutes // 60)
local_minute = int(local_total_minutes % 60)
if longitude > 0:
    direction = "East of the Prime Meridian"
elif longitude < 0:
    direction = "West of the Prime Meridian"
else:
    direction = "On the Prime Meridian (0 degrees)"
print("UTC Time Now: " + str(utc_hour).zfill(2) + ":" + str(utc_minute).zfill(2))
print("Longitude:", longitude, "degrees (" + direction + ")")
print("Time Difference from UTC:", time_difference, "minutes")
print("Approximate Local Solar Time: " + str(local_hour).zfill(2) + ":" + str(local_minute).zfill(2))
