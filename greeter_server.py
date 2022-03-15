from concurrent import futures
from distutils.debug import DEBUG
import logging
from urllib import response
import seqlog
import ping_pong_pb2
import ping_pong_pb2_grpc
import grpc
import sys


class Greeter(ping_pong_pb2_grpc.GreeterServicer):

    def PingPong(self, request, context):    
        if request.ping == 'ping':
            return ping_pong_pb2.PongReply(pong='pong')
        stout = logging.StreamHandler(sys.stdout)
        logger.error()
        return ping_pong_pb2.PongReply(pong=not_ping)    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  #???
    ping_pong_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logger = logging.getLogger('PingPongLog')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('DebugLog.log')
    fh.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(fh)
    serve()

