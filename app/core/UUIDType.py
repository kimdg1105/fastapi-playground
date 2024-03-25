import uuid

from sqlalchemy import TypeDecorator, BINARY


def generate_uuid():
    return str(uuid.uuid4())


class UUIDType(TypeDecorator):
    impl = BINARY(16)

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        return uuid.UUID(value).bytes

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        return str(uuid.UUID(bytes=value))
