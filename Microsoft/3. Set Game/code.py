import numpy as np
n = int(input())
with open('data.txt') as f:
    ctr=0
    for line in f:
        ctr +=1
        line = line[:-1]
        s = line.split(" ")
        objects = [1,2,3]
        shading = ["E", "S", "F"]
        color = ["R", "P", "G"]
        shape = ["O", "S", "D"]
        for i in range(n):
            # print(i)
            # op = "Group " + str(i+1) + ": "
            op = ""
            objects = [1,2,3]
            shading = ["E", "S", "F"]
            color = ["R", "P", "G"]
            shape = ["O", "S", "D"]



            # DOES THE FIRST TASK
            first1 = s[0][0]
            second1 = s[1][0]
            if first1 == second1:
                op += first1
            else:
                # print(s)
                objects.remove(int(first1))
                objects.remove(int(second1))
                op += str(objects[0])




            # DOES THE SECOND TASK
            first2 = s[0][1]
            second2 = s[1][1]

            if first2 == second2:
                op += first2
            else:
                # print(first2)
                shading.remove(first2)
                shading.remove(second2)
                op += (shading[0])


            # DOES THE Third TASK
            first3 = s[0][2]
            second3 = s[1][2]

            if first3 == second3:
                op += first3
            else:
                # print(first2)
                color.remove(first3)
                color.remove(second3)
                op += (color[0])


            # DOES THE Fourth TASK
            first4 = s[0][3]
            second4 = s[1][3]

            if first4 == second4:
                op += first4
            else:
                # print(first2)
                shape.remove(first4)
                shape.remove(second4)
                op += (shape[0])


        print("Group " + str(ctr) + ": " + op)
