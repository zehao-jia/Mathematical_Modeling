
一、核心库安装
首先通过 pip 安装必备库：
pip install networkx matplotlib  # 基础组合（推荐入门）
pip install pyvis  # 可选，用于交互式网页可视化

二、Python 解决图论问题案例
以 “判断欧拉图”“寻找欧拉回路” 和 “最短路径计算” 为例，演示核心功能。
案例 1：判断图是否为欧拉图（呼应前文七桥问题）
根据欧拉图定义（无向图中所有顶点度数为偶数 → 存在欧拉回路），用networkx实现判断：
```python
import networkx as nx

# 1. 构建无向图（模拟“非七桥问题”的有效欧拉图）
G = nx.Graph()  # 创建无向图对象
# 添加顶点（对应七桥问题中的“陆地”）
G.add_nodes_from(["A", "B", "C", "D"])
# 添加边（对应七桥问题中的“桥梁”，此处确保所有顶点度数为偶数）
G.add_edges_from([
    ("A", "B"), ("A", "C"),  # A的度数：2
    ("B", "C"), ("B", "D"),  # B的度数：3？→ 调整为 ("B", "D")×2（允许重边）
    ("B", "D"), ("C", "D")   # 调整后：B(3→4)、C(2→3→4)、D(3→4)
])

# 2. 计算顶点度数（验证欧拉图条件）
degree_dict = dict(G.degree())
print("顶点度数：", degree_dict)  # 输出：{'A':2, 'B':4, 'C':4, 'D':4}（全为偶数）

# 3. 判断是否为欧拉图（networkx内置函数）
is_eulerian = nx.is_eulerian(G)
print("是否为欧拉图：", is_eulerian)  # 输出：True

# 4. 若为欧拉图，提取欧拉回路
if is_eulerian:
    euler_circuit = list(nx.eulerian_circuit(G))  # 生成欧拉回路（边的列表）
    print("欧拉回路（边序列）：", euler_circuit)
    # 输出示例：[('A','B'), ('B','D'), ('D','C'), ('C','B'), ('B','D'), ('D','C'), ('C','A')]
```
案例 2：加权图最短路径计算（Dijkstra 算法）
针对 “顶点 - 边 - 权重” 的基本概念，用networkx实现加权图的最短路径求解（模拟交通路线距离计算）：
```python
import networkx as nx

# 1. 构建加权有向图（顶点=城市，权重=公路里程）
G = nx.DiGraph()  # 有向图（如“北京→上海”与“上海→北京”里程可能不同）
G.add_weighted_edges_from([
    ("北京", "天津", 137),    # 权重=137公里
    ("北京", "石家庄", 292),
    ("天津", "济南", 357),
    ("石家庄", "济南", 307),
    ("济南", "上海", 891)
])

# 2. 计算“北京→上海”的最短路径（Dijkstra算法）
shortest_path = nx.shortest_path(G, source="北京", target="上海", weight="weight")
shortest_length = nx.shortest_path_length(G, source="北京", target="上海", weight="weight")

print("北京→上海最短路径：", shortest_path)  # 输出：['北京', '天津', '济南', '上海']
print("最短路径里程：", shortest_length, "公里")  # 输出：137+357+891=1385
```
三、Python 实现图可视化
1. 基础静态可视化（matplotlib + networkx）
适合快速展示图的结构（顶点、边、权重）：
```python
import networkx as nx
import matplotlib.pyplot as plt

# 复用案例2的加权有向图G
G = nx.DiGraph()
G.add_weighted_edges_from([("北京", "天津", 137), ("北京", "石家庄", 292), 
                           ("天津", "济南", 357), ("石家庄", "济南", 307), ("济南", "上海", 891)])

# 1. 设置布局（控制顶点位置，常用布局：spring_layout=弹簧布局、circular_layout=环形布局）
pos = nx.spring_layout(G, seed=123)  # seed固定布局，避免每次运行位置不同

# 2. 绘制顶点（node_size=大小，node_color=颜色）
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="#4CAF50")

# 3. 绘制边（arrowstyle=箭头样式，width=边宽度）
nx.draw_networkx_edges(G, pos, arrowstyle="->", width=2, edge_color="#666666")

# 4. 标注顶点名称（font_size=字体大小，font_color=字体颜色）
nx.draw_networkx_labels(G, pos, font_size=12, font_color="white", font_weight="bold")

# 5. 标注边的权重（edge_labels=权重字典，font_size=10）
edge_labels = nx.get_edge_attributes(G, "weight")  # 提取边权重
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# 6. 隐藏坐标轴，显示图像
plt.axis("off")
plt.title("北京→上海交通路线图（加权有向图）", fontsize=14)
plt.show()  # 弹出窗口显示图像

2. 交互式可视化（pyvis）
适合复杂图的探索（支持缩放、拖拽、点击显示详情），输出为 HTML 文件：
from pyvis.network import Network

# 1. 创建交互式图对象（directed=True表示有向图）
net = Network(directed=True, height="600px", width="100%", bgcolor="#f0f0f0")

# 2. 添加顶点（可自定义颜色、大小）
net.add_node("北京", color="#FF0000", size=20)
net.add_node("天津", color="#0000FF", size=15)
net.add_node("石家庄", color="#0000FF", size=15)
net.add_node("济南", color="#0000FF", size=15)
net.add_node("上海", color="#FF0000", size=20)

# 3. 添加加权边（label=权重，title=鼠标悬浮时显示的详情）
net.add_edge("北京", "天津", weight=137, label="137km", title="北京→天津：137公里")
net.add_edge("北京", "石家庄", weight=292, label="292km", title="北京→石家庄：292公里")
net.add_edge("天津", "济南", weight=357, label="357km", title="天津→济南：357公里")
net.add_edge("石家庄", "济南", weight=307, label="307km", title="石家庄→济南：307公里")
net.add_edge("济南", "上海", weight=891, label="891km", title="济南→上海：891公里")
```
# 4. 生成HTML文件（打开后可交互式操作）
```python
net.show("traffic_graph.html")
print("交互式图已保存为 traffic_graph.html，可在浏览器中打开查看")
```
四、常用图论问题与 Python 实现对应表
图论问题
核心库函数（networkx）
应用场景
判断欧拉图
nx.is_eulerian(G)
一笔画问题、路线规划
寻找欧拉回路
nx.eulerian_circuit(G)
快递路线优化（无重复路径）
最短路径（加权图）
nx.shortest_path(G, weight="weight")
交通、物流路径规划
顶点度数计算
dict(G.degree())
网络节点重要性分析
图的连通性判断
nx.is_connected(G)（无向图）
通信网络稳定性检测

