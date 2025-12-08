from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        user_msg = data.get("message", "")

        # MOCK RESPONSE (since model cannot run on vercel)
        bot_reply = f"You said: {user_msg}. I'm here for you."

        response = {
            "reply": bot_reply
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))
