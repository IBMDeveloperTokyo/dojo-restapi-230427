RESTful APIデモ用プログラムです｡
以下関連情報での解説をご参照ください｡
2023/4/27実施 IBM Tech Dojo 「いまからでも遅くない！WebAPI超入門 座学編」 https://ibm-developer.connpass.com/event/278083/

# URL
* JSONレスポンス
http://localhost:8000/api/userInfo/

* 管理サイト
http://127.0.0.1:8000/admin/

* API Document
http://localhost:8000/docs/

# curlコマンドサンプル
* create
curl -X POST -H "Content-Type: application/json" -d '{"user_name": "John Doe", "birth_day": "1990-01-01", "age": 33}' http://localhost:8000/api/userInfo/ -v

* list
curl -X GET http://localhost:8000/api/userInfo/ -v

* read
curl -X GET http://localhost:8000/api/userInfo/3/ -v

* update
curl -X PUT -H "Content-Type: application/json" -d '{"user_name": "Taro Updated", "birth_day": "1990-01-01","age": 1}' http://localhost:8000/api/userInfo/3/ -v

* delete
curl -X DELETE http://localhost:8000/api/userInfo/3/ -v

* 無効なリクエスト
curl -X POST -H "Content-Type: application/json" -d '{"birth_day": "1990-01-01", "age": 33}' http://localhost:8000/api/userInfo/ -v

# コンテナ作成､実行
podman desktop起動
podman build -t myapp .
podman run -p 8000:8000 myapp

# コンテナID確認
podman ps

# コンテナ内でのコマンド実行
podman exec -it <コンテナID>> bash
