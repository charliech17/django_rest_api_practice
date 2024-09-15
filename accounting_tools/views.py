import json
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounting_tools.models import Event, Webhook

# Create your views here.
@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        # 解析 JSON 數據
        data = json.loads(request.body)
        
        # 創建 Webhook 對象，存儲 destination
        webhook = Webhook.objects.create(destination=data['destination'])
        
        # 迭代 events 並存儲 timestamp 和 replyToken
        for event_data in data.get('events', []):
            # 初始化提取的數字為 None
            extracted_number = None
            
            # 檢查事件類型是否是 message 並且類型為 text
            if event_data['type'] == 'message' and event_data['message']['type'] == 'text':
                text = event_data['message']['text']
                
                # 使用正則表達式提取數字 "[操作] 數字" 的形式
                match = re.search(r'\D*(\d+)', text)
                if match:
                    extracted_number = int(match.group(1))
            
            # 創建 Event 對象並保存提取出的數字
            event = Event.objects.create(
                timestamp=event_data['timestamp'],
                reply_token=event_data.get('replyToken', ''),
                extracted_number=extracted_number
            )
            # 將事件關聯到 Webhook
            webhook.events.add(event)
        
        # 保存 Webhook 和關聯的事件
        webhook.save()
        
        print('webhook', webhook)
        # 返回成功響應
        return JsonResponse({"status": "success"}, status=200)
    
    return JsonResponse({"error": "Invalid request"}, status=200)
