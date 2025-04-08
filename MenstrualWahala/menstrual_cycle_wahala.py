from datetime import timedelta, datetime


class MenstrualCycleWahala:
    def __init__(self, last_period_date, cycle_length, period_length):
        self.last_period_date = last_period_date
        self.cycle_length = cycle_length
        self.period_length = period_length

    def get_next_period_start(self):
        return self.last_period_date + timedelta(days=self.cycle_length)

    def get_next_period_end(self):
        return self.get_next_period_start() + timedelta(days=self.period_length - 1)


    def get_ovulation_period(self):
        return self.get_next_period_end() - timedelta(days=14)


    def get_fertile_period_start(self):
        return self.get_ovulation_period() - timedelta(days=5)


    def get_fertile_period_end(self):
        return self.get_ovulation_period() + timedelta(days=1)


    def get_safe_period1_start(self):
        return self.last_period_date


    def get_safe_period1_end(self):
        return self.get_fertile_period_start() - timedelta(days=1)


    def get_safe_period2_start(self):
        return self.get_fertile_period_end() + timedelta(days=1)


    def get_safe_period2_end(self):
        return self.get_next_period_start() - timedelta(days=1)



def main():
    today = datetime.now().date()

    while True:
        try:
            last_period_input = input("Enter first day of last period (YYYY-MM-DD): ")
            last_period = datetime.strptime(last_period_input, "%Y-%m-%d").date()
            if last_period > today:
                print("Menstrual cycle period cannot be after today's date")
                continue
            break
        except ValueError:
            print("Invalid date")


    while True:
        try:
            cycle_length = int(input("Enter menstrual cycle length (e.g., 28 days): "))
            if cycle_length <= 0:
                print("Menstrual cycle length must be a positive integer")
                continue
            break
        except ValueError:
            print("Invalid number. Please enter a valid integer")

    while True:
        try:
            period_length = int(input("Enter menstrual period length (e.g., 5 days): "))
            if period_length <= 0:
                print("Menstrual period length must be a positive integer")
                continue
            break
        except ValueError:
            print("Invalid number. Please enter a valid integer")

    calculate = MenstrualCycleWahala(last_period, cycle_length, period_length)
    date_format = "%Y-%m-%d"

    print("=========================================================================================")
    print("\nMENSTRUAL CYCLE APP Result")
    print("=========================================================================================")
    print(f"Next Period: {calculate.get_next_period_start().strftime(date_format)} to "f"{calculate.get_next_period_end().strftime(date_format)}")
    print(f"Ovulation Date: {calculate.get_ovulation_period().strftime(date_format)}")
    print(f"Fertile Range: {calculate.get_fertile_period_start().strftime(date_format)} to "
          f"{calculate.get_fertile_period_end().strftime(date_format)}")
    print(f"Safe Period 1: {calculate.get_safe_period1_start().strftime(date_format)} to "
          f"{calculate.get_safe_period1_end().strftime(date_format)}")
    print(f"Safe Period 2: {calculate.get_safe_period2_start().strftime(date_format)} to "
          f"{calculate.get_safe_period2_end().strftime(date_format)}")

if __name__ == "__main__":
    main()