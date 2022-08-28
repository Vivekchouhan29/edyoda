from admin_function import  foodfunction
from user_function import FoodFunction

print("choose 1 to login as a Admin")
print("choose 2 to login as a User")

num = int(input("select your choice :"))


if num ==1:
    class foodmain:

        def __init__(self,foodfunction_obj):
            self.foodfunction = foodfunction_obj

        def executed(self,choice):
            if choice == 1 :
                print("***ADD FOOD***")        
                self.foodfunction.add_food()

            if choice == 2 :
                print("***VIEW FOOD***")        
                self.foodfunction.view_food()

            if choice == 3 :
                print("***EDIT FOOD***")        
                self.foodfunction.edit_food()

            if choice == 4 :
                print("***REMOVE FOOD***")        
                self.foodfunction.remove_food()


    if __name__ =='__main__':
        foodfunction_obj = foodfunction()
        foodmain =  foodmain(foodfunction_obj)

        while True:
            print("Enter \n1.Add Food \n2.View Food \n3.Edit Food \n4.Remove Food")
            choice = int(input("enter your choice :"))
            foodmain.executed(choice)

elif num ==2:
    class Foodmain:

        def __init__(self,foodfunction_obj):
            self.foodfunction_obj = foodfunction_obj

        def execute(self,choice):
            if choice == 1:
                print("***********Registration***********")
                self.foodfunction_obj.registration()

            elif choice == 2:
                print("***********Log in the applicaation**********")
                self.foodfunction_obj.log_in()
                
            elif choice == 3:
                print("***********Update Your Profile**********")
                self.foodfunction_obj.update_profile()
            
            else:
                print("***Invalid Input***")

    if __name__ == "__main__":
        foodfunction_obj = FoodFunction()
        Foodmain = Foodmain(foodfunction_obj)                               

        while True:
            print("Enter \n1.Registration \n2.Log in the application \n3.Update Profile\n")
            choice = int(input("Enter your choice : "))
            Foodmain.execute(choice)

else:
    print("****TRY AGAIN****")