from rest_framework import serializers
from .models import Log,brookuser,complaint,product, cart, category, Review, order

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
    def Create(self,validated_data):
        return cart.objects.Create(**validated_data)


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
        return cart.objects.Create(**validated_data)

