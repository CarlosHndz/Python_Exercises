import json

filename = 'fav_num.txt'
try:
    with open(filename) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    fav_num = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(fav_num, f_obj)
        print("We will remember " + str(fav_num) + " as your favorite number.")
else:
    print("Your favorite number is " + fav_num)