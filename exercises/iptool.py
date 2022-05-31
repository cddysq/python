# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2022/5/11 18:51
# @version :v1.0.0
import os
from os.path import dirname, abspath

import IPy

resource_folder_path = dirname(dirname(abspath(__file__))) + os.sep + 'resources' + os.sep


def ip_to_ipc():
    """
    ip转ip c段
    """
    ips = set()
    read_path = resource_folder_path + 'ip.txt'
    write_path = resource_folder_path + 'ip_c.txt'
    out_file = open(write_path, 'a')
    with open(read_path, 'r') as f:
        for line in f:
            ip = line.strip('\n')
            ip_c = IPy.IP(ip).make_net('255.255.255.0')
            if ip_c not in ips:
                out_file.write(str(ip_c) + '\n')
                ips.add(ip_c)
    out_file.close()
    print('转换结束')


if __name__ == '__main__':
    ip_to_ipc()
