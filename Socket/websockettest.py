from websocket import create_connection
import json

# Copy the web brower header and input as a dictionary
headers = json.dumps({
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'Upgrade',
    'Host': 'echo.websocket.org',
    'Origin': 'file:///C:/Users/amdil/OneDrive/Documents/websocket.html',
    'Pragma': 'no-cache',
    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    'Sec-WebSocket-Key': 'O85SI7PPylVd4L8ka6xHpQ==',
    'Sec-WebSocket-Version': '13',
    'Upgrade': 'websocket',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
})

# Launch the connection to the server.
ws = create_connection('wss://echo.websocket.org/',headers=headers)

# Perform the handshake.
ws.send(json.dumps(" WebSocket rocks"))

# Printing all the result
while True:
    try:
        result = ws.recv()
        print(result)
    except Exception as e:
        print(e)
        break