# Software debugging and testing skills
This is the project for software debugging and testing skills for projects with large code bases. This is from beginner level to the most advance level of debugging and testing skills. The primary language here is python but the concept apply to any other programming language. **We will be using Chat GPT for writing the test cases for python.**       
## Pytest framework    

We have implemented some pytest framework based test cases examples in order to understand core concepts of software testing, particularly automated unit testing.    
Installation setup     
- Virtual environment or venv for windows     
To create virtual environment in windows10+, put this command on your terminal at your python working directory. You will have a folder created with the name .env as your local environment. 
```
python3 -m venv .env
```    
To activate the environment, use the following command in the terminal 
~~.env/bin/activate~~ for the older version the folder name is bin/activate
```

.env/Scripts/activate
```   
*NOTE:when you are not able to select correct python interpreter then try setting up environment variable or try renaming the python executable file. This will enable you to select correct python interpreter*
### Creating requirements.txt file
To create requirements.txt for current project use the following command.     
This command will give all the current library in your python virtual environment
```python
pip3 list
```   
Now run this command to create requirements.txt file from all the library
```python
pip3 freeze > requirements.txt
```
To install all the files from requirements.txt, run the following command. Make sure you have correct path for your requirements.txt file. 
```python
pip3 install -r requirements.txt
```


- pytest framework - use the documentation to install and use pytest      
After installation of pytest, to run it create the test folder and write the test cases by importing testable functions and by writing the test files. To run the test use the following command      
```

pytest .\test\test_firsttest.py
```   

### Function based tests
We can test functions using the pytest framework. 
### Classes based tests
We can test classes using the pytest framework.       
To run setup and teardown method for class based testing use the -s option in pytest.   
```
pytest .\test\test_circle.py -s
```


### Some crucial concept of pytest testing are listed below
1. marking
2. mark skip
3. mark xfail
4. parameterized testing
5. logging and reports
6. mocking - not preferable to use pytest here especially with API calls
7. fixtures decorators

##### Basic testing concept of pytest is completed here 
##### Do not prefer mocking api in pytest as it verbose, prefer some other tools to do it
### Remarks
Some upcoming stuff that need to be completed for understanding testing are 
1. use of testing in CI/CD environment 
2. Different types of testing such as integration testing, functional , unittest, behavior testing etc needs to be explored preferably with some different tools