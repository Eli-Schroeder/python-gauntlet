import math

from problems_difficulty_one import DifficultyOne
from problems_difficulty_three import DifficultyThree
from problems_difficulty_two import DifficultyTwo
from variables_and_conditions import VariablesAndConditions
from loops import Loops
from random import Random, random


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
                out = out[0:self.target] + "X" + out[self.target + 1:len(out)]
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
            if obj.dodge_projectiles(test) == "skip":
                print("Test 4 skipped")
                return True
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
            if obj.dodge_projectiles_but_harder(test) == "skip":
                print("Test 5 skipped")
                return True
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
            if obj.move_to(test, test.target) == "skip":
                print("Test 6 skipped")
                return True
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

    def test7(self):
        obj = DifficultyOne()
        self.clear_messages()
        print("Test 7")
        print("")
        for x in range(3, 100):
            is_actually_prime = True
            divisor = -1
            for n in range(2, int(math.ceil(x / 2)) + 1):
                if x % n == 0:
                    is_actually_prime = False
                    divisor = n
                    break
            is_prime = obj.check_if_prime(x)
            if is_prime == "skip":
                print("Test 7 skipped")
                return True
            if not is_actually_prime == is_prime:
                if is_prime:
                    print("Your function indicated that " + str(x) + " is prime, but it is not. It is divisible by " +
                          str(divisor))
                else:
                    print("Your function indicated that " + str(x) + " is not prime, but it is.")
                return False
        print("Good job!")
        return True

    def test8(self):
        obj = DifficultyOne()
        self.clear_messages()
        print("Test 8")
        print("")
        a = []
        b = []
        r = Random()
        for x in range(r.randint(0, 25)):
            a.append(r.randint(10, 50))
        for x in range(r.randint(0, 25)):
            b.append(r.randint(10, 50))
        expected = []
        for x in a:
            for y in b:
                if x == y:
                    expected.append(x)
        actual = obj.find_overlap(a, b)
        if actual == "skip":
            print("Test 8 skipped")
            return True
        for x in expected:
            if x not in actual:
                print(str(x) + " was in both lists, but not returned by your function.")
                print(a)
                print(b)
                return False
        for x in actual:
            if x not in expected:
                print(str(x) + " was returned by your function, but was not in both lists.")
                print(a)
                print(b)
                return False
        print("Good job!")
        return True

    def test9(self):
        obj = DifficultyOne()
        self.clear_messages()
        print("Test 9")
        print("")
        samples = [
            {
                "number": 3524,
                "cows": 2,
                "bulls": 0
            },
            {
                "number": 3127,
                "cows": 2,
                "bulls": 2
            },
            {
                "number": 9999,
                "cows": 0,
                "bulls": 0
            },
            {
                "number": 2211,
                "cows": 1,
                "bulls": 3
            }
        ]
        for sample in samples:
            cows_and_bulls = obj.cows_and_bulls(sample['number'])
            if cows_and_bulls == "skip":
                print("Test 9 skipped")
                return True
            if not cows_and_bulls[0] == sample['cows'] or not cows_and_bulls[1] == sample['bulls']:
                print(str(sample['number']))
                print("3721")
                print(f"Expected: {str(sample['cows'])} cows and {str(sample['bulls'])} bulls."
                      f" Indicated: {str(cows_and_bulls[0])} cows and {str(cows_and_bulls[1])} bulls")
                return False
        print("Good job!")
        return True

    def test10(self):
        obj = DifficultyTwo()
        self.clear_messages()
        print("Test 10")
        print("")
        lists = [
            ["abc", "def", "ghi"],
            ["cat", "dog"],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]
        for list in lists:
            last = obj.get_last_item(list)
            if last == "skip":
                print("Test 10 skipped")
                return True
            if not last == list[len(list) - 1]:
                print(str(list))
                print("Indicated last item: " + str(last))
                return False
        print("Good job!")
        return True

    def test11(self):
        obj = DifficultyTwo()
        self.clear_messages()
        print("Test 11")
        print("")
        lists = [
            ["abc", "def", "ghi", "jkl", "mno", "pqr"],
            ["cat", "dog", "mouse"],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ["a", "b"]
        ]
        r = Random()
        for list in lists:
            index = r.randint(0, len(list) - 2)
            next = obj.get_next_element(list, list[index])
            if next == "skip":
                print("Test 11 skipped")
                return True
            if not next == list[index + 1]:
                print(str(list))
                print("Element given: " + str(list[index]))
                print("Indicated next element: " + str(next))
                return False
        print("Good job!")
        return True

    def test12(self):
        obj = DifficultyTwo()
        self.clear_messages()
        print("Test 12")
        print("")
        sentences = [
            "Nice weather we're having today.",
            "The sky is blue.",
            "I like cats."
        ]
        reversed_sentences = [
            "today. having we're weather Nice",
            "blue. is sky The",
            "cats. like I"
        ]
        for i in range(len(sentences)):
            reversed = obj.reverse_word_order(sentences[i])
            if reversed == "skip":
                print("Test 12 skipped")
                return True
            if not reversed == reversed_sentences[i]:
                print("Sentence given: " + sentences[i])
                print("Indicated reversed: " + reversed)
                return False
        print("Good job!")
        return True

    def test13(self):
        obj = DifficultyThree()
        self.clear_messages()
        print("Test 13")
        print("")
        current_year = 2023
        r = Random()
        for x in range(10):
            rand = r.randint(18, 70)
            hundredth_life_anniversary = obj.get_year_when_person_will_be_one_hundred_years_old(current_year, rand)
            if hundredth_life_anniversary == "skip":
                print("Test 13 skipped")
                return True
            if not hundredth_life_anniversary == (current_year - rand) + 100:
                print("Your program indicated that a person who is " + str(rand) + " in " + str(current_year) +
                      " will be 100 years old in " + str(hundredth_life_anniversary) + ".")
                return False
        print("Good job!")
        return True

    def test14(self):
        obj = DifficultyThree()
        self.clear_messages()
        print("Test 13")
        print("")
        vowels = "aeiou"
        words = [
            "cat",
            "dog",
            "living",
            "programming",
            "block",
            "airplane"
        ]
        expected = [
            "living",
            "programming",
            "airplane"
        ]
        words_with_two_vowels = obj.get_words_with_two_or_more_vowels(words)
        if words_with_two_vowels == "skip":
            print("Test 14 skipped")
            return False
        for word in words_with_two_vowels:
            count = 0
            for x in range(len(word)):
                if word[x] in vowels:
                    count = count + 1
            if count < 2:
                print("Your function indicated that '" + word + "' has two or more vowels.")
                return False
        for word in expected:
            if word not in words_with_two_vowels:
                print("Your function did not indicate that '" + word + "' has two or more vowels.")
                return False
        print("Good job!")
        return True



if __name__ == '__main__':
    Tests().run_gauntlet()
