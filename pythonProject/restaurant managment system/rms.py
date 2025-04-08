import smtplib
from tkinter import *
import random
import time
from tkinter import filedialog,messagebox






#functions

def reset():
    textreceipt.delete(1.0,END)
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

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textpanner.config(state=DISABLED)
    textchicken.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffe.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textcolddrink.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    gstvar.set('')
    totalcostvar.set('')


def send():
    def send_email():

        # Email details
            sender_email = 'chiragkapoor1711@gmail.com'
            sender_password = 'giricpygfvonvnzd'
            mail=mailentry.get()
            message=textarea.get(1.0,END)
            subject = 'Delicious Bite'


            # SMTP server details
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587

            # Create a secure SSL context
            context = smtplib.SMTP(smtp_server, smtp_port)
            context.starttls()

            # Login to the email account
            context.login(sender_email, sender_password)

            # Create the email message
            email_message = f"Subject: {subject}\n\n{message}"

            # Send the email
            context.sendmail(sender_email, mail, email_message)

            # Close the SMTP context
            context.quit()

   
    root2=Toplevel()
    root2.title('send bill')
    root2.iconbitmap('restaurant.ico')
    root2.config(bg='grey20')
    root2.geometry('485x620+50+50')
    maillabel=Label(root2,text="Enter mail",font=('universe',18,'bold'),bg='grey20',fg='gold')
    maillabel.pack(pady=3)
    mailentry=Entry(root2,font=('universe',16),border=3,width=25)
    mailentry.pack(pady=3)
    maillabel = Label(root2, text="Bill details", font=('universe', 18, 'bold'), bg='grey20', fg='gold')
    maillabel.pack(pady=3)
    textarea=Text(root2,font=('universe',12),border=3,height=15,width=35)
    textarea.pack(pady=3)
    send_button=Button(root2,font=('universe',18,'bold'),text="send",relief=GROOVE,bg='grey20',fg='gold',
                       command=send_email)
    send_button.pack(pady=3)
    textarea.insert(END,'receipt reff. \t\t'+billnumber+'\t'+date+'\n\n')
    if costoffoodvar.get() != '0':
        textarea.insert(END, f'Cost of food  \t\t\t {priceoffood}RS\n')
    if costofdrinksvar.get() != '0':
        textarea.insert(END, f'Cost of Drinks \t\t\t {priceofdrinks}RS\n')
    if costofcakesvar.get() != '0':
        textarea.insert(END, f'Cost of cakes \t\t\t {priceofcakes}RS\n')

    textarea.insert(END, f'sub total    \t\t\t {subtotalitems}RS\n')
    textarea.insert(END, f'GST       \t\t\t {gstamount}RS\n\n')
    textarea.insert(END, f'Total cost \t\t\t {totalcost}RS\n')

    root2.mainloop()

def save():
    if textreceipt.get(1.0,END) =='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textreceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('information','your bill is succesfully saved')
