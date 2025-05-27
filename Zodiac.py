Zodiacs = {'Aries' : {'March' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                    'April' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]},

        'Taurus' : {'April' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                    'May' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]},

        'Gemini' : {'May' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                    'June' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 21]},

        'Cancer' : {'June' : [22, 23, 24, 25, 26, 27, 28, 29, 30],
                    'July' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21, 22]},

        'Leo' : {'July' : [23, 24, 25, 26, 27, 28, 29, 30, 31],
                'August' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21, 22, 23]},

        'Virgo' : {'August' : [24, 25, 26, 27, 28, 29, 30, 31],
                    'September' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21, 22, 23]},

        'Libra' : {'September' : [24, 25, 26, 27, 28, 29, 30],
                    'October' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21, 22, 23]},

        'Scorpio' : {'October' : [24, 25, 26, 27, 28, 29, 30, 31],
                    'November' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21, 22]},

        'Sagittarius' : {'November' : [23, 24, 25, 26, 27, 28, 29, 30],
                        'December' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 21]},

        'Capricon' : {'December' : [22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                    'January' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]},

        'Aquarius' : {'January' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                    'February' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19]},

        'Pisces' : {'Februery' : [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                    'March' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]}}
'''
def get_zodiac(month, date):
    if month in Aries:
        if date in Aries[month]:
            print("You are an Aries")
        else:
            print("You are not an Aries")
            
    else:
        print("Enter a valid month")  '''  

def get_zodiac(month, date):
    found = False
    for sign, date_ranges in Zodiacs.items():
        if month in date_ranges and date in date_ranges[month]:
            print(f"You are a {sign}")
            found = True
            break

    if not found:
        print("Enter a valid month and date combination.")


month_response = input('What month were you born? ').capitalize()
try:
    date_response = int(input('What date were you born? '))
except ValueError:
    print("Enter a valid date")
    exit()

get_zodiac(month_response, date_response)