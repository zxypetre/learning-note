# git-branch
1. git branch testing   
   git checkout testing   
   以上两条命令可替换为(git checkout -b testing)   
   git branch可以查看分支(当前分支会用*标记)
2. 然后正常git add ...  
   git commit -m ''   提交文件
3. git checkout master  切换master分支(提交的文件会不见)
4. git merge testing  合并分支
5. git merge --no-ff testing  不使用fast forword的模式合并分支。可以查看到分支合并情况
6. git branch -d testing  删除testing分支
7. git log --graph --pretty=oneline --abbrev-commit  查看提交情况(可看到分支合并情况)
8. git stash 储存当前进度
9. git stash list 可以查看是否有储存
10. git stash apply(git stash pop) 可以恢复进度(恢复进度的同时删除储存的进度)
11. git stash drop 删除储存的进度
12. git stash apply stash@{0}  储存了多个进度的时候恢复某个进度 
13. git branch -D testing 分支提交后未合并前删除分支 
14. git remote  查看远程库的信息(-v参数可查看更详细信息)
15. git push origin master(dev) 将本地master(dev)分支推送到远程库
