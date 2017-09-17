# Mac os 安装各种包

* 用brew 和 brew cask 管理各种Mac软件
* 用pip管理各种python软件
* 用Git管理各种文档

## 必备工具类

---
### Homebrew

* mac os 的包管理工具
* 可以用来 安装&升级 各种mac工具，如git python等
* 在Github上可找到安装brew的Raby脚本
* brew常用指令 :

	``` 
	brew info xx(xx需要是全名)
	brew search xx(xx支持部分搜索)
	brew update
	brew upgrade
	brew insatll
	```
		
### Brew cask

* 注意用利用brew来安装brew cask
* 类似于homebrew，只不过homebrew提供的都是command line的，cask都是gui的
* 主页`http://caskroom.github.io/`

## pip (github上可以搜到)
* python 的包管理工具
* 可以用来 安装&升级 各种python库，如django等

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
	



















