from concurrent import futures
import logging
import time

import grpc
from protos import users_pb2 as pb
from protos import users_pb2_grpc as pbg


class Users(pbg.UsersServicer):

    u1 = pb.User(id="1", name="jon", email="email", password="password")
    u2 = pb.User(id="2", name="Baxton", email="snail.co", password="pw")
    u3 = pb.User(id="3", name="larry", email="email", password="sswo")
    u4 = pb.User(id="4", name="Shawn", email="snail.co", password="piIkw")
    u5 = pb.User(id="5", name="max", email="email", password="LKJ")
    u6 = pb.User(id="6", name="mike", email="snail.co", password="JKL")
    users = [u1, u2, u3, u4, u5, u6]

    def GetUsers(self, request, context):

        # grpc repeatable type
        # users is a list of pb.User types
        response = pb.GetUsersResponse(users=self.users)

        return response

    def GetUserById(self, request, context):
        for user in self.users:
            if user.id == request.id:
                response = pb.GetUserByIdResponse(user=user)
                break

        return response

    def CreateUser(self, request, context):
        self.users.append(request.user)

        return request

    def UpdateUser(self, request, context):
        id = int(request.user.id)
        self.users[id-1] = request.user

        return pb.UpdateUserResponse(id="3")

    def DeleteUser(self, request, context):
        id = int(request.user.id)
        print(id)
        print(type(id))
        self.users = self.users[:(id-1)] + self.users[id:]

        return pb.DeleteUserResponse(user=request.user)

    def GetUserStream(self, request, context):

        # send stream back to client, one user at a time
        for user in self.users:
            response = pb.GetUserStreamResponse(user=user)

            yield response
            time.sleep(2)

    def CreateUserStream(self, request_iterator, context):

        # iterate over what client stream sent for demonstration
        count = 0
        for request in request_iterator:
            print(request)
            count = count + 1

        # send back struct with the demo processed count
        return pb.CreateUserStreamResponse(result=str(count))

    def CreateUserDualStream(self, request_iterator, context):

        # iterator over what client stream sent for demonstration
        for req in request_iterator:
            print(req)

        # send stream back to client
        for user in self.users:
            response = pb.GetUserStreamResponse(user=user)
            yield response
            time.sleep(2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pbg.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
