"""Lab 3: Regexes and reformatting."""

import re

# Eva Lynch

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
#######################################

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]

name = ""
location = ""
phone_number = ""

for contact in contacts:
    x = re.split(r",", contact)[0] # gets names (not formatted)
    name = re.split(r"\s", x)
    if len(name) == 2:
        name = name[1] + ", " + name[0] # formats
    else:
        name[1] = re.search(r"\w", name[1]).group() # gets rid of everything in middle name excpet first initial
        name = name[2] + ", " + name[0] + ", " + name[1] + "." # formats
    location = re.split(r",", contact)[2] # gets location
    phone_number = re.split(r",", contact)[1] # gets phone num (not formatted)
    phone_number = re.findall(r"\d", phone_number) # removes parenthesis and dashes
    if len(phone_number) > 10: # for numbers with the extra 1 at beginning
        phone_number[0] = ""
        phone_number = "(" + phone_number[1] + phone_number[2] + phone_number[3] + ") " + phone_number[4] + phone_number[5] + phone_number[6] + "-" + phone_number[7] + phone_number[8] + phone_number[9] + phone_number[10]
            else: # formatting, ^ and below
        phone_number = "(" + phone_number[0] + phone_number[1] + phone_number[2] + ") " + phone_number[3] + phone_number[4] + phone_number[5] + "-" + phone_number[6] + phone_number[7] + phone_number[8] + phone_number[9]

    print("Name: " + name + "\n" + "Location: " + location + "\n" + "Phone Number: " + phone_number + "\n")
    print("******************")
    print()







