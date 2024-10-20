### MQTT Helper Class ###
import paho.mqtt.client as mqtt
import json

class GolainClient:
    root_topic = ''
    device_name = ''
    def __init__(self, shadow_type: any):
        # self.Shadow = self._shadowType()
        self.device_name = ''
        self.root_topic = ''
        # load the connection settings from the json file
        try:
            with open('connection_settings.json') as f:
                settings = json.load(f)
                self.client_id = settings['device_name']
                self.root_topic = settings['root_topic']
                self.host = settings['host']
                # convert the port to an integer
                self.port = int(settings['port'])
        except FileNotFoundError:
            print("Connection settings file not found!")
            exit(1)
        root_topic = self.root_topic
        device_name = self.device_name
        self._SHADOW_TOPIC_R = f'{root_topic}{device_name}/device-shadow/r'
        self._SHADOW_TOPIC_W = f'{root_topic}{device_name}/device-shadow/u'
        self._DATA_TOPIC = f'{root_topic}{device_name}/device-data/'
        self._shadowType = shadow_type

    def setShadowCallback(self, callbackFunc):
      self.shadowcallback = callbackFunc

    def registerDataPoints(self,name: str):
      self.dataPointMap[name] = True

    def _publish(self, topic, payload):
        self.client.publish(topic, payload)

    def loop_blocking(self):
        self.client.loop_forever()

    def _on_message(self, client, userdata, message):
        print(f'message received on: {message.topic}')
        if self.shadowcallback:
          self.shadowcallback(message.payload)
        else:
          print('shadow callback not set')


    def _subscribe(self, topic, callback):
        self.client.subscribe(topic)
        self.client.on_message = callback

    def _on_subscribe(self, client, *xargs):
        print(f'subsription successful: {xargs}')

    def updateShadow(self, shadow):
        self._publish(self.root_topic + self.client_id + "/device-shadow/u", shadow.SerializeToString())

    def publishData(self, name: str, data):
        print(f'publishig data to {self.root_topic + self.client_id + "/device-data/" + name}')
        self._publish(self.root_topic + self.client_id + "/device-data/" + name, data)

    def connect(self):
        print(self.host)
        print(self.port)
        # Create a new MQTT client
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.client_id, reconnect_on_failure=True, clean_session=True)
        # lambda function to handle the message
        self.client.on_message = self._on_message
        try:
            self.client.tls_set(ca_certs="root_ca_cert.pem", certfile="device_cert.pem", keyfile="device_private_key.pem")
            self.client.tls_insecure_set(False)
        except FileNotFoundError:
            print("TLS certificates not found!")
            exit(1)
        try:
            self.client.on_subscribe = self._on_subscribe
            self.client.connect(self.host, self.port)
            print(self.port)
            self.client.subscribe(self.root_topic + self.client_id + "/device-shadow/r", 1)
        except Exception as e:
            print(e)
            print("Connection failed!")
            exit(1)