def draw():
      print("|   *     | |       |      |       |       ")
      print("|*  *   | |       |      |       | ")
      print("|* * *| |        |     |       |  ")
      print('-------    -------    -------')
      print()
      print("|          | |        |     |       |       ")
      print("|  *  * ||         |     |       |        ")
      print("|* * *||         |     |  *   | ")
      print('-------    -------    -------')
      print()
      print("|          | |        |     |       |       ")
      print("|          | |        |     |       |       ")
      print("|* * *| | *  *|    |  *   |")
      print('-------    -------    -------')
      print()
      print("|          ||        |     |       |       ")
      print("|          ||  *   |     |        |    ")
      print("|* * *||*  *|     |        |    ")
      print('-------    -------    -------')
      print()
      print("|          | |        |     |         |      ")
      print("|          | |   *  |     |          |    ")
      print("|          | | *  *|     |* * *|")
      print('-------    -------    -------')
      print()
      print("|          | |        |     |           |       ")
      print("|          | |        |     |           |       ")
      print("|    *   | |*  * |     |* * *|")
      print('-------    -------    -------')
      print()
      print("|          | |        | |       |")
      print("|          | |        | | *  *|")
      print("|  *     | |        | |* * *|")
      print('-------    -------    -------')
      print()
      print("|          | |        | |     *  | ")
      print("|          | |        | | *  *  |")
      print("|          | |        | |* * *|")
      print('-------    -------    -------')



      


      
def byList(size,initial,final,helper):
      if size>0:
            byList(size-1, initial,helper, final)
            temp=initial[0].pop()
            print("Moved ",temp,", from bar",initial[1], "to bar",final[1], ".")
            final[0].append(temp)
            byList(size-1, helper,final,initial)
            
def useList(size):
      initial=[[],1]
      final=[[],2]
      helper=[[],3]
      for iterator in range(1,size+1):
            initial[0].append(iterator)
      initial[0]=initial[0][::-1]
      print()
      print("initial=",initial[0])
      print("final=",final[0])
      print("helper",helper[0])
      print()
      byList(size,initial,final,helper)
      print()
      print("initial=",initial[0])
      print("final",final[0])
      print("helper",helper[0])



      


class Stack:
      def __init__(self):
            self.stack=[]

      def push(self,dataval):
            self.stack.append(dataval)

      def printer(self):
            g=list()
            for i in  range(len(self.stack)):
                  g.append(self.stack[i])
            return g
      
      def length(self):
            return(len(self.stack))
            
      def top(self):
            return self.stack[-1]
      def pop(self):
            if len(self.stack)<=0:
                  return ("No element in the Stack")           
            else:
                  return self.stack.pop()
            
      def peek(self):
            return self.stack[0]
      
      def reverse(self):
            return self.stack[::-1]

initial=Stack()
final=Stack()
helper=Stack()
Bars=[0,initial,final,helper]

def move(n,a,b,c):
      if n>0:
            move (n-1,a,c,b)
            d=(Bars[a]).top()            
            (Bars[a]).pop()
            (Bars[b]).push(d)
            print ("I moved",d,", from bar ",a,"to bar",b)            
            move(n-1,c,b,a)
      
def byStack(n):
      List=[]
      for i in range(n):
            List.append(chr(65+i))            
      List=List[::-1]
      for j in List:
            (Bars[1]).push(j)
      print()
      for i in range(1,4):
            print(Bars[i].printer())
      print()
      move(n,1,2,3)
      print()
      for i in range(1,4):
            print(Bars[i].printer())













while True:
      print()
      print(" ___________________________________________________________")
      print(" |                                This is a python implimentation of                            |")
      print(" |                                          THE TOWER OF HANOI                                         |")
      print(" |                                                                                                                                 |")
      print(" |Which form do you like to use                                                                       |")
      print(" |     1.    Recursion using List                                                                              |")
      print(" |     2.  Recursion using Stack                                                                          |")
      print(" |     3.   To draw for 3                                                                                             |")
      print(" |     4.   To Exit                                                                                                       | ")
      try:
            command=eval(input(" | Give command:  "))            
            if command==4:
                  break
            print()
            if command!=3:
                  size=eval(input(" | Give size :  "))
            if command not in[1,2,3]:
                  print(" |     Invalid command!!          Give 1 or 2 or 3                                              |")
            elif size<1:
                  print(" |     Invalid size!!   give size greater than 0                                       |")
            elif command==1:
                  useList(size)
            elif command==2:
                  byStack(size)
            elif command==3:
                  draw()
            
      except:
            print(" |    Invalid character !!!                                                                                   | ")
      print(" ___________________________________________________________")
print(" ___________________________________________________________")       
