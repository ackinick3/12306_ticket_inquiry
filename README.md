# 12306 余票查询小程序

一个使用 Python 编写的命令行小程序，可按乘车日期、出发站和目的地查询 12306 余票信息。

## 功能

- 查询车次名称、出发时间、到达时间及一等座、二等座、无座余票。
- 日期格式错误时给出提示并重新输入。
- 日期不存在或已经过期时给出提示并重新输入。
- 出发站或目的地不存在时给出提示并重新输入。
- Cookie 和 User-Agent 保存在本地配置中，不提交到 Git 仓库。

## 环境要求

- Python 3
- `requests` 库

安装依赖：

```powershell
py -3 -m pip install requests
```

## 配置

复制示例配置：

```powershell
Copy-Item config.example.json config.json
```

编辑 `config.json`，填写浏览器访问 12306 时使用的 Cookie 和 User-Agent：

```json
{
  "cookie": "你的 12306 Cookie",
  "user_agent": "你的浏览器 User-Agent"
}
```

`config.json` 已加入 `.gitignore`。请勿将其中的隐私信息提交到 Git 仓库或分享给他人。

## 使用方法

在项目目录运行：

```powershell
py -3 main.py
```

按照提示依次输入年份、月份、日期、出发站和目的地。程序会将年月日组合为 12306 查询所需的日期格式。

## 运行测试

```powershell
py -3 -m unittest discover -s tests -v
```

## 注意事项

- 本项目仅用于学习和个人查询。
- Cookie 可能会过期；查询失败时请更新本地 `config.json`。
- 请合理控制查询频率，并遵守 12306 的相关规则。
