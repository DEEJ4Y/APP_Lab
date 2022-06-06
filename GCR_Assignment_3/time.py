class Time():
    hours = 0
    minutes = 0

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, time):
        totmins = (time.minutes + self.minutes) % 60
        extraHours = (time.minutes + self.minutes) / 60
        tothours = (time.hours + self.hours + extraHours) % 24

        print(f"{int(tothours)}h{totmins}m")


t1 = Time(12, 24)
t2 = Time(12, 44)
t1.addTime(t2)
