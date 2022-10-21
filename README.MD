Test Vagrant Assignment Repository

#### Setup Instructions
    1. Make sure Python Version 3.8 or above is installed in the host system under test
    2. Refer the requirements.txt file for necessary library packages available to install for this framework.
    3. Install the package using command - pip install -r requirements.txt

#### Command for Execution
    python -m pytest --html=reports/report.html --self-contained-html  (or)
    python -m pytest tests/ --html=reports/report.html --self-contained-html

#### Folder Structure
    1. test_data directory have files like *.json, *.xlsx, etc
    2. test_utils directory holds utility operations like file parsing,formatting, etc
    3. tests directory holds the test cases created for verification.
    4. Pytest testing framework needs tests/conftest.py file and it is driver file for test execution. Here we will define our custom fixtures, test report modification hooks, etc.
    5. Once the execution is completed, html reports are generated under reports directory.

    
