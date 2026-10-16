# functionPaint

个人实验与学习项目集合，目前主要包含 **冰雹猜想（Collatz 3n+1 问题）** 的研究资料：交互式可视化页面、条件证明推导与实验代码。

## 目录结构

```
functionPaint/
├── marquee.html                    # 跑马灯效果演示页
└── collatz/
    ├── hailstone.html              # 冰雹猜想研究指南（交互式可视化，核心文件）
    ├── deepseek_collatz.md         # 冰雹猜想相关研究笔记
    ├── collatz_编码.py             # 冰雹轨迹实验代码
    ├── 测试结果.jpg                 # 实验截图
```

## 冰雹猜想简介

对任意正整数 n：

- n 为偶数 → 除以 2
- n 为奇数 → 乘 3 再加 1

**猜想**：无论从哪个正整数出发，最终都会到达 1。该猜想至今未被证明（已验证 n ≤ 2⁶⁸）。

## hailstone.html 使用说明

纯静态页面（HTML + CSS + Canvas，无外部依赖），双击即可在浏览器中打开，包含 9 个板块：

| 板块 | 内容 |
|------|------|
| 0 · 引言 | 猜想表述、历史背景、任意 n 的轨迹生成器 |
| 思路1 · 数值实验 | 轨迹播放器、批量停止时间散点图 |
| 思路2 · 逆向树 | 从 1 倒推的 Collatz 树（树形/放射形布局） |
| 思路3 · 二进制奇偶 | 二进制逐步分析、奇偶串 (parity string) |
| 思路4 · 随机模型 | 随机奇偶模型 vs 真实轨迹对比、启发式分析 |
| 思路5 · 统计与反例搜索 | 峰值/步数分布直方图、工程实践建议 |
| 思路6 · 变体推广 | kx±1 变体相图扫描 |
| 研究路线 | 8 周分阶段学习与研究计划 |
| 参考文献 | 经典文献与在线资源 |

## 实验代码

`collatz/collatz_编码.py` 提供冰雹轨迹的计算与统计，Python 3 直接运行：

```bash
python collatz/collatz_编码.py
```

## 参考资料

- [Wikipedia · Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [OEIS A006577（停止时间）](https://oeis.org/A006577)
- J. Lagarias (编.), *The Ultimate Challenge: The 3x+1 Problem*, AMS, 2010
- T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, 2019 (arXiv:1909.03562)