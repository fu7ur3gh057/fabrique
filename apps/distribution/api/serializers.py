from rest_framework import serializers

from apps.distribution.models import Distribution, Message


# Distribution

class DistributionOutputSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    filter = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = Distribution
        fields = '__all__'


class DistributionInputSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    filter = serializers.ListSerializer(child=serializers.CharField())

    class Meta:
        model = Distribution
        fields = [
            'pk_id',
            'start_time',
            'end_time',
            'text',
            'filter'
        ]

    def save(self, **kwargs: dict) -> Distribution:
        return super().save(**kwargs)


class DistributionUpdateSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    start_time = serializers.DateTimeField(required=False)
    end_time = serializers.DateTimeField(required=False)
    text = serializers.CharField(required=False)
    filter = serializers.ListSerializer(required=False, child=serializers.CharField())

    class Meta:
        model = Distribution
        fields = [
            'pk_id',
            'start_time',
            'end_time',
            'text',
            'filter'
        ]

    def update(self, instance: Distribution, validated_data: dict) -> Distribution:
        super().update(instance=instance, validated_data=validated_data)
        return instance


class DistributionStatisticSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    messages = serializers.SerializerMethodField(read_only=True)

    def get_messages(self, obj: Distribution) -> dict:
        messages = obj.messages
        created_count = messages.filter(status__exact='CREATED').all().count()
        error_count = messages.filter(status__exact='ERROR').all().count()
        success_count = messages.filter(status__exact='SUCCESS').all().count()
        expired_count = messages.filter(status__exact='EXPIRED').all().count()
        return {
            "created": created_count,
            "error": error_count,
            "success": success_count,
            "expired": expired_count,
        }

    class Meta:
        model = Distribution
        fields = [
            'pk_id',
            'messages'
        ]


class MessageOutputSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = [
            'pk_id',
            'status',
            'created_at',
            'client'
        ]


class DistributionDetailStatisticSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    filter = serializers.ListSerializer(child=serializers.CharField())
    messages = serializers.SerializerMethodField()

    def get_messages(self, obj: Distribution) -> list[MessageOutputSerializer]:
        messages = obj.messages
        return [MessageOutputSerializer(msg).data for msg in messages.all()]

    class Meta:
        model = Distribution
        fields = [
            'pk_id',
            'start_time',
            'end_time',
            'text',
            'filter',
            'messages'
        ]