def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofcakesvar.get() !='' or costofdrinksvar.get() != '':
        textreceipt.delete(1.0,END)
        x=random.randint(100,1000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Bill reff..\t\t'+billnumber+'\t\t\t'+date+'\n')
        textreceipt.insert(END,'**********************************************************************************\n')
        textreceipt.insert(END,'ITEMS:\t\t\t COST OF ITEMS(RS)\n')
        textreceipt.insert(END, '**********************************************************************************\n')
        if e_roti.get()!='0':
            textreceipt.insert(END,f'Roti\t\t\t\t{ int(e_roti.get())*10}RS\n\n')
        if e_sabji.get()!='0':
            textreceipt.insert(END,f'Sabji\t\t\t\t{ int(e_sabji.get())*100}RS\n\n')
        if e_daal.get()!='0':
            textreceipt.insert(END,f'Daal\t\t\t\t{ int(e_daal.get())*80}RS\n\n')
        if e_fish.get()!='0':
            textreceipt.insert(END,f'Fish\t\t\t\t{ int(e_fish.get())*300}RS\n\n')
        if e_kebab.get()!='0':
            textreceipt.insert(END,f'Kebab\t\t\t\t{ int(e_kebab.get())*250}RS\n\n')
        if e_chawal.get()!='0':
            textreceipt.insert(END,f'Chawal\t\t\t\t{ int(e_chawal.get())*100}RS\n\n')
        if e_mutton.get()!='0':
            textreceipt.insert(END,f'Mutton\t\t\t\t{ int(e_mutton.get())*350}RS\n\n')
        if e_panner.get()!='0':
            textreceipt.insert(END,f'Panner\t\t\t\t{ int(e_panner.get())*200}RS\n\n')
        if e_chicken.get()!='0':
            textreceipt.insert(END,f'Chicken\t\t\t\t{ int(e_chicken.get())*250}RS\n\n')

        if e_lassi.get()!='0':
            textreceipt.insert(END,f'Lassi\t\t\t\t{ int(e_lassi.get())*50}RS\n\n')
        if e_coffe.get()!='0':
            textreceipt.insert(END,f'Coffe\t\t\t\t{ int(e_coffe.get())*70}RS\n\n')
        if e_faluda.get()!='0':
            textreceipt.insert(END,f'Faluda\t\t\t\t{ int(e_faluda.get())*60}RS\n\n')
        if e_shikanji.get()!='0':
            textreceipt.insert(END,f'Shikanji\t\t\t\t{ int(e_shikanji.get())*30}RS\n\n')
        if e_jaljeera.get()!='0':
            textreceipt.insert(END,f'Jaljeera\t\t\t\t{ int(e_jaljeera.get())*30}RS\n\n')
        if e_roohafza.get()!='0':
            textreceipt.insert(END,f'Roohafza\t\t\t\t{ int(e_roohafza.get())*30}RS\n\n')
        if e_masalatea.get()!='0':
            textreceipt.insert(END,f'Masalatea\t\t\t\t{ int(e_masalatea.get())*25}RS\n\n')
        if e_badammilk.get()!='0':
            textreceipt.insert(END,f'Badammilk\t\t\t\t{ int(e_badammilk.get())*50}RS\n\n')
        if e_colddrink.get()!='0':
            textreceipt.insert(END,f'Colddrink\t\t\t\t{ int(e_colddrink.get())*25}RS\n\n')

        if e_oreo.get()!='0':
            textreceipt.insert(END,f'Oreo\t\t\t\t{ int(e_oreo.get())*250}RS\n\n')
        if e_apple.get()!='0':
            textreceipt.insert(END,f'Apple\t\t\t\t{ int(e_apple.get())*200}RS\n\n')
        if e_kitkat.get()!='0':
            textreceipt.insert(END,f'Kitkat\t\t\t\t{ int(e_kitkat.get())*300}RS\n\n')
        if e_vanilla.get()!='0':
            textreceipt.insert(END,f'Vanilla\t\t\t\t{ int(e_vanilla.get())*150}RS\n\n')
        if e_banana.get()!='0':
            textreceipt.insert(END,f'Banana\t\t\t\t{ int(e_banana.get())*200}RS\n\n')
        if e_brownie.get()!='0':
            textreceipt.insert(END,f'Brownie\t\t\t\t{ int(e_brownie.get())*400}RS\n\n')
        if e_pineapple.get()!='0':
            textreceipt.insert(END,f'Pineapple\t\t\t\t{ int(e_pineapple.get())*180}RS\n\n')
        if e_chocolate.get()!='0':
            textreceipt.insert(END,f'Chocolate\t\t\t\t{ int(e_chocolate.get())*300}RS\n\n')
        if e_blackforest.get()!='0':
            textreceipt.insert(END,f'Blackforest\t\t\t\t{ int(e_blackforest.get())*500}RS\n\n')

        textreceipt.insert(END, '**********************************************************************************\n')
        if costoffoodvar.get()!='0':
            textreceipt.insert(END,f'Cost of Food \t\t\t\t {priceoffood}RS\n\n')
        if costofdrinksvar.get()!='0':
            textreceipt.insert(END,f'Cost of Drinks \t\t\t\t {priceofdrinks}RS\n\n')
        if costofcakesvar.get()!='0':
            textreceipt.insert(END,f'Cost of Cakes \t\t\t\t {priceofcakes}RS\n\n')

        textreceipt.insert(END,f'Sub Total \t\t\t\t {subtotalitems}RS\n\n')
        textreceipt.insert(END,f'GST \t\t\t\t {gstamount}RS\n\n')
        textreceipt.insert(END, '*********************************************************************************\n')
        textreceipt.insert(END,f'Total Cost \t\t\t\t {totalcost}RS\n\n,')
        textreceipt.insert(END, '*********************************************************************************\n')
    else:
        messagebox.showerror('Eror','No items is select')




def totalcost():
    global priceoffood, priceofdrinks ,priceofcakes,subtotalitems,gstamount,totalcost
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 \
       or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 \
       or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 \
       or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 \
       or var25.get() != 0 or var26.get() != 0 or var27.get() != 0:

        item1=int(e_roti.get())
        item2=int(e_sabji.get())
        item3=int(e_daal.get())
        item4 = int(e_fish.get())
        item5 = int(e_kebab.get())
        item6 = int(e_chawal.get())
        item7 = int(e_mutton.get())
        item8 = int(e_panner.get())
        item9 = int(e_chicken.get())

        item10 = int(e_lassi.get())
        item11 = int(e_coffe.get())
        item12 = int(e_faluda.get())
        item13 = int(e_shikanji.get())
        item14 = int(e_jaljeera.get())
        item15 = int(e_roohafza.get())
        item16 = int(e_masalatea.get())
        item17= int(e_badammilk.get())
        item18 = int(e_colddrink.get())

        item19 = int(e_oreo.get())
        item20 = int(e_apple.get())
        item21 = int(e_kitkat.get())
        item22 = int(e_vanilla.get())
        item23 = int(e_banana.get())
        item24 = int(e_brownie.get())
        item25= int(e_pineapple.get())
        item26= int(e_chocolate.get())
        item27= int(e_blackforest.get())

        priceoffood=(item1*10)+(item2*100)+(item3*80)+(item4*300)+(item5*250)+(item6*100)+(item7*350)+(item8*200)\
        +(item9*250)
        priceofdrinks=(item10*50)+(item11*70)+(item12*60)+(item13*30)+(item14*30)+(item15*30)+(item16*25)\
        +(item17*50)+(item18*25)
        priceofcakes=(item19*250)+(item20*200)+(item21*300)+(item22*150)+(item23*200)+(item24*400)+(item25*180)\
        +(item26*300)+(item27*500)
        costoffoodvar.set(str(priceoffood)+' RS')
        costofdrinksvar.set(str(priceofdrinks)+ ' RS')
        costofcakesvar.set(str(priceofcakes)+' RS')
        subtotalitems=priceoffood+priceofdrinks+priceofcakes
        subtotalvar.set(str(subtotalitems)+ ' RS')
        gstamount=subtotalitems*5/100
        gstvar.set(str(gstamount)+' RS')
        totalcost=subtotalitems+gstamount
        totalcostvar.set(str(totalcost)+' RS')
    else:
        messagebox.showerror('Error','No items is select ')

def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def sabji():
    if var2.get()==1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')

def daal():
    if var3.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')
def fish():
    if var4.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')
def kebab():
    if var5.get()==1:
        textkebab.config(state=NORMAL)
        textkebab.delete(0,END)
        textkebab.focus()
    else:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')
def chawal():
    if var6.get()==1:
        textchawal.config(state=NORMAL)
        textchawal.delete(0,END)
        textchawal.focus()
    else:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')
def mutton():
    if var7.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')

def panner():
    if var8.get()==1:
        textpanner.config(state=NORMAL)
        textpanner.delete(0,END)
        textpanner.focus()
    else:
        textpanner.config(state=DISABLED)
        e_panner.set('0')
def chicken():
    if var9.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')
def coffe():
    if var11.get()==1:
        textcoffe.config(state=NORMAL)
        textcoffe.delete(0,END)
        textcoffe.focus()
    else:
        textcoffe.config(state=DISABLED)
        e_coffe.set('0')
def faluda():
    if var12.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')
def shikanji():
    if var13.get()==1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')
def jaljeera():
    if var14.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')
def roohafza():
    if var15.get()==1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')
def masalatea():
    if var16.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')
def badammilk():
    if var17.get()==1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')
def colddrink():
    if var18.get()==1:
        textcolddrink.config(state=NORMAL)
        textcolddrink.delete(0,END)
        textcolddrink.focus()
    else:
        textcolddrink.config(state=DISABLED)
        e_colddrink.set('0')
def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')
def kitkat():
    if var21.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')
def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')
def banana():
    if var23.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')
def brownie():
    if var24.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')
def pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')
def chocolate():
    if var26.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')
def blackforest():
    if var27.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')
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
roti=Checkbutton(foodframe,text='Roti',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var1,
                 command=roti,bg='grey20',fg='gold')
roti.grid(row=0,column=0,sticky=W)

sabji=Checkbutton(foodframe,text='Sabji',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var2,
                  command=sabji,bg='grey20',fg='gold')
sabji.grid(row=1,column=0,sticky=W)

dall=Checkbutton(foodframe,text='Daal',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var3,
                 command=daal,bg='grey20',fg='gold')
dall.grid(row=2,column=0,sticky=W)

fish=Checkbutton(foodframe,text='Fish',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var4,
                 command=fish,bg='grey20',fg='gold')
fish.grid(row=3,column=0,sticky=W)

kebab=Checkbutton(foodframe,text='Kebab',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var5,
                  command=kebab,bg='grey20',fg='gold')
kebab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodframe,text='Chawal',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var6,
                   command=chawal,bg='grey20',fg='gold')
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodframe,text='Mutton',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var7,
                   command=mutton,bg='grey20',fg='gold')
