import unittest
from detection.detection import RgbPoint
from detection.detection import LineSection
from detection.detection import LineAnalyzing
from detection.detection import Point
from detection.detection import SectionCalculator


class SectionCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.sectionCalculator = SectionCalculator()
        self.sectionCalculator.addSection(LineSection(50, 10, 20))
        self.sectionCalculator.addSection(LineSection(50, 15, 21))
        self.sectionCalculator.addSection(LineSection(50, 5, 25))

    def test_addSection(self):
        self.assertEqual(3, len(self.sectionCalculator.sections))

    def test_addSectionException(self):
        try:
            self.sectionCalculator.addSection(LineSection(50, 10, 20))
            self.fail("Es muesste hier eine Exception geworfen werden.")
        except Exception as e:
            a = 0

    def test_getAverageX(self):
        self.assertEqual(16, self.sectionCalculator.getAverageX())

    def test_getAverageXNotDecimal(self):
        self.assertEqual(16, self.sectionCalculator.getAverageX())


class LineAnalyzingTest(unittest.TestCase):
    def setUp(self):
        self.analyze = LineAnalyzing(5, 50)

    def test_addPointException(self):
        try:
            self.analyze.addPoint(0)
            self.fail("Es muesste hier eine Exception geworfen werden.")
        except Exception as e:
            a = 0

    def test_createSections(self):
        self.analyze.addPoint(RgbPoint(0, 10, [200]))
        self.analyze.addPoint(RgbPoint(1, 10, [200]))
        self.analyze.addPoint(RgbPoint(2, 10, [200]))
        self.analyze.addPoint(RgbPoint(5, 10, [200]))
        self.analyze.addPoint(RgbPoint(6, 10, [200]))
        self.analyze.addPoint(RgbPoint(7, 10, [200]))
        self.analyze.addPoint(RgbPoint(8, 10, [200]))
        self.analyze.addPoint(RgbPoint(15, 10, [200]))
        self.analyze.addPoint(RgbPoint(16, 10, [200]))
        self.analyze.addPoint(RgbPoint(19, 10, [200]))
        self.analyze.addPoint(RgbPoint(20, 10, [200]))
        self.analyze.addPoint(RgbPoint(21, 10, [200]))

        self.analyze.createSections()

        self.assertEqual(4, len(self.analyze.sections))

        self.assertEqual(0, self.analyze.sections[0].xStart)
        self.assertEqual(2, self.analyze.sections[0].xEnd)

        self.assertEqual(5, self.analyze.sections[1].xStart)
        self.assertEqual(8, self.analyze.sections[1].xEnd)

        self.assertEqual(15, self.analyze.sections[2].xStart)
        self.assertEqual(16, self.analyze.sections[2].xEnd)

        self.assertEqual(19, self.analyze.sections[3].xStart)
        self.assertEqual(21, self.analyze.sections[3].xEnd)

    def test_eliminiatePointsOverThreshold(self):
        self.analyze.addPoint(RgbPoint(0, 1, [150]))
        self.analyze.addPoint(RgbPoint(0, 1, [60]))
        self.analyze.addPoint(RgbPoint(0, 1, [180]))
        self.analyze.addPoint(RgbPoint(0, 1, [255]))
        self.analyze.addPoint(RgbPoint(0, 1, [70]))
        self.analyze.addPoint(RgbPoint(0, 1, [200]))
        self.analyze.addPoint(RgbPoint(0, 1, [5]))
        self.analyze.eliminiatePointsOverThreshold()
        self.assertEqual(1, len(self.analyze.line))

    def test_addPoint(self):
        p1 = RgbPoint(0, 1, [55])
        p2 = RgbPoint(0, 1, [55])
        p3 = RgbPoint(0, 1, [55])
        self.analyze.addPoint(p1)
        self.analyze.addPoint(p2)
        self.analyze.addPoint(p3)
        self.assertEqual(3, len(self.analyze.line))

    def test_getLongestSection(self):
        section1 = LineSection(59, 10, 50)
        section2 = LineSection(54, 51, 150)
        section3 = LineSection(58, 500, 521)
        self.analyze.sections.append(section1)
        self.analyze.sections.append(section2)
        self.analyze.sections.append(section3)
        longestSection = self.analyze.getLongestSection()
        self.assertEqual(54, longestSection.y)
        self.assertEqual(51, longestSection.xStart)
        self.assertEqual(150, longestSection.xEnd)

    def test_getFirstPoint(self):
        section1 = LineSection(59, 10, 50)
        section2 = LineSection(54, 51, 150)
        section3 = LineSection(58, 500, 521)
        self.analyze.sections.append(section1)
        self.analyze.sections.append(section2)
        self.analyze.sections.append(section3)
        point = self.analyze.getFirstPoint()
        self.assertEqual(5, point.y)
        self.assertEqual(51, point.x)

    def test_getLastPoint(self):
        section1 = LineSection(59, 10, 50)
        section2 = LineSection(54, 51, 150)
        section3 = LineSection(58, 500, 521)
        self.analyze.sections.append(section1)
        self.analyze.sections.append(section2)
        self.analyze.sections.append(section3)
        point = self.analyze.getLastPoint()
        self.assertEqual(5, point.y)
        self.assertEqual(150, point.x)


class LineSectionTest(unittest.TestCase):
    def setUp(self):
        self.rgbpoint = LineSection(5, 10, 15)

    def test_getWidth(self):
        self.assertEqual(15 - 10, self.rgbpoint.getWidth())

    def test_setAndGetXStart(self):
        value = 4
        self.rgbpoint.xStart = value
        self.assertEqual(value, self.rgbpoint.xStart)

    def test_setAndGetXStartToLow(self):
        value = -9
        self.rgbpoint.xStart = value
        self.assertEqual(0, self.rgbpoint.xStart)

    def test_setAndGetXEnd(self):
        value = 4
        self.rgbpoint.xEnd = value
        self.assertEqual(value, self.rgbpoint.xEnd)

    def test_setAndGetXEndToLow(self):
        value = -9
        self.rgbpoint.xEnd = value
        self.assertEqual(0, self.rgbpoint.xEnd)

    def test_setAndGetY(self):
        value = 49
        self.rgbpoint.y = value
        self.assertEqual(value, self.rgbpoint.y)

    def test_setAndGetYToLow(self):
        value = -10
        self.rgbpoint.y = value
        self.assertEqual(0, self.rgbpoint.y)


class PointTest(unittest.TestCase):
    def setUp(self):
        self.point = Point(5, 7)

    def test_setAndGetX(self):
        value = 4
        self.point.x = value
        self.assertEqual(value, self.point.x)

    def test_setAndGetXToLow(self):
        value = -9
        self.point.x = value
        self.assertEqual(0, self.point.x)

    def test_setAndGetY(self):
        value = 49
        self.point.y = value
        self.assertEqual(value, self.point.y)

    def test_setAndGetYToLow(self):
        value = -10
        self.point.y = value
        self.assertEqual(0, self.point.y)


class RgbPointTest(unittest.TestCase):
    def setUp(self):
        self.rgbpoint = RgbPoint(5, 7, [5])

    def test_setAndGetRgb(self):
        value = [0, 45, 66]
        self.rgbpoint.rgb = value
        self.assertEqual(value, self.rgbpoint.rgb)


if __name__ == '__main__':
    unittest.main()