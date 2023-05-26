from tkinter import ttk

import cv2
import time
import sys
import re
import pickle
import webbrowser
import pytesseract
import numpy as np
from tkinter import *
import pandas as pd
from PIL import Image,ImageTk
import datetime as dt
import time
from datetime import datetime
from fpdf import FPDF

from tkinter import filedialog


df=pd.read_excel("Dummy NP.xlsx",engine='openpyxl')


excel=[]
excel1=[]
reqdata=[]
login=[False]
filesdata=[]
imgpro={}
#change login list to false for authentication
def extract_num():

    data1=[""""""]
    if (not login[0]):
        import tkinter as tk

        root = tk.Tk()
        width1 = root.winfo_screenwidth()

        height1 = root.winfo_screenheight()
        h1 = int((0.6) * height1)

        root.geometry("%dx%d" % (width1, height1))
        canvas = Canvas(root, width=width1, height=h1)
        canvas.place(x=0, y=0)

        img1 = (Image.open("backi.jpg"))

        resized_image = img1.resize((width1, h1), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        canvas.create_image(10, 10, anchor=NW, image=new_image)
        labelframe = Frame(root, width=int(0.5 * width1), height=int(0.33 * height1), bg='#87CEEB')

        labelframe10 = Frame(root, width=int(0.95 * width1), height=int(0.1 * height1), bg='white')
        labelframe10.place(x=int(0.025 * width1), y=int(0.025 * height1))
        labelframe.place(x=int(0.4 * width1), y=int(0.3 * height1))

        image1 = Image.open("logo.png")
        resized_image1 = image1.resize((90, 90), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image1)
        label1 = Label(labelframe10, image=test, bg='white')
        label1.image = test
        label1.place(x=1, y=1)
        l10 = Label(labelframe10, text="SkWeB", fg='orange', bg='white', font=("Algeria", 30))
        l10.place(x=90, y=13)
        l11 = Label(labelframe10, text="DataProcessing", fg='black', bg='white', font=("Algeria", 12))
        l11.place(x=400, y=18)
        l12 = Label(labelframe10, text="Data prediction", fg='black', bg='white', font=("Algeria", 12))
        l12.place(x=580, y=18)
        l13 = Label(labelframe10, text="View Generator", fg='black', bg='white', font=("Algeria", 12))
        l13.place(x=580+180, y=18)
        l13 = Label(labelframe10, text="Natural Language Processing", fg='black', bg='white', font=("Algeria", 12))
        l13.place(x=580+360, y=18)

        # declaring string variable
        # for storing name and password
        name_var = tk.StringVar()
        passw_var = tk.StringVar()

        def submit():

            name = name_var.get()
            password = passw_var.get()
            df1 = pd.read_excel("cred.xlsx", engine='openpyxl')
            for i in df1['password'][df1['username'] == name]:
                if (i == password):
                    login[0] = True
                    root.destroy()

            """if(df1['password'][df1['username'] == name]==password):
                print("success")"""

            name_var.set("")
            passw_var.set("")

        # creating a label for
        # name using widget Label
        name_label = tk.Label(labelframe, text='Username', font=('calibre', 15, 'bold'), bg='#87CEEB')
        name_label.place(x=10, y=10)

        # creating a entry for input
        # name using widget Entry
        name_entry = tk.Entry(labelframe, textvariable=name_var, font=('calibre', 15, 'normal'))
        name_entry.place(x=10, y=40)

        # creating a label for password
        passw_label = tk.Label(labelframe, text='Password', font=('calibre', 15, 'bold'), bg='#87CEEB')
        passw_label.place(x=10, y=80)

        # creating a entry for password
        passw_entry = tk.Entry(labelframe, textvariable=passw_var, font=('calibre', 15, 'normal'), show='*')
        passw_entry.place(x=10, y=120)

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(labelframe, text='    Login to access    ', command=submit, bg='orange')
        sub_btn.place(x=140, y=160)

        # placing the label and entry in
        # the required position using grid
        # method

        # performing an infinite loop
        # for the window to display
        root.mainloop()

    time_string = time.strftime('%H:%M:%S')







































    if (login[0]):
        top = Tk()

        width = top.winfo_screenwidth()

        height = top.winfo_screenheight()
        h1 = int((0.6) * height)

        top.geometry("%dx%d" % (width, height))
        canvas = Canvas(top, width=width, height=h1)
        canvas.place(x=0, y=0)

        img1 = (Image.open("backi.jpg"))

        resized_image = img1.resize((width, h1), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

        canvas.create_image(10, 10, anchor=NW, image=new_image)
        labelframe = Frame(top, width=int(0.9 * width), height=int(0.7 * height), bg='#87CEEB')

        labelframe10 = Frame(top, width=int(0.95 * width), height=int(0.1 * height), bg='white')
        labelframe10.place(x=int(0.025 * width), y=int(0.025 * height))

        w1 = Label(labelframe, text=f"{dt.datetime.now():%a, %b %d %Y}     " + time_string, fg="gray", bg="#87CEEB",
                   font=("helvetica", 9))
        width1 = labelframe.winfo_screenwidth()
        height1 = labelframe.winfo_screenheight()
        w1.place(x=int(0.55 * width1), y=65)
        labelframe.place(x=int(0.1 * width), y=int(0.2 * height))
        """im = "result{}.jpg".format(0)
        image5 = Image.open(im)
        resized_image5 = image5.resize((420, 380), Image.ANTIALIAS)
        test5 = ImageTk.PhotoImage(resized_image5)

        labelim5 = Label(labelframe, image=test5, bg='#87CEEB')
        labelim5.image = test5
        labelim5.place(x=20, y=80)"""





        datat=[0]
        tv = ttk.Treeview(labelframe, columns=(1, 2), show='headings', height=8)
        tv.column("#1", width=180)
        tv.column("#2", width=400)
        tv.heading(1, text="Type of Algorithm")
        tv.heading(2, text="Description of Algorithm")

        tv.place(x=460, y=160)



        def process_next():
            xtest1 = reqdata[0]
            websiteperdim = reqdata[1]
            boxes = reqdata[2]
            import random
            navbar = []
            div = []
            r = []
            ids = {}

            global pred1
            global tv
            global model_nikhil





            # view generator ends




            datat[0]+=1
            print(datat)
            global tv
            global l10,l11,l12,l13,l14


            def onclick1(event):
                selected = tv.identify('item', event.y, event.y)
                temp = tv.item(selected, 'values')
                print(selected)
                print(temp)
                key="i{}".format(str(datat[0])+","+str(selected))
                print(key)
                image5 = Image.fromarray(imgpro[key].astype(np.uint8))

                resized_image5 = image5.resize((420, 380), Image.ANTIALIAS)
                test5 = ImageTk.PhotoImage(resized_image5)

                labelim5 = Label(labelframe, image=test5, bg='#87CEEB')
                labelim5.image = test5
                labelim5.place(x=20, y=80)
            if(datat[0]==1):
                key = "i{}".format("1,0")
                print(key)
                image5 = Image.fromarray(imgpro[key])

                resized_image5 = image5.resize((420, 380), Image.ANTIALIAS)
                test5 = ImageTk.PhotoImage(resized_image5)

                labelim5 = Label(labelframe, image=test5, bg='#87CEEB')
                labelim5.image = test5
                labelim5.place(x=20, y=80)
                tv = ttk.Treeview(labelframe, columns=(1, 2), show='headings', height=8)
                tv.column("#1", width=180)
                tv.column("#2", width=400)
                tv.heading(1, text="Type of Algorithm")
                tv.heading(2, text="Description of Algorithm")
                tv.place(x=460, y=160)
                tv.insert(parent='', index=0, iid=0,values=("Selective Search", "It will draw the maximum rectangles around the image object"))
                tv.insert(parent='', index=1, iid=1,values=("Non Maximum Suppression", "Otimize to the best fit rectangle around object"))
                tv.bind('<Button-1>', onclick1)
                tv.focus_set()
                children = tv.get_children()
                tv.focus(children[-2])
                tv.selection_set(children[-2])
                l10 = Label(labelframe10, text="Image Upload", fg='black', bg='white', font=("Algeria", 12))
                l10.place(x=400 - 150, y=18)
                l11 = Label(labelframe10, text="DataProcessing", fg='blue', bg='white', font=("Algeria", 12))
                l11.place(x=400, y=18)
                l12 = Label(labelframe10, text="Data prediction", fg='black', bg='white', font=("Algeria", 12))
                l12.place(x=580, y=18)
                l13 = Label(labelframe10, text="View Generator", fg='black', bg='white', font=("Algeria", 12))
                l13.place(x=580 + 180, y=18)
                l14 = Label(labelframe10, text="Natural Language Processing", fg='black', bg='white',
                            font=("Algeria", 12))
                l14.place(x=580 + 360, y=18)
            elif(datat[0]==2):
                model_nikhil = pickle.load(open('model.pkl', 'rb'))
                pred = model_nikhil.predict(xtest1)
                pred1 = np.argmax(pred, axis=1)
                pred1
                xtest1=xtest1*255
                cl=["Button","Card - div","Footer","Image","Heading/Text","Navbar"]
                tv = ttk.Treeview(labelframe, columns=(1, 2), show='headings', height=8)
                tv.column("#1", width=180)
                tv.column("#2", width=400)
                tv.heading(1, text="SL")
                tv.heading(2, text="Predicted View")
                tv.place(x=460, y=160)
                tv.bind('<Button-1>', onclick1)


                for i in range(len(xtest1)):
                    key="i2,{}".format(i)
                    imgpro[key]=xtest1[i]

                    print(cl[pred1[i]],str(i))
                    tv.insert(parent='', index=i, iid=i, values=(str(i), cl[pred1[i]]))
                tv.focus_set()
                children = tv.get_children()
                tv.focus(children[0])
                tv.selection_set(children[0])
                key = "i{}".format("2,0")
                print(imgpro)
                image5 = Image.fromarray(imgpro[key].astype(np.uint8))

                resized_image5 = image5.resize((420, 380), Image.ANTIALIAS)
                test5 = ImageTk.PhotoImage(resized_image5)

                labelim5 = Label(labelframe, image=test5, bg='#87CEEB')
                labelim5.image = test5
                labelim5.place(x=20, y=80)

                l10 = Label(labelframe10, text="Image Upload", fg='black', bg='white', font=("Algeria", 12))
                l10.place(x=400 - 150, y=18)
                l11 = Label(labelframe10, text="DataProcessing", fg='black', bg='white', font=("Algeria", 12))
                l11.place(x=400, y=18)
                l12 = Label(labelframe10, text="Data prediction", fg='blue', bg='white', font=("Algeria", 12))
                l12.place(x=580, y=18)
                l13 = Label(labelframe10, text="View Generator", fg='black', bg='white', font=("Algeria", 12))
                l13.place(x=580 + 180, y=18)
                l14 = Label(labelframe10, text="Natural Language Processing", fg='black', bg='white',
                            font=("Algeria", 12))
                l14.place(x=580 + 360, y=18)
            elif(datat[0]==3):
                tv = ttk.Treeview(labelframe, columns=(1, 2), show='headings', height=8)
                tv.column("#1", width=180)
                tv.column("#2", width=400)
                tv.heading(1, text="SL")
                tv.heading(2, text="Predicted View")
                tv.place(x=460, y=160)
                tv.destroy()
                def createview(x1, y1, x2, y2, ind, q, boxes, t1, n1, t2, n2):
                    rid = random.randint(1, 2000)
                    ids[rid] = (t1, n1, t2, n2)

                    b = 'id="{}"'.format(rid)

                    s = 'style="position:absolute;left:{}%;top:{}%;width:{}%;height:{}%;"'.format(x1, y1, x2 - x1,
                                                                                                  y2 - y1)
                    if (abs(y2 - y1) > 30):
                        s = 'style="position:absolute;left:{}%;top:{}%;width:{}%;height:{}%;box-shadow: 1px 2px 4px lightgray;background-color:orange"'.format(
                            x1, y1, x2 - x1, y2 - y1)
                        str1 = '<div {} {}>'.format(b, s)
                        im = cv2.imread(r'C:\Users\poni3001\Downloads\sketchtest.png')
                        print("before", x1, y1, x2, y2)

                        txx1, tyx1, txx2, tyx2 = boxes[q][0], boxes[q][1], boxes[q][2], boxes[q][3]
                        print("after", txx1, tyx1, txx2, tyx2)
                        im = im[int(tyx1) + 50:int(tyx2) - 50, int(txx1) + 50:int(txx2) - 50]

                        rects1_nikhil = []

                        ss_nikhil = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

                        ss_nikhil.setBaseImage(im)

                        ss_nikhil.switchToSelectiveSearchQuality()

                        rects_nikhil = ss_nikhil.process()

                        numShowRects_nikhil = 100
                        increment = 50


                        imOut = im.copy()
                        imOut1 = im.copy()
                        shapex, shapey, _ = im.shape

                        for i, rect in enumerate(rects_nikhil):
                            if (i < numShowRects_nikhil):
                                x, y, w, h = rect
                                if (w * h > 0):
                                    rects1_nikhil.append([x, y, w, h])
                                    cv2.rectangle(imOut, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
                            else:
                                 break




                        boxes = []
                        for i in rects_nikhil:
                            a = [i[0], i[1], i[0] + i[2], i[1] + i[3]]
                            a = np.array(a)
                            boxes.append(a)
                        boxes = np.array(boxes)
                        boxes
                        treshold = 0.6

                        if len(boxes) == 0:
                            return []
                        xx1 = boxes[:, 0]
                        yx1 = boxes[:, 1]
                        xx2 = boxes[:, 2]
                        yx2 = boxes[:, 3]
                        areas = (xx2 - xx1 + 1) * (yx2 - yx1 + 1)
                        indices = np.arange(len(xx1))
                        for i, box in enumerate(boxes):
                            temp_indices = indices[indices != i]
                            xx1 = np.maximum(box[0], boxes[temp_indices, 0])
                            yy1 = np.maximum(box[1], boxes[temp_indices, 1])
                            xx2 = np.minimum(box[2], boxes[temp_indices, 2])
                            yy2 = np.minimum(box[3], boxes[temp_indices, 3])
                            w = np.maximum(0, xx2 - xx1 + 1)
                            h = np.maximum(0, yy2 - yy1 + 1)
                            overlap = (w * h) / areas[temp_indices]
                            if np.any(overlap) > treshold:
                                indices = indices[indices != i]
                        boxes = boxes[indices].astype(int)
                        innerxtest = []
                        for xx1, yx1, xx2, yx2 in boxes:
                            xx1, yx1, xx2, yx2 = xx1, yx1, xx2, yx2
                            """if(x1>1):
                                x1-=1
                            if(x2<shapex-1):
                                x2+=1
                            if(y1>1):
                                y1-=1
                            if(y2<shapey-1):
                                y2+=1"""
                            imgg = im[yx1:yx2, xx1:xx2]
                            # plt.matshow(imgg)
                            imgg = cv2.resize(imgg, (224, 224))
                            innerxtest.append(imgg)
                        innerxtest = np.array(innerxtest)
                        innerxtest1 = innerxtest / 255
                        innerpred = model_nikhil.predict(innerxtest1)
                        innerpp = np.argmax(innerpred, axis=1)
                        guiw, guih = (im.shape[1], im.shape[0])
                        boxes1 = boxes * np.array([100 / guiw, 100 / guih, 100 / guiw, 100 / guih])

                        for i in range(len(boxes)):
                            xx1, yx1, xx2, yx2 = boxes1[i][0], boxes1[i][1], boxes1[i][2], boxes1[i][3]
                            ind = innerpp[i]
                            q = i
                            print("checking", txx1 + boxes[i][0], tyx1 + boxes[i][1], txx1 + boxes[i][2],
                                  tyx1 + boxes[i][3])

                            str1 += createview(xx1, yx1, xx2, yx2, ind, q, boxes, txx1 + boxes[i][0] + 50,
                                               tyx1 + boxes[i][1] + 50, txx1 + boxes[i][2] + 50,
                                               tyx1 + boxes[i][3] + 50)
                        str1 += '</div>'
                        return str1

                    if (ind == 0):
                        s = 'style="position:absolute;left:{}%;top:{}%;padding:10px;background-color:green;color:white"'.format(
                            x1, y1)
                        return '<button {} {}>button - 1</button>'.format(b, s)
                    if (ind == 1):
                        return '<input {} type="text" name="fname" placeholder="Firstname" {}>'.format(b, s)

                    if (ind == 10):
                        return '<input {} type="checkbox" name="chk" value="Checkbox" {}>'.format(b, s)
                    if (ind == 3):
                        s = 'style="position:absolute;left:{}%;top:{}%;"'.format(x1, y1)
                        return '<img {} src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/2048px-Face-smile.svg.png" height=50px width=50px alt="Image not available" {}/>'.format(
                            b, s)
                    if (ind == 33):
                        return '<progress {} value = "65" max = "100" {}/>'.format(b, s)
                    if (ind == 4):
                        s = 'style="position:absolute;left:{}%;top:{}%;"'.format(x1, y1, x2 - x1, y2 - y1)
                        return '<h1 {} {}>Heading1</h1>'.format(b, s)
                    if (ind == 2):
                        s = 'style="position:absolute;left:{}%;top:{}%;background-color:black;color:white"'.format(x1,
                                                                                                                   y1)

                        return '<button {} {}>  Click Here  </button>'.format(b, s)
                    if (ind == 5):
                        st = '<div {} style="position:absolute;left:2%;width:96%;top:2%;height:10%;background-color:white;box-shadow: 1px 2px 4px lightgray"></div>'.format(
                            b)
                        navbar.append(st)

                for i in range(len(websiteperdim)):

                    t = pred1[i]
                    print("websiteperdim",websiteperdim[i])
                    print("tt", pred1[i])
                    x1, y1, x2, y2 = websiteperdim[i][0], websiteperdim[i][1], websiteperdim[i][2], websiteperdim[i][3]
                    view_posinds = t
                    cc = createview(x1, y1, x2, y2, view_posinds, i, boxes, boxes[i][0], boxes[i][1], boxes[i][2],
                                    boxes[i][3])
                    if (cc):
                        r.append(cc)
                st = ""
                for i in navbar:
                    st += i
                    print(i)
                for i in r:
                    st += i
                    print(i)
                dup = []
                img = cv2.imread(r'C:\Users\poni3001\Downloads\sketchtest.png')
                print(ids)
                keys = list(ids.keys())

                print(keys)
                for key in keys[::-1]:
                    if (ids[key] in dup):
                        continue
                    x1, y1 = int(ids[key][0]), int(ids[key][1])
                    x2, y2 = int(ids[key][2]), int(ids[key][3])
                    width, height = x2 - x1, y2 - y1
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    text = str(key)

                    cv2.putText(img, text, (x1, y2 + 20), font, 1, (255, 0, 0), thickness=3)
                    dup.append(ids[key])


                cv2.imwrite(r'C:\Users\poni3001\Downloads\idsimage.jpg', img)
                image1 = Image.fromarray(img)
                resized_image1 = image1.resize((420, 380), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(resized_image1)
                label1 = Label(labelframe, image=test, bg='white')
                label1.image = test
                label1.place(x=20, y=80)



                name_entry = Text(labelframe, height = 15,width = 75,bg = "white")
                name_entry.insert(END, st)
                name_entry.place(x=460, y=120)


                data1[0]+=st
                html = open(r'C:\Users\poni3001\Downloads\sketch.html', "w")
                html.write(data1[0])

                def web_view():

                    webbrowser.open(r'C:\Users\poni3001\Downloads\sketch.html')

                button_view = Button(labelframe, text="      View Webpage     ", bg="#FFA500", fg='black', command=web_view)
                button_view.place(x=800, y=370)







                l10 = Label(labelframe10, text="Image Upload", fg='black', bg='white', font=("Algeria", 12))
                l10.place(x=400 - 150, y=18)
                l11 = Label(labelframe10, text="DataProcessing", fg='black', bg='white', font=("Algeria", 12))
                l11.place(x=400, y=18)
                l12 = Label(labelframe10, text="Data prediction", fg='black', bg='white', font=("Algeria", 12))
                l12.place(x=580, y=18)
                l13 = Label(labelframe10, text="View Generator", fg='blue', bg='white', font=("Algeria", 12))
                l13.place(x=580 + 180, y=18)
                l14 = Label(labelframe10, text="Natural Language Processing", fg='black', bg='white',
                            font=("Algeria", 12))
                l14.place(x=580 + 360, y=18)
            elif (datat[0] == 4):
                img=cv2.imread(r'C:\Users\poni3001\Downloads\idsimage.jpg')
                image1 = Image.fromarray(img)
                resized_image1 = image1.resize((420, 380), Image.ANTIALIAS)
                test = ImageTk.PhotoImage(resized_image1)
                label1 = Label(labelframe, image=test, bg='white')
                label1.image = test
                label1.place(x=20, y=80)

                def jscode(ind, data):
                    print(ind, data)
                    if (ind == 0 and ('background' not in data[1])):
                        str = "document.getElementById" + "('" + data[
                            0] + "')" + ".onclick=function(){document.getElementById('" + data[
                                  0] + "')" + ".style.color='" + data[2] + "'}"
                    elif (ind == 0):
                        str = "document.getElementById" + "('" + data[
                            0] + "')" + ".onclick=function(){document.getElementById('" + data[
                                  0] + "')" + ".style.backgroundColor='" + data[2] + "'}"
                    elif (ind == 1 and ('background' not in data[1])):
                        str = "document.getElementById('" + data[0] + "')" + ".style.color='" + data[2] + "'"
                    elif (ind == 1):
                        str = "document.getElementById('" + data[0] + "')" + ".style.backgroundColor='" + data[2] + "'"
                    elif (ind == 2):
                        str = "document.getElementById" + "('" + data[0] + "')" + ".onclick=function(){window.open('" + \
                              data[1] + "')}"
                    elif (ind == 8):
                        str = "document.getElementById('" + data[0] + "')" + ".innerHTML='" + data[1] + "'"
                    elif (ind == 4):
                        str = "document.getElementById('" + data[0] + "').style.width=document.getElementById('" + data[
                            0] + "').getBoundingClientRect().width" + (data[1] + data[2]) + ";"
                        str += "document.getElementById('" + data[0] + "').style.height=document.getElementById('" + \
                               data[0] + "').getBoundingClientRect().height" + (data[3] + data[4]) + ";"
                    elif (ind == 5):
                        str = "document.getElementById('" + data[0] + "').style.top ='" + data[1] + "%';"
                    elif (ind == 6):
                        str = "document.getElementById('" + data[0] + "').style.left ='" + data[1] + "%';"
                    elif (ind == 7):
                        str = "document.getElementById('" + data + "').style.visibility='hidden'"
                    elif (ind == 3):
                        str = "document.getElementById('" + data[0] + "').placeholder = '" + data[1] + "'"

                    return str

                pattern = [
                    "click[a-z ]*id[a-z ]*(\d*)([a-z ]*)color[a-z ]* (red|blue|green|orange|yellow|purple|white|black)",
                    "[a-z ]*id[a-z ]*(\d*)([a-z ]*)color.*(red|blue|green|orange|yellow|purple|white|black)",
                    "click.*id[a-z ]*(\d*).* ([a-zA-Z0-9]*\.[a-z]*)",
                    '[a-zA-Z ]*(\d*)[a-zA-Z ]*placeholder[a-zA-Z ]*"(.*)"',
                    "id[a-z ]*(\d*) .*width .* (\+|-)(\d*) .* height .* (\+|-)(\d*)",
                    "[a-zA-Z ]*id[a-z ]*(\d*)[a-z ]*top[a-z ]*(\d*)", "[a-zA-Z ]*id[a-z ]*(\d*)[a-z ]*left[a-z ]*(\d*)",
                    "remove[a-zA-Z ]*id[a-zA-Z ]*(\d*)", '.*id[a-z ]*(\d*).*"(.*)"']


                def text_trigger(text):
                    for i in range(len(pattern)):
                        if (re.findall(pattern[i], text)):
                            return jscode(i, re.findall(pattern[i], text)[0])
                            break
                    else:
                        raise "Nikhil error"

                def send():
                    send = "You : " + e.get()

                    txt.insert(END, "\n" + send)


                    user = e.get()
                    try:
                        html = open(r'C:\Users\poni3001\Downloads\sketch.html', "w")

                        html.write(data1[0])
                        temp = "<script>{}</script>".format(text_trigger(user))
                        data1[0]+=temp
                        txt.insert(END, "\n" + "Bot  : Successfully changed")
                        tt="Successfully changed"

                        html = open(r'C:\Users\poni3001\Downloads\sketch.html', "w")

                        html.write(data1[0])
                        e.delete(0, END)
                    except:
                        txt.insert(END, "\n" + "Bot  : Invalid Command Check Sentences .." )
                        tt= "Invalid Command Check Sentences .. "
                        e.delete(0, END)








                BG_GRAY = "#ABB2B9"
                BG_COLOR = "#17202A"
                TEXT_COLOR = "#EAECEE"

                FONT = "Helvetica 14"
                FONT_BOLD = "Helvetica 13 bold"
                canvas = Frame(labelframe, width=600, height=300)
                canvas.place(x=460, y=120)
                lable1 = Label(labelframe, bg=BG_COLOR, fg=TEXT_COLOR, text="WebGPT", font=FONT_BOLD, pady=10, width=20,height=1)
                lable1.place(x=500,y=100)


                txt = Text(canvas, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=600)
                txt.place(x=10, y=10)

                scrollbar = Scrollbar(txt)
                scrollbar.place(relheight=1, relx=0.974)

                e = Entry(canvas, bg="white", fg="black", font=FONT, width=550)
                e.place(x=10, y=270)

                send = Button(canvas, text="Send", font=FONT_BOLD, bg="blue",fg="white",
                              command=send)
                send.place(x=540, y=270)











                l10 = Label(labelframe10, text="Image Upload", fg='black', bg='white', font=("Algeria", 12))
                l10.place(x=400 - 150, y=18)
                l11 = Label(labelframe10, text="DataProcessing", fg='black', bg='white', font=("Algeria", 12))
                l11.place(x=400, y=18)
                l12 = Label(labelframe10, text="Data prediction", fg='black', bg='white', font=("Algeria", 12))
                l12.place(x=580, y=18)
                l13 = Label(labelframe10, text="View Generator", fg='black', bg='white', font=("Algeria", 12))
                l13.place(x=580 + 180, y=18)
                l14 = Label(labelframe10, text="Natural Language Processing", fg='blue', bg='white',
                            font=("Algeria", 12))
                l14.place(x=580 + 360, y=18)
                button_next.destroy()
        def file():
            global img
            global labelim5
            global tv
            datat[0]=0

            f_types = [('Jpg Files', '*.jpg'),('Png Files', '*.png'),('Jpeg Files', '*.jpeg')]
            filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)
            print(filename)
            img = Image.open(filename[0])
            filesdata.insert(0,filename[0])
            resized_image5 = img.resize((420, 380), Image.ANTIALIAS)
            test5 = ImageTk.PhotoImage(resized_image5)



            #Selective Search

            cv2.setUseOptimized(True);
            cv2.setNumThreads(4);

            im_nikhil = cv2.imread(filesdata[0])
            newHeight = 200
            rects1_nikhil = []
            newWidth = int(im_nikhil.shape[1] * 200 / im_nikhil.shape[0])
            print(newWidth, newHeight)

            ss_nikhil = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

            ss_nikhil.setBaseImage(im_nikhil)

            ss_nikhil.switchToSelectiveSearchQuality()

            rects_nikhil = ss_nikhil.process()
            print(rects_nikhil)
            print('Total Number of Region Proposals: {}'.format(len(rects_nikhil)))

            numShowRects_nikhil = 200
            increment = 50
            imOut = im_nikhil.copy()
            imOut1 = im_nikhil.copy()
            shapex, shapey, _ = im_nikhil.shape
            for i, rect in enumerate(rects_nikhil):
                if (i < numShowRects_nikhil):
                    x, y, w, h = rect
                    if (w * h > 0):
                        rects1_nikhil.append([x, y, w, h])
                        cv2.rectangle(imOut, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
                else:
                    break
            imgpro['i1,0']=imOut

            #Selective Search ends


            #NMS start
            import numpy as np
            boxes = []
            for i in rects_nikhil:
                a = [i[0], i[1], i[0] + i[2], i[1] + i[3]]
                a = np.array(a)
                boxes.append(a)
            boxes = np.array(boxes)
            boxes

            def NMS(boxes, treshold):
                if len(boxes) == 0:
                    return []
                x1 = boxes[:, 0]
                y1 = boxes[:, 1]
                x2 = boxes[:, 2]
                y2 = boxes[:, 3]
                areas = (x2 - x1 + 1) * (y2 - y1 + 1)
                indices = np.arange(len(x1))
                for i, box in enumerate(boxes):
                    temp_indices = indices[indices != i]
                    xx1 = np.maximum(box[0], boxes[temp_indices, 0])
                    yy1 = np.maximum(box[1], boxes[temp_indices, 1])
                    xx2 = np.minimum(box[2], boxes[temp_indices, 2])
                    yy2 = np.minimum(box[3], boxes[temp_indices, 3])
                    w = np.maximum(0, xx2 - xx1 + 1)
                    h = np.maximum(0, yy2 - yy1 + 1)
                    overlap = (w * h) / areas[temp_indices]
                    if np.any(overlap) > treshold:
                        indices = indices[indices != i]
                return boxes[indices].astype(int)

            boxes = NMS(boxes, 0.6)
            reqdata.insert(2, boxes)
            boxes
            shapex, shapey, _ = im_nikhil.shape  # Print image shape


            newdata = []
            for x1, y1, x2, y2 in boxes:
                x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 + 1, y2 + 1
                cv2.rectangle(imOut1, (x1, y1), (x2, y2), (0, 255, 0), 1, cv2.LINE_AA)


            imgpro['i1,1']=imOut1

            #NMS ends

            import numpy as np
            import matplotlib.pyplot as plt
            imOut = im_nikhil.copy()

            xtest = []
            print("boxes dimensions", boxes)
            for x1, y1, x2, y2 in boxes:
                x1, y1, x2, y2 = x1, y1, x2, y2

                imgg = im_nikhil[y1:y2, x1:x2]
                imgg = cv2.resize(imgg, (224, 224))


                #cv2.imshow("test", imgg)

                xtest.append(imgg)
            xtest =np.array(xtest)
            print(xtest[3])
            xtest1 = xtest / 255
            plt.matshow(xtest1[5])
            print(xtest1.shape)

            reqdata.insert(0,xtest1)



            #view generator starts

            guiw, guih = (im_nikhil.shape[1], im_nikhil.shape[0])
            websiteperdim = boxes * np.array([100 / guiw, 100 / guih, 100 / guiw, 100 / guih])
            reqdata.insert(1, websiteperdim)











            labelim5 = Label(labelframe, image=test5, bg='#87CEEB')
            labelim5.image = test5
            labelim5.place(x=20, y=80)
            tv = ttk.Treeview(labelframe, columns=(1, 2), show='headings', height=8)
            tv.column("#1", width=180)
            tv.column("#2", width=400)
            tv.heading(1, text="Type of Algorithm")
            tv.heading(2, text="Description of Algorithm")
            tv.insert(parent='', index=0, iid=0,values=("Image Extraction", "Sketched Image extracted using filedialog tkinter"))
            #tv.bind('<Button-1>', onclick)
            tv.focus_set()
            children = tv.get_children()
            tv.focus(children[-1])
            tv.selection_set(children[-1])

            tv.place(x=460, y=160)
            button_upload.destroy()
            l10 = Label(labelframe10, text="Image Upload", fg='blue', bg='white', font=("Algeria", 12))
            l10.place(x=250, y=18)
            l11 = Label(labelframe10, text="DataProcessing", fg='black', bg='white', font=("Algeria", 12))
            l11.place(x=400, y=18)
            l12 = Label(labelframe10, text="Data prediction", fg='black', bg='white', font=("Algeria", 12))
            l12.place(x=580, y=18)
            l13 = Label(labelframe10, text="View Generator", fg='black', bg='white', font=("Algeria", 12))
            l13.place(x=580 + 180, y=18)
            l13 = Label(labelframe10, text="Natural Language Processing", fg='black', bg='white',
                        font=("Algeria", 12))
            l13.place(x=580 + 360, y=18)



        image1 = Image.open("logo.png")
        resized_image1 = image1.resize((90, 90), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image1)
        label1 = Label(labelframe10, image=test, bg='white')
        label1.image = test
        label1.place(x=1, y=1)
        l10 = Label(labelframe10, text="SkWeB", fg='orange', bg='white', font=("Algeria", 30))
        l10.place(x=90, y=13)
        button_upload = Button(labelframe10, padx=7, pady=7,text="      Upload Image      ", bg="blue", fg='white',command=file)
        button_upload.place(x=900, y=13)




        def open_view():
            top_view = Toplevel(top)
            top_view.geometry("500x500")
            top_view.configure(bg='#87CEEB')
            selected = tv.focus()
            temp = tv.item(selected, 'values')
            if (temp[1] == '-'):
                image5 = Image.open("result.png")
                resized_image5 = image5.resize((500, 500), Image.ANTIALIAS)
                test5 = ImageTk.PhotoImage(resized_image5)

                labelim5 = Label(top_view, image=test5, bg='#87CEEB')
                labelim5.image = test5
                labelim5.place(x=0, y=0)
            else:

                imagelog = Image.open("logo.png")
                resized_imagelog = imagelog.resize((40, 40), Image.ANTIALIAS)
                testlog = ImageTk.PhotoImage(resized_imagelog)

                labellog = Label(top_view, image=test, bg='#87CEEB')
                labellog.imagelog = testlog
                labellog.place(x=1, y=10)
                print(selected)

                """df['Name'][df['Number_Plate'] == temp[0]].values[0]"""

                l4 = Label(top_view, text="UTP SAFETY AND SECURITY DEPARTMENT", bg='#87CEEB', fg='black',
                           font=('Arial', 13))
                l4.place(x=90, y=30)
                l1 = Label(top_view, text="Student Name :   " + temp[4], bg='#87CEEB')
                l1.place(x=260, y=180)
                l2 = Label(top_view, text="Vehicle Number :   " + temp[0],
                           bg='#87CEEB')
                l2.place(x=260, y=200)
                l3 = Label(top_view, text="Model name : " + temp[2], bg='#87CEEB')
                l3.place(x=260, y=220)
                l30 = Label(top_view, text="Address : " + df['address'][df['Number_Plate'] == temp[0]].values[0],
                            bg='#87CEEB')
                l30.place(x=260, y=240)

                imagelog1 = Image.open("idcard.jpeg")
                resized_imagelog1 = imagelog1.resize((200, 300), Image.ANTIALIAS)
                testlog1 = ImageTk.PhotoImage(resized_imagelog1)

                labellog1 = Label(top_view, image=testlog1, bg='white')
                labellog.imagelog1 = testlog1
                labellog1.place(x=40, y=80)

                """"fr=Frame(top_view,width=300,height=400)
                fr.configure(bg='#87CEEB')
                fr.place(x=25,y=200)
                list=[("Index","Details"),("Student name",temp[2]),("Vehicle name",temp[0]),("Model name",temp[2])]

                for row in range(4):
                    for col in range(2):
                        e=Entry(fr,width=30,bg='#87CEEB',fg='black')

                        e.grid(row=row,column=col)
                        e.insert(END,list[row][col])
                        e.configure(state='readonly',bg='#87CEEB')"""
            """l5=Label(top_view,text="You have a pending amountat Can -Stop cantina or 1580222",bg='#87CEEB')
            l5.place(x=80, y=430)"""

        def down_pdf():
            selected = tv.focus()
            temp = tv.item(selected, 'values')
            pdf = FPDF()
            pdf.add_page()
            pdf.image("logo.png", x=5, y=2, w=20, h=20, type='', link='')
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 5, txt="SAFETY AND SECURITY DEPARTMENT", ln=1,
                     align='C')
            pdf.cell(200, 20, txt="Name :   " + df['Name'][df['Number_Plate'] == temp[0]].values[0], ln=2, align='L')
            pdf.cell(200, 5, txt="Vehicle Number :   " + temp[0], ln=3, align='L')
            pdf.cell(200, 5, txt="ID : " + temp[1], align='R')

            epw = pdf.w - 2 * pdf.l_margin

            # Set column width to 1/4 of effective page width to distribute content
            # evenly across table and page
            col_width = epw / 2

            # Since we do not need to draw lines anymore, there is no need to separate
            # headers from data matrix.
            varai = df['address'][df['Number_Plate'] == temp[0]].values[0]

            data = [["Date", "Address"], [temp[3], varai]]

            # Text height is the same as current font size
            th = pdf.font_size

            pdf.set_font('Times', 'B', 14.0)
            pdf.cell(epw, 0.0, '', align='C', ln=5)
            pdf.set_font('Times', '', 10.0)
            pdf.ln(7)

            # Here we add more padding by passing 2*th as height
            for row in data:
                for datum in row:
                    # Enter data in colums
                    pdf.cell(col_width, 2 * th, str(datum), border=1)

                pdf.ln(2 * th)

            pdf.cell(200, 10, txt="---------   THANKYOU   --------", ln=8, align='C')
            pdf_name = "" + temp[0] + ".pdf"

            pdf.output(pdf_name)



        button_next = Button(labelframe, text="Next Step ->", bg='#0047AB', fg='white', padx=7, pady=7,
                             command=process_next)
        button_next.place(x=950, y=470)



        label2 = Label(labelframe, text="SKETCH AND ALGO TO WEB TRANSLATION", font=("Arial", 24), bg='#87CEEB')
        label2.place(x=int(0.15 * width1), y=10)

        label2 = Label(labelframe, text="", font=("Arial", 10), bg='#87CEEB')
        label2.place(x=int(0.225 * width1), y=50)
        label1.place(x=10, y=10)
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        top.mainloop()
extract_num()



