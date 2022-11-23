#creat object property with attributes self, cost, expenses, cash flow
#have method to find total expense- just an input
# have a method to find monthly cash flow
# have a method to find cashoncash roi- (monthly cash flow * 12)/total investment

class property():
    def __init__(self, cost, rent, total_expenses):
        self.cost = cost
        self.rent = rent
        self.total_expenses = None

    def annual_ROI(self):
        expense_1 = int(input('Amount of first expense:'))
        expense_2 = int(input('Amount of second expense:'))
        expense_3 = int(input('Amount of third expense:'))
        expense_4 = int(input('Amount of fourth expense:'))
        expense_5 = int(input('Amount of fifth expense:'))
        self.total_expenses = expense_1 + expense_2 + expense_3 + expense_4 + expense_5
        print(f'Your total expenses are {self.total_expenses}')
        monthly_flow = self.rent - self.total_expenses
        print(f'Your monthly cash flow is {monthly_flow}')
        estimated_down_payment = .06 * self.cost 
        response = input(f"We estimated your down payment to be {estimated_down_payment}, if you would like to change this please respond 'change', if you are happy with the estimated value being used, enter 'continue':")
        if response == 'change':
            down_payment = int(input('Pleas enter the amount of your down payment:'))
            # return down_payment
        elif response == 'continue':
            down_payment = estimated_down_payment
            # return down_payment
        other_costs = input("Please enter the total value of any other costs associated with the purchase of your property. This could be closing costs, rehabilitation budget, or other miscellanious expenses:")
        total_investment = down_payment + int(other_costs)
        annual_flow = monthly_flow * 12
        return_on_investment = (annual_flow/total_investment) * 100
        print(f"Your annual return on investment is {return_on_investment} percent")


new_property = property(200000, 2000, 0)
new_property.annual_ROI()


