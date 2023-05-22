from concurrent import futures

import time
import grpc
from protos import users_pb2 as pb
from protos import users_pb2_grpc as pbg

from google.protobuf.json_format import MessageToDict

URI = "localhost:50051"

u1 = pb.User(id="10", name="tester", email="m.co", password="pw")
u2 = pb.User(id="11", name="hello", email="p.co", password="123")
u3 = pb.User(id="12", name="okay", email="n.co", password="00")
test_users = [u1, u2, u3]


def request_stream():
    for user in test_users:
        req = pb.CreateUserStreamRequest(user=user)
        yield req
        time.sleep(2)


def run(URI):
    with grpc.insecure_channel(URI) as channel:
        stub = pbg.UsersStub(channel)


        """
        get_users_responses = stub.GetUserStream(pb.GetUserStreamRequest())
        print(get_users_responses)
        for response in get_users_responses:
            print(response)

        get_user_by_id_response = stub.GetUserById(users_pb2.GetUserByIdRequest(id="1"))

        u3 = users_pb2.User(id="3", name="Funky", email="mail.as", password="pwwpww")
        create_user_response = stub.CreateUser(users_pb2.CreateUserRequest(user=u3))

        u3 = users_pb2.User(id="3", name="Crap", email="mail.as", password="pwwpww")
        update_user_response = stub.UpdateUser(users_pb2.UpdateUserRequest(user=u3))

        get_another_users_response = stub.GetUsers(users_pb2.GetUsersRequest())

        delete_user_response = stub.DeleteUser(users_pb2.DeleteUserRequest(user=u3))

        get_another2_users_response = stub.GetUsers(users_pb2.GetUsersRequest())

        create_user_stream_response = stub.CreateUserStream(request_stream())
        """

        dual_stream_response = stub.CreateUserDualStream(request_stream())
        for res in dual_stream_response:
            print(res)

    """

    user = get_users_response.users[0]
    test = MessageToDict(user)

    print(test)
    print(type(test))
    print("-------------------")

    print(get_user_by_id_response)
    print(type(get_user_by_id_response))

    print("create new users--")
    print(create_user_response)
    print(type(create_user_response))

    print("--update users ---")
    print(update_user_response)
    print(type(update_user_response))

    print("--check users again--")
    print(get_another_users_response.users)
    print(type(get_another_users_response.users))
    print(type(get_another_users_response))

    print("--deleted--")
    print(delete_user_response)

    print("---after--delete--")
    print(get_another2_users_response)

    """

if __name__ == "__main__":
    run(URI)
