def doYouWantoPlay():
    print("Welcome to the Lemonade Game!")
    response = input("Do you want to play a game?, (y/n) ").lower()
    while response not in ['y', 'n']:
        print("Please enter 'y' for yes or 'n' for no.")
        response = input("Do you want to play a game?, (y/n) ").lower()
    return response == 'y'

def showRules():
    print("The rules are simple:")
    print("1. You need to sell as much Lemonade as possible.")
    print("2. Each day You can do lemonade, sell lemonade or close the stand.")

def calculateWeather():
     import random
     weatherConditions = ['Sunny', 'Cloudy', 'Rainy', 'Windy']
     weather = random.choice(weatherConditions)
     lemonadeCost = random.randint(1, 10)
     temperature = random.randint(50, 100)
     return weather, lemonadeCost, temperature

def show_forecast(weather, temp, cost):
    print(f"Today's weather is {weather} with a temperature of {temp}°F.")
    print(f"The cost of lemons today is ${cost} per lemon.")

def mainMenu():
    print("Main Menu:")
    print("1. Make Lemonade")
    print("2. Sell Lemonade")
    print("3. Close Stand")
    print("4. Weather Forecast")
    print("5. Show Rules")
    print("6. Exit Game")

def getUserChoice():
    choice = input("Please enter your choice (1-6): ")
    while choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please enter a number between 1 and 6.")
        choice = input("Please enter your choice (1-6): ")
    return int(choice)

def makeLemonade(lemonadeCost):
    lemonsMade = int(input("How many glasses of lemonade would you like to make? "))
    glassCost = lemonadeCost * 0.5
    totalCost = lemonsMade * glassCost
    print(f"The total cost to make {lemonsMade} glasses of lemonade is ${totalCost:.2f}.")
    print(f"You have made {lemonsMade} glasses of lemonade.")
    return lemonsMade, totalCost

def sellLemonade(lemonsMade):
    if lemonsMade <= 0:
        print("You don't have any lemonade to sell!")
        return 0
    glassesSold = int(input("How many glasses of lemonade would you like to sell? "))
    if glassesSold > lemonsMade:
        print("You cannot sell more glasses than you have made.")
        glassesSold = lemonsMade
    pricePerGlass = float(input("Enter price per glass: "))
    if pricePerGlass > 1:
        pricePerGlass = 1
    totalRevenue = glassesSold * pricePerGlass
    print(f"You sold {glassesSold} glasses of lemonade for a total of ${totalRevenue:.2f}.")
    return totalRevenue

def closeStand(totalRevenue):
    print(f"Closing the stand for the day. You made a total of ${totalRevenue:.2f} today.")


def playGame():
    playing = doYouWantoPlay()
    if not playing:
        print("Maybe next time!")
        return

    showRules()
    weather, lemonadeCost, temperature = calculateWeather()
    show_forecast(weather, temperature, lemonadeCost)

    cash = 50
    lemonsMade = 0
    totalRevenue = 0

    while True:
        mainMenu()
        choice = getUserChoice()

        if choice == 1:
            lemonsMade, cost = makeLemonade(lemonadeCost)
            cash -= cost
        elif choice == 2:
            revenue = sellLemonade(lemonsMade)
            totalRevenue += revenue
            cash += revenue
        elif choice == 3:
            closeStand(totalRevenue)
            break
        elif choice == 4:
            show_forecast(weather, temperature, lemonadeCost)
        elif choice == 5:
            showRules()
        elif choice == 6:
            print("Exiting the game. Thank you for playing!")
            break

    print(f"\nGame Over! Final cash balance: ${cash:.2f}")

playGame()
