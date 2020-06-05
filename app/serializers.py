from app.models import Item, User
from django.conf import settings
from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from uuid import uuid4


class ItemSerializer(serializers.Serializer):
    title = serializers.CharField(source='title')


    class Meta:
        model = Item
        fields = ('title')




class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    # password2 = serializers.CharField(
    #     required=True,
    #     label="Confirm Password",
    #     style={'input_type': 'password'}
    # )
    hobby = serializers.CharField(
        label="hobby",
        default=""
    )
    gender = serializers.CharField(required=True,  )
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
           # 'password2',
            'gender',
            'hobby'
        )

    # extra_kwargs = {
    #     'password': {'write_only': True},
    #     'password2': {'write_only': True},
    # }


    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                                              "address has already registered. Was it you?")

        return email

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value
    # def validate_password_2(self, value):
    #     data = self.get_initial()
    #     password = data.get('password')
    #     if password != value:
    #         raise serializers.ValidationError("Passwords doesn't match.")
    #     return value


    # def validate(self,data):
    #
    #     password = self.data.get('password')
    #     password2 = self.data.get('password2')
    #

        # if not password or not password2:
        #     raise serializers.ValidationError("Please enter a password and confirm it.")
        #
        # if password != password2:
        #     raise serializers.ValidationError("Those passwords don't match.")
        #
        # return password2





class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in user_id:
            user = User.objects.filter(
                Q(email=user_id) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=user_id)
        else:
            user = User.objects.filter(
                Q(username=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(username=user_id)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )


class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )