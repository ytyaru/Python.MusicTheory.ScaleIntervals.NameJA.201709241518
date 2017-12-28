#!python3.6
import unittest
import math
from MusicTheory.scale.ScaleIntervals import ScaleIntervals
"""
ScaleIntervalsのテスト。というよりenumの試用テスト。
"""
class TestScaleIntervals(unittest.TestCase):
    def test_reference(self):
        print(ScaleIntervals)
        print(dir(ScaleIntervals))
        print(ScaleIntervals.Major)
        print(ScaleIntervals == ScaleIntervals.Major)
#        print(ScaleIntervals in ScaleIntervals.Major)
        for a in ScaleIntervals: print(a)
        print(ScaleIntervals.Major in ScaleIntervals)
    def test_set(self):
        with self.assertRaises(AttributeError) as ex:
            ScaleIntervals.Major = (0,)
        self.assertIn('Cannot reassign members.', str(ex.exception))
        self.assertEqual((2,2,1,2,2,2), ScaleIntervals.Major.value)
        self.assertEqual('Major', ScaleIntervals.Major.name)
    def test_GetName(self):
        self.assertEqual('長音階', ScaleIntervals.GetName(ScaleIntervals.Major))
        self.assertEqual('短音階', ScaleIntervals.GetName(ScaleIntervals.Minor))
        self.assertEqual('和声的短音階', ScaleIntervals.GetName(ScaleIntervals.HarmonicMinor))
        self.assertEqual('旋律的短音階', ScaleIntervals.GetName(ScaleIntervals.MelodicMinor))
        with self.assertRaises(ValueError) as ex:
            ScaleIntervals.GetName('abc')
        self.assertIn("引数targetは存在しません。ScaleIntervalsにある属性のいずれかにしてください。", str(ex.exception))


if __name__ == '__main__':
    unittest.main()

