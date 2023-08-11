def rythm(song):
    phrase=list(song.split(" "))
    a="а"
    a_list=[]
    flag=0
    for i in phrase:
        temp_a=0
        for j in range(len(i)):
            if i[j]=="а":
                temp_a+=1
        b=a_list.append(temp_a)
        if b!=a_list[0]:
            flag=1
    if flag==1:
        return "пам парам"
    else:
        return "парам пам-пам"
s=input("введите фразу: ")
print(rythm(s))

#
def print_operation_table(operation, num_rows=6, num_columns=6):
    for j in range(num_rows):

        columns=""
        for i in range(num_columns):
            columns+=str((i+1)*(j+1))
            columns+=" "
        print(columns)



print_operation_table(lambda x,y:x*y)