import os
import sys
import unittest
import subprocess

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Tester(unittest.TestCase):
    def test_foobar_rust_bin(self):
        self.assertTrue(os.path.exists(sys.argv[2]))
        proc = subprocess.Popen([sys.argv[2]], stdout=subprocess.PIPE)
        proc.wait()
        self.assertEqual(proc.returncode, 0)
        stdout = proc.stdout.read().decode().replace('\r', '')
        self.assertEqual(stdout, "bin.rs:4\nlib.rs:12\nbin.rs:6\n")

    def test_example_cmake_rust(self):
        self.assertTrue(os.path.exists(sys.argv[1]))
        proc = subprocess.Popen([sys.argv[1]], stdout=subprocess.PIPE)
        proc.wait()
        self.assertEqual(proc.returncode, 0)
        stdout = proc.stdout.read().decode().replace('\r', '')
        self.assertEqual(stdout, "main.c:7\nlib.rs:6\nmain.c:10\n")

if __name__ == '__main__':
    print(sys.argv)
    suite = unittest.TestLoader().loadTestsFromTestCase(Tester)
    res = unittest.TextTestRunner().run(suite)
    if res.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(-1)
