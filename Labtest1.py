#Function to use Pascal's Formula
def make_new_row(old_row, limit):
    new_row = []
    new_list = []
    L=[]
    i=0

    new_row = old_row[:]
    while i < limit:
        new_row.append(1)
        long = len(new_row) - 1
        j=0
        h=0
        if i ==0:
            new_list = new_row[:]
            #Print list of lists
            print("Printing list of lists, one list at a time: ")
            print(old_row)

        #Formula for Pascal Triangle
        for j in range(new_row[0], long):
            new_row[j]= new_list[h] + new_list[h+1]
            j = j+1
            h = h+1
        new_list = new_row[:]

        #Printing lists
        print(new_row)

        #Adding list into whole lists
        L.append(new_row)
        i=i+1
    print("Print whole list of lists: ")
    print(L)


#Asking user for height of triangle
ans = input("Enter the desired height of Pascal's triangle: ")
lim = int(ans)
old_row = [1,1]

#Sending the row and limit to the function
make_new_row(old_row, lim)
