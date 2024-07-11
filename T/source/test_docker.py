import unittest, testinfra, subprocess

class TestDocker(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.get_host("paramiko://r3ap3rpy@centos9")

    def test_00_docker_build(self):
        self.assertEqual(self.host.run("docker build -t r3ap3rpy/demo /home/r3ap3rpy/docker").rc,0)
    def test_01_docker_run(self):
        self.assertEqual(self.host.run("docker run -d -p '8080:8080' r3ap3rpy/demo").rc, 0)
    def test_02_connection(self):
        check = subprocess.run(["curl","http://centos9:8080/"], capture_output = True)
        self.assertEqual(check.returncode, 0)
        self.assertEqual(check.stdout.decode().strip(), 'Hello World')
    def test_03_teardown(self):
        self.assertEqual(self.host.run("docker kill $(docker ps | awk '{print $1}' | grep -v CONTAINER)").rc, 0)
if __name__ == '__main__':
    unittest.main(verbosity=2)