mutton.grid(row=6,column=0,sticky=W)

panner=Checkbutton(foodframe,text='Paneer',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var8,
                   command=panner,bg='grey20',fg='gold')
panner.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodframe,text='Chicken',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var9,
                    command=chicken,bg='grey20',fg='gold')
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
lassi=Checkbutton(drinkframe,text='Lassi',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var10,
                  command=lassi,bg='grey20',fg='gold')
lassi.grid(row=0,column=0,sticky=W)

coffe=Checkbutton(drinkframe,text='Coffee',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var11,
                  command=coffe,bg='grey20',fg='gold')
coffe.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinkframe,text='Faluda',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var12,
                   command=faluda,bg='grey20',fg='gold')
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinkframe,text='Shikanji',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var13,
                     command=shikanji,bg='grey20',fg='gold')
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinkframe,text='Jaljeera',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var14,
                     command=jaljeera,bg='grey20',fg='gold')
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinkframe,text='Roohafza',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var15,
                     command=roohafza,bg='grey20',fg='gold')
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinkframe,text='Masala tea',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var16,
                      command=masalatea,bg='grey20',fg='gold')
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinkframe,text='Badam milk',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var17,
                      command=badammilk,bg='grey20',fg='gold')
badammilk.grid(row=7,column=0,sticky=W)

