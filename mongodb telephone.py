from pymongo import MongoClient
client= MongoClient()

#creating database
db=client.telephone
#creating collection
Records=db.records

# introducing data
data=[{"name":'aditya','phone':'9999999999','place':'mum'},
      {"name":'sejal','phone':'8888888888','place':'blr'},
      {"name":'kaustubh','phone':'7777777777','place':'del'},
      {"name":'shubham','phone':'6666666666','place':'mum'},
      {"name":'akshay','phone':'5555555555','place':'blr'},
      {"name":'darshan','phone':'4444444444','place':'mum'}]


 Records.insert_many(data)
#make sure to comment previous line once you have inserted data or else data would be inserted again
query=int(input("\n1 to Find  \n2 to update \n3 to delete :\n"))
if query==1:
    # query to find records you just created.

    a = int(input("\n1 to Find by Name \n2 to Find by Phone Number \n3 to Find by Place: \n"))

    if a == 1:
        Name = input("enter a name to find: \n")
        query = {"name": Name}
        data = Records.find_one(query)
        print(data)
    elif a == 2:
        phone = input("enter a number to find: \n")
        query = {"phone": phone}
        data = Records.find_one(query)
        for i in data:
            print(i)
    elif a == 3:
        place = input("enter a place to find: \n")
        query = {"place": place}
        data = Records.find_one(query)
        for i in data:
            print(i)

    else:
        print("wrong Input")

elif query==2:
    # Modify the records, use the update_one() method. The update_one() method requires two arguments, query and update.

    b = int(input("\n1 to Mobify by Name \n2 to Mobify by Phone Number \n3 to Mobify by Place \n"))

    if b == 1:
        Name = input("\n enter the Search Name\n")
        query = {"name": Name}
        data = Records.find(query)
        for i in data:
            print(i)
        Input = input("\nenter new Name\n")
        modify = Records.update_one({"name": Name}, {"$set": {"name": Input}})

        print(modify.modified_count,"is updated")
    elif b == 2:
        Phone = input("\n enter the Search number\n")
        query = {"phone": Phone}
        data = Records.find(query)
        for i in data:
            print(i)
        Input = input("\nenter new number\n")
        modify = Records.update_one({"phone": Phone}, {"$set": {"phone": Input}})

        print(modify.modified_count,"is updated")
    elif b == 3:
        place = input("\n enter the Search Place\n")
        query = {"place": place}
        data = Records.find(query)
        for i in data:
            print(i)
        Input = input("\nenter new place\n")
        modify = Records.update_one({"place": place}, {"$set": {"place": Input}})

        print(modify.modified_count,"is updated")

    else:
        print("wrong Input")

elif query==3:
    # Delete the record, use delete_one() method. delete_one() requires a query parameter
    # which specifies the document to delete.

    c = int(input("\n1 to Delete by Name \n2 to Delete by Phone Number \n3 to Delete by Place \n"))

    if c == 1:
        Name = input("\n enter the  Name\n")
        query = {"name": Name}
        data = Records.find(query)
        for i in data:
            print(i)

        delet = Records.delete_one({"name": Name})
        print(delet.deleted_count,"is deleted")

    elif c == 2:
        Phone = input("\n enter the number\n")
        query = {"phone": Phone}
        data = Records.find(query)
        for i in data:
            print(i)
        delet = Records.delete_one({"phone": Phone})
        print(delet.deleted_count,"is deleted")
    elif c == 3:
        place = input("\n enter the Place\n")
        query = {"place": place}
        data = Records.find(query)
        for i in data:
            print(i)
        delet = Records.delete_one({"place": place})
        print(delet.deleted_count,"is deleted")
else:
    print("choose query correctly")
