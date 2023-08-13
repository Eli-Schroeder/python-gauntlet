from variables_and_conditions import VariablesAndConditions
from loops import Loops
from random import Random


class InfiniteLoopError(Exception):
    pass


class Test:

    def __init__(self, method, args, expected):
        self.method = method
        self.args = args
        self.expected = expected

    def test(self):
        out = self.method(*self.args)
        if out == self.expected:
            return True
        print("Test failed.")
        print("Input: ")
        print(self.args)
        print("Output:")
        print(out)
        print("Expected:")
        print(self.expected)
        return False


class ProjectilesScenario:

    def __init__(self):
        self.positions = []
        for x in range(Random().randrange(10, 30, 2)):
            self.positions.append(Random().randint(1, 2) == 1)
        self.position = int(len(self.positions) / 2)
        self.initial_position = self.position
        self.positions[self.position] = False
        at_least_one_safe = False
        for x in range(len(self.positions)):
            if self.positions[self.position]:
                at_least_one_safe = True
                break
        if not at_least_one_safe:
            self.positions[Random().randint(0, len(self.positions) - 1)] = True

    def spaces(self):
        return len(self.positions)

    def is_safe(self, position):
        return self.positions[position]

    def print(self):
        line1 = ""
        line2 = ""
        for status in self.positions:
            if status:
                line1 = line1 + " "
                line2 = line2 + " "
            else:
                line1 = line1 + "|"
                line2 = line2 + "v"
        line3 = ""
        middle = int((self.position + self.initial_position) / 2)
        for x in range(max(self.position, self.initial_position) + 1):
            if x == self.position:
                line3 = line3 + "O"
            elif x == self.initial_position:
                line3 = line3 + "o"
            elif self.position > x > self.initial_position and x - middle <= 1 and x >= middle:
                line3 = line3 + ">"
            elif self.position < x < self.initial_position and x - middle <= 1 and x >= middle:
                line3 = line3 + "<"
            else:
                line3 = line3 + " "
        line4 = ""
        for x in range(self.position):
            line4 = line4 + " "
        line4 = line4 + "^ final position"
        line5 = ""
        for x in range(min(10, len(self.positions))):
            line5 = line5 + str(x)
        print(line1)
        print(line2)
        print("")
        print(line3)
        print(line4)
        print("")
        print(line5)
        print("")


class Scenario1(ProjectilesScenario):

    def __init__(self):
        super().__init__()

    def move_to(self, position):
        self.position = position


class Scenario2(ProjectilesScenario):

    def __init__(self):
        super().__init__()
        self.moves = 0

    def move_left(self):
        self.moves = self.moves + 1
        if self.moves > 100:
            raise InfiniteLoopError()
        if self.position > 0:
            self.position = self.position - 1
            return True
        return False

    def move_right(self):
        self.moves = self.moves + 1
        if self.moves > 100:
            raise InfiniteLoopError()
        if self.position < self.spaces() - 1:
            self.position = self.position + 1
            return True
        return False


class Scenario3():

    def __init__(self):
        self.moves = []
        self.position = Random().randint(8, 12)
        self.initial_position = self.position
        self.target = Random().randint(0, 20)

    def move_left(self):
        if len(self.moves) > 100:
            raise InfiniteLoopError()
        if self.position > 0:
            self.position = self.position - 1
            self.moves.append("Left")
            return True
        self.moves.append("Blocked")
        return False

    def move_right(self):
        if len(self.moves) > 100:
            raise InfiniteLoopError()
        if self.position < 20:
            self.position = self.position + 1
            self.moves.append("Right")
            return True
        self.moves.append("Blocked")
        return False

    def print(self):
        position = self.initial_position
        for x in self.moves:
            out = ""
            if x == "Right":
                for n in range(position):
                    out = out + " "
                out = out + ">x"
                position = position + 1
            elif x == "Left":
                for n in range(position - 1):
                    out = out + " "
                out = out + "x<"
                position = position - 1
            elif x == "Blocked":
                for n in range(position - 1):
                    out = out + " "
                out = out + "x"
                print("Wall!")
            while len(out) < self.target + 1:
                out = out + " "
            if self.target == position:
                out = out[0:self.target] + "X" + out[self.target+1:len(out)]
            else:
                out = out[0:self.target] + "T" + out[self.target + 1:len(out)]
            print(out)


