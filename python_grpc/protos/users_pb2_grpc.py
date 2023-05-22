# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import users_pb2 as users__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUsers = channel.unary_unary(
                '/users.Users/GetUsers',
                request_serializer=users__pb2.GetUsersRequest.SerializeToString,
                response_deserializer=users__pb2.GetUsersResponse.FromString,
                )
        self.GetUserById = channel.unary_unary(
                '/users.Users/GetUserById',
                request_serializer=users__pb2.GetUserByIdRequest.SerializeToString,
                response_deserializer=users__pb2.GetUserByIdResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/users.Users/CreateUser',
                request_serializer=users__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=users__pb2.CreateUserResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/users.Users/UpdateUser',
                request_serializer=users__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=users__pb2.UpdateUserResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/users.Users/DeleteUser',
                request_serializer=users__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=users__pb2.DeleteUserResponse.FromString,
                )
        self.GetUserStream = channel.unary_stream(
                '/users.Users/GetUserStream',
                request_serializer=users__pb2.GetUserStreamRequest.SerializeToString,
                response_deserializer=users__pb2.GetUserStreamResponse.FromString,
                )
        self.CreateUserStream = channel.stream_unary(
                '/users.Users/CreateUserStream',
                request_serializer=users__pb2.CreateUserStreamRequest.SerializeToString,
                response_deserializer=users__pb2.CreateUserStreamResponse.FromString,
                )
        self.CreateUserDualStream = channel.stream_stream(
                '/users.Users/CreateUserDualStream',
                request_serializer=users__pb2.CreateUserStreamRequest.SerializeToString,
                response_deserializer=users__pb2.GetUserStreamResponse.FromString,
                )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUserStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUserDualStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=users__pb2.GetUsersRequest.FromString,
                    response_serializer=users__pb2.GetUsersResponse.SerializeToString,
            ),
            'GetUserById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserById,
                    request_deserializer=users__pb2.GetUserByIdRequest.FromString,
                    response_serializer=users__pb2.GetUserByIdResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=users__pb2.CreateUserRequest.FromString,
                    response_serializer=users__pb2.CreateUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=users__pb2.UpdateUserRequest.FromString,
                    response_serializer=users__pb2.UpdateUserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=users__pb2.DeleteUserRequest.FromString,
                    response_serializer=users__pb2.DeleteUserResponse.SerializeToString,
            ),
            'GetUserStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetUserStream,
                    request_deserializer=users__pb2.GetUserStreamRequest.FromString,
                    response_serializer=users__pb2.GetUserStreamResponse.SerializeToString,
            ),
            'CreateUserStream': grpc.stream_unary_rpc_method_handler(
                    servicer.CreateUserStream,
                    request_deserializer=users__pb2.CreateUserStreamRequest.FromString,
                    response_serializer=users__pb2.CreateUserStreamResponse.SerializeToString,
            ),
            'CreateUserDualStream': grpc.stream_stream_rpc_method_handler(
                    servicer.CreateUserDualStream,
                    request_deserializer=users__pb2.CreateUserStreamRequest.FromString,
                    response_serializer=users__pb2.GetUserStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'users.Users', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/GetUsers',
            users__pb2.GetUsersRequest.SerializeToString,
            users__pb2.GetUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/GetUserById',
            users__pb2.GetUserByIdRequest.SerializeToString,
            users__pb2.GetUserByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/CreateUser',
            users__pb2.CreateUserRequest.SerializeToString,
            users__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/UpdateUser',
            users__pb2.UpdateUserRequest.SerializeToString,
            users__pb2.UpdateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.Users/DeleteUser',
            users__pb2.DeleteUserRequest.SerializeToString,
            users__pb2.DeleteUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/users.Users/GetUserStream',
            users__pb2.GetUserStreamRequest.SerializeToString,
            users__pb2.GetUserStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUserStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/users.Users/CreateUserStream',
            users__pb2.CreateUserStreamRequest.SerializeToString,
            users__pb2.CreateUserStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUserDualStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/users.Users/CreateUserDualStream',
            users__pb2.CreateUserStreamRequest.SerializeToString,
            users__pb2.GetUserStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
