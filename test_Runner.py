from Runner import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = Runner("Billy")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        rurunnern = Runner("Bob")
        for i in range(10):
            rurunnern.run()
        self.assertEqual(rurunnern.distance, 100)

    def test_challenge(self):
        walker = Runner("Billy")
        runner = Runner("Bob")
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)