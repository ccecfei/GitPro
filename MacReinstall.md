# 重装后
* 开启root帐户
* Terminal配色
	1. github仓库 solarized, osx-terminal.app-colors-solarized/
	2. 两种配置，dark ansi, light ansi,双击即可导入

# Mac os 安装各种包

* 用brew 和 brew cask 管理各种Mac软件
* 用pip管理各种python软件
* 用Git管理各种文档

## 必备工具类

---
### Homebrew
* 安装(比较久)
	`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* mac os 的包管理工具
* 可以用来 安装&升级 各种mac工具，如git python等
* brew常用指令 :

	``` 
	brew info xx(xx需要是全名)
	brew search xx(xx支持部分搜索)
	brew update
	brew upgrade
	brew insatll
	```
		
### Brew cask

* 主页`http://caskroom.github.io/`
* 注意用利用brew来安装brew cask
* 类似于homebrew，只不过homebrew提供的都是command line的，cask都是gui的
	1. brew cask install google-chrome
	2. brew cask install sublime-text


## pip (github上可以搜到)
* homebrew已经自带了pip
* python 的包管理工具
* 可以用来 安装&升级 各种python库，如django等

## python
* brew install python3(安装python3的时候，homebrew会自动安装pip)

* pip3 install --user pipenv (--user的意思是安装在用户目录，而不是全局)
	> 装好后，要把环境变量配一下。  
	在 Linux 和 macOS 上，运行 python -m site --user-base 找到用户基础目录，然后把 bin 加到目录末尾。  
	比如，上述命令典型地会打印出 ~/.local``（ ``~ 会扩展为您的家目录的局对路径），  
	然后将 ~/.local/bin 添加到 PATH 中。您可以通过 修改 ~/.profile(mac下是.bash_profile) 永久地设置 PATH。

* 强制使用pipevn
	
	在.bash_profile下面加入export PIP_REQUIRE_VIRTUALENV=true


* pipenv的使用
	> 在项目目录下，直接安装包 pipenv install requests  
	使用安装好的包，pipenv run python main.py


### Git

安装步骤

1. brew install git
2. brew install bash-completion(补全，注意有两个版本，1支持3.X的bash，2支持4.X的bash)
3. 然后加一段话到.bash_profile，重启terminal之后，补全才能生效
	
	```bash
	if [ -f $(brew --prefix)/etc/bash_completion ]; then
    	. $(brew --prefix)/etc/bash_completion
	fi
	```



---
## 普通类

* sublime 3

	```
	github 找秘钥
	安装 package control
	CMD+SHIFT+P
	```
* 新建快捷方式: option＋command 然后拖到桌面




















