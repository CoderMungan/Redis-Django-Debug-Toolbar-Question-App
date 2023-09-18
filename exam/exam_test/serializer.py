from .models import Question
from rest_framework.serializers import ModelSerializer


class QuestionsSerializers(ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"