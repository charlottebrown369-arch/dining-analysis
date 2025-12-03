"""
Charlotte Brown
CSE 160
This program analyzes a student's dining plan usage and reports whether the
student should spend more or less money, how much they should spend per day,
and whether they may need to change their dining plan level.
"""


class DiningAnalysis:

    def __init__(self, name, dining_plan_level, move_in_date, move_out_date, days_home_total):
        """
        Initializes a DiningAnalysis object for a student.

        Parameters:
        - name: str, student's name
        - dining_plan_level: int (1-indexed) representing the dining plan
        - move_in_date: tuple (month, day)
        - move_out_date: tuple (month, day)
        - days_home_total: int, number of days away from campus during quarter
        """
        self.name = name

        dining_levels = [1253, 1422, 1593, 1763, 2105, 2803]
        self.total_dining_dollars = dining_levels[dining_plan_level - 1]

        self.move_in_date = move_in_date
        self.total_quarter_days = self.calc_total_days(move_in_date, move_out_date, days_home_total)

    def calc_total_days(self, move_in_date, move_out_date, days_home_total):
        """
        Computes the total number of days the student spends on campus.

        Parameters:
        - move_in_date: (month, day)
        - move_out_date: (month, day)
        - days_home_total: int

        Returns:
        - int, total on-campus days for the quarter
        """
        month_length = [31, 28, 31, 30, 31, 30,
                        31, 31, 30, 31, 30, 31]

        move_in_month, move_in_day = move_in_date
        move_out_month, move_out_day = move_out_date

        # Days remaining in move-in month
        total_days = month_length[move_in_month - 1] - move_in_day + 1

        # Full months between move-in and move-out
        for m in range(move_in_month + 1, move_out_month):
            total_days += month_length[m - 1]

        # Days in move-out month
        total_days += move_out_day

        # Subtract days away from campus
        total_days -= days_home_total

        return total_days

    def calc_days_elapsed(self, current_date, days_home_current):
        """
        Computes the number of on-campus days elapsed so far.

        Parameters:
        - current_date: tuple (month, day)
        - days_home_current: int

        Returns:
        - int, on-campus days up to the current date
        """
        month_length = [31, 28, 31, 30, 31, 30,
                        31, 31, 30, 31, 30, 31]

        move_in_month, move_in_day = self.move_in_date
        current_month, current_day = current_date

        # Days remaining in move-in month
        days_elapsed = month_length[move_in_month - 1] - move_in_day

        # Full months between move-in month and current month
        for m in range(move_in_month + 1, current_month):
            days_elapsed += month_length[m - 1]

        # Days into the current month
        days_elapsed += current_day

        # Subtract days they went home
        days_elapsed -= days_home_current

        return days_elapsed

    def calc_fraction_left(self, current_date, days_home_current):
        """
        Returns the fraction of the quarter remaining.
        """
        days_elapsed = self.calc_days_elapsed(current_date, days_home_current)
        return 1 - (days_elapsed / self.total_quarter_days)

    def calc_expected_balance(self, current_date, days_home_current):
        """
        Expected balance if spending is on track.
        """
        fraction_left = self.calc_fraction_left(current_date, days_home_current)
        return fraction_left * self.total_dining_dollars

    def calc_excess(self, current_date, days_home_current, current_balance):
        """
        Returns how much above (positive) or below (negative)
        the student is compared to expected spending.
        """
        expected = self.calc_expected_balance(current_date, days_home_current)
        return current_balance - expected

    def projected_final_balance(self, current_date, days_home_current, current_balance):
        """
        Estimates final balance based on current spending rate.
        """
        days_elapsed = self.calc_days_elapsed(current_date, days_home_current)
        spending_rate = (self.total_dining_dollars - current_balance) / days_elapsed
        projected_spent_at_end = spending_rate * self.total_quarter_days
        return self.total_dining_dollars - projected_spent_at_end

    def print_analysis(self, current_date, days_home_current, current_balance):
        """
        Prints a summary of whether the student is overspending or underspending,
        how much they should spend per day, and whether they should consider
        changing dining plan levels.
        """
        excess = round(self.calc_excess(current_date, days_home_current, current_balance), 2)
        days_elapsed = self.calc_days_elapsed(current_date, days_home_current)
        days_remaining = self.total_quarter_days - days_elapsed

        recommended_daily_spending = round(current_balance / days_remaining, 2)

        print("Hello,", self.name)

        if excess > 15:
            print("You have", str(excess), "extra dollars, so spend more")
        elif excess < 0:
            print("You need to spend", str(-1 * excess), "dollars less")
        else:
            print("You're pretty close to on track with", str(excess), "extra dollars")

        print("You should aim to spend", recommended_daily_spending,
              "dollars per day for the rest of the quarter")

        final_projection = self.projected_final_balance(
            current_date, days_home_current, current_balance
        )

        if final_projection > 200:
            print("You may want to decrease your dining level next quarter")
        elif final_projection < -200:
            print("You may want to increase your dining level next quarter")
