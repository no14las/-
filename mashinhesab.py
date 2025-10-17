opmojaz=['+','-','*','/']
#a simpel calculatro from no14
print("welcom to calculator")
#the baner
def mashinhesab():
    print(r'''
         .-"      "-.
       .'              '.
      /   O        O     \
     :           ⏳        :
     |     \______/      |
     :     /      \      :
      \   \      /     /
       '.  '----'   .'
         '-.____.-'

         /    |    \
        /     |     \
       /______|______\
             / \
            /   \
           /     \

        ( mashinhesab )
    ''')

mashinhesab()
#end of baner
print("lotfa add awal ra vared konid")
#get nub from user
numb1=input()
print("==============================")
print("add dovom")
#get nub2 from user
numb2=input()
print("lotfa amliyat moprd nazar ra entekhab konid")
#get op from user
#taein vorodi hay mojas

while True :
  op=input("")
  if op in opmojaz:
      break
  print("lotfa dorost vared konid faghat mitonid az - + / * estefade konid")  
print("JAVAB SHOMA HAST")
#input  str hast  tabdil be exampel int(ex)+int(ex)
if op == '+' :
      result = int(numb1) + int(numb2)
elif op == '*':
    result = int(numb1) * int(numb2)
elif op == '-':
     result = int(numb1) - int(numb2)
elif op == '/' :
    result = int (numb1) / int(numb2)
print("/////==================================///////////////")
print(f"{numb1}{op}{numb2} = {result}")
print("/////==================================///////////////")
