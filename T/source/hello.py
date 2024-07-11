import unittest
import testinfra

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("r3ap3rpy")

def test_tmp_file(host):
    temp = host.file("/tmp/demo")
    assert temp.contains("Hello World")
