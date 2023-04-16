# ベースイメージの指定
FROM python:3.9

# コンテナ内での作業ディレクトリの指定
WORKDIR /code

# 必要なファイルをコピー
COPY requirements.txt /code/
COPY . /code/

# pipコマンドを実行してパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナのポートを開放
EXPOSE 8000

# コンテナ起動時に実行するコマンドの指定
CMD ["python", "/code/api_test/manage.py", "runserver", "0.0.0.0:8000"]