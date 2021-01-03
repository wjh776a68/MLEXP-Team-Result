//Author: wjh776a68
//Datetime: 2021/01/03 15:15
//Function: The GUI Client for ours Machine-learning Project

var folderpath	//全局图片文件夹路径
var destinefile="final.jpg" //目标图片文件名称
var software_title="Photo_Combine"
var part_picture_path=null
var result_picture_path=null

function 浏览框0_选择改变()
    
    folderpath=browsegettext("浏览框0") 
    add_listview()
end


function add_listview()
    
    var file_save_array,folder_save_array
    filetraverse(folderpath,file_save_array,folder_save_array)
    var file_len = arraysize(file_save_array)
    for(var i = 0;i < file_len;i++)
        if(file_save_array[i]==destinefile)
            continue
        end
        listaddtext("列表框0",file_save_array[i]) 
    end
end


function 列表框0_选择改变()
    //这里添加你要执行的代码
    
    picturesetpicture("图片框0",folderpath & "\\" & listgetchecktext("列表框0")) 
    part_picture_path=folderpath & "\\" & listgetchecktext("列表框0")
    controlenable("按钮0",true)
    
    
end


function 按钮0_点击()
    var 路径=sysgetcurrentpath()
    var i=0
    //cmd(路径 & "\\Python\\python.exe OpenCVStitch.py " & folderpath,true)
    if(fileexist(folderpath & "\\" & destinefile)==1)
        filedelete(folderpath & "\\" & destinefile)
    end
    progresssetprogress("进度条0",5*i)
    sleep(1000,false)
    i=i+1
    //var 句柄 = openprocessex(路径 & "Python\\python.exe",路径 & "Python\\OpenCVStitch.py " & folderpath)
    //messagebox("python " & 路径 & "Python\\OpenCVStitch.py " & folderpath)
    cmd("python " & 路径 & "Python\\OpenCVStitch.py " & folderpath,true)
    while(i<20 && fileexist(folderpath & "\\" & destinefile)==0)
        progresssetprogress("进度条0",5*i)
        sleep(1000,false)
        i=i+1
    end
    
    while(fileexist(folderpath & "\\" & destinefile)==0)
        i=i+1
        sleep(1000,false)
        
        if(i>120)
            messagebox("全景图片生成异常,请尝试使用其他图片组.\r\n如有需要请在github项目进行反馈!",software_title)
            return -1
        end
    end
    
    progresssetprogress("进度条0",99)
    picturesetpicture("图片框1",folderpath & "\\" & destinefile)
    result_picture_path=folderpath & "\\" & destinefile
    controlenable("按钮1",true)
    sleep(1000)
    progresssetprogress("进度条0",0)
    messagebox("全景图生成完成",software_title)
    
end




function 按钮1_点击()
    
    cmd("explorer " & folderpath,true)
    
end


function photo_combine_初始化()
    
    //messagebox("检测到本台电脑尚未安装环境,是否现在进行安装?")
    messagebox("本软件正常运行需提前安装:\r\n        python>=3.6\r\n        opencv-python>=3.1\r\n        opencv-contrib-python>=3.1\r\n如未安装请提前自行安装!",software_title)
end


function 按钮2_点击()
    messagebox("    全景图像生成器 V1.0\r\n项目地址: https://github.com/try-better/photo_combine",software_title)
end


功能 图片框0_左键单击()
    
    cmd("explorer " & part_picture_path,true)
    
结束


功能 图片框1_左键单击()
    //这里添加你要执行的代码
    cmd("explorer " & result_picture_path,true)
结束
