from create import create_student
from read import read_student
from update import update_student
from delete import delete_student


def inquiry():
    selection = input("Enter your selection c/r/u/d/e ")
    selection = selection.lower()

    def exit_message():
        print("Thank you. See you again !!")
    if selection == "c":
        create_student()
    elif selection == "r":
        read_student()
    elif selection == "u":
        update_student()
    elif selection == "d":
        delete_student()
    else:
        exit_message()


if __name__ == "__main__":
    inquiry()
