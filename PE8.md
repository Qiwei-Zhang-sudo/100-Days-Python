1. PEP 8 - 官方代码风格指南
PEP 8 是 Python 官方推荐的代码风格指南，涵盖了命名、缩进、空格、注释等方面的规范。
命名规范：
变量和函数名：使用小写字母和下划线（snake_case），例如：my_variable, calculate_sum()。
类名：使用大驼峰命名法（PascalCase），例如：MyClass。
常量：全部大写并用下划线分隔，例如：MAX_SIZE。
模块名：使用小写字母，避免下划线（除非必要），例如：mymodule.py。
缩进与空格：
使用 4个空格 进行缩进（禁止使用 Tab）。
操作符前后加空格，例如：x = 1 + 2。
函数参数逗号后加空格，例如：func(arg1, arg2)。
避免行尾多余空格。
行长度限制：
每行代码不超过 79个字符（文档字符串不超过 72个字符）。
超长行可通过括号或反斜杠换行。
空行规则：
函数之间用 两个空行 分隔。
类的方法之间用 一个空行 分隔。
文件顶部导入语句与其他代码之间用 两个空行 分隔。
2. 注释与文档字符串
单行注释：使用 # 开头，并在 # 后加一个空格。
python
# 这是一个单行注释
多行注释：对于复杂逻辑，建议使用多行注释说明意图。
文档字符串（docstring）：
使用三重引号 """ 包裹。
函数、类、模块应有清晰的 docstring 描述其功能、参数和返回值。
python
def add(a, b):
    """
    计算两个数的和。

    Args:
        a (int): 第一个数。
        b (int): 第二个数。

    Returns:
        int: 两数之和。
    """
    return a + b
3. 导入规范
所有 import 语句放在文件顶部。
按以下顺序分组导入：
标准库模块（如 os, sys）
第三方库（如 numpy, requests）
自定义模块
每组之间用空行分隔。
避免使用 from module import *，明确指定所需内容。
python
import os
import sys

import numpy as np
import requests

from mymodule import MyClass
4. 异常处理
尽量捕获具体异常而不是通用异常（如 Exception）。
使用 try-except-finally 结构时，确保资源正确释放。
python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误: {e}")
finally:
    print("清理资源")
5. 类型提示（Type Hints）
从 Python 3.5 开始支持类型提示，增强代码可读性和静态检查能力。

python
def greet(name: str) -> str:
    return f"Hello, {name}!"
6. 工具辅助
使用自动化工具检查代码是否符合规范：
flake8：检测 PEP 8 规范及潜在错误。
black：自动格式化代码。
isort：自动整理 import 语句。
mypy：静态类型检查。
7. 其他建议
避免过深的嵌套结构，优先使用早期返回或异常处理简化逻辑。
使用列表推导式、生成器表达式等简洁语法替代冗余循环。
保持函数职责单一，避免函数过长（一般不超过 50 行）。
以上是 Python 主要的代码规范要点。实际开发中可根据项目需求适当调整，但建议始终以 PEP 8 为基准。