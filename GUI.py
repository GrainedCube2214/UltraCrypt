from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import graphing,encryption, os, pygame

root = Tk()
root.title('UltraCrypt - Encryptor for CS Project')
root.iconbitmap('images/icon.ico')

def raise_frame(frame):
    frame.tkraise()

file_enc = None

def addfile_enc():
    global file_enc
    choice = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (('Text Files','*.txt'),("all files","*.*")))
    file_enc=choice
file_dec = None

def addfile_dec():
    global file_dec
    choice = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (('Text Files','*.txt'),("all files","*.*")))
    file_dec=choice
outfile=''

def addfilegraph():
    global outfile
    choice = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (('Text Files','*.txt'),("all files","*.*")))
    outfile=choice


#playing music
pygame.init()
mxstate = 0  # music play state
pygame.mixer.music.load('music/bg1.mp3')
def Play_music():
    global mxstate
    if mxstate == 0:  # music not started
        pygame.mixer.music.play()
        btn11.configure(text="Pause")
        mxstate = 1
        return

    if mxstate == 1:  # music playing
        pygame.mixer.music.pause()
        btn11.configure(text="Resume")
    else:  # music paused
        pygame.mixer.music.unpause()
        btn11.configure(text="Pause")
    mxstate = 3 - mxstate  # swap pause state


#declaring frames
menu = LabelFrame(root, text = 'Menu')
encrypt = LabelFrame(root, text = 'Encryption')
graph = LabelFrame(root, text = 'Graphing')
decrypt = LabelFrame(root, text = 'Decryption')
easter_egg = LabelFrame(root, text = 'Secret')
outputframe_enc = LabelFrame(root, text = 'Output')
outputframe_dec = LabelFrame(root, text = 'Output')
file_encrypt = LabelFrame(root, text='File Based Encryption')
file_decrypt = LabelFrame(root, text='File Based Decryption')
ui_settings = LabelFrame(root, text='UI Settings')

for frame in (menu,encrypt,decrypt,graph,easter_egg,outputframe_enc, outputframe_dec, file_encrypt, file_decrypt, ui_settings):
    frame.grid(row=0, column=0, sticky='news')                             #row=3, column=15, padx=250, sticky='news'

#background
for frame in (menu,encrypt,decrypt,graph,easter_egg,outputframe_enc, outputframe_dec, file_encrypt, file_decrypt, ui_settings):
    im = Image.open('images/newbg.jpg')
    w,h=im.size
    canvas = Canvas(frame, height=h, width=w)
    canvas.pack()
    canvas.image = ImageTk.PhotoImage(im)
    background = canvas.create_image(0, 0, image=canvas.image, anchor='nw')


#Menu
Button(menu, text='Encryption',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(encrypt)).place(x=25, y=75, height = 30, width = 80)
Button(menu, text='Graphing',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(graph)).place(x=125, y=75, height = 30, width = 80)
Button(menu, text='Decryption',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(decrypt)).place(x=225, y=75, height = 30, width = 80)
Button(menu, text='How To',bg='red', font=('Segoe UI',11), fg='white', command=lambda:os.startfile('about.txt')).place(x=325, y=75, height = 30, width = 80)
Button(menu, text='Encryption (file based)',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(file_encrypt)).place(x=35, y=125, height = 30, width = 160)
Button(menu, text='Decryption (file based)',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(file_decrypt)).place(x=235, y=125, height = 30, width = 160)
btn11 = Button(menu, text='Toggle Music', width=14, bg='#333847', font=('Segoe UI',9), fg='white', command=Play_music)
btn11.place(x=105, y=200)
Button(menu, text='UI Settings', width=14, bg='#333847', font=('Segoe UI',9), fg='white', command= lambda:raise_frame(ui_settings)).place(x=255, y=200)

#UI Settings
music_list = ['---Choose Music---', 'Aetheral (default)', 'Cheery 1', 'Cheery 2', 'Cheery 3', 'Cheery 4', 'Dramatic 1', 'Dramatic 2', 'Dramatic 3']
music_choice = StringVar()
music_choice.set(music_list[0])
Label(ui_settings, text = 'Music Settings:',bg='#333847', font=('Segoe UI',11), fg='white').place(x=20,y=20)
music_dd = OptionMenu(ui_settings, music_choice, *music_list)
music_dd.place(x=20, y=50)
musicpathlist = ['music/bg1.mp3','music/bg2.mp3','music/bg3.mp3','music/bg4.mp3','music/bg5.mp3','music/bg6.mp3','music/bg7.mp3','music/bg8.mp3']
def switch_music():
    music = music_choice.get()
    if music == '---Choose Music---':
        x=1
    else:
        for i in range(len(music_list)):
            if music_list[i]==music: i1=i-1
        print(i1)
        mtp = musicpathlist[i1]
        pygame.mixer.music.load(mtp)
        pygame.mixer.music.play(-1)
