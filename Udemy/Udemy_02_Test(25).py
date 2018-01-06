#Creating a function
def  minutes_to_hours(minutes):
    hours = minutes/60
    return hours

def seconds_to_hours(seconds):
    hours = seconds/3600
    return hours

print(minutes_to_hours(310)) # 5.167
print(seconds_to_hours(3212)) # 0.89

def time_to_hours(minutes, seconds=0):
    hours = minutes/60 + seconds/3600
    return hours

print(time_to_hours(150, 7000))
print(time_to_hours(120)) # ponieważ default = 0, to pozwoli odpalic, bo zdefiniowalismy default (0) w funkcji

