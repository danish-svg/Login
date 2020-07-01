def log():
    with open('/home/danish/password/login.txt','a') as file:
        pass
    with open('/home/danish/password/login.txt','r') as file:
        holy = file.read()
    if holy:
        passWord = input("Hello boss.\nEnter your password please:")
        while passWord!=holy:
            print("Access Denied")
            print("Your password is incorrect.")
            again = input("Would you like to create a new password? (y/n) :")
            if again=='Y' or again=='y':
                super = input("Do you remember the superhero you like most in the starting?\nWhich superhero was that? :")
                with open('/home/danish/password/superHero.txt','r') as hero:
                    supero = hero.read()
                if super==supero:
                    print("You are saved !")
                    newPass = input("Enter your new password and don't forget to write it in a notebook :")
                    with open('/home/danish/password/login.txt','w') as file:
                        file.write(newPass)
                    print("Welcome Boss !")
                else:
                    print("Sorry I can't do anything now !")
                break
            else:
                print("OK Goodbye")
                break
    else:
        print("Hello Sir\nPlease write a strong password and make sure that you remember it :",end='')
        passw = input()
        with open('/home/danish/password/login.txt','a') as file:
            file.write(passw)
        superHero = input("Which superhero you like most :")
        with open('/home/danish/password/superHero.txt','a') as hero:
            hero.write(superHero)
        print("Your password is saved successfully.")

log()

