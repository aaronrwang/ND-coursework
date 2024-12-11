import unittest
import subprocess

class TestClass (unittest.TestCase):

    def test_non_recursive(self):
        nrd1 = ['fmnc_manager.cc', 'ParamDictionary.cc', 'PktQueue.cc', 'RIPPS_PktPair.cc', 'Thread_IO.cc']
        nrd2 = ['Adapter.cc', 'fmnc_manager.cc', 'fmnc_test_sequence.cc', 'ip-utils.cc', 'ParamDictionary.cc', 'PktQueue.cc', 'RIPPS_PktPair.cc', 'Thread_IO.cc', 'TWiCE_Gateway.cc', 'whirlwind_gateway.cc']
        nrd3 = ['Adapter.cc', 'AdapterFile.cc', 'AdapterPCap.cc']
        def non_recursive(path):
            # get all base names from searchdir
            result = subprocess.run(['python3', 'hw6searchdir.py', path], stdout=subprocess.PIPE,universal_newlines=True)
            result = [i.split(', ') for i in result.stdout.splitlines()]
            result.pop()
            return [i[1] for i in result]

        self.assertEqual(non_recursive('tests/data/nrd-1'),nrd1)
        self.assertEqual(non_recursive('tests/data/nrd-2'),nrd2)
        self.assertEqual(non_recursive('tests/data/nrd-3'),nrd3)


    def test_recursive(self):
        rd1 = ['fmnc_manager.cc', 'ParamDictionary.cc', 'PktQueue.cc', 'RIPPS_PktPair.cc', 'TWiCE_Gateway.cc', 'whirlwind_gateway.cc', 'Thread_IO.cc']
        rd2 = ['fmnc_client.cc', 'fmnc_connection.cc', 'fmnc_connection_tcp_slice.cc', 'fmnc_manager.cc', 'fmnc_measurement_packet.cc', 'fmnc_session.cc', 'fmnc_support.cc', 'fmnc_test_analysis.cc', 'fmnc_test_sequence.cc', 'MemPoolCustom.cc', 'MemPoolObject.cc']
        rd3 = ['Adapter.cc', 'AdapterFile.cc', 'AdapterPCap.cc', 'Monitor.cc', 'Thread_Archive.cc', 'Thread_Timer.cc', 'NetAddress.cc', 'NetAddressEthernet.cc', 'NetAddressIPv4.cc', 'NetAddressIPv4Subnet.cc', 'PacketCacheEntry.cc', 'PacketCacheModule.cc', 'PacketCacheSupport.cc', 'PacketCacheTable.cc']
        rd4 = ['AdapterPCap.cc']
        def recursive(path):
            # get all base names from searchdir
            result = subprocess.run(['python3', 'hw6searchdir.py', path, '-r'], stdout=subprocess.PIPE,universal_newlines=True)
            result = [i.split(', ') for i in result.stdout.splitlines()]
            result.pop()
            return [i[1] for i in result]

        self.assertEqual(recursive('tests/data/rd-1'),rd1)
        self.assertEqual(recursive('tests/data/rd-2'),rd2)
        self.assertEqual(recursive('tests/data/rd-3'),rd3)
        self.assertEqual(recursive('tests/data/rd-4'),rd4)

    def test_recursive_extra(self):
        ex1 = ['fmnc_manager.cc', 'PktQueue.cc', 'RIPPS_PktPair.cc', 'ParamDictionary.cc', 'TWiCE_Gateway.cc', 'whirlwind_gateway.cc', 'Thread_IO.cc']
        ex2 = ['fmnc_manager.cc', 'ParamDictionary.cc', 'PktQueue.cc', 'RIPPS_PktPair.cc', 'TWiCE_Gateway.cc', 'whirlwind_gateway.cc', 'Thread_IO.cc']
        def recursive(path):
            # get all base names from searchdir
            result = subprocess.run(['python3', 'hw6searchdir.py', path, '-r'], stdout=subprocess.PIPE,universal_newlines=True)
            result = [i.split(', ') for i in result.stdout.splitlines()]
            result.pop()
            return [i[1] for i in result]
        self.assertEqual(recursive('tests/data/ex-1'),ex1)
        self.assertEqual(recursive('tests/data/ex-2'),ex2)

    def test_no_directory(self):
        result = subprocess.run(['python3', 'hw6searchdir.py'],universal_newlines=True,stderr=subprocess.PIPE)
        self.assertEqual(result.stderr[:6],'usage:')

    def test_directory_valid(self):
        result = subprocess.run(['python3', 'hw6searchdir.py', 'README.md'], stdout=subprocess.PIPE,universal_newlines=True)
        self.assertEqual(result.stdout[-11:],'directory.\n')

    def test_invalid_arg(self):
        result = subprocess.run(['python3', 'hw6searchdir.py','tests/data/nrd-1/fmnc.cc','--skdjlfhalkjsdf'],universal_newlines=True,stderr=subprocess.PIPE)
        self.assertEqual(result.stderr[:6],'usage:')


if __name__ == "__main__":
    unittest.main(verbosity=2)