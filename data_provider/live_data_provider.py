from data_provider.base_data_provider import BaseDataProvider

class LiveDataProvider(BaseDataProvider):
    def __init__(self, broker_instance):
        super().__init__(live_trading=True)

    def start_data_feed(self):
        """Simulate listening to a live data stream and trigger events"""
        while True:
            new_data = self.data_stream.get_next_tick()
            self.on_new_data(new_data)