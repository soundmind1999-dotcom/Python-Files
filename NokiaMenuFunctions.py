def main_menu():
    while True:
        menu = """
        Menu Functions
        1. Phonebook
        2. Messages
        3. Chat
        4. Call Register
        5. Tones
        6. Settings
        7. Call divert
        8. Games
        9. Calculator
        10. Reminders
        11. Clock
        12. Profiles
        13. SIM Services
        0. Exit
        """
        print(menu)
        choice = int(input("Enter a menu number: "))

        if choice == 1:
            phonebook_menu()
        elif choice == 2:
            messages_menu()
        elif choice == 3:
            print("Chat\n")
        elif choice == 4:
            call_register_menu()
        elif choice == 5:
            tones_menu()
        elif choice == 6:
            settings_menu()
        elif choice == 7:
            print("Call divert\n")
        elif choice == 8:
            print("Games\n")
        elif choice == 9:
            print("Calculator\n")
        elif choice == 10:
            print("Reminders\n")
        elif choice == 11:
            clock_menu()
        elif choice == 12:
            print("Profiles\n")
        elif choice == 13:
            print("SIM Services\n")
        elif choice == 0:
            print("Exiting")
            break
        else:
            print("Invalid Option!\n")


def phonebook_menu():
    while True:
        print("""
        Phonebook
        1. Search
        2. Service Nos.
        3. Add name
        4. Erase
        5. Edit
        6. Assign tone
        7. Send b’card
        8. Options
        9. Speed dials
        10. Voice tags
        0. Back
        """)

        choice = int(input("Select a Phonebook option: "))

        if choice == 8:
            phonebook_options_menu()
        elif choice == 0:
            break
        else:
            print("Submenu not implemented yet.\n")


def phonebook_options_menu():
    while True:
        print("""
        Options
        1. Type of view
        2. Memory status
        3. Back
        4. Main menu
        """)

        choice = int(input("Choose an option: "))

        if choice == 3:
            break
        elif choice == 4:
            main_menu()
            return
        else:
            print("Option selected.\n")



def messages_menu():
    while True:
        print("""
        Messages
        1. Write Messages
        2. Inbox
        3. Outbox
        4. Picture Messages
        5. Templates
        6. Smileys
        7. Message Settings
        8. Info service
        9. Voice mailbox number
        10. Service command editor
        0. Back
        """)

        choice = int(input("Select an option: "))

        if choice == 7:
            message_settings_menu()
        elif choice == 0:
            break
        else:
            print("Submenu not implemented yet.\n")


def message_settings_menu():
    print("""
    Message Settings
    1. Set
    2. Common
    """)

    choice = int(input("Choose a Message Settings option: "))

    if choice == 1:
        print("""
        Set
        1. Message centre number
        2. Messages sent as
        3. Message validity
        """)
    elif choice == 2:
        print("""
        Common
        1. Delivery reports
        2. Reply via same centre
        3. Character support
        """)
    else:
        print("Invalid option.\n")



def call_register_menu():
    print("""
    Call Register
    1. Missed calls
    2. Received calls
    3. Dialled calls
    4. Erase recent call lists
    5. Show call duration
    6. Show call costs
    7. Call cost settings
    8. Prepaid credit
    """)

    choice = int(input("Select an option: "))

    if choice == 5:
        print("""
        Show Call Duration
        1. Last call duration
        2. All calls' duration
        3. Received calls' duration
        4. Dialled calls' duration
        5. Clear timers
        """)
    elif choice == 6:
        print("""
        Show Call Costs
        1. Last call cost
        2. All calls' cost
        3. Clear counters
        """)
    elif choice == 7:
        print("""
        Call Cost Settings
        1. Call cost limit
        2. Show costs in
        """)
    else:
        print("Submenu not implemented yet.\n")



def tones_menu():
    print("""
    Tones
    1. Ringing tone
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver
    """)


def settings_menu():
    print("""
    Settings
    1. Call settings
    2. Phone settings
    3. Security settings
    4. Restore factory settings
    """)

    choice = int(input("Choose a Settings option: "))

    if choice == 1:
        print("""
        Call Settings
        1. Automatic redial
        2. Speed dialling
        3. Call waiting options
        4. Own number sending
        5. Phone line in use
        6. Automatic answer
        """)
    elif choice == 2:
        print("""
        Phone Settings
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Lights
        6. Confirm SIM service actions
        """)
    elif choice == 3:
        print("""
        Security Settings
        1. PIN code request
        2. Call barring service
        3. Fixed dialling
        4. Closed user group
        5. Phone security
        6. Change access codes
        """)
    else:
        print("Invalid option.\n")



def clock_menu():
    print("""
    Clock
    1. Alarm clock
    2. Clock settings
    3. Date setting
    4. Stopwatch
    5. Countdown timer
    6. Auto update of date and time
    """)




