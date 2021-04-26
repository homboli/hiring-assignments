# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='statistics',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\nstatistics\"\xb4\x01\n\x18ProcessStatisticsRequest\x12&\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\x14.statistics.Document\x12:\n\x12\x61ggregationColumns\x18\x02 \x01(\x0b\x32\x1e.statistics.AggregationColumns\x12\x34\n\x0f\x65xcludedColumns\x18\x03 \x01(\x0b\x32\x1b.statistics.ExcludedColumns\")\n\x16ProcessStatisticsReply\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"G\n\x08\x44ocument\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12*\n\x06source\x18\x02 \x01(\x0b\x32\x1a.statistics.DocumentSource\"\"\n\x0e\x44ocumentSource\x12\x10\n\x08http_uri\x18\x01 \x01(\t\"0\n\x12\x41ggregationColumns\x12\x1a\n\x12\x61ggregationColumns\x18\x01 \x03(\t\"*\n\x0f\x45xcludedColumns\x12\x17\n\x0f\x65xcludedColumns\x18\x01 \x03(\t2}\n\x1aSummaryStatisticsProcessor\x12_\n\x11ProcessStatistics\x12$.statistics.ProcessStatisticsRequest\x1a\".statistics.ProcessStatisticsReply\"\x00\x62\x06proto3'
)




_PROCESSSTATISTICSREQUEST = _descriptor.Descriptor(
  name='ProcessStatisticsRequest',
  full_name='statistics.ProcessStatisticsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='document', full_name='statistics.ProcessStatisticsRequest.document', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregationColumns', full_name='statistics.ProcessStatisticsRequest.aggregationColumns', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='excludedColumns', full_name='statistics.ProcessStatisticsRequest.excludedColumns', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=26,
  serialized_end=206,
)


_PROCESSSTATISTICSREPLY = _descriptor.Descriptor(
  name='ProcessStatisticsReply',
  full_name='statistics.ProcessStatisticsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='statistics.ProcessStatisticsReply.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=208,
  serialized_end=249,
)


_DOCUMENT = _descriptor.Descriptor(
  name='Document',
  full_name='statistics.Document',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='statistics.Document.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='statistics.Document.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=251,
  serialized_end=322,
)


_DOCUMENTSOURCE = _descriptor.Descriptor(
  name='DocumentSource',
  full_name='statistics.DocumentSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_uri', full_name='statistics.DocumentSource.http_uri', index=0,
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
  serialized_start=324,
  serialized_end=358,
)


_AGGREGATIONCOLUMNS = _descriptor.Descriptor(
  name='AggregationColumns',
  full_name='statistics.AggregationColumns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='aggregationColumns', full_name='statistics.AggregationColumns.aggregationColumns', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=408,
)


_EXCLUDEDCOLUMNS = _descriptor.Descriptor(
  name='ExcludedColumns',
  full_name='statistics.ExcludedColumns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='excludedColumns', full_name='statistics.ExcludedColumns.excludedColumns', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=452,
)

_PROCESSSTATISTICSREQUEST.fields_by_name['document'].message_type = _DOCUMENT
_PROCESSSTATISTICSREQUEST.fields_by_name['aggregationColumns'].message_type = _AGGREGATIONCOLUMNS
_PROCESSSTATISTICSREQUEST.fields_by_name['excludedColumns'].message_type = _EXCLUDEDCOLUMNS
_DOCUMENT.fields_by_name['source'].message_type = _DOCUMENTSOURCE
DESCRIPTOR.message_types_by_name['ProcessStatisticsRequest'] = _PROCESSSTATISTICSREQUEST
DESCRIPTOR.message_types_by_name['ProcessStatisticsReply'] = _PROCESSSTATISTICSREPLY
DESCRIPTOR.message_types_by_name['Document'] = _DOCUMENT
DESCRIPTOR.message_types_by_name['DocumentSource'] = _DOCUMENTSOURCE
DESCRIPTOR.message_types_by_name['AggregationColumns'] = _AGGREGATIONCOLUMNS
DESCRIPTOR.message_types_by_name['ExcludedColumns'] = _EXCLUDEDCOLUMNS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessStatisticsRequest = _reflection.GeneratedProtocolMessageType('ProcessStatisticsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSSTATISTICSREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:statistics.ProcessStatisticsRequest)
  })
_sym_db.RegisterMessage(ProcessStatisticsRequest)

ProcessStatisticsReply = _reflection.GeneratedProtocolMessageType('ProcessStatisticsReply', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSSTATISTICSREPLY,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:statistics.ProcessStatisticsReply)
  })
_sym_db.RegisterMessage(ProcessStatisticsReply)

Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:statistics.Document)
  })
_sym_db.RegisterMessage(Document)

DocumentSource = _reflection.GeneratedProtocolMessageType('DocumentSource', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTSOURCE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:statistics.DocumentSource)
  })
_sym_db.RegisterMessage(DocumentSource)

AggregationColumns = _reflection.GeneratedProtocolMessageType('AggregationColumns', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATIONCOLUMNS,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:statistics.AggregationColumns)
  })
_sym_db.RegisterMessage(AggregationColumns)

ExcludedColumns = _reflection.GeneratedProtocolMessageType('ExcludedColumns', (_message.Message,), {
  'DESCRIPTOR' : _EXCLUDEDCOLUMNS,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:statistics.ExcludedColumns)
  })
_sym_db.RegisterMessage(ExcludedColumns)



_SUMMARYSTATISTICSPROCESSOR = _descriptor.ServiceDescriptor(
  name='SummaryStatisticsProcessor',
  full_name='statistics.SummaryStatisticsProcessor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=454,
  serialized_end=579,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessStatistics',
    full_name='statistics.SummaryStatisticsProcessor.ProcessStatistics',
    index=0,
    containing_service=None,
    input_type=_PROCESSSTATISTICSREQUEST,
    output_type=_PROCESSSTATISTICSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUMMARYSTATISTICSPROCESSOR)

DESCRIPTOR.services_by_name['SummaryStatisticsProcessor'] = _SUMMARYSTATISTICSPROCESSOR

# @@protoc_insertion_point(module_scope)
