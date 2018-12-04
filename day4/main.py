from datetime import datetime
import re
from pathlib import Path


class SleepPeriod:
    def __init__(self, start: datetime, end: datetime):
        self.start: datetime = start
        self.end: datetime = end

    def get_minutes_slept(self):
        return divmod((self.end - self.start).total_seconds(), 60)[0]


class Guard:
    def __init__(self, number: int):
        self.number = number
        self.sleep_periods = []

    def add_sleep(self, period: SleepPeriod):
        self.sleep_periods.append(period)

    def get_total_time_slept(self):
        return sum([sleep_period.get_minutes_slept() for sleep_period in self.sleep_periods])

    def compute_slept_minutes(self):
        minutes_slept = {}

        for sleep_period in self.sleep_periods:
            for minute in range(sleep_period.start.minute, sleep_period.end.minute):
                minutes_slept[minute] = minutes_slept.setdefault(minute, 0) + 1

        return minutes_slept

    def compute_most_slept_minute_with_value(self):
        minutes_slept = self.compute_slept_minutes()

        most_present_minute = max(minutes_slept.keys(), key=(lambda key: minutes_slept[key]))
        return most_present_minute, minutes_slept[most_present_minute]

    def compute_most_present_minute(self):
        minutes_slept = self.compute_slept_minutes()

        return max(minutes_slept.keys(), key=(lambda key: minutes_slept[key]))


pattern_begin_shift = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] Guard #(\d+) begins shift"
pattern_falls_asleep = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] falls asleep"
pattern_wakes_up = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] wakes up"
time_pattern = "%Y-%m-%d %H:%M"

if __name__ == '__main__':
    p = Path("input.txt")

    lines = p.read_text().splitlines()

    organized_logs = sorted(lines)
    guards = {}
    i = 0
    while i < len(organized_logs):
        begin_matcher = re.search(pattern_begin_shift, organized_logs[i])
        fall_asleep_matcher = re.search(pattern_falls_asleep, organized_logs[i])

        if begin_matcher:
            guard = Guard(int(begin_matcher.group(2)))
            i += 1
            while i < len(organized_logs):
                fall_asleep_matcher = re.search(pattern_falls_asleep, organized_logs[i])

                if fall_asleep_matcher:
                    wake_up_matcher = re.search(pattern_wakes_up, organized_logs[i+1])

                    asleep_time = datetime.strptime(fall_asleep_matcher.group(1), time_pattern)
                    wake_up_time = datetime.strptime(wake_up_matcher.group(1), time_pattern)

                    guards.setdefault(guard.number, guard).add_sleep(SleepPeriod(asleep_time, wake_up_time))

                    i += 2
                else:
                    break

    sorted_guards_by_laziness = sorted(guards.values(), key=Guard.get_total_time_slept, reverse=True)
    laziest_fuck: Guard = sorted_guards_by_laziness[0]

    biggest_time = -1
    selected_guard = None
    selected_minute = -1
    for guard in guards.values():
        biggest_minute, times = guard.compute_most_slept_minute_with_value()
        if times > biggest_time:
            biggest_time = times
            selected_guard = guard
            selected_minute = biggest_minute

    guard_id = selected_guard.number

    print("The laziest fuck is Guard number {} with {} minutes slept. \nThe minute he slept the most is {}\n"
          "The wanted number for strategy 2 is {} i'm tired please work"
          .format(laziest_fuck.number, laziest_fuck.get_total_time_slept(), laziest_fuck.compute_most_present_minute(),
                  guard_id * selected_minute))
