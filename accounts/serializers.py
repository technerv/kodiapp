from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User
from .utils import validate_email as email_is_valid

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    
    # groups_all = serializers.ListField(source='get_groups')
    # permissions_all = serializers.ListField(source='get_all_permissions')
    class Meta: #User Model
        model = User 
        fields = ('salutation', 'first_name', 'middle_name', 'last_name', 'email', 
                  'mobile_number', 'gender', 'is_owner', 'is_tenant', 'profile_image')

# Owner Register Serializer
class OwnerRegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ('id', 'salutation', 'first_name', 'middle_name', 'last_name', 'gender',
                  'email', 'mobile_number', 'profile_image', 'password')
        extra_kwargs={'password': {'write_only':True}}


    def create(self, validated_data):
        """
        Create the object.

        :param validated_data: string
        """
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_owner = True # save if user account is owner type
        user.save()
        return user

    def validate_email(self, value):
        """
        Validate if email is valid or there is an user using the email.

        :param value: string
        :return: string
        """

        if not email_is_valid(value):
            raise serializers.ValidationError('Please use a different email address provider.')

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already in use, please use a different email address.')

        return value

# # Tenant Register Serializer
class TenantRegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ('id', 'salutation', 'first_name', 'middle_name', 'last_name', 'gender',
                  'email', 'mobile_number', 'profile_image', 'password')
        extra_kwargs={'password': {'write_only':True}}


    def create(self, validated_data):
        """
        Create the object.

        :param validated_data: string
        """
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_tenant = True # save if user account is tenant type
        user.save()
        return user

    def validate_email(self, value):
        """
        Validate if email is valid or there is an user using the email.

        :param value: string
        :return: string
        """

        if not email_is_valid(value):
            raise serializers.ValidationError('Please use a different email address provider.')

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already in use, please use a different email address.')

        return value


# Login Serializer
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    
    class Meta:
        model = User
        fields = ('email', 'password')
    
    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')
        
        if not email or not password:
            raise serializers.ValidationError("Please give both email and password")
       
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist")
        
        user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            
        if not user:
            raise serializers.ValidationError("Wrong Credentials")
        attrs['user']=user
        return attrs

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)   
    
    class Meta:
        model = User
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# from django.contrib.auth.tokens import default_token_generator
# from djoser.serializers import UidAndTokenSerializer, PasswordRetypeSerializer
# from djoser import utils
# from rest_framework import serializers

# # Generate UUID Token Serializer
# class UidAndTokenSerializer(UidAndTokenSerializer):

#     def validate_uid(self, value):
#         try:
#             uid = utils.decode_uid(value)
#             self.user = User.objects.get(pk=uid)
#         except (
#                 User.DoesNotExist,
#                 ValueError,
#                 TypeError,
#                 OverflowError
#                 ) as error:
#             raise serializers.ValidationError(
#                 self.error_messages['invalid_uid'])
#         return value

#     def validate(self, attrs):
#         self.validate_uid(attrs['uid'])
#         if not default_token_generator.check_token(self.user, attrs['token']):
#             raise serializers.ValidationError(
#                 self.error_messages['invalid_token'])
#         return attrs

# # Password Reset Confirm Retype Serializer
# class PasswordResetConfirmRetypeSerializer(
#         UidAndTokenSerializer, PasswordRetypeSerializer
#         ):
#     def validate(self, attrs):
#         attrs = super(PasswordResetConfirmRetypeSerializer, self)\
#             .validate(attrs)
#         if attrs['new_password'] != attrs['re_new_password']:
#             raise serializers.ValidationError(
#                 self.error_messages['password_mismatch'])
#         return attrs