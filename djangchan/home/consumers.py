from channels.generic.websocket import WebsocketConsumer

class TestConsumer(WebsocketConsumer):
    

    def connect(self):
        self.room_name='test_consumer'
        self.room_group_name='test_consumer_group'
        
        return super().connect()
    def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data, bytes_data)
    def disconnect(self, code):
        return super().disconnect(code)