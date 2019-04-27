#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Robin Wen <blockxyz@gmail.com>
#
# Distributed under terms of the MIT license.

import socket
import os
import sys



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
    f = open('github_hosts.txt','w')
    f.write("# GitHub Start\n")
    f.close()

    with open("github_domain.txt", "r") as ins:
        for host in ins:
            ip=get_ip(host.strip())
            with open('github_hosts.txt', 'a') as result:
                result.write(ip.strip('\n') + " " + host)

    f = open('github_hosts.txt','a')
    f.write("# GitHub End\n")
    f.close()

if __name__ == "__main__":
    main()