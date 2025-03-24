<div align="center">
  <a href="#english-readme">English</a> | <a href="#中文文档">中文</a>
</div>

---

<a id="english-readme"></a>
# Rigid-tube MPC
Reproduction of the Simulation Section from the Paper
[D. Q. Mayne, M. M. Seron, and S. V. Raković, "Robust Model Predictive Control of Constrained Linear Systems with Bounded Disturbances," Automatica, vol. 41, no. 2, pp. 219–224, 2005.](https://www.sciencedirect.com/science/article/pii/S0005109804002870)
Additionally, comparative cases incorporating LQR (Linear Quadratic Regulator) and Linear MPC (Model Predictive Control) have been included.

## Installation
### 1. Create and Activate Virtual Environment (Optional but Recommended)
```bash
# For Linux/macOS
python -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Install Package with Dependencies
#### Method 1: Install directly from GitHub (Recommended)
```bash
pip install git+https://github.com/rui-huang-opt/tmpc.git
```

#### Method 2: Clone repository and install
```bash
git clone https://github.com/rui-huang-opt/tmpc.git
cd tmpc

# Install the package and its dependencies (automatically resolved from pyproject.toml).
pip install .
```

---

<a id="中文文档"></a>
# Rigid-tube MPC
关于论文[D. Q. Mayne, M. M. Seron, and S. V. Raković, “Robust model predictive control of constrained linear systems with bounded disturbances,” Automatica, vol. 41, no. 2, pp. 219–224, 2005.](https://www.sciencedirect.com/science/article/pii/S0005109804002870)中仿真部分的复现。此外，还加入了LQR和线性MPC的对比案例。

## 安装
### 1. 创建虚拟环境 (非必须但是推荐这样做)
```bash
# Linux/macOS 系统
python -m venv .venv
source .venv/bin/activate

# Windows 系统
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. 安装包（以及依赖）
#### 方法1：直接从 GitHub 安装（推荐）
```bash
pip install git+https://github.com/rui-huang-opt/tmpc.git
```

#### 方法2：克隆仓库后安装
```bash
git clone https://github.com/rui-huang-opt/tmpc.git
cd tmpc

# 安装包及其依赖（自动从 pyproject.toml 读取）
pip install .
```

## 多面体类测试结果
### 多面体平移
![img](results/poly_test/fig_1.png)

### 多面体间闵可夫斯基和
![img](results/poly_test/fig_2.png)

### 多面体间庞特里亚金差
下图表示庞特里亚金差不是将集合内所有向量取反再闵可夫斯基和

![img](results/poly_test/fig_3.png)

### 线性坐标变换（对集合进行矩阵乘法）
实际可以进行升维和降维，这里未展示

![img](results/poly_test/fig_4.png)

### 向量空间
![img](results/poly_test/fig_5.png)

### 单位立方体
![img](results/poly_test/fig_6.png)

### 一个多面体内的最大椭球（球心确定）
![img](results/poly_test/fig_7.png)

## LQR 与 MPC 对比结果
### 状态轨迹对比
![img](results/lqr_and_linear_mpc/fig_1.gif)

### 输入序列对比
![img](results/lqr_and_linear_mpc/fig_2.png)

### MPC初始状态可行域
初始状态属于这个集合问题才可解

![img](results/lqr_and_linear_mpc/fig_3.png)

## 多面体终端集椭球终端集
### 状态轨迹对比
可以看出离稳定点越远，区别越大，反之越小，但都可以稳定（多面体终端集初始可行域更大）

![img](results/polyhedron_and_ellipsoid_terminal_set/fig_1.gif)
![img](results/polyhedron_and_ellipsoid_terminal_set/fig_2.gif)

### 输入序列对比
![img](results/polyhedron_and_ellipsoid_terminal_set/fig_3.png)
![img](results/polyhedron_and_ellipsoid_terminal_set/fig_4.png)

## Tube based MPC结果
### 状态轨迹
实际状态始终在以名义状态为中心的管道内

![img](results/tube_based_mpc/fig_1.gif)

### 输入序列
分为两部分，不考虑噪声的名义系统输入和用于抑制噪声的输入

![img](results/tube_based_mpc/fig_2.png)

### Tube based MPC初始状态可行域
蓝色为实际可行域，红色表示控制器内预测状态序列的第一步的状态的可行域

![img](results/tube_based_mpc/fig_3.png)

### 正鲁棒不变集测试效果
下图说明一个状态方程为 $x_{k+1}=Ax_{k}+w$的系统，其中w为有界噪声，则当它进入鲁棒不变集后就不会再出去

![img](results/tube_based_mpc/fig_4.gif)