x = 10
class Cinema:
    def __init__(self, row, seats):
        self.Booked_seat = 0
        self.prize_of_ticket = 0
        self.Total_Income = 0
        self.Booked_ticket_Person = [[None for j in range(seats)] for i in range(row)]
        self.Total_seats = row * seats

    def cinema_hall(self):
        seats_chart = {}
        for i in range(row):
            seats_in_row = {}
            for j in range(seats):
                seats_in_row[str(j + 1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    def show_seat(self, hall):
        print('\nCINEMA :')
        if seats < 10:
            for seat in range(seats):
                print(seat, end='  ')
            print(seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, seats):
                print(seat, end=' ')
            print(seats)
        if seats < 10:
            for num in hall.keys():
                print(int(num) + 1, end='  ')
                for no in hall[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in hall.keys():
                if int(list(hall.keys())[count_num]) < 9:
                    print(int(num) + 1, end='  ')
                else:
                    print(int(num) + 1, end=' ')
                count_key = 0
                for no in hall[num].values():
                    if int(list(hall[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant seats = ', self.Total_seats - self.Booked_seat)
        print()

    def buy_ticket(self, hall):
        Row_number = int(input('Enter row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if Row_number in range(1, row + 1) and Column_number in range(1, seats + 1):
            if hall[str(Row_number - 1)][str(Column_number)] == 'S':
                if row * seats <= 60:
                    self.prize_of_ticket = 10
                elif Row_number <= int(row / 2):
                    self.prize_of_ticket = 10
                else:
                    self.prize_of_ticket = 8
                print('prize_of_ticket - ', '$', self.prize_of_ticket)
                confirm = input('yes for booking and no for Stop booking - ')
                person_detail = {}
                if confirm == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = self.prize_of_ticket
                    hall[str(Row_number - 1)][str(Column_number)] = '\033[1m' + 'B' + '\033[0m'
                    self.Booked_seat += 1
                    self.Total_Income += self.prize_of_ticket
                else:
                    return
                self.Booked_ticket_Person[Row_number - 1][Column_number - 1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by someone')
        else:
            print('\n******  Invalid Input  ******\n')

    def find_percentage(self):
        percentage = (self.Booked_seat / self.Total_seats) * 100
        return percentage

    def Statistics(self):
        print('Number of purchased Ticket - ', self.Booked_seat)
        print('Percentage - ', c.find_percentage())
        print('Current  Income - ', '$', self.prize_of_ticket)
        print('Total Income - ', '$', self.Total_Income)
        print()

    def show_ticket(self, hall):
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, row + 1) and Enter_column in range(1, seats + 1):
            if hall[str(Enter_row - 1)][str(Enter_column)] == '\033[1m' + 'B' + '\033[0m':
                person = self.Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
                print('Phone number - ', person['Phone_No'])

            else:
                print('\n------  Vacant seat  ------')
        else:
            print('\n******  Invalid Input  ******\n')



row = int(input('Enter number of rows - \n'))
seats = int(input('Enter number of seats in a row - \n'))
c = Cinema(row, seats)
hall = c.cinema_hall()

while x != 0:
    print('1. Show the seats \n2. Buy a ticket \n3. Statistics \n4. Show booked tickets User Info \n0. Exit')
    x = int(input('Select Option - '))
    if x == 1:
        c.show_seat(hall)

    elif x == 2:
        c.buy_ticket(hall)

    elif x == 3:
        c.Statistics()

    elif x == 4:
        c.show_ticket(hall)

    elif x>=5:
        print('\n******  Invalid Input , Select correct Option  ******\n')

    else:
        print('\n******  Exit Cinema  ******\n')