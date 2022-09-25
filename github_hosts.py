#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Robin Wen <bkbiblzh@duck.com>
#
# Distributed under terms of the MIT license.

import socket
import os
import sys

file_path = os.path.split(os.path.realpath(__file__))[0]

def get_ip(host):
    """
    Get ip of host.
    """
    try:
        host_ip = socket.gethostbyname(host)
        return host_ip
    except:
        print("Unable to get IP of Hostname")

def main():
    f = open('%s/github_hosts.txt' % file_path,'w')
    f.write("# GitHub Start\n")
    f.close()

    with open("%s/github_domain.txt" % file_path, "r") as ins:
        for host in ins:
            ip=get_ip(host.strip())
            with open('%s/github_hosts.txt' % file_path, 'a') as result:
                result.write(ip.strip('\n') + " " + host)

    f = open('%s/github_hosts.txt' % file_path,'a')
    f.write("\n# GitHub End\n")
    f.close()

if __name__ == "__main__":
    main()
