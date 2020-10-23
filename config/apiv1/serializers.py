from rest_framework import serializers

from users.models import User, Post, Comment, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'price', 'car_type']

    def update(self, instance, validated_data): 
        instance.author.username = validated_data.get('author', instance.author.username)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.price = validated_data.get('price', instance.price)
        instance.car_type = validated_data.get('car_type', instance.car_type)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    userpro = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'introduction', 'address', 'userpro', 'icon']
        # extra_kwargs = {
        #     'userpro': {'validators': []},
        # }

    def update(self, instance, validated_data): 
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.address = validated_data.get('address', instance.address)
        instance.userpro.username = validated_data.get('username', instance.userpro.username)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = ('__all__')