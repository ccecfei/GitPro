《 GitPro 》

直接记录快照，而非差异比较


初次运行配置：
1. git config

a. 设置/etc/gitconfig文件
	--system 
	针对所有用户

b. 设置〜/.gitconfig文件
	--global
	当前用户

c. git目录中的config文件
	针对该仓库

设置用户信息
	git config user.name 'xxx'
	git config user.email xxx@xx.com
显示配置信息
	git config --list

获取帮助
	git help config


