from tkinter import *
import random
import time
from tkinter import filedialog,messagebox

root=Tk()
root.geometry('1485x750+0+0')
root.resizable(0,0)
root.config(bg='grey20')
root.title("restaurant managment system")
root.iconbitmap('restaurant.ico')
topframe=Frame(root,bd=10,relief=RIDGE,bg='grey11')
topframe.pack(side=TOP)
labeltitle=Label(topframe,text='Restaurant Management System',font=('lucida handwriting',30,'bold'),fg='gold',
                 bg='grey20',width=52,pady=10)
labeltitle.grid(row=0,column=0)
# all frames
#left sides frames
menuframe=Frame(root,bd=10,relief=RIDGE,bg="grey20")
menuframe.pack(side=LEFT)

costframe=Frame(menuframe,bd=5,relief=RIDGE,bg='grey20',pady=28)
costframe.pack(side=BOTTOM)

foodframe=LabelFrame(menuframe,text='Food',bd=10,relief=RIDGE,font=('lucida handwriting',18,'bold'),fg='gold',
bg='grey20')
foodframe.pack(side=LEFT)

drinkframe=LabelFrame(menuframe,text='Drinks',bd=10,relief=RIDGE,font=('lucida handwriting',18,'bold'),fg='gold',
                      bg='grey20')
drinkframe.pack(side=LEFT)

cakesframe=LabelFrame(menuframe,text='Cakes',bd=10,relief=RIDGE,font=('lucida handwriting',18,'bold'),fg='gold',
                      bg='grey20')
cakesframe.pack(side=LEFT)

#right side frames
rightframe=Frame(root,bd=10,relief=RIDGE,padx=64,bg='grey20')
rightframe.pack(side=RIGHT,pady=45)

calculatorframe=Frame(rightframe,bd=4,relief=RIDGE,bg='grey20')
calculatorframe.pack()

recieptframe=Frame(rightframe,relief=RIDGE,bd=4,bg='grey20')
recieptframe.pack()

buttonframe=Frame(rightframe,bd=4,relief=RIDGE,bg='grey20')
buttonframe.pack()
#all variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

#entry food
e_roti=StringVar()
e_daal=StringVar()
e_sabji=StringVar()
e_fish=StringVar()
e_kebab=StringVar()
e_chawal=StringVar()
e_mutton=StringVar()
e_panner=StringVar()
e_chicken=StringVar()

#entry drinks
e_lassi=StringVar()
e_coffe=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_jaljeera=StringVar()
e_roohafza=StringVar()
e_masalatea=StringVar()
e_badammilk=StringVar()
e_colddrink=StringVar()

#entry cakes
e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pineapple=StringVar()
e_chocolate=StringVar()
e_blackforest=StringVar()


costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
totalcostvar=StringVar()
gstvar=StringVar()
subtotalvar=StringVar()

# default set value

e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_panner.set('0')
e_chicken.set('0')

e_lassi.set('0')
e_coffe.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_roohafza.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_colddrink.set('0')

e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')
e_blackforest.set('0')

#food
roti=Checkbutton(foodframe,text='Roti',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var1,bg='grey20',fg='gold')
roti.grid(row=0,column=0,sticky=W)

sabji=Checkbutton(foodframe,text='Sabji',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var2,bg='grey20',fg='gold')
sabji.grid(row=1,column=0,sticky=W)

dall=Checkbutton(foodframe,text='Daal',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var3,bg='grey20',fg='gold')
dall.grid(row=2,column=0,sticky=W)

fish=Checkbutton(foodframe,text='Fish',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var4,bg='grey20',fg='gold')
fish.grid(row=3,column=0,sticky=W)

kebab=Checkbutton(foodframe,text='Kebab',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var5,bg='grey20',fg='gold')
kebab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodframe,text='Chawal',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var6
,bg='grey20',fg='gold')
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodframe,text='Mutton',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var7
,bg='grey20',fg='gold')
mutton.grid(row=6,column=0,sticky=W)

panner=Checkbutton(foodframe,text='Paneer',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var8
,bg='grey20',fg='gold')
panner.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodframe,text='Chicken',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var9
    ,bg='grey20',fg='gold')
