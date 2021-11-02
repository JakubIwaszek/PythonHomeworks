correctPin = "0805"
insertedRightPin = False
maxTries = 3
tries = 0

while(insertedRightPin == False):
    pin = str(input("Enter the PIN code: "))
    if pin == correctPin:
        print("Success, You have inserted the right PIN code")
        break
    else:
        print("Incorrect")
        tries += 1
        if tries == maxTries:
            print("Sorry, your payment card has been blocked")
            break