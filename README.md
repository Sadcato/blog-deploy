# 部署小程序说明

这是一个用于自动执行Hexo命令的部署小程序。该程序会在当前目录下依次执行 `hexo clean`、`hexo generate` 和 `hexo deploy` 命令，以便于用户将Hexo博客内容自动生成并部署到远程服务器上。

## 主要功能

- 清理旧的Hexo生成的文件
- 生成静态文件
- 部署生成的静态文件到远程服务器

## 使用方法

### 前提条件

- 安装 [Python](https://www.python.org/downloads/)（推荐使用3.8及以上版本）
- 安装 [PyInstaller](https://www.pyinstaller.org/)
- 安装 [Git](https://git-scm.com/)
- 配置好Hexo博客环境


### 步骤
1. **克隆或下载此仓库**
```bash
   git clone [https://github.com/yourusername/yourrepository.git](https://github.com/Sadcato/blog-deploy.git)
   cd yourrepository
```
2. **修改 deploy.py 文件**
修改为本地git bash的bash.exe文件地址
```bash
run_command(f'D:\git\Git\bin\bash.exe -c "{command}"')
```
3. **使用PyInstaller生成EXE文件**
   在命令行中运行以下命令，将Python脚本打包成EXE文件：
```bash
pyinstaller --onefile deploy.py
```
这将生成一个 dist 目录，其中包含 deploy.exe 文件。  

4. **运行EXE文件**
双击 dist 目录中的 deploy.exe 文件，它将在当前目录下执行Hexo命令。













