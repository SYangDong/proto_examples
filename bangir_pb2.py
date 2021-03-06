# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bangir.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bangir.proto',
  package='tvm',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x62\x61ngir.proto\x12\x03tvm\"$\n\tFusedNode\x12\x17\n\x04node\x18\x01 \x03(\x0b\x32\t.tvm.Node\"\xfa\x01\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12\x10\n\x08op_index\x18\x03 \x01(\x05\x12 \n\tdata_type\x18\x04 \x01(\x0e\x32\r.tvm.DataType\x12\r\n\x05input\x18\x05 \x03(\t\x12+\n\x0finput_datashape\x18\x06 \x03(\x0b\x32\x12.tvm.ListOfInteger\x12\"\n\ndata_shape\x18\x07 \x03(\x0b\x32\x0e.tvm.DataShape\x12!\n\tconvparam\x18\x65 \x01(\x0b\x32\x0e.tvm.ConvParam\x12!\n\tdataparam\x18\x66 \x01(\x0b\x32\x0e.tvm.DataParam\"\x1b\n\tDataShape\x12\x0e\n\x06number\x18\x01 \x01(\x05\"k\n\tConvParam\x12\x13\n\x0bkernel_size\x18\x01 \x03(\x05\x12\x0b\n\x03pad\x18\x02 \x03(\x05\x12\x0e\n\x06stride\x18\x03 \x03(\x05\x12\x10\n\x08\x64ilation\x18\x04 \x03(\x05\x12\x0c\n\x04\x62ias\x18\x05 \x01(\x08\x12\x0c\n\x04relu\x18\x06 \x01(\x08\"\x1d\n\rListOfInteger\x12\x0c\n\x04ints\x18\x02 \x03(\x05\"b\n\tDataParam\x12\x1f\n\x06layout\x18\x01 \x01(\x0e\x32\x0f.tvm.DataLayout\x12\x10\n\x08position\x18\x02 \x01(\x05\x12\r\n\x05scale\x18\x03 \x01(\x02\x12\x13\n\x0b\x64ump_folder\x18\x04 \x01(\t*9\n\x08\x44\x61taType\x12\x0b\n\x07\x46LOAT16\x10\x00\x12\x0b\n\x07\x46LOAT32\x10\x01\x12\x08\n\x04INT8\x10\x02\x12\t\n\x05INT16\x10\x03*?\n\nDataLayout\x12\x0b\n\x07ONE_DIM\x10\x00\x12\x08\n\x04NHWC\x10\x01\x12\x08\n\x04NCHW\x10\x02\x12\x07\n\x03\x43HW\x10\x03\x12\x07\n\x03HWC\x10\x04\x62\x06proto3')
)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='tvm.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOAT16', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT32', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT8', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT16', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=581,
  serialized_end=638,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_DATALAYOUT = _descriptor.EnumDescriptor(
  name='DataLayout',
  full_name='tvm.DataLayout',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ONE_DIM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NHWC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NCHW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHW', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HWC', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=640,
  serialized_end=703,
)
_sym_db.RegisterEnumDescriptor(_DATALAYOUT)

DataLayout = enum_type_wrapper.EnumTypeWrapper(_DATALAYOUT)
FLOAT16 = 0
FLOAT32 = 1
INT8 = 2
INT16 = 3
ONE_DIM = 0
NHWC = 1
NCHW = 2
CHW = 3
HWC = 4



_FUSEDNODE = _descriptor.Descriptor(
  name='FusedNode',
  full_name='tvm.FusedNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='tvm.FusedNode.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=21,
  serialized_end=57,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='tvm.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tvm.Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='tvm.Node.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op_index', full_name='tvm.Node.op_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='tvm.Node.data_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input', full_name='tvm.Node.input', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_datashape', full_name='tvm.Node.input_datashape', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_shape', full_name='tvm.Node.data_shape', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='convparam', full_name='tvm.Node.convparam', index=7,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataparam', full_name='tvm.Node.dataparam', index=8,
      number=102, type=11, cpp_type=10, label=1,
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
  serialized_start=60,
  serialized_end=310,
)


