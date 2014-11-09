Prometheus（测试系统）
========

###word_segmentation.py(分词)

利用[分词网站](http://www.xunsearch.com/scws/demo/v4.php)对testDoc目录下的文件进行分词和词性标注，结果保存在segmentDoc文件夹下

###extract.py（提取）

利用编写的cpp(extract.cpp)将segementDoc目录下的文件夹过滤后保存在stopdoc下

###compile.py(编译)

将cppsource下的源文件编译成可执行文件保存在bin下

###entropy.py(信息熵)

调用entropy.cpp的方法计算信息熵,除去信息熵低的词

###gibbs.jar（gibbs采样）

对于data/LdaOriginalDocs下的文件跑gibbs采样，参数保存在data/LdaParameter下，结果保存在data/LdaResults下

###calc.py

对结果计算cos距离和jsd距离




