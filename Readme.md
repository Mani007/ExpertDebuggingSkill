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
```
.env/bin/activate
```   

- pytest framework - use the documentation to install and use pytest      
After installation of pytest, to run it create the test folder and write the test cases by importing testable functions and by writing the test files. To run the test use the following command      
```
pytest .\test\test_firsttest.py
```   

### Function based tests
We can test functions using the pytest framework. 
### Classes based tests
We can test classes using the pytest framework