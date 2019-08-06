#更多文档操作可以见http://www.tcl.tk/man/tcl8.6/TkCmd/text.htm#M85
#encoding=utf-8
from tkinter import filedialog
import tkinter as tk
class Note():
    def __init__(self):
        self.mytk=tk.Tk()
        self.creatUI() #设置菜单
        self.mytk.mainloop() #展示界面
    def creatUI(self):
        menubar=tk.Menu(self.mytk)
        #定义一个空菜单单元
        filemenu=tk.Menu(menubar,tearoff=0)
        #将空菜单单元绑定到menu中，标签为file
        menubar.add_cascade(label='File',menu=filemenu)
        #在filemenu中添加相应的操作
        filemenu.add_command(label='new',command=self.creatFile)
        filemenu.add_command(label='open',command=self.openFile)
        filemenu.add_command(label='save',command=self.saveFile)
        #定义一个空菜单单元
        editmenu=tk.Menu(menubar,tearoff=0)
        #将空菜单单元绑定到menu中，标签为file
        menubar.add_cascade(label='Edit',menu=editmenu)
        #在editmenu中添加相应的操作
        editmenu.add_command(label='cut',command=self.cutContent)
        editmenu.add_command(label='copy',command=self.copyContent)
        editmenu.add_command(label='paste',command=self.pasteContent)
        self.mytk.config(menu=menubar)
        self.mytext=tk.Text(self.mytk)
        self.mytext.pack()
    def creatFile(self):
        #先保存正在工作的文档，再新建空文档
        self.saveFile() 
        self.work_filename=''
        self.mytext.delete('1.0','end')
    def openFile(self):
        self.work_filename=filedialog.askopenfilename()
        with open(self.work_filename,'rb') as f:
            var=f.read()
            #删除文本框中的原本的内容，覆盖为新文件中的内容
            self.mytext.delete(1.0) 
            self.mytext.insert('insert',var)
            f.close()
    def saveFile(self):
        var=self.mytext.get('1.0','end')
        #如果要打开的文档，则保存打开的文档，否则新建一个文档保存数据
        if len(self.work_filename):
            with open(self.work_filename,'wb') as f:
                f.write(var.encode())
                f.close()
        else:
            temp_filename=filedialog.asksaveasfilename()
            with open(temp_filename,'wb') as f:
                f.write(var.encode())
                f.close()
    #复制同时把当前选择内容删除，选择的内容可以sel的tag表示，可以用sel.first和sel.last来寻址
    def cutContent(self):
        self.tempVar=self.mytext.get('sel.first','sel.last')
        self.mytext.delete('sel.first','sel.last')
    #复制选择的内容
    def copyContent(self):
        self.tempVar=self.mytext.get('sel.first','sel.last')
    #粘贴在剪贴版上的内容
    def pasteContent(self):
        self.mytext.insert('insert',self.tempVar)
if __name__=='__main__':     
    Note()
