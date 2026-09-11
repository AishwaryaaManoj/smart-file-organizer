import os
print ("Enter the folder to be organized:")
folder = input()
h= os.path.expanduser("~")
d= os.path.join(h, folder)
x=os.listdir(d)
print ("Organizing the folder: ",os.listdir(d))
for i in range(len(x)):
    if x[i].endswith(".jpg"):
        os.makedirs(os.path.join(d, "Images"), exist_ok=True)
        os.rename(os.path.join(d, x[i]), os.path.join(d, "Images", x[i]))
    elif x[i].endswith(".mp4"):
        os.makedirs(os.path.join(d, "Videos"), exist_ok=True)
        os.rename(os.path.join(d, x[i]), os.path.join(d, "Videos", x[i])) 
    elif x[i].endswith(".pdf"):
        os.makedirs(os.path.join(d, "Documents"), exist_ok=True)
        os.rename(os.path.join(d, x[i]), os.path.join(d, "Documents", x[i]))
    elif x[i].endswith(".mp3"):
        os.makedirs(os.path.join(d, "Music"), exist_ok=True)
        os.rename(os.path.join(d, x[i]), os.path.join(d, "Music", x[i]))
    elif x[i].endswith(".txt"):
        os.makedirs(os.path.join(d, "TextFiles"), exist_ok=True)
        os.rename(os.path.join(d, x[i]), os.path.join(d, "TextFiles", x[i]))
    elif x[i].endswith(".zip"):
        os.makedirs(os.path.join(d, "Compressed"), exist_ok=True)
        os.rename(os.path.join(d, x[i]), os.path.join(d, "Compressed", x[i]))
    
