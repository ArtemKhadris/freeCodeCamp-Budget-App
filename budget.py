class Category:

    # initialisation
    # desc - description
    def __init__(self, desc):
        self.desc = desc
        self.ledger = []
        self.balance = 0.0

    # deposit mothod (check readme)
    # am - amount
    def deposit(self, am, desc = ''):
        self.ledger.append({'amount':am, 'description':desc})
        self.balance += am
    
    # withdraw method (check readme)
    def withdraw(self, am, desc=''):
        if self.balance - am >= 0:
            self.ledger.append({'amount': -1 * am, 'description': desc})
            self.balance -= am
            return True
        else:
            return False
    
    # get_balance method (check readme)
    def get_balance(self):
        return self.balance
        
    # transfer method (check readme)
    # cat - category 
    def transfer(self, am, budget_cat):
        if self.check_funds(am):
            a = 'Transfer to ' + budget_cat.desc
            b = 'Transfer from ' + self.desc
            self.withdraw(am, a)
            budget_cat.deposit(am, b)
            return True
        else:
            return False

    # check_funds method (check readme)
    def check_funds(self, am):
        if am <= self.get_balance():
            return True
        else:
            return False

    # output
    def __str__(self):
        output = self.desc.center(30, '*') + '\n'
        for i in self.ledger:
            a = i['description'][:23].ljust(23) + format(i['amount'], '.2f').rjust(7) + '\n'
            output += a
        b = 'Total: '+ format(self.get_balance(), '.2f')
        output += b
        return output

# another output (percentage)
# perc - percentage
def create_spend_chart(cats):
    cat_descs = []
    spent = []
    spent_percs = []

    for cat in cats:
        summ = 0
        for i in cat.ledger:
            if i['amount'] < 0:
                summ -= i['amount']
        spent.append(round(summ, 2))
        cat_descs.append(cat.desc)

    for am in spent:
        a = round(am / sum(spent), 2) * 100
        spent_percs.append(a)

    check = 'Percentage spent by category\n'
    P = range(100, -10, -10)

    for p in P:
        check = check + str(p).rjust(3) + '| '
        for percent in spent_percs:
            if percent >= p:
                check += 'o  '
            else:
                check += '   '
        check += '\n'

    check += '    ----' + ('---' * (len(cat_descs) - 1))
    check += '\n     '

    # l - longest discription
    l = 0

    for desc in cat_descs:
        if l < len(desc):
            l = len(desc)

    for i in range(l):
        for desc in cat_descs:
            if len(desc) > i:
                check += desc[i] + '  '
            else:
                check += '   '
        if i < l - 1:
            check += '\n     '

    return(check)