chicken.grid(row=8,column=0,sticky=W)




#entry
textroti=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textsabji=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=1,column=1)

textdaal=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=2,column=1)

textfish=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_fish)
textfish.grid(row=3,column=1)

textkebab=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_kebab)
textkebab.grid(row=4,column=1)

textchawal=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_chawal)
textchawal.grid(row=5,column=1)

textmutton=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textpanner=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_panner)
textpanner.grid(row=7,column=1)

textchicken=Entry(foodframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=8,column=1)


#drinks
lassi=Checkbutton(drinkframe,text='Lassi',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var10,bg='grey20',fg='gold')
lassi.grid(row=0,column=0,sticky=W)

coffe=Checkbutton(drinkframe,text='Coffee',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var11,bg='grey20',fg='gold')
coffe.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinkframe,text='Faluda',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var12,
bg='grey20',fg='gold')
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinkframe,text='Shikanji',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var13,
            bg='grey20',fg='gold')
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinkframe,text='Jaljeera',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var14,
            bg='grey20',fg='gold')
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinkframe,text='Roohafza',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var15,
            bg='grey20',fg='gold')
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinkframe,text='Masala tea',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var16,
                bg='grey20',fg='gold')
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinkframe,text='Badam milk',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var17,
                bg='grey20',fg='gold')
badammilk.grid(row=7,column=0,sticky=W)

colddrink=Checkbutton(drinkframe,text='Cold drink',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var18,
                bg='grey20',fg='gold')
colddrink.grid(row=8,column=0,sticky=W)

#entry drinks

textlassi=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffe=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_coffe)
textcoffe.grid(row=1,column=1)

textfaluda=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2,column=1)

textshikanji=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=3,column=1)

textjaljeera=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=4,column=1)

textroohafza=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=5,column=1)

textmasalatea=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6,column=1)

textbadammilk=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=7,column=1)

textcolddrink=Entry(drinkframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_colddrink)
textcolddrink.grid(row=8,column=1)

#cakes

oreo=Checkbutton(cakesframe,text='Oreo',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var19,bg='grey20',fg='gold')
oreo.grid(row=0,column=0,sticky=W)

apple=Checkbutton(cakesframe,text='Apple',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var20,bg='grey20',fg='gold')
apple.grid(row=1,column=0,sticky=W)

kitkat=Checkbutton(cakesframe,text='Kitkat',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var21,
bg='grey20',fg='gold')
kitkat.grid(row=2,column=0,sticky=W)

vanilla=Checkbutton(cakesframe,text='Vanilla',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var22,
    bg='grey20',fg='gold')
vanilla.grid(row=3,column=0,sticky=W)

banana=Checkbutton(cakesframe,text='Banana',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var23,
bg='grey20',fg='gold')
banana.grid(row=4,column=0,sticky=W)

brownie=Checkbutton(cakesframe,text='Brownie',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var24,
    bg='grey20',fg='gold')
brownie.grid(row=5,column=0,sticky=W)

pineapple=Checkbutton(cakesframe,text='Pineapple',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var25,
                bg='grey20',fg='gold')
pineapple.grid(row=6,column=0,sticky=W)

chocolate=Checkbutton(cakesframe,text='Chocolate',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var26,
                bg='grey20',fg='gold')
chocolate.grid(row=7,column=0,sticky=W)

blackforest=Checkbutton(cakesframe,text='Blackforest',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,
                        variable=var27,bg='grey20',fg='gold')
blackforest.grid(row=8,column=0,sticky=W)

#entry cakes

textoreo=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textbrownie=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)

textpineapple=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textchocolate=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)

textblackforest=Entry(cakesframe,font=('universe',18,'bold'),bd=7,width=5,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)

#cost frame

labelcostoffood=Label(costframe,text='Cost Of Food',font=('universe',15,'bold'),bg='grey20',fg='gold')
labelcostoffood.grid(row=0,column=0)
textcostoffood=Entry(costframe,font=('universe',18,'bold'),bd=4,width=14,state='readonly',textvariable=costoffoodvar)
textcostoffood.grid(row=0,column=1,padx=27)

