class VariablesAndConditions:

    def maximum_integer(self, integer_1, integer_2):
        return max(integer_1, integer_2)

    def divide_max_by_min(self, integer_1, integer_2):
        return self.maximum_integer(integer_1, integer_2) / min(integer_1, integer_2)

    def thing_in_ohio(self, string_1, string_2):
        return (string_1 if len(string_1) > len(string_2) else string_2) + " in Ohio"
