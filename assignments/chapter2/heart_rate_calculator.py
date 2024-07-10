users_age = int(input("Enter your age in years: "))
maximum_heartrate = 220 - users_age
min_users_target_heartrate = ( 50 /100 ) * maximum_heartrate
max_users_target_heartrate = (85 / 100 ) * maximum_heartrate
print('Your maximum heart rate is ', maximum_heartrate)
print('Your maximum target heart rate is ', max_users_target_heartrate)
print('Your minimum target heart rate is ', min_users_target_heartrate)
