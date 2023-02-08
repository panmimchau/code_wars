x = ["Ryan", "Jimmy", "123", "4", "Cool Man"]

def friend(x):
    
    friend_list = []

    for i in x:
        if len(i) == 4:
            friend_list.append(i)
    
    return friend_list

friend(x)