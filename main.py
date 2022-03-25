try:
    from PyInstaller.utils.hooks import collect_submodules
    import tkinter  as tk
    from tkinter import *
    from tkinter import  ttk,filedialog , scrolledtext
    from tkinter.filedialog import askopenfilenames , askdirectory ,asksaveasfile
    from PIL import Image , ImageTk
    import datetime  , os , pygame , sys  ,time  , subprocess  , socket , qrcode , webbrowser , requests ,ipaddress ,ftplib , ctypes
except ImportError:
    print('ติดตั้งmoduleก่อน')
    target = os.path.join(os.path.dirname(__file__), 'installmodule')
    os.chdir(target)
    os.startfile("install.bat")
    #os.chdir(target)
    #os.startfile("path.py")
now = datetime.datetime.now()
format = "%d - %m - %Y "
#format datetime using strftime()
hiddenimports = collect_submodules('django.contrib')
nowdate = now.strftime(format)
i = 0
class mainapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bgmainhome   = os.path.join(os.path.dirname(__file__), 'Asserts/HOME/BG.png')
        self.bghome= ImageTk.PhotoImage(file=self.bgmainhome)
        self.bmain = tk.Label(self , image = self.bghome)
        self.bmain.place(x = 0 , y=  0)
        frame1 = tk.LabelFrame(self , text = "เมนูหลักโปรแกรม" ,  bg = 'white', padx = 10, pady = 5)
        frame1.place(x  = 50 , y = 20)
        self.music_B = tk.Button(frame1,text = 'MUSIC'  ,cursor="heart" , width = 20 , height =5 , command =  self.openmusic_page,font=("times new roman",8,"bold"),fg="black",bg="SeaGreen2")
        self.music_B.grid(row = 0 ,  column = 0 )
        self.email_B = tk.Button(frame1 , text = 'FTP' , cursor = "heart" , width = 20 , height = 5   , command = self.open_portpage,font=("times new roman",8,"bold"),fg="black",bg="orange") 
        self.email_B.grid(row = 1, column = 0 , pady = 10 )
        self.cmd_B = tk.Button(frame1 , text = 'CMD' , width  = 20 , height = 5 , command = self.OPEN_CMD_PAGE  , cursor = 'heart',font=("times new roman",8,"bold"),fg="black",bg="pink") 
        self.cmd_B.grid(row = 2 , column = 0 , pady = 10)
        self.sb = tk.Button(frame1,text = 'HTTP' , width = 20 , height = 5 , command = self.opensharepage  , cursor = 'heart',font=("times new roman",8,"bold"),fg="black",bg="Firebrick1") 
        self.sb.grid(row = 3 , column = 0 , pady = 10 )
        installpip = tk.Button(self , text  = 'INSTALL MODULE' , command = self.install_module, bg = 'LightBlue1' , font=("times new roman",10,"bold") , cursor = 'star').place (x =  571,  y = 50)
    def openmusic_page(self):
        music = music_page(self)
        music.protocol("WM_DELETE_WINDOW", lambda x=music: close_music_page(x))
        self.music_B['state'] = DISABLED
        def close_music_page(window):
            music.destroy()
            self.music_B['state'] = ACTIVE
    def OPEN_CMD_PAGE(self):
        mini = CMD_MINI(self)
        mini.protocol("WM_DELETE_WINDOW", lambda x=mini: close_cmd(x))
        self.cmd_B['state']= DISABLED
        def close_cmd(window):
            self.cmd_B['state']= ACTIVE
            mini.destroy()
    def opensharepage(self):
        share = sharepage(self )
        share.protocol("WM_DELETE_WINDOW", lambda x=share: close_share(x))
        self.sb['state']= DISABLED
        def close_share(window):
            self.sb['state']= ACTIVE
            share.destroy()
    def open_portpage(self):
        port = port_page(self)
        port.protocol("WM_DELETE_WINDOW", lambda x=port: close_portpage(x))
        self.email_B['state']=DISABLED
        def close_portpage(window):
             self.email_B['state']=ACTIVE
             port.destroy()
    def install_module(self):
        target = os.path.join(os.path.dirname(__file__), 'installmodule')
        os.chdir(target)
        os.startfile("install.bat")
