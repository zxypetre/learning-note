`pwd` 显示当前目录 
`git init` 创建git仓库
`git add`  在git中添加文件
`git commit -m '修改信息'`  提交文件（既修改信息）
`git status`  查看git库的状态
`git diff`  查看修改了哪些
`git diff HEAD -- 文件名`    查看文件修改了哪些 哪些在暂存区还没提交
`git checkout -- 文件名`    回到文件最后一次commit前的状态
`git config --global core.quotepath false`     git status 解决中文乱码
* global命令使配置对所有项目生效，没有global则对当前配置生效。
* 全局配置修改的内容在根目录的.gitconfig中 当前修改的在当前的目录的.gitconfig中