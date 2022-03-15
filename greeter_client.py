from __future__ import print_function
from urllib import request

import grpc
import logging
import seqlog
import ping_pong_pb2
import ping_pong_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8080') as chanell:
        stub = ping_pong_pb2_grpc.GreeterStub(chanell)
        req = 'fing'
        responce = stub.PingPong(ping_pong_pb2.PingRequest(ping=req))
        print(f'{req}\n'
              f'{responce.pong}\n')

if __name__ == '__main__':
    logger = logging.getLogger('PingPongLog')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('DebugLog.log')
    fh.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(fh)
    logging.basicConfig
    run()