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


app = Flask(__name__)

#環境変数取得
talk = {
    "おっぱい大きいね":"お客さんもね！",
    "どんな人がタイプ？":"風俗利用しない人ですかねー",
    "俺のこと好き？":"あー、うん（時計見ながら）",
    "ちょっとだけ入れていい？":"今度来てくれたらね(^.^)",
    "相性いいよね":"ほんとだね～",
    "今度食事行こうよ":"ハイ、お店予約時に言って頂ければ",
}

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
def message_text(event):
    if  event.message.text in talk:
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text = talk[event.message.text])
        )



if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