class Tests:
    display_scenarios = 10

    def run_gauntlet(self):
        n = 1
        passed = True
        while hasattr(self, "test" + str(n)) and passed:
            try:
                passed = passed and getattr(self, "test" + str(n))()
                if not passed:
                    break
                print("Passed test " + str(n))
                n = n + 1
            except NotImplementedError:
                break

    def clear_messages(self):
        for x in range(100):
            print("")

    def test1(self):
        obj = VariablesAndConditions()
        tests = [
            Test(obj.maximum_integer, [5, 3], 5),
            Test(obj.maximum_integer, [2, 11], 11),
            Test(obj.maximum_integer, [3, 3], 3),
            Test(obj.maximum_integer, [-14, 1], 1),
            Test(obj.maximum_integer, [-3, -2], -2)
        ]
        for test in tests:
            if not test.test():
                return False
        return True

    def test2(self):
        obj = VariablesAndConditions()
        tests = [
            Test(obj.divide_max_by_min, [10, 2], 5),
            Test(obj.divide_max_by_min, [3, 6], 2),
            Test(obj.divide_max_by_min, [1, 2], 2)
        ]
        for test in tests:
            if not test.test():
                return False
        return True

    def test3(self):
        obj = VariablesAndConditions()
        tests = [
            Test(obj.thing_in_ohio, ["Cats", "Lions"], "Lions in Ohio"),
            Test(obj.thing_in_ohio, ["Dogs", "Dogs"], "Dogs in Ohio"),
            Test(obj.thing_in_ohio, ["White collar workers", "Blue collar workers"], "White collar workers in Ohio"),
            Test(obj.thing_in_ohio, ["", ""], " in Ohio")
        ]
        for test in tests:
            if not test.test():
                return False
        return True

    def test4(self):
        obj = Loops()
        tests = []
        self.clear_messages()
        print("Test 4")
        print("")
        for x in range(100):
            test = Scenario1()
            obj.dodge_projectiles(test)
            if not test.is_safe(test.position):
                print("Test failed!")
                test.print()
                return False
            tests.append(test)
        print("Good job!")
        print("Scenarios 1-" + str(len(tests) - self.display_scenarios) + " ommitted for brevity..")
        for x in range(self.display_scenarios):
            print("")
            print("Scenario " + str(len(tests) - (self.display_scenarios - (x + 1))) + ":")
            tests[len(tests) - (self.display_scenarios + 1 - x)].print()
        return True

    def test5(self):
        obj = Loops()
        tests = []
        self.clear_messages()
        print("Test 5")
        print("")
        for x in range(1000):
            test = Scenario2()
            obj.dodge_projectiles_but_harder(test)
            if not test.is_safe(test.position):
                print("Test failed!")
                test.print()
                return False
            tests.append(test)
        print("Good job!")
        print("Scenarios 1-" + str(len(tests) - self.display_scenarios) + " ommitted for brevity..")
        for x in range(self.display_scenarios):
            print("")
            print("Scenario " + str(len(tests) - (self.display_scenarios - (x + 1))) + ":")
            tests[len(tests) - (self.display_scenarios + 1 - x)].print()
        return True

    def test6(self):
        obj = Loops()
        tests = []
        self.clear_messages()
        print("Test 6")
        print("")
        for x in range(1000):
            test = Scenario3()
            obj.move_to(test, test.target)
            if not test.position == test.target:
                print("Test failed!")
                test.print()
                return False
            tests.append(test)
        print("Good job!")
        print("Scenarios 1-" + str(len(tests) - self.display_scenarios) + " ommitted for brevity..")
        for x in range(self.display_scenarios):
            print("")
            print("Scenario " + str(len(tests) - (self.display_scenarios - (x + 1))) + ":")
            tests[len(tests) - (self.display_scenarios + 1 - x)].print()
        return True


if __name__ == '__main__':
    Tests().run_gauntlet()
