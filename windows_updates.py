from typing import Tuple
from sys import platform
import win32com.client
import re

#it is not perfect, microsoft has changed their coding system for updates, and it can not catch them all.
def scan_for_windows_updates() -> Tuple[dict, dict]:

    #checks platform
    if platform == "linux" or platform == "linux2":
        print("This is a linux computer, this function is only available for Windows machines.")
        return {}, {}
    elif platform == "darwin":
        print("This is a mac computer, this function is only available for Windows machines.")
        return {}, {}
 
        
    w_client = win32com.client.Dispatch("Microsoft.Update.Session")
    update_searcher = w_client.CreateUpdateSearcher()


    # Search for installed softwares from windows.
    search_installed = update_searcher.Search("IsInstalled=1 and Type='Software'")
    #updates_installed = win32com.client.Dispatch("Microsoft.Update.UpdateColl")


    print("\nListing installed Updates...\n")
    installed_updates = []
    new_updates = []

    installed_categories = []
    new_categories = []

    installed_dict = {}
    new_dict = {}


    # regex for windows codes.
    updates_pattern = re.compile(r'KB+\d+')


    for i in range(len(search_installed.Updates)):

        # saves updates names
        installed = search_installed.Updates.Item(i)

        for j in range(len(installed.Categories)):

            # gets windows update code
            update_code = updates_pattern.findall(str(installed))

            # saves installed updates names
            category = installed.Categories.Item(j).Name
            print("[*] Name: " + str(installed) + " - " +
                  "url: " + "https://support.microsoft.com/en-us/kb/{}".format(
                "".join(update_code).strip("KB")) + " - " +
                  "Category: " + category)
            installed_updates.append(str(installed))
            installed_categories.append(category)


    # converts list to tuple
    installed_hashable = tuple(installed_updates)
    installed_hashable_category = tuple(installed_categories)


    # creates dictionary
    for update in installed_hashable:
        for category_update in installed_hashable_category:
            installed_dict[category_update] = str(update)

    # Searches aupdates not installed
    search_available = update_searcher.Search("IsInstalled=0 and Type='Software'")
    updates_available = win32com.client.Dispatch("Microsoft.Update.UpdateColl")

    print("\nListing Updates not installed...\n")
    for i in range(len(search_available.Updates)):
        update_available = search_available.Updates.Item(i)

        for j in range(len(updates_available.Categories)):

            # extracts Update code.
            update_code = updates_pattern.findall(str(update_available))


            # saves installed categories names
            category = updates_available.Categories.Item(j).Name
            print("[*] Name: " + str(update_available) + " - " +
                  "url: " + "https://support.microsoft.com/en-us/kb/{}".format(
                "".join(update_code).strip("KB")) + " - " +
                  "Category: " + category)
            new_updates.append(str(update_available))
            new_categories.append(category)


    # converts lists to tuples
    available_hashable = tuple(new_updates)
    available_hashable_category = tuple(new_categories)

    # creates dictionary
    for update in available_hashable:
        for category_update in available_hashable_category:
            new_dict[category_update] = str(update)

    
    print("\nGoing back to main menu.\n")

    return installed_dict, new_dict


