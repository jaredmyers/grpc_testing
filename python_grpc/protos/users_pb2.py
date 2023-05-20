# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x05users\"A\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"\x11\n\x0fGetUsersRequest\".\n\x10GetUsersResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b\x32\x0b.users.User\"\x16\n\x14GetUserStreamRequest\"2\n\x15GetUserStreamResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"0\n\x13GetUserByIdResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\".\n\x11\x43reateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12\x43reateUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"4\n\x17\x43reateUserStreamRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"*\n\x18\x43reateUserStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\".\n\x11UpdateUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\" \n\x12UpdateUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\".\n\x11\x44\x65leteUserRequest\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User\"/\n\x12\x44\x65leteUserResponse\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.users.User2\x86\x04\n\x05Users\x12=\n\x08GetUsers\x12\x16.users.GetUsersRequest\x1a\x17.users.GetUsersResponse\"\x00\x12\x46\n\x0bGetUserById\x12\x19.users.GetUserByIdRequest\x1a\x1a.users.GetUserByIdResponse\"\x00\x12\x43\n\nCreateUser\x12\x18.users.CreateUserRequest\x1a\x19.users.CreateUserResponse\"\x00\x12\x43\n\nUpdateUser\x12\x18.users.UpdateUserRequest\x1a\x19.users.UpdateUserResponse\"\x00\x12\x43\n\nDeleteUser\x12\x18.users.DeleteUserRequest\x1a\x19.users.DeleteUserResponse\"\x00\x12N\n\rGetUserStream\x12\x1b.users.GetUserStreamRequest\x1a\x1c.users.GetUserStreamResponse\"\x00\x30\x01\x12W\n\x10\x43reateUserStream\x12\x1e.users.CreateUserStreamRequest\x1a\x1f.users.CreateUserStreamResponse\"\x00(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=22
  _USER._serialized_end=87
  _GETUSERSREQUEST._serialized_start=89
  _GETUSERSREQUEST._serialized_end=106
  _GETUSERSRESPONSE._serialized_start=108
  _GETUSERSRESPONSE._serialized_end=154
  _GETUSERSTREAMREQUEST._serialized_start=156
  _GETUSERSTREAMREQUEST._serialized_end=178
  _GETUSERSTREAMRESPONSE._serialized_start=180
  _GETUSERSTREAMRESPONSE._serialized_end=230
  _GETUSERBYIDREQUEST._serialized_start=232
  _GETUSERBYIDREQUEST._serialized_end=264
  _GETUSERBYIDRESPONSE._serialized_start=266
  _GETUSERBYIDRESPONSE._serialized_end=314
  _CREATEUSERREQUEST._serialized_start=316
  _CREATEUSERREQUEST._serialized_end=362
  _CREATEUSERRESPONSE._serialized_start=364
  _CREATEUSERRESPONSE._serialized_end=411
  _CREATEUSERSTREAMREQUEST._serialized_start=413
  _CREATEUSERSTREAMREQUEST._serialized_end=465
  _CREATEUSERSTREAMRESPONSE._serialized_start=467
  _CREATEUSERSTREAMRESPONSE._serialized_end=509
  _UPDATEUSERREQUEST._serialized_start=511
  _UPDATEUSERREQUEST._serialized_end=557
  _UPDATEUSERRESPONSE._serialized_start=559
  _UPDATEUSERRESPONSE._serialized_end=591
  _DELETEUSERREQUEST._serialized_start=593
  _DELETEUSERREQUEST._serialized_end=639
  _DELETEUSERRESPONSE._serialized_start=641
  _DELETEUSERRESPONSE._serialized_end=688
  _USERS._serialized_start=691
  _USERS._serialized_end=1209
# @@protoc_insertion_point(module_scope)