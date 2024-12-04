class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    
    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
    
    def test_str(self):
        runner = Runner("Usain Bolt")
        self.assertEqual(str(runner), "Usain Bolt")


unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))



