class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.expenditure = 0

    def __str__(self):
        length = len(self.category)
        if length % 2 == 0:
            title = (((30 - length) // 2) * ('*')) + self.category + (((30 - length) // 2) * ('*')) + '\n'
        else:
            title = (((30 - length) // 2) * ('*')) + self.category + ((((30 - length) // 2) + 1) * ('*')) + '\n'
        
        expenses = ''
        for expense in self.ledger:
            amount, description = list(expense.values())
            amountt = f'{amount:.2f}'
            expenses += f'{description[:23]}{(23 - len(description[:23])) * ' '}{(7 - len(amountt)) * ' '}{amount:.2f}\n'
            
        expenses += f'Total: {self.balance}'
        return title + expenses
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def check_funds(self, amount):
        return False if self.balance < amount else True

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({'amount': amount * -1, 'description': description})
            self.balance -= amount
            self.expenditure += amount
            return True
        

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            other_category.deposit(amount, f'Transfer from {self.category}')
            self.withdraw(amount, f'Transfer to {other_category.category}')
        else:
            return False
            
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(16, 'shirt')
total_expenditur = food.expenditure + clothing.expenditure
# print(total_expenditur)
# # print(food.expenditure)
print(round((food.expenditure / total_expenditur) * 100) >= 100)
# print(food)

def round(number):
    if number % 10 < 5:
        return number - (number % 10)
    else:
        return number - (number % 10) + 10

def max_length(first_list):
    length_list = [len(first_list[i]) for i in range(len(first_list))]
    return max(length_list)

def create_spend_chart(categories):
    string = ''
    string += 'Percentage spent by category'
    string += '\n'
    total_expenditure = 0
    liste_de_longueurs = []
    for category in categories:
        total_expenditure += category.expenditure
    percentage = 100
    while percentage >= 0:
        string += (3 - len(str(percentage))) * ' '
        string += f'{percentage}'
        string += '|'
        string += ' '
        for i in categories:
            if round((i.expenditure / total_expenditure) * 100) >= percentage:
                string += 'o  '
            else:
                string += '   '
        string += '\n' 
        percentage -= 10
        
    string += 4 * ' '
    string += '-'
    for category in categories:
        string += '---'
    string += '\n'
    for cat in categories:
        liste_de_longueurs.append(cat.category)
    maximum_length = max_length(liste_de_longueurs)
    for i in range(maximum_length):
        string += 5 * ' '
        for j in categories:
            cat_length = len(j.category)
            if i <= (len(j.category) - 1):
                string += str(j.category[i]) + 2 * ' '
            else:
                string += 3 * ' '
        if i == maximum_length - 1:
            return string
        else:
            string += '\n'
    return string

print(create_spend_chart([food, clothing]))
