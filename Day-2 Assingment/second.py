def addElement():
    arr=[]
    while True:
        num = input("Enter your element or press X : ")

        if num == 'x' or num =='X':
            break

        arr.append(num)
        print(f"Updated array {arr}")
    print(arr)

addElement()
        
