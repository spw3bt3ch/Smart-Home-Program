import sqlite3
from functions import *
import datetime as dt


today_date = dt.datetime.today()
date = today_date.strftime("%d-%m-%Y")

now_time = dt.datetime.now()
time = now_time.strftime("%H:%M")

# Database connection
while True:
    try:
        connection = sqlite3.connect("SMI_Smart_Home_User2.db")
        cursor = connection.cursor()
        # print("SMI Smart_Home_User Application Database has been created successfully")
        # cursor.execute("CREATE TABLE smi_sh_users ('Name', 'Nickname', 'User Satus', 'Access')")
        # print("A table has successfully been created")

        # cursor.execute("DROP TABLE visitors")
        # print("Visitor\'s Table has been deleted")

        smi_sh_users = [
            ('Olujimi Samuel', 'SP', 'Father', '190987'),
            ('Olujimi Moyosore', 'Moyo', 'Mother', '080592'),
            ('Olujimi OreOluwa', 'Bobo-K', 'First-Son', '170223'),
            ('Olujimi MomoreOluwa', 'Momo', 'Second-Son', '220724')
        ]

        # cursor.executemany("INSERT INTO smi_sh_users VALUES (?,?,?,?)", smi_sh_users)
        # print("A new set of records has been created.")

        # cursor.execute("UPDATE smi_sh_users SET 'Access codes' = '220723' WHERE rowid = 4")
        # print("A record has been updated.")
        print("************************************************")
        print("SMI SMART HOME CLI APPLICATION")
        print(f"{date} || {time}-GMT")
        get_time_hour()
        print("************************************************")
        print("")
        get_user()

        connection.commit()
        # connection.close()

    except KeyboardInterrupt:
        exit_confirmation = input("\n\n************************************************\n"
                                  "Are you sure you want to Exit this App (Y/N)? ").lower()
        if exit_confirmation == "y":
            print("\nYou\'ve Exited the Program\nThank you for your time. Bye!")
            exit()
        else:
            continue





