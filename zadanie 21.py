
userFileName = input("Enter file name")

with open(userFileName+".txt", "a") as file:
    file.write("Jakiś string \n")