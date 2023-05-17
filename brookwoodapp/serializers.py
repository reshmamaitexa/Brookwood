from rest_framework import serializers
from django.conf import settings
from .models import Log,brookuser,complaint,product, cart, category, Review, order, payment

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = brookuser
        fields = '__all__'
    def Create(self, validated_data):
        return brookuser.objects.Create(**validated_data)

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = product
#         fields = '__all__'
#     def Create(self,validated_data):
#         return product.objects.Create(**validated_data)

# class FeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = feedback
#         fields = '__all__'
#     def Create(self,validated_data):
#         return feedback.objects.Create(**validated_data)

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = complaint
        fields = '__all__'
    def Create(self,validated_data):
        return complaint.objects.Create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__' 

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = '__all__'
    def create(self,validated_data):
        return cart.objects.create(**validated_data)

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if obj.image:
    #         return request.build_absolute_uri(obj.image.url)
    #     return None


# class CartSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()

#     class Meta:
#         model = cart
#         fields = '__all__'

#     def Create(self,validated_data):
#         return cart.objects.Create(**validated_data)

#     def get_image_url(self, obj):
#         if obj.image:
#             return self.context['request'].build_absolute_uri(obj.image.url)
#         return None


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    def Create(self,validated_data):
        return Review.objects.Create(**validated_data)

        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
    def Create(self,validated_data):
        return order.objects.Create(**validated_data)



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
    def Create(self,validated_data):
        return payment.objects.Create(**validated_data)

