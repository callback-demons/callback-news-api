import os
from django.core.mail import send_mail
from rest_framework import serializers
from .models import User

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


class UserSerializer(serializers.ModelSerializer):
    """
    Default user Serielizer
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'country', 'birth_date',)


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Serializer for create an User model
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'country', 'birth_date', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = user.email
        user.set_password(password)
        user.save()

        self.welcome_mail(user)
        return user

    def welcome_mail(self, user):
        module_dir = os.path.dirname(__file__)

        port = os.environ.get('EMAIL_PORT')
        smtp_server = os.environ.get('EMAIL_HOST')
        login = os.environ.get('EMAIL_HOST_USER')
        password = os.environ.get('EMAIL_HOST_PASSWORD')

        sender_email = "Callback News Team <team@callback-news.com>"
        receiver_email = user.email
        message = MIMEMultipart("related")
        message["Subject"] = "CID image test"
        message["From"] = sender_email
        message["To"] = receiver_email

        with open(os.path.join(module_dir, 'mailing/welcome.html')) as template_html:
            html = template_html.read()

        part = MIMEText(html, "html")
        message.attach(part)

        fp = open(os.path.join(module_dir, "mailing/logo.png"), 'rb')
        image = MIMEImage(fp.read())
        fp.close()

        image.add_header('Content-ID', '<Mailtrapimage>')
        message.attach(image)

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            if os.environ.get('EMAIL_USE_TLS') == 'True':
                server.starttls()
            server.login(login, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string().encode('utf-8')
            )

class UpdateUserSerializer(serializers.ModelSerializer):
    """
        Serializer for update an User model
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'country', 'birth_date', 'password')
        extra_kwargs = {}

        @staticmethod
        def update(instance, validated_data):
            email = validated_data.get('email', '')

            if User.objects.exclude(id=instance.id).filter(email=email):
                raise serializers.ValidationError('User with this email already exists.')

            instance.__dict__.update(**validated_data)
            instance.save()

            return instance


