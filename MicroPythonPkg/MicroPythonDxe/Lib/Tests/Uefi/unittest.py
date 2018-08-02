import sys

def log(indent_level, *msgs):
    if indent_level:
        print('  ' * indent_level, *msgs, end='\r\n')
    else:
        print(*msgs, end='\r\n')

TEST_THIS = sys.argv[0] if sys.argv else 0
TEST_ALL  = not TEST_THIS or TEST_THIS.lower() == 'all'

class TestCase(object):
    def __init__(self, case=''):
        if not case:
            case = TEST_THIS

        if case:
            case = 'test_' + case

        self.setUp()

        for method in dir(self):
            if not method.startswith("test_"):
                continue

            if not case or case == method:
                try:
                    getattr(self, method)()
                except AssertionError as Excpt:
                    log(0, "\n[FAILED]",  method, '\r\n')
                    raise
                except:
                    raise

                if case:
                    break 

        self.tearDown()

    def setUp(self):
        ''' Test case setup '''
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    pass

