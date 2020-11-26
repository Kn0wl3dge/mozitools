import unittest

from mozitools.decoder import MoziDecoder
from mozitools.unpacker import MoziUnpacker

SAMPLE_HASH = "8f3a5bc6088b999d50bce0eef02c41860bc8ac5e63a2379508c20a1c188eb38d"
SAMPLE_CONFIG = b"""{"raw_config": "[ss]botv2[/ss][dip]192.168.2.100:80[/dip][hp]88888888[/hp][count]http://ia.51.la/go1?id=17675125&pu=http%3a%2f%2fv.baidu.com/[idp][/count]\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000e\\u00a8)\\r<k<\\u0082Tk\\u00c5\\u00c4\\u008b\\u00fb.E#\\u00f1 \\u000f\\u00d8\\u0003L#1\\u0000\\u00ee\\u00f62\\u009a\\u0088\\u00ce\\u00b2X\\u00a5\\u008b,\\u00d7\\u00a1N\\u00ab\\u00c2,\\u00d9<\\u00dcf}w\\u00e5QE\\u00e3~\\u001e \\u0005\\u00ab\\u008c\\u008eTm\\u00bf\\u00a97\\u00a5\\u00ac\\u00d2\\u00bbD\\u009d\\u00fc\\u00fd\\u00bd\\u00c4v\\u0096<l\\u0094\\u00ba\\u00993\\u00e8\\u00d4J\\u0015\\u00bb*\\u0082\\u0094,o\\u0001\\u00e5O\\u00d7Oo~\\u008dYk\\u0002\\u008b&;d\\u00e9\\u00a3?\\u00bdlD\\u00f4?\\u00dc\\u00a5\\u007f^\\u00f8/I&\\u00f8z;3\\u00b3\\u00de\\u0015\\u00c0\\u00ab?\\u00ec@\\u009a\\u0003\\u00f1\\bIwO\\u00a2\\u00f5\\u00e0\\u00853\\u00dc|t\\u00e2\\u007fN`\\u00b1k\\u00af\\u0089oR\\u00bd\\u009d\\u00dfN\\u008e\\u001a\\u0000\\u00ac\\u00d0\\u00e6pA\\u001e\\u00de~n\\u009e\\r\\u001f\\u00a7\\u0002\\u00b4\\u00f1\\u0000b*\\n\\u00e04\\u00c7DO~\\u008e\\u00b1", "signature1": "b0e74673720d660dd4a369e706576943f6be4f71966516acb1c842d5bf36cfc86717caf562b1fbc12b0a80fab170217ba2aa3e3bad1844af856320add9c1f8afe2eac3acf522c7737d7568551b902b926fd65c969a2c4f34aa4a380fe2ada249", "version": 2, "signature2": "c33f318d0bee9747640f78bbb90b9b4192c325d178e7e50575d67c3566917abee559b6cf1acb5d2bc4db08a420afea4d921a2e6dff86cc92e603ce6987f2f2a100e8408f2c184a53ccb29978bbd16261e964ee7e80aa86296d9880429a31e1cf", "config": {"ss": "botv2", "hp": "88888888", "dip": "192.168.2.100:80", "count": "http://ia.51.la/go1?id=17675125&pu=http%3a%2f%2fv.baidu.com/", "idp": true}}"""


class TestDecoder(unittest.TestCase):
    def test_decode_sample(self):
        u = MoziUnpacker("/tmp/mozi-decoder-test/Mozi.m")
        u.unpack()
        d = MoziDecoder("/tmp/mozi-decoder-test/" + SAMPLE_HASH)
        config = d.decode()
        print(config)
        self.assertEqual(config, SAMPLE_CONFIG)


if __name__ == '__main__':
    unittest.main()
