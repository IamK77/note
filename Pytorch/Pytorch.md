# Pytorch的安装

## 1.保证CUDA已经安装

首先检查自己的显卡是否支持CUDA，本文在此不过多赘述.

在cmd中使用代码检测是否安装了cuda，并且查看cuda版本，后续下载pytorch的时候需要与对应的cuda版本对应.

```nvidia-smi```

如果正确安装了cuda，那么就可以在下图中看到，CUDA Version: 12.1.



![step1](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step1.png)







## 2.在官网中安装pytorch

### 常规下载方式

进入到pytorch的官网：https://pytorch.org/

这里可以看到有两种常用的安装方式：Pip和Conda

注意在CUDA版本选择的时候，要选择上文已经查看了的CUDA版本

本文适用于conda 和 pip安装都装不下的情况：

在我自己下载的时候，pip下载需要80个小时，conda安装下来是CPU版本，所以不得不选择其他方法，**建议读者先尝试这两种传统方法可不可行**

如果可行，并且确定下载的pytorch的版本是GPU版本，那么现在就可以退出了。

Stable是稳定版本  Preview是尝鲜版本，如果不是特殊需求下载稳定版即可！

![step2.1](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_1.png)

### 直接下轮子的方式

我现在网速还算比较快，所以在下载中看上去时间其实并不久，但是如果下载时间过长，那么下载程序会中断，然后前功尽弃。

![step2.2](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_2.png)

我们现在来解析一下这一串下载代码

```pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121```

torch,torchvision,torchaudio 这三个是我们需要下载的东西

--index-url 这个后面跟了一串网址，指令就是从这个网站上下载的，所以我们之间进入的这个网站里去

``` https://download.pytorch.org/whl/cu121```

大概结构为如图

![step2.3](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_3.png)

常规的pytorch的下载只需要下载三个东西：torch,torchvision,torchaudio 

点击torch，进去后发现东西很多：

![step2.4](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_4.png)

torch-x.x.x是torch版本；

cuxxx指的是cuda版本，如果是121那么就是12.1；

cp310是python版本，我的python版本为3.10；

最后一个为自己电脑的电脑系统



根据个人配置进行选择！选到合适的就可以单击进行下载了

等待下载完成后就可以把下载好的文件，拖入到cmd中 然后就可以开始下载了

如果没什么爆红就可以了

![step2.5](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_5.png)

后面以同样的方式，下载另外两个

一个是torchvision

![step2.7](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_7.png)

另外一个是torchaudio 

![step2.6](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step2_6.png)

这时候可能会遇到一个问题，那就是这三个包中间的版本可能也会有冲突，这时候需要查看错误提示，提示会告诉你适配的版本是哪个，然后再按照相同的方式，去下载对应的包，方法和上面一样！可以说只要下载好了第一个，后续下载就没有什么问题了！



## 3.检查最终是否下载成功，已经是否是GPU版本

![step3](https://github.com/baizilw0807/note/blob/master/Pytorch/imgs/step3.png)

一切检查就绪后，就可以在虚拟环境中输入python，然后导入torch包，如果torch.cuda.is_available()返回的是true，那么就代表安装成功，

如果是false，首先检查是否安装了CUDA，或者显卡是否支持CUDA，其次检查检查是否安装的是GPU版本！
