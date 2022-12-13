from decimal import Decimal
from bson.codec_options import CodecOptions, TypeCodec, TypeRegistry
from bson.decimal128 import Decimal128


class DecimalCodec(TypeCodec):
    python_type = Decimal
    bson_type = Decimal128

    def transform_python(self, value: Decimal) -> Decimal128:
        return Decimal128(value)

    def transform_bson(self, value: Decimal128) -> Decimal:
        return value.to_decimal().quantize(Decimal("0.00"))

type_registry = TypeRegistry([DecimalCodec()])
codec_options = CodecOptions(type_registry=type_registry)