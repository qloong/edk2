import sys
from ucollections import OrderedDict
from unittest import *
import _re as re

class OnigurumaReUnitTest(TestCase):
    def setUp(self):
        log(0, "[OnigRE: BEGIN]")

    def tearDown(self):
        log(0, "\n[OnigRE: PASS]")

    def test_cases_from_ure1(self):
        r = re.compile(".+")
        m = r.match("abc")
        print(m.group(0))
        try:
            m.group(1)
        except IndexError:
            print("IndexError")

        # conversion of re and match to string
        str(r)
        str(m)

        r = re.compile("(.+)1")
        m = r.match("xyz781")
        print(m.group(0))
        print(m.group(1))
        try:
            m.group(2)
        except IndexError:
            print("IndexError")

        r = re.compile("[a-cu-z]")
        m = r.match("a")
        print(m.group(0))
        m = r.match("z")
        print(m.group(0))
        m = r.match("d")
        print(m)
        m = r.match("A")
        print(m)
        print("===")

        r = re.compile("[^a-cu-z]")
        m = r.match("a")
        print(m)
        m = r.match("z")
        print(m)
        m = r.match("d")
        print(m.group(0))
        m = r.match("A")
        print(m.group(0))
        print("===")

        # '-' character within character class block
        print(re.match("[-a]+", "-a]d").group(0))
        print(re.match("[a-]+", "-a]d").group(0))
        print("===")

        r = re.compile("o+")
        m = r.search("foobar")
        print(m.group(0))
        try:
            m.group(1)
        except IndexError:
            print("IndexError")


        m = re.match(".*", "foo")
        print(m.group(0))

        m = re.search("w.r", "hello world")
        print(m.group(0))

        m = re.match('a+?', 'ab');  print(m.group(0))
        m = re.match('a*?', 'ab');  print(m.group(0))
        m = re.match('^ab$', 'ab'); print(m.group(0))
        m = re.match('a|b', 'b');   print(m.group(0))
        m = re.match('a|b|c', 'c'); print(m.group(0))

        # Case where anchors fail to match
        r = re.compile("^b|b$")
        m = r.search("abc")
        print(m)

        try:
            re.compile("*")
        except:
            print("Caught invalid regex")

        # bytes objects
        m = re.match(rb'a+?', b'ab');  print(m.group(0))

    def _try_re(self, r):
        try:
            re.compile(r)
            print("OK")
        except: # uPy and CPy use different errors, so just ignore the type
            print("Error")

    def test_cases_from_ure_error(self):
        self._try_re(r'?')
        self._try_re(r'*')
        self._try_re(r'+')
        self._try_re(r')')
        self._try_re(r'[')
        self._try_re(r'([')
        self._try_re(r'([)')

    def test_cases_from_ure_group(self):
        def print_groups(match):
            print('----')
            try:
                i = 0
                while True:
                    print(match.group(i))
                    i += 1
            except IndexError:
                pass

        m = re.match(r'(([0-9]*)([a-z]*)[0-9]*)','1234hello567')
        print_groups(m)

        m = re.match(r'([0-9]*)(([a-z]*)([0-9]*))','1234hello567')
        print_groups(m)

        # optional group that matches
        print_groups(re.match(r'(a)?b(c)', 'abc'))

        # optional group that doesn't match
        print_groups(re.match(r'(a)?b(c)', 'bc'))

    def test_cases_from_ure_namedclass(self):
        def print_groups(match):
            print('----')
            try:
                i = 0
                while True:
                    print(m.group(i))
                    i += 1
            except IndexError:
                pass

        m = re.match(r'\w+','1234hello567 abc')
        print_groups(m)

        m = re.match(r'(\w+)\s+(\w+)','ABC \t1234hello567 abc')
        print_groups(m)

        m = re.match(r'(\S+)\s+(\D+)','ABC \thello abc567 abc')
        print_groups(m)

        m = re.match(r'(([0-9]*)([a-z]*)\d*)','1234hello567')
        print_groups(m)

    def test_cases_from_ure_split(self):
        r = re.compile(" ")
        s = r.split("a b c foobar")
        print(s)

        r = re.compile(" +")
        s = r.split("a b    c   foobar")
        print(s)

        r = re.compile(" +")
        s = r.split("a b    c   foobar", 1)
        print(s)

        r = re.compile(" +")
        s = r.split("a b    c   foobar", 2)
        print(s)

        r = re.compile("[a-f]+")
        s = r.split("0a3b9")
        print(s)

        # bytes objects
        r = re.compile(b"x")
        s = r.split(b"fooxbar")
        print(s)

    def test_cases_from_ure_split_empty(self):
        r = re.compile("f +")   # ' *' does not work in oni-re
        s = r.split("a b    c   foobar")
        print(s)

        r = re.compile("x+")
        s = r.split("foo")
        print(s)

        r = re.compile("bx+")   # 'x+' does not work in oni-re
        s = r.split("axbc")
        print(s)

    def test_cases_from_ure_split_notimpl(self):
        log(1, "\r\n[ure_split_notimpl]")
        r = re.compile('( )')
        try:
            log(2, "split '( )' on 'a b c foobar'")
            s = r.split("a b c foobar")
            log(2, "got", s)
            log(2, "Oniguruma RE implemented grouping")
        except NotImplementedError:
            assert(False)

    def test_cases_from_ure_stack_overflow(self):
        log(1, "\r\n[ure_stack_overflow]")
        try:
            log(2, "matching '(a*)*' against 'aaa'")
            m = re.match("(a*)*", "aaa")
            log(2, "got", m.group(0))
        except Exception as Excpt:
            print("Error:", str(Excpt))
            assert(False)

    def test_search(self):
        log(1, "\r\n[search: number]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        m = re.search("([0-9]+)", test_string)
        log(2, "Found first number '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == "1234")

        log(1, "\r\n[search: non-alphanum]")
        test_string = "kajsdk1234jfkda;ks 5667 jks;ldkfj 98 kj"
        m = re.search("([^0-9a-z]+)", test_string)
        log(2, "Found first non-alphanum '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == ";")

    def test_match(self):
        log(1, "\r\n[match: number]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        m = re.match("[0-9]+", test_string)
        log(2, "Found number '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == "1234")

        log(1, "\r\n[match: non-alphanum]")
        test_string = "kajsdk1234jfkdaks; +5667 jks;ldkfj 98 kj"
        m = re.match("[^0-9a-z]+", test_string)
        log(2, "Found non-alphanum '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == "; +")

        del m

    def test_split(self):
        log(1, "\r\n[split: by number]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        r = re.split("[0-9]+", test_string)
        log(2, "Splitted: %s (\"%s\")" % (r, test_string))
        assert (len(r) == 4)

        log(1, "\r\n[split: by-alphanum]")
        test_string = ";kajsdk1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        r = re.split("[0-9a-z]+", test_string)
        log(2, "Splitted: %s (\"%s\")" % (r, test_string))
        assert (len(r) == 9)

        log(1, "\r\n[split: by non-alphanum]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        r = re.split("[^0-9a-z]+", test_string)
        log(2, "Splitted: %s (\"%s\")" % (r, test_string))
        assert (len(r) == 10)

    def test_compile_search(self):
        log(1, "\r\n[re_obj.search: number]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        p = re.compile("([0-9]+)")
        m = p.search(test_string)
        log(2, "Found first number '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == "1234")

        log(1, "\r\n[re_obj.search: non-alphanum]")
        test_string = "kajsdk1234jfkda;ks 5667 jks;ldkfj 98 kj"
        p = re.compile("([^0-9a-z]+)")
        m = p.search(test_string)
        log(2, "Found first non-alphanum '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == ";")

        del p

    def test_compile_match(self):
        log(1, "\r\n[re_obj.match: number]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        p = re.compile("([0-9]+)")
        m = p.match(test_string)
        log(2, "Found number '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == "1234")

        log(1, "\r\n[re_obj.match: non-alphanum]")
        test_string = "kajsdk1234jfkdaks; +5667 jks;ldkfj 98 kj"
        p = re.compile("[^0-9a-z]+")
        m = p.match(test_string)
        log(2, "Found non-alphanum '%s' (\"%s\")" % (m.group(0), test_string))
        assert (m.group(0) == "; +")

        del p
        del m

    def test_compile_split(self):
        log(1, "\r\n[re_obj.split: by number]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        p = re.compile("[0-9]+")
        r = p.split(test_string)
        log(2, "Splitted: %s (\"%s\")" % (r, test_string))
        assert (len(r) == 4)

        log(1, "\r\n[re_obj.split: by-alphanum]")
        test_string = ";kajsdk1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        p = re.compile("[0-9a-z]+")
        r = p.split(test_string)
        log(2, "Splitted: %s (\"%s\")" % (r, test_string))
        assert (len(r) == 9)

        log(1, "\r\n[re_obj.split: by non-alphanum]")
        test_string = ";kajsdk 1234 jfkda;ks 5667 jks;ldkfj 98 kj"
        p = re.compile("[^0-9a-z]+")
        r = p.split(test_string)
        log(2, "Splitted: %s (\"%s\")" % (r, test_string))
        assert (len(r) == 10)

        del p

if __name__ == '__main__':
    mytest = OnigurumaReUnitTest()

