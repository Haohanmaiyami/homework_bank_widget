![Test_photo](https://toppsta.com/media/thumbnails/large/7%20Easy%20Programming%20Languages%20for%20Kids.webp)
# Data processing project
## Project description 
Project designed for data processing and 
includes masking info regarding personal data,
filtering, generators and sorting various functions. 
tests have also been added. 
The pytest library is used to test the project. 
The tests (all tests in the folder **tests**) cover key functions of all modules, including masks, widget, generators and processing.
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

### Generators info
1. Filter_by_currency function, 
usage example:
```
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
2. transaction_descriptions function, 
usage example:
```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```

3. card_number_generator function,
usage example:
```
for card_number in card_number_generator(1, 5):
    print(card_number)
>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005

```


### Documentation
Links:

[Python official documentation](https://docs.python.org/3/)

[Git documention](https://git-scm.com/doc)

[Pytest](https://docs.pytest.org/en/stable/contents.html)




### License

*This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.*