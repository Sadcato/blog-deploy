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
