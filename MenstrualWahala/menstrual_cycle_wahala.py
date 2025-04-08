from datetime import timedelta


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


