from django.contrib.auth import get_user_model
from django.db import models


USER = get_user_model()


class ChatSession(models.Model):
    """
    Represents an arbitrary chat session, which is a container of a conversation
    between a user and an AI agent on a particular starter topic

    attributes:
        name(str): Name of the session based on starter topic
        user(djangoUser): User who created the session
        created_at(datetime): Time that session is created
    """
    name = models.CharField(max_length=128)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """
    Represents an arbitrary message, which is a container of an atomic part of a
    turn of a conversation between a user and an AI agent on a particular starter topic

    attributes:
        session(ChatSession): ChatSession that the message belongs to
        content(str): Message content
        agent(str): Name of the AI agent that wrote the message. If none, it indicates message is created by user
                    who created the session
        timestamp(datetime): Time that message is created
    """
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    agent = models.CharField(max_length=128, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

