# MOVIELENS
# ****__这个项目用于展示通过训练movielens数据集对用户进行电影推荐
__项目初期，需要用到很多包，例如numpy、pandas、sklearn、os、math等等，本人是缺什么包就在cmd命令行下面pip什么包，后来在
__实际运行中发现很多问题：pip自己安装的包，只安装该包所依赖的包，并非该包完整的包，在实际导入中会出现诸多can't find __module这类的问题，很让人蛋疼。
****笔者总结后给出一个这类问题的解决方案：强烈建议不要偷懒使用pip，应当去官网上自己手动下载相应的安装包后缀名为.whl
给出一个网址，该网址包含了python目前几乎所有的版本的安装包  
[Python各安装包](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy "Python安装包")
下载完之后再手动pip install 路径\文件名.whl
## 使用pandas对数据集进行读取查看操作
下载完movielens数据集后




