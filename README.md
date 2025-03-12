# 有道词典发音下载工具

这是一个简单的Python工具，用于从有道词典下载单词的发音MP3文件。

## 功能

- 通过控制台输入单词，多个单词用逗号分隔
- 自动从有道词典获取单词的发音
- 支持选择美式发音或英式发音
- 将MP3文件下载到本地指定目录

## 使用方法

1. 安装依赖项：
   ```
   pip install -r requirements.txt
   ```

2. 运行程序：
   ```
   python main.py
   ```

3. 按照提示输入单词、保存目录和发音类型

## 示例

```
欢迎使用有道词典发音下载工具
请输入要下载发音的单词，多个单词用逗号分隔
单词: hello, world, python

请输入保存目录 (默认为 'pronunciations'): 

请选择发音类型:
1. 美式发音
2. 英式发音
请输入选项 (默认为美式发音): 1

正在处理单词: hello
已下载 'hello' 的发音到 pronunciations/hello.mp3

正在处理单词: world
已下载 'world' 的发音到 pronunciations/world.mp3

正在处理单词: python
已下载 'python' 的发音到 pronunciations/python.mp3

下载完成! 成功下载 3/3 个单词的发音
```

## 注意事项

- 程序会在每次请求之间添加1秒的延迟，以避免被有道词典封IP
- 默认保存目录为当前目录下的"pronunciations"文件夹
- 程序使用有道词典的公开API，如果API变更可能会导致程序失效