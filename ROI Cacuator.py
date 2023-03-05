# 明确项目目标
# 拆解项目需求
# 执行


def QA1():
    # Income
    global total_income
    global rental_income
    global laundry
    global storage
    global misc

    rental_income = input('What is your monthly income?')
    laundry = input('What is your laundry monthly income?')
    storage = input('What is your storage income?')
    misc = input('What is your miscellaneous income?')


def QA2():
    # Expense
    global tax
    global insurance
    global total_utilities
    global total_expense1

    tax = input("What is your tax expense?")
    insurance = input("What is your insurance expense?")
    total_utilities = input("Do you have any utility expenses? Type 'yes' or 'no'")
    if total_utilities == "yes":
        electric = input("What is your electricity expense?")
        water = input("What is your water expense?")
        sewer = input("What is your sewer expense?")
        gas = input("What is your gas expense?")
        total_utilities = float(electric) + float(water) + float(sewer) + float(gas)
        total_expense1 = float(tax) + float(insurance) + float(total_utilities)
    else:
        hoa = input("What is your hoa expense?")
        snow = input("What is your snow expense?")
        repair = input("What is your repair expense?")
        capex = input("What is your capex expense?")
        mortgage = input("What is your mortgage expense?")
        property_manage = input("What is your management expense?")
        vacancy = input("What is your vacancy expense?")
        total_utilities = 0
        total_expense1 = float(tax) + float(insurance) + float(total_utilities) + float(hoa) + float(snow) + float(
            vacancy) + float(repair) + float(capex) + float(property_manage) + float(mortgage)


def QA3():
    global down_payment
    global closing_costs
    global rehab_budget
    global misellanous
    down_payment = input("What is your downpayment")
    closing_costs = input ("What is your closing?")
    rehab_budget= input("What is your rehab budget")
    misellanous = input ("What is your misellanous investment")


def total_income():
    global total_income
    total_income = float(rental_income) + float(laundry) + float(storage) + float(misc)
    print("=" * 30)
    print(f"Your total income is {total_income}$")
    print("=" * 30)


def total_expense():
    global total_expense
    print("=" * 30)
    print(f"Your total expense is {total_expense1}$")
    print("=" * 30)


def cash_flow():
    global Anuanl_cashflow
    global cash_flow
    cash_flow = float(total_income) - float(total_expense1)
    Anuanl_cashflow = float(cash_flow) * 12
    print("=" * 30)
    print(f"Your total cashflow is {cash_flow}， your anuanl cashflow is{Anuanl_cashflow}")
    print("=" * 30)


def investment():
    global total_investment
    print ("Let's look at your investment.")
    total_investment = float(down_payment) + float(closing_costs) + float(rehab_budget) + float(misellanous)
    print("=" * 30)
    print(f"your total investment are {total_investment}$")
    print("=" * 30)

def summary():
    print("-----------------------------------------------------------")
    print(f"Total monthly income .......... ${total_income}")
    print(f"Total monthly expenses .......... ${total_expense1}")
    print(f"Total monthly cash flow .......... ${cash_flow}")
    print(f"Total annual cash flow .......... ${Anuanl_cashflow}")
    print("-----------------------------------------------------------")

def roi():

    roi = float(Anuanl_cashflow) % float(total_investment)
    print("**********************************")
    print(f"Your cash on cash ROI is {roi}%")
    print("**********************************")



def main():
    print("Welcome to use Return On Investment (ROI) Caculator!")
    QA1()
    total_income()
    QA2()
    total_expense()
    cash_flow()
    QA3()
    investment()
    summary()
    roi()


main()

