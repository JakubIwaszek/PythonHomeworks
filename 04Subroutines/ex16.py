def month(monthNumber):
    if monthNumber < 1 or monthNumber > 12:
        return "Wrong month number"
    else:
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return months[monthNumber - 1]
    
print(month(7))