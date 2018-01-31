import os
def rename():
    path='D:\\XX\\XX'
    cnt = 1
    prename = "000000"
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files)#原来的文件路径
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue
        filename=os.path.splitext(files)[0]#文件名
        filetype=os.path.splitext(files)[1]#文件扩展名
        
        #style 1: 00000XX
        Newdir=os.path.join(path,prename[0:len(prename)-len(str(cnt))]+str(cnt)+filetype);#新的文件路径
        
        #style 2:imagesXX
        #Newdir=os.path.join(path,'images'+str(cnt)+filetype);
        
        os.rename(Olddir,Newdir);#重命名
        cnt+=1;
rename();
