# 研究DJMAX 2.0 DJ POWER算法的

## 请帮忙贡献更多样本！！！！！

### 关于样本格式

请看`data`文件夹中的csv

以`rate,power`的格式填写

文件名为难度，NM/HD/MX直接写数字，SC写sc几

文件末尾请务必留一行空行

### 关于数据

目前90-98这块的数据相对较少，特别是低分部分

### 关于目前的结论

~~认为有可能是tanh，参数规律未知~~

根据拟合的结果，似乎是正态分布累积更合适，但rate>=99.5处极有可能存在多个线性分段

### 关于其余文件

`diff_coeff.py`计算的是所谓难度系数

`djpower_perfect.py`计算的是在rate=100%时的djpower

`kr_algorithm.py`是从[韩国论坛](https://gall.dcinside.com/mgallery/board/view/?id=djmaxrespect&no=626587)上搞来的，但我认为这个分段曲线不太对劲。。。

`plot_power.py`和`approximate.py`是本研究项目的主要程序

#### 本人的一些批话

我真觉得牛尾子自己也没算明白

尝试过逆向分析，奈何技术不够没发现什么有用的

我怀疑牛尾子在做这个系统的时候程序去问策划power算法怎么写策划直接随手画了条曲线让程序去做结果就有了这种人不人鬼不鬼的神经玩意

很喜欢日本网友的一句话：*DJMAXのDJ POWERが内部でどういう計算になってるのか本当に意味不明だ*
