from django.db import models

# Create your models here.
# 定義 Event 模型，只保存 timestamp 和 replyToken
class Event(models.Model):
    timestamp = models.BigIntegerField()
    reply_token = models.CharField(max_length=255, null=True, blank=True)
    extracted_number = models.IntegerField(null=True, blank=True)  # 新增一個欄位來存數字

# 定義 Webhook 模型，只保存 destination 和關聯的多個 Event
class Webhook(models.Model):
    destination = models.CharField(max_length=255)
    events = models.ManyToManyField(Event)