labelcostofdrinks=Label(costframe,text='Cost Of Drinks',font=('universe',15,'bold'),bg='grey20',fg='gold')
labelcostofdrinks.grid(row=1,column=0)
textcostofdrinks=Entry(costframe,font=('universe',18,'bold'),bd=4,width=14,state='readonly',textvariable=costofdrinksvar)
textcostofdrinks.grid(row=1,column=1,padx=27)

labelcostofcakes=Label(costframe,text='Cost Of Cakes',font=('universe',15,'bold'),bg='grey20',fg='gold')
labelcostofcakes.grid(row=2,column=0)
textcostofcakes=Entry(costframe,font=('universe',18,'bold'),bd=4,width=14,state='readonly',textvariable=costofcakesvar)
textcostofcakes.grid(row=2,column=1,padx=27)

labelsubtotal=Label(costframe,text='Sub Total',font=('universe',15,'bold'),bg='grey20',fg='gold')
labelsubtotal.grid(row=0,column=2)
textsubtotal=Entry(costframe,font=('universe',18,'bold'),bd=4,width=14,state='readonly',textvariable=subtotalvar)
textsubtotal.grid(row=0,column=3,padx=27)

labelgst=Label(costframe,text='GST',font=('universe',15,'bold'),bg='grey20',fg='gold')
labelgst.grid(row=1,column=2)
textgst=Entry(costframe,font=('universe',18,'bold'),bd=4,width=14,state='readonly',textvariable=gstvar)
textgst.grid(row=1,column=3,padx=27)

labeltotalcost=Label(costframe,text='Total Cost',font=('universe',15,'bold'),bg='grey20',fg='gold')
labeltotalcost.grid(row=2,column=2)
texttotalcost=Entry(costframe,font=('universe',18,'bold'),bd=4,width=14,state='readonly',textvariable=totalcostvar)
texttotalcost.grid(row=2,column=3,padx=27)

#buttons
buttontotal=Button(buttonframe,text='Total',font=('universe',14,'bold'),bd=3,fg='yellow',bg='grey20',padx=32,
                   )
buttontotal.grid(row=0,column=0)

buttonreceipt=Button(buttonframe,text='Receipt',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15,
                )
buttonreceipt.grid(row=0,column=1)

buttonsend=Button(buttonframe,text='Send',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15,
)
buttonsend.grid(row=0,column=2)

buttonsave=Button(buttonframe,text='Save',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15,
)
buttonsave.grid(row=0,column=3)

buttonreset=Button(buttonframe,text='Reset',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15
        )
buttonreset.grid(row=0,column=4)
#text area for receipt
textreceipt=Text(recieptframe,font=('universe',12,'bold'),bd=3,width=55,height=10)
textreceipt.grid(row=0,column=0)

#calculator
operator=''
def buttonclick(number):
    global operator
    operator=operator+number
    calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)
def clear():
    global operator
    calculatorfield.delete(0,END)
    operator=''
def ans():
    global operator
    result=str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0,result)
    operator=''

calculatorfield=Entry(calculatorframe,font=('universe',18,'bold'),width=40,bd=5)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorframe,text='7',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorframe,text='8',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorframe,text='9',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorframe,text='+',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                  command=lambda:buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorframe,text='4',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorframe,text='5',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorframe,text='6',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorframe,text='-',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                   command=lambda:buttonclick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calculatorframe,text='1',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorframe,text='2',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorframe,text='3',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
               command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonmul=Button(calculatorframe,text='*',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                 command=lambda:buttonclick('*'))
buttonmul.grid(row=3,column=3)

buttonans=Button(calculatorframe,text='Ans',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                 command=ans)
buttonans.grid(row=4,column=0)

buttonclear=Button(calculatorframe,text='Clear',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                   command=clear)
buttonclear.grid(row=4,column=1)

buttonzero=Button(calculatorframe,text='0',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                  command=lambda:buttonclick('0'))
buttonzero.grid(row=4,column=2)

buttondivison=Button(calculatorframe,text='/',bd=5,fg='gold',bg='grey20',font=('universe',16,'bold'),width=9,
                     command=lambda:buttonclick('/'))
buttondivison.grid(row=4,column=3)



root.mainloop()