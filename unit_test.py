import math
import unittest
import pathing


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)


    def setUp(self):
        self.test_graph = [
            # Node, adjacent_nodes
            [(0, 0), [1, 2]],       # Node 0 (Start)
            [(10, 0), [0, 3]],      # Node 1
            [(0, 10), [0, 3]],      # Node 2
            [(10, 10), [1, 2, 4]],  # Node 3
            [(20, 10), [3, 5]],     # Node 4 (Target)
            [(30, 10), [4]],        # Node 5 (Goal)
        ]


    def test_dfs_segment_path(self):
        # Get path from get_segment_path_dfs
        path = pathing.get_segment_path_dfs(self.test_graph, start = 0, goal = 4)

        # Verify path starts at node 0 and ends at node 4 (target) since multiple possible paths
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 4)

        # Verify consecutive nodes are connected by an edge
        for i in range(len(path) - 1):
            self.assertIn(path[i + 1], self.test_graph[path[i]][1]) 


    def test_bfs_segment_path(self):
        # Get path from get_segment_path_bfs
        path = pathing.get_segment_path_bfs(self.test_graph, start = 0, goal = 4)
        
        # 0, 1, 3, 4 = expected path
        expected_path = [0, 1, 3, 4]

        # Check if expected_path and actual path are equal
        self.assertEqual(path, expected_path)
        

    def test_dfs_and_bfs_full_multi_phase_path(self):
        start = 0
        target = 4
        goal = 5

        dfs_segment_1 = pathing.get_segment_path_dfs(self.test_graph, start, target)
        dfs_segment_2 = pathing.get_segment_path_dfs(self.test_graph, target, goal)
        dfs_path_full = dfs_segment_1 + dfs_segment_2[1:]

        bfs_seg1 = pathing.get_segment_path_bfs(self.test_graph, start, target)
        bfs_seg2 = pathing.get_segment_path_bfs(self.test_graph, target, goal)
        bfs_path_full = bfs_seg1 + bfs_seg2[1:]

        for path in [dfs_path_full, bfs_path_full]:
            self.assertIn(target, path)
            self.assertEqual(path[-1], goal)
            self.assertEqual(path[0], start)


if __name__ == '__main__':
    unittest.main()
