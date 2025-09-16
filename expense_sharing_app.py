class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends
        self.balances = {friend: 0 for friend in friends}

    def add_expense(self, payer, amount, participants):
        split_amount = amount / len(participants)
        for participant in participants:
            self.balances[participant] -= split_amount
        self.balances[payer] += amount

    def calculate_settlement(self):
        creditors = []
        debtors = []

        for friend, balance in self.balances.items():
            if balance > 0:
                creditors.append((friend, balance))
            elif balance < 0:
                debtors.append((friend, -balance))

        print("\nSettlement Summary:")
        while debtors and creditors:
            debtor, debt_amount = debtors.pop()
            creditor, credit_amount = creditors.pop()

            payment = min(debt_amount, credit_amount)

            print(f"{debtor} owes {creditor}: Rs.{payment:.2f}")

            if debt_amount > payment:
                debtors.append((debtor, debt_amount - payment))
            if credit_amount > payment:
                creditors.append((creditor, credit_amount - payment))


if __name__ == "__main__":
    friends = input("Enter the names of friends, separated by commas: ").split(",")
    friends = [friend.strip() for friend in friends]

    expense_sharing = ExpenseSharing(friends)

    while True:
        payer = input("Enter the name of the person who paid (or 'done' to finish): ").strip()
        if payer.lower() == "done":
            break

        amount = float(input("Enter the amount paid: "))

        participants = input("Enter the names of participants for this expense, separated by commas: ").split(",")
        participants = [participant.strip() for participant in participants]

        expense_sharing.add_expense(payer, amount, participants)

    expense_sharing.calculate_settlement()
