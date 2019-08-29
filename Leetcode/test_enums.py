from enum import Enum


class Frequency(Enum):
    Morning = 1
    Afternoon = 2
    Evening = 3
    Three_times = (Morning, Afternoon, Evening)


if __name__ == "__main__":
    print(Frequency.Three_times.value)
