# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: userinfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='userinfo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0euserinfo.proto\"\x1f\n\x0bUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\")\n\tUserReply\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t25\n\x08UserInfo\x12)\n\x0bGetUserInfo\x12\x0c.UserRequest\x1a\n.UserReply\"\x00\x62\x06proto3'
)




_USERREQUEST = _descriptor.Descriptor(
  name='UserRequest',
  full_name='UserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='UserRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=49,
)


_USERREPLY = _descriptor.Descriptor(
  name='UserReply',
  full_name='UserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserReply.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='UserReply.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['UserRequest'] = _USERREQUEST
DESCRIPTOR.message_types_by_name['UserReply'] = _USERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserRequest = _reflection.GeneratedProtocolMessageType('UserRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREQUEST,
  '__module__' : 'userinfo_pb2'
  # @@protoc_insertion_point(class_scope:UserRequest)
  })
_sym_db.RegisterMessage(UserRequest)

UserReply = _reflection.GeneratedProtocolMessageType('UserReply', (_message.Message,), {
  'DESCRIPTOR' : _USERREPLY,
  '__module__' : 'userinfo_pb2'
  # @@protoc_insertion_point(class_scope:UserReply)
  })
_sym_db.RegisterMessage(UserReply)



_USERINFO = _descriptor.ServiceDescriptor(
  name='UserInfo',
  full_name='UserInfo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=94,
  serialized_end=147,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserInfo',
    full_name='UserInfo.GetUserInfo',
    index=0,
    containing_service=None,
    input_type=_USERREQUEST,
    output_type=_USERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERINFO)

DESCRIPTOR.services_by_name['UserInfo'] = _USERINFO

# @@protoc_insertion_point(module_scope)
