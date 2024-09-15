import sys
from io import StringIO
from basicFunctions import main
from basicFunctions import doubleNumber

def test_main(capsys):

    # Capture the output of the main function
    captured_output = StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__

    # Check the output
    assert captured_output.getvalue() == "Hello World!\nThis is a test file.\n"

def test_doubleNumber():

    assert doubleNumber(2) == 4
    assert doubleNumber(-3) == -6
    assert doubleNumber(0) == 0