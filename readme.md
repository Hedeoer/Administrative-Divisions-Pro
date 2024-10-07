# 国家统计局行政区划 信息爬虫 

> 主要使用两个脚本：
> 1. main.py 用于爬取数据并生成json文件
> 2. json2csv.py 用于将json文件转换为csv文件

---
## 1. main.py 


### 使用说明

本脚本是一个用于爬取国家统计局行政区划信息的 Python 脚本，能够根据指定的起始 URL 爬取行政区划数据，并将结果保存到指定的目录中。

#### 1. Python 版本要求

- **Python 3**：建议使用 Python 3.6 或更高版本。

#### 2. 依赖的模块

在运行本脚本之前，需要确保安装以下 Python 模块和依赖项：

#### Python 库

- **requests**：用于发送 HTTP 请求。
- **BeautifulSoup (`bs4`)**：用于解析 HTML 内容。
- **selenium**：用于模拟浏览器行为，处理动态内容。
- **lxml**：用于解析 HTML/XML 内容。
- **argparse**：用于解析命令行参数（Python 标准库，无需额外安装）。

#### 其他依赖

- **Chrome 浏览器**：脚本使用 Chrome 浏览器进行网页渲染。
- **ChromeDriver**：与 Chrome 浏览器对应的驱动程序，确保版本匹配。

#### 安装依赖模块

您可以使用以下命令安装所需的 Python 模块：

```bash
pip install requests beautifulsoup4 selenium lxml
```

#### 配置 ChromeDriver

1. **下载 ChromeDriver**：根据您安装的 Chrome 浏览器版本，从以下地址下载对应版本的 ChromeDriver：
   - 下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads
2. **配置环境变量**：将下载的 `chromedriver` 可执行文件放置在系统的 `PATH` 目录中，或者在脚本中指定 `chromedriver` 的路径。

### 3. 脚本参数说明

#### 参数列表

 ```shell
  -s 或 --source
  ```

指定要爬取的起始 URL。

  - **默认值**：`http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2022/`

 ```shell
  -o 或 --output
  ```

指定存放爬取结果的目录。

  - **默认值**：`crawl_result`

#### 使用方法

##### 示例 1：使用默认参数运行脚本

```bash
python your_script.py
```

这将使用默认的起始 URL 和输出目录，爬取数据并将结果保存到当前目录下的 `crawl_result` 目录中。

##### 示例 2：指定起始 URL 和输出目录

```bash
python your_script.py -s http://example.com/start_url/ -o /path/to/output_dir
```

- `-s`：将 `http://example.com/start_url/` 替换为您要爬取的起始 URL。
- `-o`：将 `/path/to/output_dir` 替换为您希望存放爬取结果的目录路径。

##### 示例 3：完整示例

```bash
python your_script.py --source http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/ --output data_output
```

上述命令将以 `http://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/` 作为起始 URL，爬取数据并将结果保存到当前目录下的 `data_output` 目录中。如果目录不存在，脚本将自动创建该目录。


## 2. json2csv.py

```shell
执行如下命令查看使用帮助：
python .\json2csv.py -h
```

### TODO
1. 优化爬取效率
2. ...

此项目借鉴了以下项目,表示由衷感谢：
https://github.com/obaby/administrative-division-spider
