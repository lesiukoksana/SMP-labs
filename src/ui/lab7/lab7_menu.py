import requests
import json
import csv
import re
import unittest
from termcolor import colored

from src.bll.classes.lab7.Application import Application

def show_menu():
    print(colored("Welcome to the Cat Facts App", "cyan"))
    print("1. View Cat Facts (Table)")
    print("2. View Cat Facts (List)")
    print("3. Save Data (JSON)")
    print("4. Save Data (CSV)")
    print("5. Save Data (TXT)")
    print("6. View Query History")
    print("7. Exit")

def main():
    app = Application()

    while True:
        show_menu()
        choice = input("Please select an option (1-7): ")

        match choice:
            case "1":
                app.fetch_and_display_data("table")
            case "2":
                app.fetch_and_display_data("list")
            case "3":
                data = app.api_client.fetch_data()
                app.save_data(data, "json")
            case "4":
                data = app.api_client.fetch_data()
                app.save_data(data, "csv")
            case "5":
                data = app.api_client.fetch_data()
                app.save_data(data, "txt")
            case "6":
                app.show_history()
            case "7":
                print(colored("Goodbye!", "magenta"))
                break
            case _:
                print(colored("Invalid choice, please try again.", "red"))


if __name__ == "__main__":
    main()
