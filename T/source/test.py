import unittest
import testinfra

class TestCentos(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.get_host("paramiko://r3ap3rpy@centos9")

    def test_firewall(self):
        self.assertTrue(self.host.service("firewalld").is_running)

    def test_check_script(self):
        self.assertEqual(self.host.run("/tmp/check.sh").rc,0)

    def test_git_installed(self):
        self.assertTrue(self.host.package('git').is_installed)
if __name__ == '__main__':
    unittest.main()
