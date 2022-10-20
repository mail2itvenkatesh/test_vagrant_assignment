import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark to execute only smoke tests"
    )

    config.addinivalue_line(
        "markers", "regression: mark to execute only regression tests"
    )





