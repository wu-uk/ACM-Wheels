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

- acm-wheels/
  - [LICENSE](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/LICENSE)
  - [README.md](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/README.md)
  - [cpp/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp)
    - [dataStructure/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp/dataStructure)
      - [dsu.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/dataStructure/dsu.cpp)
      - [lazySegtree.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/dataStructure/lazySegtree.cpp)
      - [sparseTable.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/dataStructure/sparseTable.cpp)
    - [geometry/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp/geometry)
      - [simple.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/geometry/simple.cpp)
    - [graph/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp/graph)
      - [dijkstra.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/graph/dijkstra.cpp)
      - [heavyLinkDivision.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/graph/heavyLinkDivision.cpp)
      - [topoSort.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/graph/topoSort.cpp)
    - [math/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp/math)
      - [Matrix.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/math/Matrix.cpp)
      - [sieve.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/math/sieve.cpp)
    - [others/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp/others)
      - [int128.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/others/int128.cpp)
      - [mint.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/others/mint.cpp)
    - [string/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/cpp/string)
      - [manacher.cpp](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/cpp/string/manacher.cpp)
  - [python/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/python)
    - [dataStructure/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/python/dataStructure)
      - [dsu.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/dataStructure/dsu.py)
      - [fenwick.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/dataStructure/fenwick.py)
      - [monoQueue.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/dataStructure/monoQueue.py)
      - [monoStack.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/dataStructure/monoStack.py)
      - [sparseTable.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/dataStructure/sparseTable.py)
      - [trie.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/dataStructure/trie.py)
    - [graph/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/python/graph)
      - [dijkstra.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/graph/dijkstra.py)
      - [heavySplit.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/graph/heavySplit.py)
      - [toposort.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/graph/toposort.py)
    - [math/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/python/math)
      - [discretisize.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/math/discretisize.py)
      - [fft.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/math/fft.py)
      - [sieve.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/math/sieve.py)
    - [string/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/python/string)
      - [kmp.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/python/string/kmp.py)
  - [utils/](https://github.com/wu-uk/ACM-Wheels/blob/main/tree/main/utils)
    - [snippet.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/utils/snippet.py)
    - [update.py](https://github.com/wu-uk/ACM-Wheels/blob/main/blob/main/utils/update.py)

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
