# 操作系统

## 操作系统的发展
- 手工操作系统
- 批处理阶段: 分为两种
   - 单道批处理: 单次单个任务, 不能并发, 资源利用率低
   - 多道批处理: 同时多个任务, 能并发, 资源利用率高点
- 分时操作系统: 能人机交互, 把CPU运行时间分片, 进程按顺序使用时间片, 时间用完立马下一位
- 实时操作系统: 某任务一定要在某时间完成, 和家用电脑没什么关系, 一般是飞行器控制系统, 银行系统, 特点是及时和可靠
- 网络操作系统和分布式计算机系统: 不重要


## CPU的两种工作状态
- 内核态: 执行危险指令, 管理硬件相关,把能破坏系统（访问软硬件资源）的危险指令锁在仓库
- 用户态: 执行普通应用程序, 当应用程序需要用到危险指令时用户态就给内核态打个申请表（访管指令）, 内核态进仓库取完东西后, 再交付给用户态

> 内核态能执行除访管指令外的全部指令  
> 用户态只能执行普通指令和访管指令  
> 内核态和用户态的切换由硬件（cpu内小开关）完成

## 系统调用
操作系统管理硬件, 将硬件方法抽象为系统调用, 并提供给应用程序
- 库函数: 语言or操作系统根据系统调用/算法提供给开发者的 底层包含系统调用的函数接口/纯用户态的函数；如cpp的stl、win的Windows API

假设C中使用函数open, 用于打开某文件
库函数open->系统调用中文件管理的接口->用户态调用访管指令->进入内核态->访问文件所在的硬盘地址
传递系统调用参数: 同样以open为例, 操作系统在访问文件前, 也需要先知道文件在文件系统中所在的路径, 这个路径由系统调用参数传递给内核态

## 操作系统四大特性
虚拟、并发、共享、异步

- 虚拟: 假设计算机采用16G的内存条, 但所有任务占用的总内存为20G, 于是操作系统仅将各任务的执行到的步骤的数据调入内存, 剩下的部分仍在硬盘
- 并发: 单CPU在极短时间内快速切换处理的任务, 例如第1毫秒执行任务1, 10ms后执行任务2, 再10ms后切换回任务1, 不断切换；这样在人眼里就好像任务1和任务2同时运行一样
- 共享: 操作系统中的资源（打印机、文件等）可以供多个任务使用；有些资源可以同时使用, 例如能点开多个test.txt文件；有些不能同时使用, 例如打印机不能同时打两个程序给的pdf
- 异步: 不重要

## 操作系统管了什么
- 时钟管理
- 中断机制
- 原语
- 进程管理
- 内存管理
- 文件系统
- 设备驱动器

> 原语: 乐高小积木, 能被频繁公用的小程序  
> 不可打断, 得一气呵成  
> 原语执行前会关中断, 执行完再打开

## 中断
让操作系统内核强行夺回CPU控制权, 使CPU从用户态变为内核态

为什么要中断: 提高资源利用率

中断服务程序: 对不同的中断, 操作系统有不同的处理流程, 这个处理流程就是中断服务程序

中断向量表: 操作系统记录了所有的中断类型, 并进行编号, 保存在中断向量表中, 中断向量表还记录了各个中断类型对应的中断服务程序的地址, 这个地址称为中断向量

### 中断执行过程
```
关中断->保存断点->中断服务程序寻址->
保存现场和屏蔽字->开中断->执行中断服务程序->关中断->恢复现场和屏蔽字->开中断->中断返回
```

第一步关闭中断, 是为了防止中断执行被其他中断打断  
第二步保存断点, 是将PC(程序计数器, 保存下一步要执行指令的地址)的内容放入内核空间的栈中  
第三步中断服务程序寻址, 根据中断向量表, 寻找当前中断编号对应的中断服务程序的地址  
前三步由硬件掌管, 后面由操作系统接管  
第四步保存现场和屏蔽字, 将除了PC之外的其他寄存器的内容, 放入内核空间的栈中  
第五步开中断, 执行中断服务程序的过程中允许更高优先级的中断发生  
第六步关中断, 恢复现场不允许中断打断  
第七步恢复现场和屏蔽字, 将在内核空间栈中的关键信息恢复到寄存器中  
第八步, 开中断  
第九步, 中断返回

> 保存断点是将PC压入内核空间的栈中  
> 保存现场是将被中断进程的其他寄存器的东西压入内核空间的栈中  
> 前三步称为中断隐指令, 由硬件自动完成  
> 保存现场和恢复现场均不允许中断打断


## 内核空间和用户空间
内核空间: 在内存中仅有一个, 所有进程共享, 用户态下无法访问内核空间

用户空间: 每个进程都分配一个, 用来存放程序数据

