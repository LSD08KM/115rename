import os
from fake115upload3c import *
from OOF_Rename import *
from configparser import ConfigParser

if __name__ == '__main__':
    config_file = 'config.ini'  #获取 config.ini 内的变量
    config = ConfigParser()
    config.read(config_file, encoding='UTF-8')
    getlinks_file = config['webhard']['links_outfile']
    uplinks_fileS = config['common']['success_output_folder'] + '/' + "RenameSu.txt"
    uplinks_fileF = config['common']['failed_output_file']
    fake115upload("getlinks", getlinks_file)
    print("[+] 下载转存链结束!!!")
    OOF_Rename()    
    print("[+] 重命名转存链结束!!!")
    if config['auto']['mode'] == '1':
        print("[+] 开始上传重命名成功文件")
        fake115upload("uplinks", uplinks_fileS)
        if os.path.exists(uplinks_fileF):
            print("[+] 开始上传重命名失败文件")
            fake115upload("uplinks", uplinks_fileF)
    elif config['auto']['mode'] == '2':
        print("[+]模式2不上传。请查看转存链文档 "+getlinks_file+" "+uplinks_fileS+" "+uplinks_fileF)
    print("[+] 任务结束!!!")
    input("[+][+]请按下任意键关闭窗口")    