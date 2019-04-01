#猜单词游戏，在实际应用中把输入的单词从文件读取或者在源码中修改直接写好。
#定义函数
def guessWord(word):
    print("play the game:")
    wrong=0
    getWords=list(word)
    bind=["_"]*len(word)
    win= False
    gragh=["————————————————————",
      "|           |",
	  "|           |",
	  "|           o",
	  "|           |",
	  "|          /|\ ",
	  "|          /|\ "
	  ]
    while wrong<len(word)-1:
        charater=input()
        if charater in getWords:
            print("祝贺你答对了，加油哦")
            c_index=getWords.index(charater)
            bind[c_index]=charater
            getWords[c_index]='$'
        else:
            wrong+=1
            if wrong<len(gragh)+1:
                for i in range(wrong):
                    print(gragh[i])
			#print(gragh[0:wrong+1])
        if "_" not in bind:
            print("你赢了")
            win=True
            break
    if not win:
        print("你输了")

#打印图像
import os
wpath=os.path.join("D:\\","practiceForPython","word.txt")
with open(wpath,'r') as f:
    myword=f.read().strip('\n')
print("如果要修改单词，请到word.txt的修改单词")
print(myword)
guessWord(myword)


