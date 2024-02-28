"""_summary_
    Group Members: Syed Ali Mustafa Wasti, Youssef Marrak
    Date: 05/02/2024
    Manifesto: This program is designed to convert currency based on user input.
"""

global Euros #We made these into a global variable so that we do not need to keep defining them everywhere.
global Pounds
global Dollars

Euros = 0.251075 #Constant for Euro
Pounds = 0.214637 #Constant for British Pounds
Dollars = 0.272257 #Constant for US Dollar

def AED_Euro(money): #Defining the function AED_Euro.
    ans = money * Euros #The calculation for the currency conversion of AED to Euros.
    print(money, "AED is equal to", ans, "Euros") #Printing the results of the conversion.
        
def AED_BPound(money): #Defining the function AED_BPound.
    ans = money * Pounds #The calculation for the currency conversion of AED to British Pounds.
    print(money, "AED is equal to", ans, "British Pounds") #Printing the results of the conversion.
    
def AED_USDollar(money): #Defining the function AED_USDollar.
    ans = money * Dollars #The calculation for the currency conversion of AED to US Dollars.
    print(money, "AED is equal to", ans, "USD") #Printing the results of the conversion.

def Euro_AED(amount): #Defining the function Euro_AED.
    ans = amount / Euros #The calculation for the currency conversion of Euros to AED.
    print(amount, "Euros are equal to", ans, "AED") #Printing the results of the conversion.

def BPound_AED(amount): #Defining the function BPound_AED.
    ans = amount / Pounds #The calculation for the currency conversion of British Pounds to AED.
    print(amount,"British Pounds are equal to", ans, "AED") #Printing the results of the conversion.

def USDollar_AED(amount): #Defining the function USDollar_AED.
    ans = amount / Dollars #The calculation for the currency conversion of US Dollars to AED.
    print(amount,"USD is equal to", ans, "AED") #Printing the results of the conversion.

def main(): #Defining the main function
    print("Main Menu") #Making the UI for the Main Menu
    print("Welcome to Currency Convertor")
    print("---------------------------------------------------------------------------------------------")
    
    while True: #while True makes it so that the code within the loop will keep getting looped till the code is broken using the "break" function
    
        print("Select the conversion direction: \n1. AED to other currencies \n2. Other currencies to AED \n3. Exit") #Printing options for conversion direction.
        
        amount = float(input("Enter your amount you want to convert: ")) #Taking input for the amount to convert
        
        if amount < 0: #This statement makes it so that the user cannot input an amount less than 0
            print("Amount can not be less than 0.")
            break
        
        choice = int(input("Enter your choice (1/2/3): ")) #Taking input for choice of conversion direction
        
        if choice == 1: #If the choice is 1 which is AED to other currencies
            
            print("1. AED to Euro (EUR)\n2. AED to British Pound (GBP)\n3. AED to US Dollar\n4. Exit") #Printing options for which currency to convert to
            choice2 = int(input("Enter the choice of currency (1/2/3/4): ")) #Taking input for choice of currency to convert to
            
            if choice2 == 1: #If choice is 1 for choice of currency
                
                AED_Euro(amount) #Runs the AED_Euro() function
                
            elif choice2 == 2: #If choice is 2 for choice of currency
            
                AED_BPound(amount) #Runs the AED_BPound() function
                
            elif choice2 == 3: #If choice is 3 for choice of currency
            
                AED_USDollar(amount) #Runs the AED_USDollar() function
                
            elif choice2 == 4: #If choice is 4 for choice of currency
                
                break #Exits the loop
            
            else:
                
                print("You have entered an invalid choice.") #If the user inputs another choice
        
        elif choice == 2: #If the choice is 2 which is other currencies to AED
            
            print("1. Euro to AED (EUR)\n2. British pound to AED (GBP)\n3. US Dollar to AED\n4. Exit") #Printing options for which currency to convert from
            choice2 = int(input("Enter the choice of currency (1/2/3/4): ")) #Taking input for choice of currency to convert from
            
            if choice2 == 1: #If choice is 1 for choice of currency
                
                Euro_AED(amount) #Runs the Euro_AED() function
                
            elif choice2 == 2: #If choice is 2 for choice of currency
            
                BPound_AED(amount) #Runs the BPound_AED() function
                
            elif choice2 == 3: #If choice is 3 for choice of currency
            
                USDollar_AED(amount) #Runs the USDollar_AED() function
                
            elif choice2 == 4: #If choice is 4 for choice of currency
                
                break #Exits the loop
            
            else:
                
                print("You have entered an invalid choice.") #If the user inputs another choice
                
        elif choice == 3: #If choice is 3 which is exiting the menu
            
            break #Exits the loop
            
        else:
            
            print("You have entered an invalid choice.") #If the user inputs another choice
        
        run = input("Do you want to continue? (y/n): ") #Taking input if the user wants to run the program again
            
        print("---------------------------------------------------------------------------------------------")
        
        if run == "n": #If the user input is "n" then the program exits using the "break" function

            print("Exiting the program.") #Tells the user that the program in ending
            
            break #Exits the loop

if __name__ == "__main__": #Used if the main() function has a different name other than main
    main()