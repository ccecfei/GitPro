# GitPro Notes


### 注意点

直接记录快照，而非差异比较


### git config

* --system参数
	* 设置/etc/gitconfig文件  
	* 针对所有用户
	
* --global参数 
	* 设置〜/.gitconfig文件
	* 当前用户(name, email都用这个选项吧)

* 不带参数
	* git目录中的config文件
	* 针对该仓库

* 设置用户信息

```
	git config user.name 'xxx'
	git config user.email xxx@xx.com
```

* 显示所有配置信息
	* git config --list

* 显示指定的配置信息

```
	git config <key>
	eg: git config user.name
```


### .gitignore

* 对某个仓库来说，如果某类型的文件，是该仓库的所有用户都需要忽略的，那么配置在gitignore里面
	* 因为gitignore会放入仓库的版本控制中，其它人clone的时候就一起下载了

* 如果仅仅是本用户忽略，则配置在exclude里面

* 两者的路径都是：$GIT_DIR/.git/info/下面

* 规则

```
	'#':表示本行为注释
	'!':取反

	使用简化正则：
		* : 0到多个字符
		[]: []内的任意一个
		? : 任意一个字符
		**: 任意中间目录，如a/**/c

	可以去github上找到大神设置好的，各种语言的ignore
```


### 获取帮助
* git help config


## 基础操作

### git init
* 在某个目录下执行git init,则会把这个目录初始化为一个仓库


### git add filename

* 参数可以是目录或文件
* 用来把某个文件或某个目录下的所有文件加入跟踪


### git clone url

每种协议都有自己的利弊,url支持下面几种协议：

1. https
2. git 
1. ssh



### 文件始终处于四种状态之一

1. untracked
2. unmodified
3. modified
1. staged


### git status

查看当前仓库文件状态
	
* -s(--short)

```
	A 新添加,已add到暂存区
	M ：
		M :左M modified,且放入了暂存区
		 M:右M modified,未放入暂存区
		MM:双M modified放入暂存区后，又进行了修改
```


### git diff

* 不加参数：比较工作区与暂存区
* --staged:已暂存，下次将要提交的内容


### git commit -m "commit log"

* 每一次运行提交操作，都是对你项目作一次快照，以后可以回到这个状态，或者进行比较。
* -a: 跳过暂存区，将工作区的修改，直接提交到仓库
	* eg: git commit -a -m "commit log"


### git rm

* 删除工作区某文件，并且会从电脑删除此文件
* -f(force): 删除暂存区的文件


### git mv file_from file_to

移动文件（文件重命名）

### git log 

* 显示提交的log
* -p 显示每次提交的diff
* -n 显示最近n次提交
* -stat 显示每次提交的简略统计信息
* --pretty=format 以指定的格式显示，具体参考文档吧
* 时间参数
	* --after(since)='YYYY-MM-DD' 自某天以来
	* --before(until)='YYYY-MM-DD' 到某天为止
	* --after=2.weeks 最近两周
	
* --oneline 一条log显示在一行上
* --graph
	* git log --oneline --graph

* 可以用grep对log进行搜索 

### 撤消 undo

* `git commit --amend -m "log"`
	* 追加提交
	* 如果上次提交有文件漏add了，或者提交log需要修改

* `git reset HEAD <file>`
	* 撤消暂存区中，被多add的文件

* `git checkout -- <file>`
	* 注意空格
	* 丢弃工作区且还没放到暂存区的修改，使文件回到未修改状态


### 作者&提交者

* 作者：写此段代码的人，可以看作是workspace->staged阶段
* 提交者：把修改并入仓库的人，staged->仓库





### 远程仓库操作

* `git remote -v`
	* 显示远程仓库

* `git remot show [remotename]`
	* 显示指定远程库的详细信息

* `git remote add <shortname> <url>`
	* 关联远程仓库url, 并将此关联用shortname作为简写，以后可以用shortname来引用
	* add 的时候支持多种协议：
		1. https
			* `git remote add origin https://github.com/ccecfei/GitPro`
			* 把github上的GitPro与本地关联，并且缩写名为origin
		2. ssh协议
			* `git remote add origin git@github.com:ccecfei/GitPro.git`
			* 功能和上面一样，只不过协议用ssh

* `git remote rename src_name dest_name`
	
	重命名src_name为dest_name

* `git remote remove <shortname>`

	删除和远程库的关联

* `git push [remote-name] [branch-name]`

	eg:`git push origin master`


* `git fetch <remotename>`与`git pull`的区别
	*  `git fetch`拉取最新提交，并更新fetch_head
	*  `git pull`做了fetch的工作后，还会多一步自动merge到当前分支




























