newbg=''

def apply():
        switch_music()
Button(ui_settings, text='Apply',bg='#333847', font=('Segoe UI',11), fg='white', command=apply).place(x=20, y=85)
Button(ui_settings, text='Back',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(menu)).place(x=20,y=125)

#Encryption/decryption Protocols
protocol_list = ['---Choose Protocol---','Morse Code','Caesar Cipher','Advanced Caesar Cipher', 'Homo-phonic Substitution Cipher', 'Four Square Cipher', 'At_bash Cipher']
protocol_choice=StringVar()
protocol_choice.set(protocol_list[0])


#Encryption Menu
dd=OptionMenu(encrypt, protocol_choice, *protocol_list)
dd.place(x = 10, y = 10)
Label(encrypt, text = 'Enter string to encrypt:',bg='#333847', font=('Segoe UI',11), fg='white').place(x=10, y=50)
textin = Entry(encrypt, width = 50)
textin.place(x=10, y=80)
Label(encrypt, text = 'Create a key (only for Caesar Cipher (both types)):',bg='#333847', font=('Segoe UI',11), fg='white').place(x=10,y=110)
keyin_enc = Entry(encrypt, width = 50)
keyin_enc.place(x=10,y=140)

def getkey():
    ret = keyin_enc.get()
    return ret

def encryptstr():
    chosen_protocol = protocol_choice.get()
    input_text = textin.get()
    key = getkey()
    print('\'',key,'\'', type(key))
    if chosen_protocol == '---Choose Protocol---':
        messagebox.showerror("Error!", "Please select a valid protocol.")
    elif input_text == '':
        messagebox.showerror("Error!", "Please enter a string.")
    else:
        encrypted_str = ''
        done = True
        if chosen_protocol == 'Morse Code':
            encrypted_str = encryption.morse_enc(input_text)
        if chosen_protocol == 'Caesar Cipher':
            try:
                key = int(key)
                print(key)
            except:
                messagebox.showerror("Error!", "Please enter a vaild key (numeric type within 26).")
                done = False
            encrypted_str = encryption.custom_enc(input_text, key)
        if chosen_protocol == 'Advanced Caesar Cipher':
            if key.isalpha() == False:
                messagebox.showerror("Error!", "Please enter a vaild key (alpahbetic).")
                done = False
            encrypted_str = encryption.cc2_enc(input_text, key)
        if chosen_protocol == 'Homo-phonic Substitution Cipher':
            encrypted_str = encryption.hsc_enc(input_text)
        if chosen_protocol == 'Four Square Cipher':
            encrypted_str = encryption.four_square_enc(encryption.sch(input_text))
        if chosen_protocol == 'At_bash Cipher':
            encrypted_str = encryption.at_bash(input_text)
        if done == True:
            global outputlabel_enc
            print(encrypted_str)
            outputlabel_enc = Label(outputframe_enc, text='Your output is:\n'+encrypted_str,bg='#333847', font=('Segoe UI',11), fg='white')
            outputlabel_enc.place(x=20, y=20)
            raise_frame(outputframe_enc)
def back_to_enc():
    outputlabel_enc.destroy()
    raise_frame(encrypt)
Button(encrypt, text='                Go              ',bg='#333847', font=('Segoe UI',11), fg='white', command=encryptstr).place(x=10,y=170)
Button(encrypt, text='              Back              ',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(menu)).place(x=10,y=210)
Button(outputframe_enc, text='              Back              ',bg='#333847', font=('Segoe UI',11), fg='white', command=back_to_enc).place(x=10,y=210)
Button(encrypt, bg='red', font=('Segoe UI',11), fg='white',text = '  ?  ',command =lambda: os.startfile('about_encryption.txt')).place(x=300,y=20)

