# お部屋探しサイト
## URL
http://taowata.work/

## 機能一覧

- ユーザー登録、ログイン
- ゲストログイン
- 絞り込み検索機能
- 不動産へのいいね機能(Ajax)
- いいね数を動的に表示する機能(Ajax)
- レスポンシブデザイン

## スクリーンショット

## ER図


# 開発環境構築手順
### 前提事項
- Dockerがインストール済みであること。
### リポジトリのクローン
- このリポジトリをforkする。
- forkしたリポジトリをローカルにcloneする。

### local_settings.pyを作成(すでに作成済みの場合は不要)
クローンしたディレクトリに移動し、SECRET_KEYを生成するスクリプトを実行する。これによりSECRET_KEYが書き込まれたlocal_settings.pyが作成される。
```
$ docker-compose run web python3 generate_secretkey.py
```

### コンテナを起動する
クローンしたディレクトリに移動し、以下を実行する。
```
$ docker-compose up -d
```
### マイグレーション
まず、コンテナ内に入る。
```
$ docker-compose exec web bash
```

マイグレーションファイルを作成し、マイグレーションを実行。
```
(container) $ python3 manage.py makemigrations
(container) $ python3 manage.py migrate
```

### サーバー起動&動作確認
```
(container) $ python3 manage.py runserver 0.0.0.0:8000
```

ブラウザから http://localhost:8000 にアクセスすることで確認できる。

## DBへアクセスする
`docker-compose up`の後で、以下を実行してDBコンテナに入る。
```
$ docker-compose exec db bash
```
コンテナ内で以下を実行し、PostgreSQLへの接続する。
```
(container) $ psql -U postgres
```
次のコマンドでテーブルを確認できる。
```
postgres=# \dt
```
