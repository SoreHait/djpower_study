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

认为有可能是tanh，参数规律未知

### 关于其余文件

`diff_coeff.py`计算的是所谓难度系数

`djpower_perfect.py`计算的是在rate=100%时的djpower

`kr_algorithm.py`是从[韩国论坛](https://gall.dcinside.com/mgallery/board/view/?id=djmaxrespect&no=626587)上搞来的，但我认为这个分段曲线不太对劲。。。

`plot_power.py`是本研究项目的主要程序
