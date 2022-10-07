import time

asc = time.asctime()


class FraudDict:

    minimum_withdrawal = 200

    withdraw_range_per_day = 100_000

    withdraw_limit = 110_000

    bank_balance = 2_111_789

    def withdraw(self):

        # number_of_days_money_was_withdrawn =

        print(' Withdraw Cash')

        statement = []

        limit = int(input('Enter withdraw times: '))

        for i in range(limit):

            amount = float(input('Enter amount: '))

            statement.append(amount)

            balance = FraudDict.bank_balance - amount
            if amount < FraudDict.minimum_withdrawal:

                print('Service not available try again')

            elif sum(statement) > 600_500:

                print('Fraud dictated')

            else:
                print(f'confirmed you have @ {asc} you have withdraw {amount:,} successful')

        else:
            print(f'Confirmed {asc} you have withdraw {sum(statement):,} successful ')

        print(statement)


fraud = FraudDict()
fraud.withdraw()