class music_page(tk.Toplevel):
    def __init__(self, musicpage):
        super().__init__(musicpage)
        self.geometry('735x315')
        self.title('เครื่องเล่นเพลง')
        musicico = os.path.join(os.path.dirname(__file__), 'Asserts/icon/music.ico')
        self.iconbitmap(musicico)
        self['bg'] = 'LightBlue1'
        self.resizable(False, False)
        self.file  = os.path.join(os.path.dirname(__file__), 'Asserts/gif/miku.gif')
        info = Image.open(self.file)
        self.frames = info.n_frames
        self.im = [tk.PhotoImage(file=self.file,format=f"gif -index {i}") for i in range(self.frames)]
        count = 0
        anim = None
        pygame.init()
    # Initiating Pygame Mixer
        pygame.mixer.init()
    # Declaring track Variable
        self.track = StringVar()
    # Declaring Status Variable
        self.status = StringVar()
     #gif anime
        self.framegif = tk.LabelFrame(self , bg = "white" )
        self.framegif.place(x = 0 , y = 0)
        self.gif_label = tk.Button(self.framegif,image="" , width = 320  , height = 211 , cursor = 'heart')
        self.gif_label.pack()
        self.animation(count)
        frame_music =  tk.LabelFrame(self , text = "เล่นเพลง" , bg = 'LightBlue1' , font=("times new roman",10,"bold") , cursor = 'star')
        frame_music.place(x = 5  , y =230 , width=350,height=80)
        self.songtrack = tk.Button(frame_music,textvariable=self.track,width=20,font=("times new roman",14,"bold"),bg="white",fg="maroon1" ,relief="groove").grid(row=0,column=0,padx=5,pady=5)
        self.trackstatus = tk.Button(frame_music,textvariable=self.status,font=("times new roman",14,"bold"),bg="brown3",fg="gold" ,relief="raised").grid(row=0,column=1,padx=5,pady=5)
        
        buttonframe = tk.LabelFrame(self , text = "ควบคุม" , bg = "LightBlue1", font=("times new roman",10,"bold") , cursor = 'dot' )
        buttonframe.place(x  =360 , y = 238)
    # Inserting Play Button
        playbtn = Button(buttonframe,text="เล่นเพลง",width=8,height=1,font=("times new roman",11,"bold"),fg="black",bg="SeaGreen2" , command = self.playsong).grid(row=0,column=0,padx=5,pady=5)
    # Inserting Pause Button
        pausebtn = Button(buttonframe,text="พัก",width=8,height=1,font=("times new roman",11,"bold"),fg="black",bg="orange", command = self.pausesong).grid(row=0,column=1,padx=5,pady=5)
    # Inserting Unpause Button
        unpausebtn = Button(buttonframe,text="หยุดพัก",width=8,height=1,font=("times new roman",11,"bold"),fg="black",bg="gold" , command =  self.unpausesong).grid(row=0,column=2,padx=5,pady=5)
    # Inserting Stop Button
        stopbtn = Button(buttonframe,text="หยุดเพลง",width=8,height=1,font=("times new roman",11,"bold"),fg="black",bg="IndianRed1" , command = self.stopsong).grid(row=0,column=3,padx=5,pady=5)

    # Creating Playlist Frame
        songlistframe = LabelFrame(self , text="คลังเพลง❤ นาย มงคล นามะวงค์ ",font=("times new roman",14,"bold"),bg="black",fg="LightSalmon",bd=5,relief=GROOVE , cursor = 'circle')
        songlistframe.place(x=330,y=0,width=405,height=220)
    # Inserting scrollbar
        self.scrol_y = Scrollbar(songlistframe,orient=VERTICAL)
    # Inserting Playlist listbox
        self.playlist = Listbox(songlistframe,yscrollcommand=self.scrol_y.set,selectbackground="SeaGreen3",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="pink",fg="black",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
        self.scrol_y.pack(side=RIGHT,fill=Y)
        self.scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
    # Changing Directory for fetching Songs)
        path = askdirectory(title='เลือกโฟลเดอร์เก็บเพลง') # shows dialog box and return the path
        #print(path)
        os.chdir(path)
        #Fetching Songs
        songtracks = os.listdir()
    # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)
    def openmfile(self):
        path = askdirectory(title='เลือกโฟลเดอร์เก็บเพลง') # shows dialog box and return the path
        os.chdir(path)
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END,track)
    def animation(self , count):
        global anim
        im2 = self.im[count]

        self.gif_label.configure(image=im2)
        count += 1
        if count == self.frames:
            count = 0
        anim = self.framegif.after(60,lambda :self.animation(count))
    def playsong(self):
    # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
        self.status.set("-Playing")
    # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
        pygame.mixer.music.play()
    def stopsong(self):
    # Displaying Status
        self.status.set("-Stopped")
    # Stopped Song
        pygame.mixer.music.stop()
    def pausesong(self):
    # Displaying Status
        self.status.set("-Paused")
    # Paused Song
        pygame.mixer.music.pause()
    def unpausesong(self):
    # It will Display the  Status
        self.status.set("-Playing")
    # Playing back Song
        pygame.mixer.music.unpause()
