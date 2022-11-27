from tkinter import*

yashgoyal_root = Tk()  #yhe ek basic gui creat kardeta h         #base hota h root  #yashgoyal el variable name h

yashgoyal_root.geometry("733x434")            #width x height

yashgoyal_root.minsize(200,100)             #width, height   yhe min size bata rha h

yashgoyal_root.maxsize(900,500)              #width, height   yhe max size bata rha h

yashgoyal_root = Label(text="YASH G is a Good YouTuber")     #variable name aap chahge kar sakte h (lable is not intracting with user)

yashgoyal_root.pack()                          #pack nhi kia tu yashgoyalg nhi milne wala GUI mai

yashgoyal_root.mainloop()  #yhe mainly aapko gui window mai rakhta h or intractive banata h or aapne jo gui la logic lagay tha usse yaad rakhta h