#Decryption Menu
dd=OptionMenu(decrypt, protocol_choice, *protocol_list)
dd.place(x = 10, y = 10)
Label(decrypt, text = 'Enter string to decrypt:',bg='#333847', font=('Segoe UI',11), fg='white').place(x=10, y=50)
textin_dec = Entry(decrypt, width = 50)
textin_dec.place(x=10, y=80)
Label(decrypt, text = 'Enter your key (only for Caesar Cipher (both types)):',bg='#333847', font=('Segoe UI',11), fg='white').place(x=10,y=110)
keyin_dec = Entry(decrypt, width = 50)
keyin_dec.place(x=10,y=140)
def decryptstr():
    chosen_protocol = protocol_choice.get()
    input_text = textin_dec.get()
    if chosen_protocol == '---Choose Protocol---':
        messagebox.showerror("Error!", "Please select a valid protocol.")
    elif input_text == '':
        messagebox.showerror("Error!", "Please enter a string.")
    else:
        decrypted_str = ''
        done = True
        if  chosen_protocol == 'Morse Code':
            try:
                decrypted_str = encryption.morse_dec(input_text)
            except:
                messagebox.showerror("Error!", "Please enter a vaild decryption string (ie dots and dashes).")
                done = False
        if  chosen_protocol == 'Caesar Cipher':
            try:
                key = int(keyin_dec.get())
            except:
                messagebox.showerror("Error!", "Please enter a vaild key (numeric type within 26).")
                done = False
            decrypted_str = encryption.custom_dec(input_text, key)
        if  chosen_protocol == 'Advanced Caesar Cipher':
            key = str(keyin_dec.get())
            if key.isalpha() == False:
                messagebox.showerror("Error!", "Please enter a vaild key (alpahbetic).")
                done = False
            decrypted_str = encryption.cc2_dec(input_text, key)
        if  chosen_protocol == 'Homo-phonic Substitution Cipher':
            decrypted_str = encryption.hsc_dec(input_text)
        if  chosen_protocol == 'Four Square Cipher':
            decrypted_str = encryption.four_square_dec(encryption.sch(input_text.lower()))
        if  chosen_protocol == 'At_bash Cipher':
            decrypted_str = encryption.at_bash(input_text)
        if done == True:
            global outputlabel_dec
            print(decrypted_str)
            outputlabel_dec = Label(outputframe_dec, text='Your output is:\n'+decrypted_str)
            outputlabel_dec.place(x=20, y=20)
            raise_frame(outputframe_dec)
def back_to_dec():
    outputlabel_dec.destroy()
    raise_frame(decrypt)
Button(decrypt, text='                Go              ',bg='#333847', font=('Segoe UI',11), fg='white', command=decryptstr).place(x=10,y=170)
Button(decrypt, text='              Back              ',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(menu)).place(x=10,y=210)
Button(outputframe_dec, text='              Back              ',bg='#333847', font=('Segoe UI',11), fg='white', command=back_to_dec).place(x=10,y=210)
Button(decrypt, bg='red', font=('Segoe UI',11), fg='white',text = '  ?  ',command =lambda: os.startfile('about_encryption.txt')).place(x=300,y=20)

#File Based Encryption
Button(file_encrypt, text='Back',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(menu)).place(x=195,y=230)
Button(file_encrypt, text='Select File To Encrypt',bg='#333847', font=('Segoe UI',11), fg='white', command=addfile_enc).place(x=140, y=0)
Label(file_encrypt, text = 'Create a key (only for Caesar Cipher (both types)):',bg='#333847', font=('Segoe UI',11), fg='white').place(x=40,y=40)
keyin_fe = Entry(file_encrypt, width = 50)
keyin_fe.place(x=60,y=70)
dd=OptionMenu(file_encrypt, protocol_choice, *protocol_list)
dd.place(x = 140, y = 100)
Label(file_encrypt, text = 'Name your output file with path(eg. C/out.txt):',bg='#333847', font=('Segoe UI',11), fg='white').place(x=50,y=130)
output_file_enc = Entry(file_encrypt, width = 50)
output_file_enc.place(x=60, y=160)
Button(file_encrypt, bg='red', font=('Segoe UI',11), fg='white',text = '  ?  ',command =lambda: os.startfile('about_encryption.txt')).place(x=390,y=10)

def getkey_file():
    retfi = keyin_fe.get()
    return retfi

def file_encryptstr(input_text):
    chosen_protocol = protocol_choice.get()
    if chosen_protocol == '---Choose Protocol---':
        messagebox.showerror("Error!", "Please select a valid protocol.")
    else:
        encrypted_str = ''
        done = True
        if chosen_protocol == 'Morse Code':
            encrypted_str = encryption.morse_enc(input_text)
        if chosen_protocol == 'Caesar Cipher':
            try:
                key = int(getkey_file())
                encrypted_str = encryption.custom_enc(input_text, key)
            except:
                messagebox.showerror("Error!", "Please enter a vaild key (numeric type within 26).")
                done = False
        if chosen_protocol == 'Advanced Caesar Cipher':
            key = str(getkey_file())
            if key.isalpha() == False:
                messagebox.showerror("Error!", "Please enter a vaild key (alpahbetic).")
                done = False
            encrypted_str = encryption.cc2_enc(input_text, key)
        if chosen_protocol == 'Homo-phonic Substitution Cipher':
            encrypted_str = encryption.hsc_enc(input_text)
        if chosen_protocol == 'Four Square Cipher':
            encrypted_str = encryption.four_square_enc(encryption.sch(input_text))
        if chosen_protocol == 'At_bash Cipher':
            encrypted_str = encryption.at_bash(input_text)
        if done == True:
            return encrypted_str