# gif player
class  port_page(tk.Toplevel):
    def __init__(self, port):
        super().__init__(port )
        self.geometry('800x624')
        self.title('FTP นาย มงคล นามะวงค์')
        portico = os.path.join(os.path.dirname(__file__), 'Asserts/icon/FTP.ico')
        self.iconbitmap(portico)
        self.resizable(False, False)
        self.configure(bg='black')
        bg   = os.path.join(os.path.dirname(__file__), 'Asserts/FTP/BG.png')
        self.bgport= ImageTk.PhotoImage(file=bg)
        self.portbg = tk.Label(self , image = self.bgport)
        self.portbg.place(x = 0 , y=  0)
       #Portcheck menu
        self.name_status = StringVar(port , 'Status')
        self.Entry_host = tk.Entry(self , bg = 'black'  ,fg="limegreen",insertbackground='orange' ,highlightthickness=1,font=("times new roman",11,"bold") )
        self.Entry_host.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.Entry_host.place(x = 140 , y = 49 )
        self.Entry_port  = tk.Entry(self, bg = 'black'    ,fg="limegreen",insertbackground='orange' ,highlightthickness=1,font=("times new roman",11,"bold") )
        self.Entry_port.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.Entry_port.place(x = 140  , y =100 )
        self.statusport = tk.Button(self  , bg = 'black'  ,fg="Firebrick2" , textvariable  = self.name_status , font=("times new roman",11,"bold"))
        self.statusport.place(x = 200 , y = 165)
        b_send = tk.Button(self , text  = 'Check' , command = self.scan, bg = 'black'  ,fg="limegreen" , font=("times new roman",11,"bold") )
        b_send.place(x = 100 , y = 165)
        #upload
        upload = tk.Button(self , text = "Upload" , command = self.upload , bg = 'black'  ,fg="limegreen" , font=("times new roman",11,"bold")) 
        upload.place(x =450, y = 210)
        self.pathtext  = scrolledtext.ScrolledText(self , width  = 50 , height = 10  , pady  = 5 ,  bg = 'black'  ,fg="limegreen",insertbackground='orange')
        self.pathtext.place(x = 378 , y = 41)
        okupload = tk.Button(self , text  = 'Submit' , command = self.okupload, bg = 'black'  ,fg="limegreen" , font=("times new roman",11,"bold") ).place(x = 550 , y = 210)
        # LOG
        self.filelog = scrolledtext.ScrolledText(self , width  = 76  ,height = 16 , bg = 'black'  ,fg="limegreen",insertbackground='orange')
        self.filelog.place(x = 226 , y = 296)
        clearftp = tk.Button(self , text  = 'Clear',width=8,height=1,font=("times new roman",11,"bold"),fg="limegreen",bg="black" , borderwidth= 5,  command = self.clearlog).place(x = 460 , y = 560)
        # input  host FTP
        self.hostftp = tk.Entry(self,bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange')
        self.hostftp.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.hostftp.place(x = 70, y = 400)
        self.idftp = tk.Entry(self ,bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange')
        self.idftp.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.idftp.place(x  = 70 , y = 430)
        self.passftp = tk.Entry(self ,bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange')
        self.passftp.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.passftp.place(x = 70 , y = 460)
        self.dirftp = tk.Entry(self,bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange')
        self.dirftp.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.dirftp.place(x = 70 ,y = 490)
        dirbu = tk.Button(self , text = 'Download' , command = self.dowload,font=("times new roman",10,"bold"),fg="limegreen",bg="black") .place(x = 70 , y = 340)
        #dowlaod menu
        self.nameinfile = tk.Entry(self  ,bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange')
        self.nameinfile.config(highlightbackground = "limegreen", highlightcolor= "limegreen",font=("times new roman",8,"bold"))
        self.nameinfile.place(x = 70, y = 312)
        bdfile = tk.Button(self , text = 'LocalFiles' , command = self.dir,font=("times new roman",9,"bold"),fg="limegreen",bg="black").place(x = 70 , y = 535)
    def scan(self):
        #convert to  Entry get    to ip address
        p_check  =int(self.Entry_port.get() )
        hostip = self.Entry_host.get() 
        resultip = str(ipaddress.ip_address(hostip))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(( resultip ,p_check))
        if result == 0:
            p_open = 'PORT OPEN'
            self.name_status.set("PORT OPEN")
        else:
            p_close = 'PORT CLOSE'
            self.name_status.set("PORT :CLOSE")
    def dir(self):
        self.clearlog()
        hostin = str(self.hostftp.get())
        resulthost = str(ipaddress.ip_address(hostin))
        inid  = str( self.idftp.get() )
        inpass =str( self.passftp.get() )
        indir  = str(self.dirftp.get() )
        with ftplib.FTP(hostin) as ftp:
            try:
                ftp.login(inid,inpass)
                ftp.cwd(indir)  
                files = []
                ftp.dir(files.append)
                ftp.quit()
                index = 0
                for  line in files:
                    index+=1
                    formatresult = f'\n-{index} {line}'
                    self.filelog.insert('1.0' ,str(formatresult))
                resultall =f'\n result all = {index}'
                self.filelog.insert('1.0' ,str(resultall))
            except Exception as Error:
                print(Error)
                ftp.quit()
    def dowload(self):
        self.clearlog()
        inid  = str( self.idftp.get() )
        inpass =str( self.passftp.get() )
        indir  = str(self.dirftp.get() )
        hostin = str(self.hostftp.get())
        dow =str( self.nameinfile.get() )
        resulthost = str(ipaddress.ip_address(hostin))
        #directory = "FTPDownloads"
        pathsave = askdirectory(title='เลือกโฟลเดอร์เก็บเพลง')
        tosaveftp = os.path.join(pathsave , dow)
        #print(tosaveftp)
        #print(tosaveftp)
        try:
            with ftplib.FTP(hostin) as ftp:
                ftp.login(inid,inpass)
                ftp.cwd(indir)  
                with open(tosaveftp, "wb" ) as file:
                    ftp.retrbinary(f"RETR {dow}", file.write)
                    #resultdowload  = f'DOWLOAD  {dow } SUCSESS   SAVE   AS ftpdow'
                    resultdowload  = f'DOWLOAD  {dow } SUCSESS   SAVE   AS {tosaveftp}'
                    self.filelog.insert('1.0',resultdowload)
                    ftp.quit()
                self.nameinfile.delete(0, END)
        except Exception as Error:
            print(Error)
            resultdowloadbad  = f'Dowload {dow } NOT  SUCSESS !!!'
            self.filelog.insert('1.0',resultdowloadbad)
            ftp.quit()
    def clearlog(self):
         self.filelog.delete('1.0',END)
    def upload(self):
        self.pathtext.delete('1.0' , END)
        self.up = filedialog.askopenfilename(initialdir = "/",title = "เลือกไฟล์ของคุณ",filetypes = (("jpeg files","*.jpg") , (" PDF" , "*.pdf"), ("EXE" , "*.exe"),("RAR" , "*.rar"),("PNG" , "*.png"),("all files","*.*")),multiple =False)
        self.pathtext.insert('1.0',self.up)
    def okupload(self):
        hostin = str(self.hostftp.get())
        indir  = str(self.dirftp.get() )
        inpass =str( self.passftp.get() )
        inid  = str( self.idftp.get() )
        try:
            self.pathtext.delete('1.0',END)
            with ftplib.FTP(hostin) as ftp:
                ftp.login(inid,inpass)
                ftp.cwd(indir)
                try:
                    upftp = open(self.up,'rb')
                    ftp.storbinary('STOR %s' % os.path.basename(self.up ), upftp, 1024)
                    ftp.close()
                    okcheck  = f'file{self.up} UPLOAD SUCCESS  in {indir}'
                    self.filelog.insert('1.0',okcheck)
                except Exception as Error:
                    errorcheck = f'file{self.up} UPLOAD NOT SUCCESS !!!!!!!!!!!!!!'
                    self.filelog.insert('1.0',errorcheck)
                    ftp.close()
        except Exception as e :
             ftp.close()
class CMD_MINI(tk.Toplevel):
    def __init__(self, TO_DO):
        super().__init__(TO_DO)
        self.geometry('840x650')
        self.title('CMD นายมงคล นามะวงค์')
        cmdico = os.path.join(os.path.dirname(__file__), 'Asserts/icon/CMD.ico')
        self.iconbitmap(cmdico)
        self.resizable(False, False)
        frame_in = tk.LabelFrame(self , text = "cmd" , padx = 5  , pady = 5, width = 150 , height = 10 ,bg = 'black' , font=("times new roman",14,"bold") ,fg="limegreen")
        frame_in.place(x = 0 , y =  0)
        self.tool  = tk.scrolledtext.ScrolledText(frame_in , bg = 'black' , font=("times new roman",14,"bold") ,fg="limegreen",insertbackground='orange')
        self.tool.grid(row = 0 , column = 0)
        self.tool.bind('<Return>' , self.run)
        frame_in2 = tk.LabelFrame(self , text = "ควบคุม" ,padx = 5 , pady = 5 , bg = 'grey' , font=("times new roman",12,"bold") ,fg="limegreen")
        frame_in2.place(x = 40 , y = 570 )
        clear_cmd = tk.Button(frame_in2 , width  =9, height = 3 , text =  "เคลียร์" , command = self.clear_cmd_tool)
        clear_cmd.grid(row = 0 ,column = 0 , padx = 5)
        max_ram = tk.Button(frame_in2 , width  =9, height = 3 , text =  "แรมสูงสุด" , command = self.maxram)
        max_ram.grid(row = 0 ,column = 1 , padx = 5)
        max_ram = tk.Button(frame_in2 , width  =9, height = 3 , text =  "หาไอพี" , command = self.ip)
        max_ram.grid(row = 0 ,column = 3 , padx = 5)
        share = tk.Button(frame_in2 , width  = 9 , height = 3 , text  = "ข้อมูลOS" , command = self.OS)
        share.grid(row = 0 , column = 4 , padx =5)
        wifi = tk.Button(frame_in2 , width  = 9 , height = 3 , text  = "ประวัติติดตั้ง" , command = self.install)
        wifi.grid(row = 0 , column = 5 , padx =5)
        share = tk.Button(frame_in2 , width  = 9 , height = 3 , text  = "เช็คพอต" , command = self.net)
        share.grid(row = 0 , column = 6 , padx =5)
        task =  tk.Button(frame_in2 , width  = 9 , height = 3 , text  = "การทำงาน" , command = self.tasklist)
        task.grid(row = 0 , column = 7 , padx = 5)
        task =  tk.Button(frame_in2 , width  = 9 , height = 3 , text  = "ตำแหน่งไฟล์" , command = self.dir)
        task.grid(row = 0 , column = 8 , padx = 5)
        notepad = tk.Button(frame_in2 , width  = 9 , height = 3 , text  = "notepad" , command = self.note)
        notepad.grid(row = 0 , column = 9 , padx = 5)
    def run(self , event):
        cmd = self.tool
        command = cmd.get('1.0', 'end').split('\n')[-2]
        if command == 'exit':
            exit()
        elif command == 'clar' or 'cls':
            cmd.delete('1.0',END)
        cmd.insert('end', f'\n{subprocess.getoutput(command)}')
    def clear_cmd_tool(self):
        cmd = self.tool
        cmd.delete('1.0',END)
    def  maxram(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT, "wmic memphysical get MaxCapacity, MemoryDevices")
    def ip(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT, "ipconfig")
    def OS(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT, "systeminfo")
    def install(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT,'wmic product get name')
    def net(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT,'netstat')
    def tasklist(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT,'Tasklist')
    def dir(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT,'dir')
    def note(self):
        cmd = self.tool
        cmd.delete('1.0',END)
        cmd.insert(INSERT,'notepad.exe')
class  sharepage(tk.Toplevel):
    def __init__(self,pshare ):
        super().__init__(pshare )
        self.geometry("706x526")
        self.title('HTTP นายมงคล นามะวงค์')
        HTTPICO = os.path.join(os.path.dirname(__file__), 'Asserts/icon/HTTP.ico')
        self.iconbitmap(HTTPICO)
        self.resizable(False, False)
        #blackground
        bg   = os.path.join(os.path.dirname(__file__), 'Asserts/HTTP/bg.png')
        self.bghttp= ImageTk.PhotoImage(file=bg)
        self.http = tk.Label(self , image = self.bghttp)
        self.http.place(x = 0 , y=  0)
        #Button
        bu = tk.LabelFrame(self  , bg = 'black' ,padx = 5 , pady = 5)
        bu.place(x = 70 ,y = 460)
        bs = tk.Button (bu , text = 'OK' , command = self.okshare,font=("times new roman",9,"bold"),fg="limegreen",bg="black").grid(row = 1 , column = 0 , padx = 5)
        bs1 = tk.Button (bu , text = 'HOST' , command = self.host,font=("times new roman",9,"bold"),fg="limegreen",bg="black").grid(row = 1 , column = 1 , padx = 5)
        bs2 = tk.Button(bu , text = 'FIND MY IP' , command =self.web,font=("times new roman",9,"bold"),fg="limegreen",bg="black" ).grid(row = 1 , column = 2  , padx = 5 )
        con = tk.Button(bu , text = 'STATUS CHECK' , command =self.refresh,font=("times new roman",9,"bold"),fg="limegreen",bg="black" ).grid(row = 1 , column = 3 , padx = 5 )
        # IP number
        Lframe = tk.LabelFrame(self ,  padx = 5 , pady = 5, bg = 'black' )
        Lframe.place(x = 95 , y= 410)
        ls1  = tk.Label(Lframe , text  =  'เลขไอพี' ,bg = 'black' ,font=("times new roman",10,"bold"),fg="limegreen").grid(row = 0 , column = 0 , padx = 5)
        self.IPinput = tk.Entry(Lframe , bg = 'black'  ,fg="limegreen",insertbackground='orange' ,highlightthickness=1,font=("times new roman",11,"bold") )
        self.IPinput.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
        self.IPinput.grid(row = 0 , column = 1)
        #show_my_ip
        self.Laip =  tk.LabelFrame(self , padx = 5 , pady = 5 , tex = "MY IP" , bg = 'grey' ,font=("times new roman",14))
        self.Laip.place(x = 25 , y = 220)
        self.myip()
        #Browse Files
        browse = tk.Button(self ,command =  self.browsefile , text = 'BrowseFile',font=("times new roman",9,"bold"),fg="limegreen",bg="black").place(x = 490 , y = 298)
        self.logb = scrolledtext.ScrolledText(self , width  = 35  ,height = 8 , bg = 'black'  ,fg="limegreen",insertbackground='orange')
        self.logb.place(x = 24 , y = 39)
        buclearlog = tk.Button(self  , command = self.clearlogb,  text = 'Clear',font=("times new roman",9,"bold"),fg="limegreen",bg="black").place(x = 120 , y = 180)
    def clearlogb(self):
        self.logb.delete('1.0',END)
    def web(self):
        webbrowser.open_new('https://www.myip.com/')
    def goweb(self):
        resultgoweb  = str(self.E1.get() )
        resultdata = f"http://{resultgoweb}:8000"
        re = str(resultdata)
        webbrowser.open('localhost:8000')
    def okshare(self):
        try:
            self.logb.delete('1.0',END)
            texthttp = StringVar()
            result  = str(self.IPinput.get() )
            data = f"http://{result}:8000"
            nameqrcode = 'QRCODE.png'
            pathsave = askdirectory(title='เลือกโฟลเดอร์เก็บ QRCODE' )
            tosaveqr = os.path.join(pathsave , nameqrcode)
            img = qrcode.make(data)
            img.save(tosaveqr)
            loginsert =  f'Save {nameqrcode}  As\n{pathsave}'
            self.logb.insert('1.0' , loginsert) 
            #genhttp
            self.htp = tk.LabelFrame(self , text = "WEBSITE" ,padx = 5 , pady = 5 ,bg = 'black' ,fg="limegreen", font=("times new roman",12,"bold"))
            self.htp.place(x = 380 , y = 400)
            http = tk.Entry(self.htp ,textvariable=texthttp , width = 30 ,font=("times new roman",12,"bold"),bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange' )
            http.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
            texthttp.set (str(data))
            http.pack()
        except Exception as Error:
            print(Error)
    def browsefile(self):
        targetphoto = filedialog.askopenfilename(initialdir =  "/", title = "เลือกไฟล์ QRCODE", filetype =((" PNG files","*.png"),("all files","*.*")) )
        #targetphoto = os.path.join(os.path.dirname(__file__), 'qrcode/qrcode.png')
        img=Image.open(targetphoto) 
        img=img.resize((330,250)) 
        img=ImageTk.PhotoImage(img)
        self.Labelpng = tk.Button(self)
        self.Labelpng.place(x = 350 , y = 25)
        self.Labelpng.image = img
        self.Labelpng['image']=img
    def host(self):
        target = os.path.join(os.path.dirname(__file__), 'share')
        os.chdir(target)
        os.startfile("server limit")
    def myip(self):
        self.text = StringVar()
        self.reip = tk.Button(self.Laip , width = 20 , height = 2 , textvariable=self.text  , bg = 'black'  , font=("times new roman",15,"bold") ,fg="limegreen")
        self.reip.grid(row = 0 , column = 0)
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)
        self.text.set(str(IPAddr))
    def refresh(self):
        try:
            self.statuscon = tk.LabelFrame(self , text  =   'STATUS SERVER HTTP' , bg = 'black' , fg  = 'limegreen')
            self.statuscon.place(x = 450,  y = 465 )
            self.st = tk.Entry (self.statuscon,bg = 'black' , fg = 'limegreen' ,highlightthickness=1 ,insertbackground = 'orange')
            self.st.config(highlightbackground = "limegreen", highlightcolor= "limegreen")
            self.st.pack()
            self.st.delete(0,END)
            formatip  = str(self.IPinput.get() )
            r =requests.get(f"http://{formatip}:8000")
            resultcode  = r.status_code
            print(resultcode)
            self.st.insert(0,resultcode)
            if resultcode == 200:
                self.st.insert(0,f'OK statuscode = ' )
        except Exception as code_error:
            self.st.insert(0,'BAD')
            print(code_error)
if __name__ == "__main__":
    app = mainapp()
    app.geometry("706x424")
    app.resizable(False, False)
    mainico = os.path.join(os.path.dirname(__file__), 'Asserts/icon/main.ico')
    app.iconbitmap(mainico)
    app.title('หน้าหลัก ❤ นาย มงคล นามะวงค์ ')
    app.mainloop()
