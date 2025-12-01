class dining_analysis:

    def __init__(self, name, dining_plan, move_in, move_out, total_days_home):
        self.name = name

        levels = [1253, 1422, 1593, 1763, 2105, 2803]
        self.level = levels[dining_plan - 1]

        self.move_in = move_in
        self.total_days = self.calc_total_days(move_in, move_out,
                                               total_days_home)

    def calc_total_days(self, move_in, move_out, total_days_home):
        month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        output = month_length[move_in[0] - 1]
        output += -move_in[1] + 1
        for month in range(move_in[0] + 1, move_out[0]):
            output += month_length[month - 1]
        output += move_out[1]
        output -= total_days_home

        return output

    def calc_current_days(self, current_date, current_days_home):
        month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        move_in = self.move_in
        output = month_length[move_in[0]] - move_in[1]
        for month in range(move_in[0] + 1, current_date[0]):
            output += month_length[month]
        output += current_date[1]
        output -= current_days_home

        return output

    def calc_q_left(self, current_date, current_days_home):
        current_days = self.calc_current_days(current_date, current_days_home)
        return 1 - (current_days / self.total_days)

    def calc_expected_balance(self, current_date, current_days_home):
        q_left = self.calc_q_left(current_date, current_days_home)
        return q_left * self.level

    def calc_excess(self, current_date, current_days_home, balance):
        expected = self.calc_expected_balance(current_date, current_days_home)
        return balance - expected

    def expected_final_amount(self, current_date, current_days_home, balance):
        current_days = self.calc_current_days(current_date, current_days_home)
        exp = (self.level - balance) / current_days * self.total_days
        return self.level - exp

    def print_analysis(self, current_date, current_days_home, balance):
        excess = self.calc_excess(current_date, current_days_home, balance)
        excess = round(excess, 2)
        current_days = self.calc_current_days(current_date, current_days_home)
        days_left = self.total_days - current_days
        advise = balance / days_left
        advise = str(round(advise, 2))
        print("Hello,", self.name)
        if excess > 15:
            print("You have", str(excess), "extra dollars, so spend more")
        elif excess < 0:
            print("You need to spend", str(-1 * excess), "dollars less")
        else:
            print("Keep it up, you have only", str(excess), "extra dollars")

        print("You should try to spend", advise,
              "dollars a day until the end of the quarter")

        final = self.expected_final_amount(current_date, current_days_home,
                                           balance)

        if final > 200:
            print("I also reccommed looking into decreasing your dining level")
        elif final < -200:
            print("I also reccommed looking into increasing your dining level")
