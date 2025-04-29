# ACM-Wheels
专为算法竞赛设计的算法模板仓库。

## 项目简介
本项目收集了常用的算法模板，涵盖数据结构、图论、数学等多个领域，旨在为算法竞赛提供快速参考和实现。

## 主要功能
- **数据结构**：线段树、树状数组、并查集、KMP等
- **图论算法**：Dijkstra、SPFA、Tarjan、HLD等
- **数学工具**：快速幂、矩阵运算、FFT、线性筛等
- **其他工具**：大整数运算、字符串匹配等

## 项目结构

```
acm-wheels/
├── cpp/                # C++实现
│   ├── dataStructure/  # 数据结构
│   │   ├── dsu.cpp     # 并查集
│   │   ├── lazySegtree.cpp  # 线段树
│   │   └── sparseTable.cpp  # ST表
│   ├── graph/          # 图论算法
│   │   ├── dijkstra.cpp      # Dijkstra算法
│   │   └── heavyLinkDivision.cpp  # 树链剖分
│   ├── math/           # 数学工具
│   │   ├── Matrix.cpp  # 矩阵运算
│   │   └── sieve.cpp   # 线性筛
│   └── others/         # 其他工具
│       └── int128.cpp  # 大整数运算
├── python/             # Python实现
│   ├── dataStructure/
│   │   ├── dsu.py      # 并查集
│   │   ├── fenwick.py  # 树状数组
│   │   └── trie.py     # 字典树
│   ├── graph/
│   │   ├── dijkstra.py      # Dijkstra算法
│   │   └── heavySplit.py    # 树链剖分
│   ├── math/
│   │   ├── fft.py      # 快速傅里叶变换
│   │   └── sieve.py    # 素数筛
│   └── string/
│       └── kmp.py      # KMP算法
├── utils/              # 实用工具
│   └── snippet.py      # 代码片段生成器
├── LICENSE             # 开源协议
└── README.md           # 项目说明
```
        
# 项目说明

## 使用说明
1. 选择需要的算法模板
2. 复制对应文件到您的项目中
3. 根据具体问题调整模板参数
4. 在代码中调用相关函数

## 贡献指南
欢迎提交新的算法模板或改进现有实现，请遵循以下步骤：
1. Fork 本项目
2. 创建新的分支 (git checkout -b feature/your-feature)
3. 提交您的修改 (git commit -am 'Add some feature')
4. 推送分支 (git push origin feature/your-feature)
5. 创建 Pull Request

## 开源协议
本项目采用 MIT 开源协议，详情请参阅 LICENSE 文件。
