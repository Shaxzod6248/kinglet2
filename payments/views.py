import stripe
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CardPaymentSerializer
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class CardPaymentView(generics.CreateAPIView):
    serializer_class = CardPaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        card_number = serializer.validated_data['card_number']
        exp_month = serializer.validated_data['exp_month']
        exp_year = serializer.validated_data['exp_year']
        cvc = serializer.validated_data['cvc']
        amount = serializer.validated_data['amount']

        try:
            token = stripe.Token.create(
                card={
                    "number": card_number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc
                }
            )

            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token.id
            )

            return Response({'success': True, 'charge': charge})
        except stripe.error.StripeError as e:
            return Response({'success': False, 'error': str(e)})
