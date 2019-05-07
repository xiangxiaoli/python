# python
一、开始使用python进行编程

（一）搭建python开发环境

1.登陆https://www.python.org/downloads/release/python-373/ 下载供windows使用的python安装包；或者登陆百度网盘下载

2.一路next安装到指定的文件夹，然后添加所在的文件夹到环境变量Path下面，按住win+R运行cmd命令，然后在cmd 环境中输入python -v,输出版本信息则证明安装成功，否则就是不成功。

      Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
      Type "help", "copyright", "credits" or "license" for more information.
      import 'atexit' # <class '_frozen_importlib.BuiltinImporter'>
3.使用auto-py-to-exe将python程序变成window可运行的exe，首先是到GitHUb（地址：https://github.com/brentvollebregt/auto-py-to-exe.git） 上面下载压缩包，然后解压到指定的文件夹下面，在非联网状态下第一次安装失败，报告的错误是pip安装的版本不对，后来联网后把pip更新到最新的版本，再安装就成功了。步骤有三步：
    You can run this project locally by following these steps:
    
       1. Clone/download the repo
       2. Open cmd/terminal and cd into the project
       3. Execute python -m pip install -r requirements.txt
    
    Now to run the application, execute python -m auto_py_to_exe. A Chrome window in app mode will open with the project running inside.

        Make sure you are in the directory below auto_py_to_exe (you will be after step 3) when calling python -m auto_py_to_exe or you   will   need to reference the folder auto_py_to_exe absolutely/relatively to where you currently are.
 4.安装notepad++，并将notepad++设置为python开发环境，设置步骤见文档
