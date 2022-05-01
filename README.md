# flask_test_api
- sicom テスト用のAPIです
## HTMLファイルのテストコードを参照して下さい
- https://github.com/takayanagishinnosuke/flask_test_api/blob/main/test.html
## ガイド
- 通信方法 ajax
-  右記のURLを叩いて下さい　"https://shicortytestapi.herokuapp.com/"
- data型: json
- type: POST
- 画像ファイルは base64 split(",")でエンコード
- 正しくPOSTされた際のレスポンスはjsonで返します
- テスト用なので画像に人の顔が写っているか否かで返します

## レスポンス
- 人の顔を検知したら ({"result": 'Danger'})
- 何も検知しなければ ({"result": 'NoProblem'})
## イメージ
https://github.com/takayanagishinnosuke/flask_test_api/issues/1#issue-1222261246
