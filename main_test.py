import io
import sys
import re
import main

def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut

    main.main()

    sys.stdout = sys.__stdout__

    lines = captureOut.getvalue().split('\n')

    res = re.search(r'[\w,\W]*Programming[\w,\W]*', lines[2])
    assert res is not None

    res = re.search(r'[\w,\W]*Python[\w,\W]*', lines[1])
    assert res is not None

    res = re.search(r'[\w,\W]*Programming[\w,\W]*Python[\w,\W]*', lines[3])
    assert res is not None

if __name__ == '__main__':
    test_main_1()

