# Budget App

A Python-based budgeting program which manages transactions by category and visualizes spending distribution using a text-based bar chart.

## Features
- `Category`: A class that has the following attributes:
    - `ledger`: A list of dictionaries. Each dictionary represents a transaction and contains:
        - amount: Transaction amount (positive = deposit, negative = withdrawal)
        - description: Description of the transaction.
    - `balance`: Amount of money currently available.
    - `expenditure`: Amount of money spent.

- `deposit`: deposits a given amount of money for the category. Adds the transaction to the ledger, and the given amount to the balance.
    - Parameters:
        - `amount`
        - `description`: optional, set to `''` by default

- `withdraw`: withdraws a given amount of money from the category. Checks if the action's possible first. If so, adds the transaction to the ledger. subtracts the given amount from the balance and adds it to the expenditure.
    - Parameters:
        - `amount`
        - `description`: optional, set to `''` by default

- `get_balance`: returns the current amount of balance available.

- `transfer`: Transfers a given amount from a category to another. Checks to see if the action's possible first. If so, withdraws the given amount from current category and deposits it in the other category.
    - Parameters:
        - `amount`
        - `other_category`: the category in which the given amount will be deposited
    
- `check_funds`: Helper method (used in `withdraw` and `transfer` methods). Returns false if the balance is less than the specified amount and true otherwise.
    - Parameters:
        - `amount`: specified amount

- `create_spend_chart`: Prints a text-based bar chart showing each category’s share of total expenditure to the terminal.
    - Parameters:
        - `categories`: a list of categories.


## Usage

```python
from budget_app import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(50, "groceries")

clothing = Category("Clothing")
food.transfer(100, clothing)

print(food)
print(create_spend_chart([food, clothing]))

""" Output:

*************Food*************
initial deposit        1000.00
groceries               -50.00
Total: 950.00

Percentage spent by category
100|
 90|
 80| o
 70| o
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o
  0| o  o
    -------
     F  C
     o  l
     o  o
     d  t
        h
        i
        n
        g
"""
```

## Concepts Utilized

- Object-Oriented Programming (OOP)
- Encapsulation
- Data structures (lists and dictionaries)
- String formatting and output alignment
- Basic data visualization (text-based bar chart)