_DATASHAPE = _descriptor.Descriptor(
  name='DataShape',
  full_name='tvm.DataShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='tvm.DataShape.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=312,
  serialized_end=339,
)


_CONVPARAM = _descriptor.Descriptor(
  name='ConvParam',
  full_name='tvm.ConvParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kernel_size', full_name='tvm.ConvParam.kernel_size', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pad', full_name='tvm.ConvParam.pad', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride', full_name='tvm.ConvParam.stride', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dilation', full_name='tvm.ConvParam.dilation', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bias', full_name='tvm.ConvParam.bias', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relu', full_name='tvm.ConvParam.relu', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=341,
  serialized_end=448,
)


_LISTOFINTEGER = _descriptor.Descriptor(
  name='ListOfInteger',
  full_name='tvm.ListOfInteger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ints', full_name='tvm.ListOfInteger.ints', index=0,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=450,
  serialized_end=479,
)


_DATAPARAM = _descriptor.Descriptor(
  name='DataParam',
  full_name='tvm.DataParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layout', full_name='tvm.DataParam.layout', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='tvm.DataParam.position', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='tvm.DataParam.scale', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dump_folder', full_name='tvm.DataParam.dump_folder', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=481,
  serialized_end=579,
)

_FUSEDNODE.fields_by_name['node'].message_type = _NODE
_NODE.fields_by_name['data_type'].enum_type = _DATATYPE
_NODE.fields_by_name['input_datashape'].message_type = _LISTOFINTEGER
_NODE.fields_by_name['data_shape'].message_type = _DATASHAPE
_NODE.fields_by_name['convparam'].message_type = _CONVPARAM
_NODE.fields_by_name['dataparam'].message_type = _DATAPARAM
_DATAPARAM.fields_by_name['layout'].enum_type = _DATALAYOUT
DESCRIPTOR.message_types_by_name['FusedNode'] = _FUSEDNODE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['DataShape'] = _DATASHAPE
DESCRIPTOR.message_types_by_name['ConvParam'] = _CONVPARAM
DESCRIPTOR.message_types_by_name['ListOfInteger'] = _LISTOFINTEGER
DESCRIPTOR.message_types_by_name['DataParam'] = _DATAPARAM
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
DESCRIPTOR.enum_types_by_name['DataLayout'] = _DATALAYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FusedNode = _reflection.GeneratedProtocolMessageType('FusedNode', (_message.Message,), dict(
  DESCRIPTOR = _FUSEDNODE,
  __module__ = 'bangir_pb2'
  # @@protoc_insertion_point(class_scope:tvm.FusedNode)
  ))
_sym_db.RegisterMessage(FusedNode)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'bangir_pb2'
  # @@protoc_insertion_point(class_scope:tvm.Node)
  ))
_sym_db.RegisterMessage(Node)

DataShape = _reflection.GeneratedProtocolMessageType('DataShape', (_message.Message,), dict(
  DESCRIPTOR = _DATASHAPE,
  __module__ = 'bangir_pb2'
  # @@protoc_insertion_point(class_scope:tvm.DataShape)
  ))
_sym_db.RegisterMessage(DataShape)

ConvParam = _reflection.GeneratedProtocolMessageType('ConvParam', (_message.Message,), dict(
  DESCRIPTOR = _CONVPARAM,
  __module__ = 'bangir_pb2'
  # @@protoc_insertion_point(class_scope:tvm.ConvParam)
  ))
_sym_db.RegisterMessage(ConvParam)

ListOfInteger = _reflection.GeneratedProtocolMessageType('ListOfInteger', (_message.Message,), dict(
  DESCRIPTOR = _LISTOFINTEGER,
  __module__ = 'bangir_pb2'
  # @@protoc_insertion_point(class_scope:tvm.ListOfInteger)
  ))
_sym_db.RegisterMessage(ListOfInteger)

DataParam = _reflection.GeneratedProtocolMessageType('DataParam', (_message.Message,), dict(
  DESCRIPTOR = _DATAPARAM,
  __module__ = 'bangir_pb2'
  # @@protoc_insertion_point(class_scope:tvm.DataParam)
  ))
_sym_db.RegisterMessage(DataParam)


# @@protoc_insertion_point(module_scope)