colddrink=Checkbutton(drinkframe,text='Cold drink',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var18,
                      command=colddrink,bg='grey20',fg='gold')
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

oreo=Checkbutton(cakesframe,text='Oreo',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var19,
                 command=oreo,bg='grey20',fg='gold')
oreo.grid(row=0,column=0,sticky=W)

apple=Checkbutton(cakesframe,text='Apple',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var20,
                  command=apple,bg='grey20',fg='gold')
apple.grid(row=1,column=0,sticky=W)

kitkat=Checkbutton(cakesframe,text='Kitkat',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var21,
                   command=kitkat,bg='grey20',fg='gold')
kitkat.grid(row=2,column=0,sticky=W)

vanilla=Checkbutton(cakesframe,text='Vanilla',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var22,
                    command=vanilla,bg='grey20',fg='gold')
vanilla.grid(row=3,column=0,sticky=W)

banana=Checkbutton(cakesframe,text='Banana',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var23,
                   command=banana,bg='grey20',fg='gold')
banana.grid(row=4,column=0,sticky=W)

brownie=Checkbutton(cakesframe,text='Brownie',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var24,
                    command=brownie,bg='grey20',fg='gold')
brownie.grid(row=5,column=0,sticky=W)

pineapple=Checkbutton(cakesframe,text='Pineapple',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var25,
                      command=pineapple,bg='grey20',fg='gold')
pineapple.grid(row=6,column=0,sticky=W)

chocolate=Checkbutton(cakesframe,text='Chocolate',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,variable=var26,
                      command=chocolate,bg='grey20',fg='gold')
chocolate.grid(row=7,column=0,sticky=W)

blackforest=Checkbutton(cakesframe,text='Blackforest',font=('universe' ,18,'bold'),offvalue=0,onvalue=1,
                        variable=var27,command=blackforest,bg='grey20',fg='gold')
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
                   command=totalcost)
buttontotal.grid(row=0,column=0)

buttonreceipt=Button(buttonframe,text='Receipt',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15,
                     command=receipt)
buttonreceipt.grid(row=0,column=1)

buttonsend=Button(buttonframe,text='Send',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15,
                  command=send)
buttonsend.grid(row=0,column=2)

buttonsave=Button(buttonframe,text='Save',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15,
                  command=save)
buttonsave.grid(row=0,column=3)

buttonreset=Button(buttonframe,text='Reset',font=('universe',14,'bold'),bd=3,fg='gold',bg='grey20',padx=15
                   ,command=reset)
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