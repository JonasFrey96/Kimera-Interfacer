# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Block.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Block.proto',
  package='voxblox',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x42lock.proto\x12\x07voxblox\"\x95\x01\n\nBlockProto\x12\x17\n\x0fvoxels_per_side\x18\x01 \x01(\x05\x12\x12\n\nvoxel_size\x18\x02 \x01(\x01\x12\x10\n\x08origin_x\x18\x03 \x01(\x01\x12\x10\n\x08origin_y\x18\x04 \x01(\x01\x12\x10\n\x08origin_z\x18\x05 \x01(\x01\x12\x10\n\x08has_data\x18\x06 \x01(\x08\x12\x12\n\nvoxel_data\x18\x07 \x03(\r'
)




_BLOCKPROTO = _descriptor.Descriptor(
  name='BlockProto',
  full_name='voxblox.BlockProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='voxels_per_side', full_name='voxblox.BlockProto.voxels_per_side', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voxel_size', full_name='voxblox.BlockProto.voxel_size', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_x', full_name='voxblox.BlockProto.origin_x', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_y', full_name='voxblox.BlockProto.origin_y', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_z', full_name='voxblox.BlockProto.origin_z', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_data', full_name='voxblox.BlockProto.has_data', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voxel_data', full_name='voxblox.BlockProto.voxel_data', index=6,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['BlockProto'] = _BLOCKPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockProto = _reflection.GeneratedProtocolMessageType('BlockProto', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKPROTO,
  '__module__' : 'Block_pb2'
  # @@protoc_insertion_point(class_scope:voxblox.BlockProto)
  })
_sym_db.RegisterMessage(BlockProto)


# @@protoc_insertion_point(module_scope)
