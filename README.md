# 115影片重命名工具
# 正在构思中

修改自项目：
<a title="Fake115Upload" target="_blank" href="https://github.com/T3rry7f/Fake115Upload">Fake115Upload</a> 
<a title="AV Data Capture (CLI)" target="_blank" href="https://github.com/yoshiko2/AV_Data_Capture">AV Data Capture (CLI)</a>

获得指定文件夹下的所有文件的hash链，借助AV_Data_Capture爬取影片数据，重命名hash链的文件名，最终输出到txt文件。

原始文件名需要符合AV_Data_Capture规则。

只构想了一半的流程，获得重命名后的115 sha1。上传需要在网页上手动转存。

不知道删除文件的接口，并且直接删除原文件有风险。研究清楚Fake115Upload的上传原理以后，增加上传到根目录的流程。
