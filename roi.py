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
        extra_income = input("Does your property generate income from laundy, storage or any other miscelanious tenant expense? If yes, enter the total amount, if no enter 'no'.")
        if extra_income == int:
            self.rent = self.rent + extra_income
        taxes = int(input('Enter the amount of taxes paid:'))
        insurance = int(input('Enter your insurance payment amount:'))
        utilities = int(input('Enter total amount of utilities paid (water, electric, gas, etc):'))
        HOA = int(input('Enter HOA payment amount:'))
        vacancy = int(input('Enter amount paid due to vacancy:'))
        repairs =  int(input('Enter amount allocated for repairs:'))
        property = int(input("Enter amount paid in property management expenses:"))
        mortgage = int(input("Enter amount of your mortgage payment:"))
        self.total_expenses = taxes + insurance +utilities + HOA + vacancy + repairs + property + mortgage
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
        closing_costs = int(input("Enter the amount you paid in closing costs:"))
        rehab_budget = int(input("Enter the amount allocated for a rehabilitation budget:"))
        total_investment = down_payment + closing_costs + rehab_budget
        annual_flow = monthly_flow * 12
        return_on_investment = (annual_flow/total_investment) * 100
        print(f"Your annual return on investment is {return_on_investment} percent")


new_property = property(200000, 2000, 0)
new_property.annual_ROI()


