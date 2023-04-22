RESTful APIデモ用プログラムです｡
以下関連情報での解説をご参照ください｡  
2023/4/27実施 IBM Tech Dojo 「いまからでも遅くない！WebAPI超入門 座学編」 https://ibm-developer.connpass.com/event/278083/

# 動作確認環境
* コンテナ：Podman 4.4.4
* 言語：Python 3.9.6
* Webアプリケーションフレームワーク：Django 4.2
* RESTful APIフレームワーク：Django REST framework 3.14.0
* インメモリデータベース：SQLite3
* APIドキュメント生成パッケージ：drf-yasg
* アクセストークンによる認証：djangorestframework-simplejwt

# URL
* JSONレスポンス
http://localhost:8000/api/userInfo/

* 管理サイト
http://127.0.0.1:8000/admin/

* API Document
http://localhost:8000/docs/

# curlコマンドサンプル
* アクセストークンの取得
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=password&username=<USER_NAME>&password=<PASSWORD>" http://localhost:8000/api/token/

* list  
curl -X GET http://localhost:8000/api/userInfo/ -H "Authorization: Bearer <ACCESS_TOKEN>"

* create  
curl -X POST http://localhost:8000/api/userInfo/ \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{"user_name": "John Doe", "member_since": "1990-01-01", "membership_years": 33}'

* update  
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"user_name": "Taro Updated", "member_since": "1990-01-01","membership_years": 1}' http://localhost:8000/api/userInfo/3/

* delete  
curl -X DELETE -H "Authorization: Bearer <ACCESS_TOKEN>" http://localhost:8000/api/userInfo/3/

* 無効なリクエスト(認証エラー->401)
curl -X GET http://localhost:8000/api/userInfo/ -H "Authorization: Bearer xxx"

* 無効なリクエスト(必須項目のuser_nameが存在しない->400)
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"member_since": "1990-01-01", "membership_years": 33}' http://localhost:8000/api/userInfo/

* read  
curl -X GET http://localhost:8000/api/userInfo/3/ -H "Authorization: Bearer <ACCESS_TOKEN>"

# コンテナ作成､実行
* podman desktop起動
* podman build -t myapp .
* podman run -p 8000:8000 myapp

# コンテナIDの確認
* podman ps

# コンテナ内でのコマンド実行
* podman exec -it <コンテナID> bash
