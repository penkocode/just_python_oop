# 2.Time

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.hours in range(0, 10) or self.minutes in range(0, 10) or self.seconds in range(0, 10):
            self.hours = f'{self.hours:02}'
            self.minutes = f'{self.minutes:02}'
            self.seconds = f'{self.seconds:02}'
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        if self.seconds == 60 or self.seconds == Time.max_seconds:
            self.seconds += 1
            self.minutes += 1
            self.seconds = 0

            if self.minutes == 60 or self.minutes == Time.max_minutes:
                self.hours += 1
                self.minutes = 0

            if self.hours == 24 or self.hours == Time.max_hours:
                self.hours = 0
        else:
            self.seconds += 1

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
time = Time(1, 20, 30)
print(time.next_second())
time = Time(0, 0, 0)
print(time.next_second())
t = Time(1, 2, 3)
t.set_time(9, 2, 1)
print(t.get_time())
