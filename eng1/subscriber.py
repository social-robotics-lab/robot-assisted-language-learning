import collections
import copy
import json
import socket
import threading
import time
import typing


class TCPSubscriber(object):

    def __init__(self, ip:str, port:int, maxlen:typing.Optional[int]=None):
        self.__conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__conn.connect((ip, port))
        self.__memory = collections.deque(maxlen=maxlen)
        self.__lock = threading.Lock()

    def subscribe(self):
        t = threading.Thread(target=self.__run, daemon=True)
        t.start()

    def get_memory(self, duration:typing.Optional[float]=None) -> list:
        with self.__lock:
            if duration is None:
                return copy.deepcopy(self.__memory)
            else:
                return [e for e in self.__memory if time.time() - e['timestamp'] < duration]

    def get_memory_between(self, begin:float, end:float) -> list:
        with self.__lock:
            return [e for e in self.__memory if begin < e['timestamp'] < end]
            
    def close(self):
        self.__conn.close()

    def __run(self):
        try:                
            while True:
                data = self.__recv()
                if data == b'': break
                json_str = data.decode('utf8')
                obj = json.loads(json_str)
                with self.__lock:
                    self.__memory.append(obj)
        except ConnectionResetError:
            pass
        except ConnectionAbortedError:
            pass
        self.__conn.close()

    def __read_size(self) -> int:
        b_size = self.__conn.recv(4)
        return int.from_bytes(b_size, byteorder='big')

    def __read_data(self, size:int) -> bytes:
        chunks = []
        bytes_recved = 0
        while bytes_recved < size:
            chunk = self.__conn.recv(size - bytes_recved)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recved += len(chunk)
        return b''.join(chunks)

    def __recv(self) -> bytes:
        size = self.__read_size()
        data = self.__read_data(size)
        return data
