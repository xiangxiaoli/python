# python
使用auto-py-to-exe将python程序变成window可运行的exe，首先是到GitHUb（地址：https://github.com/brentvollebregt/auto-py-to-exe.git）上面下载压缩包
然后解压到指定的文件夹下面，在非联网状态下第一次安装失败，报告的错误是pip安装的版本不对，后来联网后把pip更新到最新的版本，再安装就成功了。步骤有三步：
You can run this project locally by following these steps:

   1. Clone/download the repo
   2. Open cmd/terminal and cd into the project
   3. Execute python -m pip install -r requirements.txt

Now to run the application, execute python -m auto_py_to_exe. A Chrome window in app mode will open with the project running inside.

    Make sure you are in the directory below auto_py_to_exe (you will be after step 3) when calling python -m auto_py_to_exe or you will need to reference the folder auto_py_to_exe absolutely/relatively to where you currently are.
