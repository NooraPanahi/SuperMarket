foodList = {"milk" : 10 , "chocolate" : 50 , "burger" : 35 , "tea" : 40 , "banana" : 25}
selectedFoodList = []
totalPrice = 0

for key,values in foodList.items():
    print(f"{key}, price : {values}")

try:
    while True:
        selectedFood = input("choose the food you want: ")
        if selectedFood in foodList:
            selectedFoodList.append(selectedFood)
            selectedFoodListPrice = foodList[selectedFood]
            totalPrice += selectedFoodListPrice
        else:
            print("not available!")
except KeyboardInterrupt as e:
    print(f"your list : {selectedFoodList} , {totalPrice} toman.")
    with open("List.txt" , "w") as file :
        file.write(f"your list : {selectedFoodList} , {totalPrice} toman.")
