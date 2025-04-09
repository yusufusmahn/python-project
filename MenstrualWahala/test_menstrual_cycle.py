import unittest
from datetime import datetime, timedelta
from menstrual_cycle_wahala import MenstrualCycleWahala

class TestMenstrualCycleWahala(unittest.TestCase):

    def test_get_next_period_start(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = last_period + timedelta(days=cycle_length)
        self.assertEqual(calculator.get_next_period_start(), expected)

    def test_get_next_period_end(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = calculator.get_next_period_start() + timedelta(days=period_length - 1)
        self.assertEqual(calculator.get_next_period_end(), expected)

    def test_get_ovulation_period(self):
        def test_get_ovulation_period(self):
            last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
            cycle_length = 28
            period_length = 5
            calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
            expected = calculator.get_next_period_end()  + timedelta(days= - 14)
            self.assertEqual(calculator.get_ovulation_period(), expected)

    def test_get_fertile_period_start(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = calculator.get_ovulation_period() - timedelta(days=5)
        self.assertEqual(calculator.get_fertile_period_start(), expected)

    def test_get_fertile_period_end(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = calculator.get_ovulation_period() + timedelta(days=1)
        self.assertEqual(calculator.get_fertile_period_end(), expected)

    def test_get_safe_period1_start(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = last_period
        self.assertEqual(calculator.get_safe_period1_start(), expected)

    def test_get_safe_period1_end(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = calculator.get_fertile_period_start() - timedelta(days=1)
        self.assertEqual(calculator.get_safe_period1_end(), expected)

    def test_get_safe_period2_start(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = calculator.get_fertile_period_end() + timedelta(days=1)
        self.assertEqual(calculator.get_safe_period2_start(), expected)

    def test_get_safe_period2_end(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 5
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected = calculator.get_next_period_start() - timedelta(days=1)
        self.assertEqual(calculator.get_safe_period2_end(), expected)

    def test_different_cycle_length(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()

        calculator = MenstrualCycleWahala(last_period, 30, 5)
        expected_start = last_period + timedelta(days=30)
        expected_end = expected_start + timedelta(days=4)
        self.assertEqual(calculator.get_next_period_start(), expected_start)
        self.assertEqual(calculator.get_next_period_end(), expected_end)

    def test_different_period_length(self):
        last_period = datetime.strptime("2025-03-01", "%Y-%m-%d").date()
        cycle_length = 28
        period_length = 7
        calculator = MenstrualCycleWahala(last_period, cycle_length, period_length)
        expected_end = calculator.get_next_period_start() + timedelta(days=period_length - 1)
        self.assertEqual(calculator.get_next_period_end(), expected_end)



if __name__ == "__main__":
    unittest.main()
