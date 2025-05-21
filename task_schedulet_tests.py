import unittest
from task_scheduler_5 import *

class TestTaskScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = PriorityQueue()
        self.scheduler.add_task("Task1", 1)
        self.scheduler.add_task("Task2", 3)
        self.scheduler.add_task("Task3", 2)

    def test_priority_order(self):
        task = self.scheduler.process_task()
        self.assertEqual(task.task_name, "Task2")
        task = self.scheduler.process_task()
        self.assertEqual(task.task_name, "Task3")
        task = self.scheduler.process_task()
        self.assertEqual(task.task_name, "Task1")

    def test_empty_queue(self):
        self.scheduler.process_task()
        self.scheduler.process_task()
        self.scheduler.process_task()
        self.assertTrue(self.scheduler.is_empty())
        self.assertIsNone(self.scheduler.process_task())

if __name__ == '__main__':
    unittest.main()
