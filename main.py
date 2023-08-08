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
        for x in range(self.position):
            line3 = line3 + " "
        line3 = line3 + "O"
        print(line1)
        print(line2)
        print("")
        print(line3)


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


class Tests:

    def run_gauntlet(self):
        n = 0
        passed = True
        while hasattr(self, "test" + str(n)) and passed:
            try:
                passed = passed and getattr(self, "test" + str(n))()
                if not passed:
                    break
                n = n + 1
                print("Passed test " + str(n))
            except NotImplementedError:
                break

    def test0(self):
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

    def test1(self):
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

    def test2(self):
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

    def test3(self):
        obj = VariablesAndConditions()
        tests = [
            Test(obj.is_common_house_pet, ["Cat"], "Cat is a common house pet"),
            Test(obj.is_common_house_pet, ["Dog"], "Good boy"),
            Test(obj.is_common_house_pet, ["Elephant"], "Elephant is not a common house pet"),
            Test(obj.is_common_house_pet, ["Giraffe"], "Giraffe is not a common house pet")
        ]
        for test in tests:
            if not test.test():
                return False
        return True

    def test4(self):
        obj = Loops()
        last = None
        for x in range(100):
            test = Scenario1()
            obj.dodge_projectiles(test)
            if not test.is_safe(test.position):
                print("Test failed!")
                test.print()
                return False
            last = test
        print("Good job!")
        last.print()
        return True

    def test5(self):
        obj = Loops()
        last = None
        for x in range(1000):
            test = Scenario2()
            obj.dodge_projectiles_but_harder(test)
            if not test.is_safe(test.position):
                print("Test failed!")
                test.print()
                return False
            last = test
        print("Good job!")
        last.print()
        return True


if __name__ == '__main__':
    Tests().run_gauntlet()
