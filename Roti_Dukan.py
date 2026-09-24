def roti_banao():
    """
    ye function roti banata hai or bill bhi return krta hai
    """
    print("Roti type:- lambi, moti, choti")
    roti_type = input("Enter your roti type:- ")
    how_much = int(input("kitni roti chahiye:- "))
    print("Thank you! Aapki Roti ban rhi hai")
    if roti_type == "lambi":
        price = 5
    else:
        price = 10
        
    total = price * how_much
    return total

bill = roti_banao()
print(f"Bill = {bill}Rs")
