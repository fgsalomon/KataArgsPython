import unittest
import ArgsParser


class ArgsParserTest(unittest.TestCase):

    def testCompleteAndCorrectArgs(self):
        parser = ArgsParser.ArgsParser(schema={'-l': True, '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', 'False', '-p', '8081', '-d', '/var/logs'])
        self.assertEqual(True, parser.parse())
        self.assertEqual(False, parser.get('-l'))
        self.assertEqual(8081, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))

    def testMissingArgValue(self):
        parser = ArgsParser.ArgsParser(schema={'-l': True, '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', '-p', '8081', '-d', '/var/logs'])
        self.assertEqual(True, parser.parse())
        self.assertEqual(True, parser.get('-l'))
        self.assertEqual(8081, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))

    def testMissingArg(self):
        parser = ArgsParser.ArgsParser(schema={'-l': True, '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', 'False', '-p', '8081'])
        self.assertEqual(False, parser.parse())
        self.assertEqual(False, parser.get('-l'))
        self.assertEqual(8081, parser.get('-p'))
        self.assertEqual('/usr/logs', parser.get('-d'))

    def testUnorderedArgs(self):
        parser = ArgsParser.ArgsParser(schema={'-l': True, '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', '-d', '/var/logs', '-p', '8081'])
        self.assertEqual(True, parser.parse())
        self.assertEqual(True, parser.get('-l'))
        self.assertEqual(8081, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))

    def testNegativeArgValue(self):
        parser = ArgsParser.ArgsParser(schema={'-l': True, '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', '-d', '/var/logs', '-p', '-8081'])
        self.assertEqual(True, parser.parse())
        self.assertEqual(True, parser.get('-l'))
        self.assertEqual(-8081, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))

    def testArgList(self):
        parser = ArgsParser.ArgsParser(schema={'-l': ['this', 'is', 'a', 'list'], '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', 'list,a,is,this', '-p', '8081', '-d', '/var/logs'])
        self.assertEqual(True, parser.parse())
        self.assertEqual(['list', 'a', 'is', 'this'], parser.get('-l'))
        self.assertEqual(8081, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))

    def testDefaultArgList(self):
        parser = ArgsParser.ArgsParser(schema={'-l': ['this', 'is', 'a', 'list'], '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', '-p', '8081', '-d', '/var/logs'])
        self.assertEqual(True, parser.parse())
        self.assertEqual(['this', 'is', 'a', 'list'], parser.get('-l'))
        self.assertEqual(8081, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))

    def testIncorrectArgIntegerType(self):
        parser = ArgsParser.ArgsParser(schema={'-l': True, '-p': 8080, '-d': '/usr/logs'},
                                       args=['-l', '-d', '/var/logs', '-p', 'verbose'])
        self.assertEqual(False, parser.parse())
        self.assertEqual(True, parser.get('-l'))
        self.assertEqual(8080, parser.get('-p'))
        self.assertEqual('/var/logs', parser.get('-d'))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
