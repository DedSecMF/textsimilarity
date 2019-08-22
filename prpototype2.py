#!/usr/bin/env python
# coding: utf-8

# In[16]:


from tkinter.filedialog import *
import tkinter.scrolledtext as tkst
from tkinter import filedialog
import nltk,string,numpy,math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from tkinter import messagebox

class notepad:
    #main window
    root = Tk()
    
    #objects required to form the text editor
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight() 
    textarea=tkst.ScrolledText( master = root  ,width=90, height = 30)
    textarea1=tkst.ScrolledText( master = root  ,width=90, height = 30)
    textarea2=tkst.ScrolledText( master = root  ,width=90, height = 10)
    textarea3=tkst.ScrolledText( master = root  ,width=70, height = 10)
    mainmenu = Menu(master=root)
    filemenu = Menu(master=mainmenu,tearoff=0)
    editmenu = Menu(master=mainmenu,tearoff=0)
    thememenu = Menu(master=mainmenu,tearoff=0)
    helpmenu = Menu(master=mainmenu,tearoff=0)
    filemenu1 = Menu(master=mainmenu,tearoff=0)
    editmenu1 = Menu(master=mainmenu,tearoff=0)
    thememenu1 = Menu(master=mainmenu,tearoff=0)
    helpmenu1 = Menu(master=mainmenu,tearoff=0)    
    blankmenu = Menu(mainmenu, tearoff=0)
    cfile = None
    dirt = None
    doc=[]
    def __init__(self):
        # Set icon 
        try: 
                self.root.wm_iconbitmap("icon.png")  
        except: 
                pass
        # Set the window text 
        self.root.title("Untitled - Notepad") 
  
        # Center the window 
        screenWidth = self.root.winfo_screenwidth() 
        screenHeight = self.root.winfo_screenheight() 
        
        # For left-alling 
        left = 0
          
        # For right-allign 
        top = 0
          
        # For top and bottom 
        self.root.geometry('%dx%d+%d+%d' %(self.screenWidth,self.screenHeight,left, top))  
  
        # To make the textarea auto resizable  
  
        # Add controls (widget) 
        self.textarea.place(x=15,y=15)
        self.textarea1.place(x=775,y=15)
        self.textarea2.place(x=15,y=550)
        self.textarea3.place(x=900,y=550)

        #Adding menu items(file menu)
        self.filemenu.add_command(label="New",command=self.newfile)
        
        self.filemenu.add_command(label="Open",command=self.openfile)
        
        self.filemenu.add_command(label="Save",command=self.savefile)
        
        self.filemenu.add_command(label="Save as",command=self.saveasfile)
        
        self.filemenu.add_separator()
        
        self.filemenu.add_command(label="Exit",command=self.exitfile)
        
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)

        #Adding menu items(edit menu)
        self.editmenu.add_command(label="Cut",command=self.cut)
        
        self.editmenu.add_command(label="Copy",command=self.copy)
        
        self.editmenu.add_command(label="Paste",command=self.paste)
        
        self.mainmenu.add_cascade(label="Edit",menu=self.editmenu)

        #Adding help menu
        self.thememenu.add_command(label="Red",command=self.red)

        self.thememenu.add_command(label="Yellow",command=self.yellow)

        self.thememenu.add_command(label="White",command=self.white)
        
        self.mainmenu.add_cascade(label="Themes",menu=self.thememenu)

        #Adding help menu
        self.helpmenu.add_command(label="About",command=self.about)
        
        self.mainmenu.add_cascade(label="Help",menu=self.helpmenu)
        #copied menubuton
        
        self.mainmenu.add_cascade(label="".ljust(200), menu=self.blankmenu)
        
        self.filemenu1.add_command(label="Open Text",command=self.opentxt1)
        self.filemenu1.add_separator()
        
        self.filemenu1.add_command(label="Open Folder",command=self.openfile1)
        self.filemenu1.add_separator()
        
        self.filemenu1.add_command(label="Open Zip",command=self.openzip1)


        
        self.mainmenu.add_cascade(label="File",menu=self.filemenu1)

        
        #place in on the obj
        self.root.config(menu=self.mainmenu)
        l1=Label(master=self.root,text="SIMILARITY INDEX")
        l1.place(x=775,y=550) 


    #file menu
    
    def newfile(self):
        self.root.title("Untitled-Notepad")
        self.cfile=None
        self.textarea.delete(1.0,END)
                 
    def openfile(self):
        self.cfile=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
        if self.cfile=="":
            self.cfile=None
        else:
            self.root.title(os.path.basename(self.cfile) +"-Notepad")
            self.textarea.delete(1.0,END)
            self.doc=[]
            self.textarea1.delete(1.0,END)
            fptr=open(self.cfile,"r")
            self.textarea.insert(1.0,fptr.read())
            self.doc.append(self.cfile)
            fptr.close()
        
    def savefile(self):
        if self.cfile!=None:
            fptr=open(self.cfile,"w")
            fptr.write(self.textarea.get(1.0,END))
            self.doc[0]=self.cfile
            fptr.close()
        else:
            self.saveasfile()
        
    def saveasfile(self):
        if self.cfile=="":
            self.cfile=None
        else:    
            self.cfile=asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            file=open(self.cfile,"w")
            file.write(self.textarea.get(1.0,END))
            self.doc[0]=self.cfile
            file.close()
            self.root.title(os.path.basename(self.cfile) +"- Notepad")
            
    def exitfile(self):
            self.root.destroy()
    #edit menu
    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    #themes
    def red(self):
        self.textarea.config(background='red')
    def yellow(self):
        self.textarea.config(background='yellow')
    def white(self):
        self.textarea.config(background='white')
        
    #textbar2
    def opentxt1(self):
        self.cfile1=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
        if self.cfile1=="":
            self.cfile1=None
        else:
            self.root.title(os.path.basename(self.cfile1) +"-Notepad")
            self.textarea1.delete(1.0,END)
            fptr=open(self.cfile1,"r")
            for i in range(1,len(self.doc)):
                self.doc.pop()    
            self.textarea1.insert(1.0,fptr.read())
            self.doc.append(self.cfile1)
            fptr.close()
            
    def openfile1(self):
        self.dirt=filedialog.askdirectory()
        self.textarea1.delete(1.0,END)
        arr=os.listdir(self.dirt)
        for i in range(1,len(self.doc)):
                self.doc.pop()  
        for i in arr:
            st=str(self.dirt)+"/"+i
            self.textarea1.insert(1.0,i+"\n")
            self.doc.append(st)

    def openzip1(self):
        pass
            
   
    #about
    def about(self):
        showinfo("NOTEPAD","hurrah-bebe rexha")

    #cosine function
    
    #for running mainloop  
    def run(self):
        self.root.mainloop()  

