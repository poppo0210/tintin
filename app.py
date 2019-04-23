# # インポートするライブラリ
# from flask import Flask, request, abort

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
# )
# import os

# # 軽量なウェブアプリケーションフレームワーク:Flask
# app = Flask(__name__)


# # #環境変数からLINE Access Tokenを設定
# # LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_TOKEN"]
# # #環境変数からLINE Channel Secretを設定
# # LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

# # line_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# # handler = WebhookHandler(LINE_CHANNEL_SECRET)

# line_api = LineBotApi('XXH3eq5CN3s7L0aoZm9ah70fwdg8uLncGNd7PuN9JSzzDMC7XWayg2vXSAZLno8nMlOCG00KmbJqt822AeYowRS1IrkoiV/k9aM1sIVfXTFIssq52IVyWpoKGeM/vrc14RtA6Dp8RGm38yJ0WizCEQdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('93f48b7595a4d0035a99c38ecb2d1a02')

# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'

# # MessageEvent
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
# 	line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text='「' + event.message.text + '」って何？')
#      )

# if __name__ == "__main__":
#     port = int(os.getenv("PORT"))
#     app.run(host="0.0.0.0", port=port)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#環境変数取得


line_bot_api = LineBotApi('XXH3eq5CN3s7L0aoZm9ah70fwdg8uLncGNd7PuN9JSzzDMC7XWayg2vXSAZLno8nMlOCG00KmbJqt822AeYowRS1IrkoiV/k9aM1sIVfXTFIssq52IVyWpoKGeM/vrc14RtA6Dp8RGm38yJ0WizCEQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('93f48b7595a4d0035a99c38ecb2d1a02')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="おはようございます！"))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