def encrypt_file():
    global file_enc
    if file_enc == None or file_enc == '':
        messagebox.showerror("Error!", "Please select a file.")
    file = open(file_enc, 'r')
    outputfile = output_file_enc.get()
    if outputfile == None or outputfile == '':
        messagebox.showerror("Error!", "Please enter a valid file path.")
    output = open(outputfile, 'w')
    line = file.readline()
    while line != '':
        x = str(line)[0:-1].lower()
        out = file_encryptstr(x)
        print(out)
        output.write(out+'\n')
        line = file.readline()
    file.close()
    output.close()
    os.startfile(outputfile)

Button(file_encrypt, text = 'Encrypt!', bg='#333847', font=('Segoe UI',11), fg='white', command= encrypt_file).place(x=185, y=190)

#File Based Decryption
Button(file_decrypt, text='Back',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(menu)).place(x=195,y=230)
Button(file_decrypt, text='Select File To Decrypt',bg='#333847', font=('Segoe UI',11), fg='white', command=addfile_dec).place(x=140, y=0)
Label(file_decrypt, text = 'Create a key (only for Caesar Cipher (both types)):',bg='#333847', font=('Segoe UI',11), fg='white').place(x=40,y=40)
keyin = Entry(file_decrypt, width = 50)
keyin.place(x=60,y=70)
dd=OptionMenu(file_decrypt, protocol_choice, *protocol_list)
dd.place(x = 140, y = 100)
Label(file_decrypt, text = 'Name your output file with path(eg. C/out.txt):',bg='#333847', font=('Segoe UI',11), fg='white').place(x=50,y=130)
output_file_dec = Entry(file_decrypt, width = 50)
output_file_dec.place(x=60, y=160)
Button(file_decrypt, bg='red', font=('Segoe UI',11), fg='white',text = '  ?  ',command =lambda: os.startfile('about_encryption.txt')).place(x=390,y=10)

def file_decryptstr(input_text):
    chosen_protocol = protocol_choice.get()
    if chosen_protocol == '---Choose Protocol---':
        messagebox.showerror("Error!", "Please select a valid protocol.")
    else:
        decrypted_str = ''
        done = True
        if chosen_protocol == 'Morse Code':
            decrypted_str = encryption.morse_dec(input_text)
        if chosen_protocol == 'Caesar Cipher':
            try:
                key = int(keyin.get())
            except:
                messagebox.showerror("Error!", "Please enter a vaild key (numeric type within 26).")
                done = False
            decrypted_str = encryption.custom_dec(input_text, key)
        if chosen_protocol == 'Advanced Caesar Cipher':
            key = str(keyin.get())
            if key.isalpha() == False:
                messagebox.showerror("Error!", "Please enter a vaild key (alpahbetic).")
                done = False
            decrypted_str = encryption.cc2_dec(input_text, key)
        if chosen_protocol == 'Homo-phonic Substitution Cipher':
            decrypted_str = encryption.hsc_dec(input_text)
        if chosen_protocol == 'Four Square Cipher':
            decrypted_str = encryption.four_square_dec(encryption.sch(input_text))
        if chosen_protocol == 'At_bash Cipher':
            decrypted_str = encryption.at_bash(input_text)
        if done == True:
            return decrypted_str

def decrypt_file():
    global file_dec
    if file_dec == None or file_dec == '':
        messagebox.showerror("Error!", "Please select a file.")
    file = open(file_dec, 'r')
    outputfile = output_file_dec.get()
    if outputfile == None or outputfile == '':
        messagebox.showerror("Error!", "Please enter a valid file path.")
    output = open(outputfile, 'w')
    line = file.readline()
    while line != '':
        x = str(line)[0:-1].lower()
        out = file_decryptstr(x)
        print(out)
        output.write(out+'\n')
        line = file.readline()
    file.close()
    output.close()
    os.startfile(outputfile)

Button(file_decrypt, text = 'Decrypt!', bg='#333847', font=('Segoe UI',11), fg='white', command= decrypt_file).place(x=185, y=190)

#Graphing Menu
Button(graph, text='Select File To Graph',bg='#333847', font=('Segoe UI',11), fg='white', command=addfilegraph,width=17,height=1).place(x=150, y=20)

def graphit():
    global outfile
    if outfile == '':
        messagebox.showerror("Error!", "Please select a valid file.")
        return
    f = graphing.freq(outfile)
    graphing.graph(f, "Character", "No. of occurences")

Button(graph, text='Show Graph',bg='#333847', font=('Segoe UI',11), fg='white', command=graphit,width=17,height=1).place(x=150, y=55)
Button(graph, text='Back',bg='#333847', font=('Segoe UI',11), fg='white', command=lambda:raise_frame(menu),width=17,height=1).place(x=150, y=90)


raise_frame(menu)
mainloop()
