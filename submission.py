import random

class Solution:

        # 1
        #The function "printer", prints the numbers starting in descending order
        def printer(self,number_one):
            number_one = int(number_one)
            flag = False
            while number_one >= 1:
                temp = number_one
                if number_one == 1:
                    print(temp)
                    print('\n')
                    exit(1)
                else:
                    while temp >= 1:
                        print(temp, end=' ')
                        temp -= 1

                    print('\n')

                number_one -= 1

                self.printer(number_one)

        #Checker checks if the given number is an integer or not(validaiton function)
        #It makes sure that the number is neither string nor a negative number
        def checker(self,number_one):
            while number_one is not int:
                try:
                    temp = int(number_one)
                    if temp <= 0:
                        print("Enter a positive integer")
                        number_one = input()
                        temp = int(number_one)
                    elif temp >= 0:
                        break

                    break
                except:
                    print(f'You have entered {number_one}, please enter an integer greater than 0')
                    number_one = input('Enter an integer greater than 0')
                    continue

            self.printer(number_one)


        #2
        #This function prints the series after accepting a number
        def Series_Printer(self, number):

            if self.number >= 0:

                print(f"Since you entered {self.number}, the series is as below : ")

                for i in range(self.number):

                    if i == self.number - 1:

                        print(self.sum, )
                    elif i != self.number:

                        print(self.sum, end=', ')


                    self.sum = self.sum + self.counter
                    self.counter += 1


        #This is yet another implementation of validating the user by input
        def making_sure_number_is_integer(self):

            # Exception handling if user enters a string
            while True:
                try:
                    int(self.number)
                    break
                except Exception as e:
                    print(e)

                if isinstance(self.number, int) and self.number > 0:
                    break

                else:
                    self.number = input("Enter number of numbers to display : ")

            self.number = int(self.number)
            self.Series_Printer(self.number)


        #3
        # "USF_TIME" converts time from 24hrs to USF time standard
        def usf_time(self):

            flag1 = -1
            flag2 = -1
            flag3 = -1

            while True:

                time_list = []
                #Here the user needs to enter time im HH:MM:MM AM/PM format
                #it is a validation function so that the user has to enter
                #time in hours between 1-12, minutes between 0-60 & seconds between 0-60
                while flag1 != 1:
                    try:
                        if flag1 == -1:
                            time = input("Please enter time in 12 Hour (HH:MM:MM AM/PM) format followed by AM/PM :")
                            print(time)
                            time_list = []
                            time_list = time.split(":")
                            print(time_list)
                            if int(time_list[0][0:]) and (0 <= int(time_list[0][0:]) <= 12):
                                flag1 = 1
                                break
                    except Exception as e:
                        print(e)
                        time_list[0] = input("Enter the correct time HOURS")
                        continue

                while flag2 != 1:
                    try:

                        if flag2 == -1:
                            if int(time_list[1]) and (0 <= int(time_list[1]) < 60):
                                flag2 = 1
                                break
                    except Exception as e:
                        print(e)
                        # print("Please enter an integer time followed by AM OR PM")
                        time_list[1] = input("Enter the correct time MINUTES")
                        continue

                while flag3 != 1:
                    try:
                        if flag3 == -1:
                            number_is_int = int(time_list[2][0:2])
                            number_is_btw_0_and_60 = 0 <= int(time_list[2][0:2]) < 60
                            time_of_day = ("AM" in time_list[2][1:]) or ("PM" in time_list[2][1:])

                        if number_is_int:
                            if number_is_btw_0_and_60:
                                if time_of_day:
                                    flag3 = 1
                    except Exception as e:
                        print(e)
                        print("Please enter an integer time followed by AM OR PM")
                        time_list[2] = input("Enter the correct time SECONDS")
                        continue

                if flag1 == flag2 == flag3 == 1:
                    break
                else:
                    continue

            if flag1 == flag2 == flag3 == 1:

                sum = 0

                #Here the for loop calculates/converts the time

                for i in range(len(time_list)):
                    # print(i)
                    if i == 0:
                        if "AM" in time:
                            sum = int(time_list[i]) * 60 * 60

                        elif "PM" in time:
                            sum = (int(time_list[i])+12) * 60 * 60

                    elif i == 1:
                        sum = sum + int(time_list[i]) * 60

                    elif i == 2:
                        sum = sum + int(time_list[i][:2])


                u_hrs = sum/(60*45)

                s_mins = (u_hrs - int(u_hrs))*60

                f_seconds = (s_mins - int(s_mins))*45


                print(f"OUTPUT : {int(u_hrs)}:{int(s_mins)}:{int(f_seconds)} ")

        #4
        #"USF_NUMBERS", accepts numbers_per_line & k_number to print
        def usf_numbers(self, numbers_per_line=12, k_number=112):
            print('\n\n')
            print('USF Numbers : \n')
            for i in range(1, k_number):
                if i % numbers_per_line == 0:
                    print("\n")

                if i % 3 == i % 5 == i % 7 == 0:
                    print("USF", end=' ')
                elif i % 3 == i % 5 == 0:
                    print("US", end=' ')
                elif i % 3 == i % 7 == 0:
                    print("UF", end=' ')
                elif i % 5 == i % 7 == 0:
                    print("SF", end=' ')
                elif i % 7 == 0:
                    print("F", end=' ')
                elif i % 5 == 0:
                    print("S", end=' ')
                elif i % 3 == 0:
                    print("U", end=' ')
                else:
                    print(i, end=' ')

            print('\n')

        #5
        pali_indexes = []
        #This function checks to see whether the given workd is a palindrome or not
        def check_pali(self, concat_word):

            # Converting all characters to lower case
            # input_five = [x.lower() for x in input_five]
            start = 0
            end = len(concat_word) - 1

            if len(concat_word) % 2 != 0:

                while start < (int(len(concat_word) / 2) + 1):

                    if concat_word[start] == concat_word[end]:

                        start += 1
                        end -= 1
                    elif concat_word[start] != concat_word[end]:

                        return False
                return True
            elif len(concat_word) % 2 == 0:
                while start <= (len(concat_word) / 2) + 1:
                    if concat_word[start] == concat_word[end]:
                        start += 1
                        end -= 1
                    elif concat_word[start] != concat_word[end]:

                        return False
                return True

        #"Pali_func" is combines the different elements in the list
        #and then send it over to check_pali to check if its a palindrome or not
        def pali_func(self):

            i = 0
            while i != len(ip) - 1:
                word = ip[i]
                for j in range(len(ip)):
                    if i == j:
                        pass

                    else:
                        new_word = word + ip[j]
                        bool_cond = self.check_pali(new_word)
                        if bool_cond:
                            self.pali_indexes.append([i, j])

                i += 1


            print("Combinations which generate palindrome are :")
            print(self.pali_indexes)

        sum = 1
        counter = 2
        number = 6

        #6
        #This function decides who is going to be the winner
        #I used python random library to randomly generate the users stones to pick(either 1, 2 or 3)
        def Stones(self,total):

            temp = total

            p_moves = []
            first_flag = 1
            while temp != 0:

                if first_flag == 1:

                    p1 = random.randint(1, 3)
                    p_moves.append('ONE')

                    p_moves.append(p1)
                    p2 = random.randint(1, 3)
                    p_moves.append('TWO')
                    p_moves.append(p2)

                    first_flag = 0

                # if temp-p2 > 0:
                if temp - p1 == 0:

                    p_moves.pop()
                    p_moves.pop()
                    # print(p_moves)
                    break
                elif temp - p1 < 0:
                    p_moves.pop()
                    p_moves.pop()

                    p1 = random.randint(1, p1 - temp)

                    temp = temp - p1
                    p_moves.append('ONE')
                    p_moves.append(p1)
                    continue
                else:
                    temp = temp - p1

                    p1 = random.randint(1, 3)
                    p_moves.append('ONE')
                    p_moves.append(p1)


                if temp - p2 == 0:

                    p_moves.pop()
                    p_moves.pop()

                    break
                elif temp - p2 < 0:
                    p_moves.pop()
                    p_moves.pop()
                    p2 = random.randint(1, p2 - temp)

                    temp = temp - p2
                    p_moves.append('TWO')
                    p_moves.append(p2)
                    continue
                else:
                    temp = temp - p2
                    p2 = random.randint(1, 3)
                    p_moves.append('TWO')
                    p_moves.append(p2)
            print(p_moves)








ip = ["abcd", "dcba", "lls", "s", "sssll"]


obj = Solution()

#5
obj.pali_func()

#2
numbers_per_line = 12
k_number = 112

#4
obj.usf_numbers(numbers_per_line, k_number)


#2
number = 6
obj.Series_Printer(number)

#3
obj.usf_time()

#6
total = 5
obj.Stones(total)

#1
number_one = input('Enter an integer greater than 0')
obj.checker(number_one)