np=notepad()

def ptoline(fptr):
    try:
        f = open(fptr, 'r')
        lines = f.readlines()
        mystr = ' '.join([line.strip() for line in lines])
        return mystr
    except:
        messagebox.showinfo("ERROR", "Enter Only files not Folders")
        

lemmer = nltk.stem.WordNetLemmatizer()

def get_key(val,arr): 
    for key, value in arr.items(): 
        if val == value: 
            return key

def nontrival(txt1,txt2,arr):
    ref=[x + y for x, y in zip(txt1,txt2)]
    string=[]
    for i in range(len(ref)):
        if(i>100):
            break
        if(ref[i]<2):
            continue
        else:
            string.append(str(""+get_key(i,arr)+" : "+str(ref[i])))
    np.textarea2.insert(1.0,string)
        
        
        
        
def LemTokens(tokens):
     return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    
def cosine(vect1,vect2):
    num=0
    den1=0
    den2=0
    for i in range(len(vect1)):
        num=num+vect1[i]*vect2[i]
        den1+=vect1[i]*vect1[i]
        den2+=vect2[i]*vect2[i]
    cos=num/(math.sqrt(den1)*math.sqrt(den2))    
    return(cos)
    

def cl():
    np.textarea2.delete(1.0,END)
    documents=[ptoline(i) for i in np.doc]
    print(" ")
    LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
    LemVectorizer.fit_transform(documents)
    print("")
    print (LemVectorizer.vocabulary_)
    print("")
    cosine_matrix=tf_matrix = LemVectorizer.transform(documents).toarray()
    tf_matrix.shape
    if(len(tf_matrix)==2):
        nontrival(tf_matrix[0],tf_matrix[1],LemVectorizer.vocabulary_)
    elif(len(tf_matrix>=3)):
        for i in range(1,len(tf_matrix)):
            nontrival(tf_matrix[0],tf_matrix[i],LemVectorizer.vocabulary_)
            

    tfidfTran = TfidfTransformer(norm="l2")
    tfidfTran.fit(tf_matrix)
    print("")
    tfidf_matrix = tfidfTran.transform(tf_matrix)
    cos_similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()
    print (cos_similarity_matrix)
    
    if(len(cos_similarity_matrix)==2):
        np.textarea3.delete(1.0,END)
        np.textarea3.insert(1.0,cos_similarity_matrix[0][1])
    else:
        np.textarea3.delete(1.0,END)
        np.textarea3.insert(1.0,cos_similarity_matrix)

    return tf_matrix
def c2():
    np.textarea2.delete(1.0,END)
    cosine_matrix=cl()
    print(cosine_matrix)
    
    cosine_mat=[[cosine(i,j) for j in cosine_matrix] for i in cosine_matrix]
    print(cosine_mat)
    
    if(len(cosine_mat)==2):

        np.textarea3.delete(1.0,END)
        np.textarea3.insert(1.0,cosine_mat[0][1])
        
    else:
        
        np.textarea3.insert(1.0,cosine_mat)
       
        

    
button=Button(np.root,text="click tdif",command=cl)
button.place(x=775,y=600)


button1=Button(np.root,text="click cos",command=c2)
button1.place(x=775,y=650)
np.run()
    


# In[ ]:





# In[ ]:




