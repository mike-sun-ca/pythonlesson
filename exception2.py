while True:
    try:
        myNumber= int(input("Give me an integer"))
    except Exception as e:
        print("There is something wrong", e)
    print(myNumber)
   