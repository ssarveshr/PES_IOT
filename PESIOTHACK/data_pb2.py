# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: data.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'data.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndata.proto\"_\n\x06Shadow\x12\x0b\n\x03sv1\x18\x01 \x01(\x05\x12\x0b\n\x03sm1\x18\x02 \x01(\x05\x12\x0b\n\x03sv2\x18\x03 \x01(\x05\x12\x0b\n\x03sm2\x18\x04 \x01(\x05\x12\t\n\x01h\x18\x05 \x01(\x02\x12\n\n\x02t1\x18\x06 \x01(\x02\x12\n\n\x02t2\x18\x07 \x01(\x02*P\n\nsensortype\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04PM25\x10\x01\x12\x08\n\x04PM10\x10\x02\x12\x07\n\x03\x43O2\x10\x03\x12\x06\n\x02O3\x10\x04\x12\x07\n\x03NO2\x10\x05\x12\x07\n\x03S02\x10\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENSORTYPE']._serialized_start=111
  _globals['_SENSORTYPE']._serialized_end=191
  _globals['_SHADOW']._serialized_start=14
  _globals['_SHADOW']._serialized_end=109
# @@protoc_insertion_point(module_scope)
