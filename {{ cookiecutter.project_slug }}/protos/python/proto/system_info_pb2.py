# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/system_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/system_info.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x17proto/system_info.proto\"5\n\x11SystemInfoRequest\x12 \n\x0b\x63lient_info\x18\x01 \x01(\x0b\x32\x0b.ClientInfo\"X\n\x12SystemInfoResponse\x12 \n\x0b\x63lient_info\x18\x01 \x01(\x0b\x32\x0b.ClientInfo\x12 \n\x0bserver_info\x18\x02 \x01(\x0b\x32\x0b.ServerInfo\"*\n\nClientInfo\x12\x1c\n\thost_info\x18\x01 \x01(\x0b\x32\t.HostInfo\"*\n\nServerInfo\x12\x1c\n\thost_info\x18\x01 \x01(\x0b\x32\t.HostInfo\"N\n\x08HostInfo\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x0f\n\x07ip_addr\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x05\x32\x45\n\nSystemInfo\x12\x37\n\nSystemInfo\x12\x12.SystemInfoRequest\x1a\x13.SystemInfoResponse\"\x00\x62\x06proto3')
)




_SYSTEMINFOREQUEST = _descriptor.Descriptor(
  name='SystemInfoRequest',
  full_name='SystemInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_info', full_name='SystemInfoRequest.client_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=80,
)


_SYSTEMINFORESPONSE = _descriptor.Descriptor(
  name='SystemInfoResponse',
  full_name='SystemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_info', full_name='SystemInfoResponse.client_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_info', full_name='SystemInfoResponse.server_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=170,
)


_CLIENTINFO = _descriptor.Descriptor(
  name='ClientInfo',
  full_name='ClientInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_info', full_name='ClientInfo.host_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=214,
)


_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_info', full_name='ServerInfo.host_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=258,
)


_HOSTINFO = _descriptor.Descriptor(
  name='HostInfo',
  full_name='HostInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='HostInfo.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_addr', full_name='HostInfo.ip_addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='HostInfo.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='HostInfo.timestamp', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=338,
)

_SYSTEMINFOREQUEST.fields_by_name['client_info'].message_type = _CLIENTINFO
_SYSTEMINFORESPONSE.fields_by_name['client_info'].message_type = _CLIENTINFO
_SYSTEMINFORESPONSE.fields_by_name['server_info'].message_type = _SERVERINFO
_CLIENTINFO.fields_by_name['host_info'].message_type = _HOSTINFO
_SERVERINFO.fields_by_name['host_info'].message_type = _HOSTINFO
DESCRIPTOR.message_types_by_name['SystemInfoRequest'] = _SYSTEMINFOREQUEST
DESCRIPTOR.message_types_by_name['SystemInfoResponse'] = _SYSTEMINFORESPONSE
DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['HostInfo'] = _HOSTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemInfoRequest = _reflection.GeneratedProtocolMessageType('SystemInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMINFOREQUEST,
  __module__ = 'proto.system_info_pb2'
  # @@protoc_insertion_point(class_scope:SystemInfoRequest)
  ))
_sym_db.RegisterMessage(SystemInfoRequest)

SystemInfoResponse = _reflection.GeneratedProtocolMessageType('SystemInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMINFORESPONSE,
  __module__ = 'proto.system_info_pb2'
  # @@protoc_insertion_point(class_scope:SystemInfoResponse)
  ))
_sym_db.RegisterMessage(SystemInfoResponse)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTINFO,
  __module__ = 'proto.system_info_pb2'
  # @@protoc_insertion_point(class_scope:ClientInfo)
  ))
_sym_db.RegisterMessage(ClientInfo)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO,
  __module__ = 'proto.system_info_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo)
  ))
_sym_db.RegisterMessage(ServerInfo)

HostInfo = _reflection.GeneratedProtocolMessageType('HostInfo', (_message.Message,), dict(
  DESCRIPTOR = _HOSTINFO,
  __module__ = 'proto.system_info_pb2'
  # @@protoc_insertion_point(class_scope:HostInfo)
  ))
_sym_db.RegisterMessage(HostInfo)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class SystemInfoStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.SystemInfo = channel.unary_unary(
          '/SystemInfo/SystemInfo',
          request_serializer=SystemInfoRequest.SerializeToString,
          response_deserializer=SystemInfoResponse.FromString,
          )


  class SystemInfoServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def SystemInfo(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_SystemInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SystemInfo': grpc.unary_unary_rpc_method_handler(
            servicer.SystemInfo,
            request_deserializer=SystemInfoRequest.FromString,
            response_serializer=SystemInfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'SystemInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaSystemInfoServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def SystemInfo(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaSystemInfoStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def SystemInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    SystemInfo.future = None


  def beta_create_SystemInfo_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('SystemInfo', 'SystemInfo'): SystemInfoRequest.FromString,
    }
    response_serializers = {
      ('SystemInfo', 'SystemInfo'): SystemInfoResponse.SerializeToString,
    }
    method_implementations = {
      ('SystemInfo', 'SystemInfo'): face_utilities.unary_unary_inline(servicer.SystemInfo),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_SystemInfo_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('SystemInfo', 'SystemInfo'): SystemInfoRequest.SerializeToString,
    }
    response_deserializers = {
      ('SystemInfo', 'SystemInfo'): SystemInfoResponse.FromString,
    }
    cardinalities = {
      'SystemInfo': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'SystemInfo', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
