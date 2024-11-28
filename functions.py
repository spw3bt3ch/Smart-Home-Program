import sqlite3
import time
import datetime as dt


connection = sqlite3.connect("SMI_Smart_Home_User2.db")
cursor = connection.cursor()


# def get_username():
#     cursor.execute("SELECT Nickname FROM smi_sh_users WHERE rowid = 1")
#     name = cursor.fetchall()
#     for n in name:
#         print(name)


def get_time_hour():
    hour = dt.datetime.now().hour
    if (hour >= 12) and (hour < 16):
        print("Good Afternoon!")
    elif (hour >= 16) and (hour < 24):
        print("Good Evening!")
    elif hour <= 24 and hour < 12:
        print("Good Morning!")


def all_users():
    cursor.execute("SELECT rowid, * FROM smi_sh_users")
    users_table = cursor.fetchall()
    for users in users_table:
        print(users)


def meet_appointment():
    while True:
        attempt = 0
        print("")
        pin_code = int(input("ENTER YOUR PIN CODE>> "))
        if pin_code == 1122:
            while True:
                print("")
                confirm_pin = int(input("PLEASE CONFIRM YOUR PIN CODE>> "))
                attempt += 1
                if confirm_pin == pin_code:
                    print("Access Granted!\nYou Are Welcome")
                    exit()
                elif attempt > 2:
                    print("This is a suspicious number of attempts!\n")
                    print("Calling the Cops...")
                    time.sleep(2)
                    exit()
                elif confirm_pin != pin_code:
                    print("PIN not match! Please try again.")
                    continue
        else:
            print("Access Denied")
            continue


def drop_a_message():
    message_options = ["Text Message", "Voice Message"]
    print("")
    messanger_name = input("What\'s Your Name? ")
    print("")
    print("MESSAGE OPTIONS")
    for sn, message_opt in zip(range(len(message_options)), message_options):
        print(f"{sn+1}. {message_opt}")
    print("")
    choose_mssg_opt = int(input(f"Hello {messanger_name}, Please Choose Your Messaging Option: "))
    print("")
    if choose_mssg_opt == 1:
        text = input("Type Your Message Here... ")
        print("")
        print(f"""Confirm Your Message: 
{text}""")
        print("")
        send_option = input("Type 'Y' to Send, or Type 'N' to cancel: ").lower()
        if send_option == "y":
            print("Sending Your Message...")
            time.sleep(2)
            print("")
            print("Message Sent!")
        else:
            print("Alright, Thank you")
            exit()

    elif choose_mssg_opt == 2:
        print("Record your voice message...")
        send_option = input("Type 'Y' to Send, or Type 'N' to cancel: ").lower()
        if send_option == "y":
            print("Sending Your Voice Message...")
            time.sleep(2)
            print("")
            print("Voice Message Sent!")
        else:
            print("Alright, Thank you")
            exit()


def get_user():
    user_attempts = 0
    while True:
        pin_code = input("ENTER YOUR PIN CODE>> ")
        user_attempts += 1
        cursor.execute(f"SELECT rowid, * FROM smi_sh_users WHERE Access = '{pin_code}'")
        user = cursor.fetchall()

        cursor.execute(f"SELECT Name FROM smi_sh_users WHERE Access = '{pin_code}'")
        username = cursor.fetchall()

        if user:
            while True:
                main_menu = ["Gain Access", "Meet An Appointment", "Leave A Message", "Exit"]
                print("")
                time.sleep(1)
                for name in username:
                    for n in name:
                        print(f"YOU ARE WELCOME, {n}")
                        print("")
                    print("MAIN MENU")
                for sn, menu in zip(range(len(main_menu)), main_menu):
                    print(f"{sn+1}. {menu}")
                print("")
                user_option = int(input("Choose from an Option above >> "))
                if user_option == 1:
                    while True:
                        user_pin_code_confirmation = input("Please confirm Access Code: ")
                        cursor.execute(f"SELECT rowid, * FROM smi_sh_users WHERE Access = '{user_pin_code_confirmation}'")
                        user = cursor.fetchall()
                        if user:
                            print("")
                            print("You are most welcome, please come-in")
                            print("")
                            while True:
                                print("")
                                print("What Would You Like To Do? ")
                                user_asset_option = [
                                    "Add A New User",
                                    "View All Users",
                                    "Received Message",
                                    "Security",
                                    "Other Notifications",
                                    "Exit"
                                ]
                                for sn, uao in zip(range(len(user_asset_option)),user_asset_option):
                                    print(f"{sn+1}. {uao}")
                                print("")
                                main_user_option = int(input("Choose An Option: "))
                                if main_user_option == 1:
                                    user_name = input('FULL NAME: ')
                                    user_nick_name = input("NICK NAME: ")
                                    user_status = input("USER STATUS: ")
                                    user_access_code = input("ACCESS CODE: ")
                                    cursor.execute(f"INSERT INTO smi_sh_users VALUES ("
                                                   f"'{user_name}', '{user_nick_name}', '{user_status}', '{user_access_code}'"
                                                   f")")
                                    print("")
                                    print("You have successfully added a new user!")
                                elif main_user_option == 2:
                                    all_users()
                                elif main_user_option == 3:
                                    print("Message box is empty")
                                elif main_user_option == 4:
                                    print("Camera not yet set")
                                elif main_user_option == 5:
                                    print("Notification box is presently empty")
                                elif main_user_option == 6:
                                    exit()
                                else:
                                    print("Invalid Option")
                                    continue
                            break
                        else:
                            print("Please crosscheck and try it again")
                            continue
                    continue

                elif user_option == 2:
                    meet_appointment()

                elif user_option == 3:
                    drop_a_message()

                elif user_option == 4:
                    exit()

        elif user_attempts > 2:
            print("Acting Suspicious")
            print("")
            print("Calling the Cops...")
            time.sleep(2)
            exit()
        else:
            print("Access Denied!")
            break


connection.commit()
# connection.close()
