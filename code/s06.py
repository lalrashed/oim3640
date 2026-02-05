def draw_square(size):
    for i in range(size):
        #print('❤️' *size )
        for i in range (size):
            print('❤️' ,end="")

        print()

draw_square(2)

#copying in the function i wrote for exercise in ch 3
def triangle (string, int):
   for i in range (int+1): # needed to add one to not cut off level
      print (string*i)

triangle("😺",10)

# i wrote my method different from what was presented in class, 
# it makes more sense to me to add 1 to size in the range 
def back_triangle (string, int):
   for i in range (int+1): # needed to add one to not cut off level
      spaces=int-i
      print (" "*spaces + string*i)

back_triangle('A', 5)