from rest_framework import serializers


class CardPaymentSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=20)
    exp_month = serializers.IntegerField()
    exp_year = serializers.IntegerField()
    cvc = serializers.IntegerField()
    amount = serializers.IntegerField()
