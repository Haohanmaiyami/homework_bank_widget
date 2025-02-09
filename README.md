![Test_photo](https://toppsta.com/media/thumbnails/large/7%20Easy%20Programming%20Languages%20for%20Kids.webp)
# Data processing project
## Project description 
Project designed for data processing and 
includes masking info regarding personal data,
filtering and sorting various functions. 
tests have also been added. 
The pytest library is used to test the project. 
The tests (all tests in the folder **tests**) cover key functions of all modules, including masks, widget, and processing.
The project is 
developed using GitFlow and hosted on GitHub 
for collaboration. 
### Usage examples
1. First, download the project code to your computer from GitHub
2. Second, create your virtual environment
3. To run the project, simply execute: 
```python main.py```
4. For testing make sure that you install all dependencies. 
For testing just use command ```pytest```
5. To check tests coverage input ```poetry run pytest --cov```, also you can see percentages by using ```pytest --cov=src --cov-report=html```. It will automatically create file index.html with the results of the testing

### Fixtures and Parameterization
The tests use fixtures **(conftest.py)** to generate test data.
Parameterization is used to test different inputs without duplicating tests.

### +

1. Test coverage is more than 80%
2. 

### Documentation
Links:

[Python official documentation](https://docs.python.org/3/)

[Git documention](https://git-scm.com/doc)

[Pytest](https://docs.pytest.org/en/stable/contents.html)




### License

*This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.*