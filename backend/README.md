# SchoolForum-backend

## 部署与运行

本项目使用[Astral uv](https://docs.astral.sh/uv/)作为包管理工具。

### 1. 安装依赖

```bash
uv sync
```

### 2. 配置与初始化数据库

本项目在`app/config.py`中提供了三种不同场景下的的配置。分别修改其中的`SQLALCHEMY_DATABASE_URI`属性为想要使用的PostgreSQL服务器URL。

之后，执行以下命令初始化数据库：

```bash
# <model_name> 的可用取值为：prod, dev, test
uv run flask --app 'app:create_app("<mode_name>")' initdb
# uv run flask initdb 与 uv run flask --app 'app:create_app("prod")' initdb 等价
```

### 3. 启动服务器

执行以下命令启动服务器：

```bash
# <model_name> 的可用取值为：prod, dev, test
uv run flask --app 'app:create_app("<mode_name>")' run
# 同样的，uv run flask run 与 uv run flask --app 'app:create_app("prod")' run 等价
```
