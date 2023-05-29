from newsApi import news
from PIL import Image,ImageTk
from customtkinter import * 
import webbrowser

class Window(CTk):
    def __init__(self):
        super().__init__()
        CTk.resizable(self,width=False,height=False)
        self.iconbitmap("images\\news.ico")
        self.img=ImageTk.PhotoImage(Image.open("images\\breakingNews.jpg"))  # type: ignore
        self.width,self.height = self.img.width(),self.img.height()
        self.canvas1=CTkCanvas(width=self.width,height=self.height)
        self.canvas1.pack()
        self.canvas1.create_image((0,0),anchor=NW,image=self.img)
        self.title('News')
        self.eval("tk::PlaceWindow . center")
        def click(event):
            x=newWindow(event)
            return x

        button1_img= (Image.open("images\\euro.png"))  # type: ignore
        resized_button1_image= button1_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button1_image= CTkImage(resized_button1_image)
        self.button1=CTkButton(self,text="Economics",command=lambda: click("business"),width=10,height=10,cursor="hand2",image=new_button1_image,text_color="black",fg_color="red",bg_color="transparent",hover_color="#FFFF63") # type: ignore
        self.button1.image=new_button1_image  # type: ignore
        self.button1.place(relx=0.4,rely=0.1)

        button2_img= (Image.open("images\\entertainment.png"))  # type: ignore
        resized_button2_image= button2_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button2_image= CTkImage(resized_button2_image)
        self.button2=CTkButton(self,text="Entertainment",command=lambda: click("entertainment"),width=10,height=10,cursor="hand2",image=new_button2_image,text_color="black",fg_color="red",bg_color="transparent",hover_color="#FFFF63")
        self.button2.image=new_button2_image  # type: ignore
        self.button2.place(relx=0.4,rely=0.25)
        
        button3_img= (Image.open("images\\health.png"))  # type: ignore
        resized_button3_image= button3_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button3_image= CTkImage(resized_button3_image)
        self.button3=CTkButton(self,text="Health",command=lambda: click("health"),width=10,height=10,cursor="hand2",image=new_button3_image,text_color="black",fg_color="red",bg_color="transparent",hover_color="#FFFF63")
        self.button3.image=new_button3_image  # type: ignore
        self.button3.place(relx=0.4,rely=0.4)
        
        button4_img= (Image.open("images\\science.png"))  # type: ignore
        resized_button4_image= button4_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button4_image= CTkImage(resized_button4_image)
        self.button4=CTkButton(self,text="Science",command=lambda: click("science"),width=10,height=10,cursor="hand2",image=new_button4_image,text_color="black",fg_color="red",bg_color="transparent",hover_color="#FFFF63")
        self.button4.image=new_button4_image  # type: ignore
        self.button4.place(relx=0.4,rely=0.55)
        
        button5_img= (Image.open("images\\ball.png"))  # type: ignore
        resized_button5_image= button5_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button5_image= CTkImage(resized_button5_image)        
        self.button5=CTkButton(self,text="Sports",command=lambda: click("sports"),width=10,height=10,cursor="hand2",image=new_button5_image,text_color="black",fg_color="red",bg_color="transparent",hover_color="#FFFF63") 
        self.button5.image=new_button5_image   # type: ignore
        self.button5.place(relx=0.4,rely=0.7)
        
        button6_img= (Image.open("images\\technology.png"))  # type: ignore
        resized_button6_image= button6_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button6_image= CTkImage(resized_button6_image) 
        self.button6=CTkButton(self,text="Technology",command=lambda: click("technology"),width=10,height=10,cursor="hand2",image=new_button6_image,text_color="black",fg_color="red",bg_color="transparent",hover_color="#FFFF63")
        self.button6.image=new_button6_image  # type: ignore
        self.button6.place(relx=0.4,rely=0.85)

    def callback(self,url):
            webbrowser.open_new_tab(url)  
    
class newWindow():
    def __init__(self,category):
        self.category=category
        news.get_news(self.category,news.newsList)
        self._newWindow = CTkToplevel()
        self._newWindow.resizable(width=False,height=False)
        self._newWindow.title(f"{self.category.capitalize()} News")
        self.img=ImageTk.PhotoImage(Image.open(f"images\\{self.category}.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.canvas=CTkCanvas(self._newWindow,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        self._newWindow.lift()
        self._newWindow.attributes("-topmost",True)
        i=0
        k=0
        j=0
        self.button = []
        for x in news.tempList:
            self.button.append(CTkButton(self.canvas,hover_color="red",text=news.tempList[i],font=("Helvetica 12 bold",13),bg_color="transparent",text_color="black",fg_color="white",command=lambda k=k: a.callback(news.tempList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=W)
            i+=2
            k+=2
            j+=1
            if k ==20:
                break
        
a=Window()
a.mainloop()