from rest_framework import serializers


class PrimaryKeyModelSerializer(
    serializers.PrimaryKeyRelatedField,
    serializers.ModelSerializer,
):

    def to_internal_value(self, data):
        return serializers.PrimaryKeyRelatedField.to_internal_value(self, data)

    def to_representation(self, value):
        return serializers.ModelSerializer.to_representation(self, value)

    def use_pk_only_optimization(self):
        return False if self.queryset or self.read_only else True
