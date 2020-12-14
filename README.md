# お部屋探しサイト
## URL

AWS EC2

http://taowata.work/

## 機能一覧

- ユーザー登録、ログイン
- ゲストログイン
- 絞り込み検索機能
- 不動産へのいいね機能(Ajax)
- いいね数を動的に表示する機能(Ajax)
- レスポンシブデザイン

## スクリーンショット

ログイン画面

<img width="600" alt="スクリーンショット 2020-12-14 0 44 17" src="https://user-images.githubusercontent.com/57245344/102016712-91350000-3da5-11eb-893f-3773d594dd16.png">

絞り込み検索&一覧表示画面

<img width="600" alt="スクリーンショット 2020-12-14 0 43 34" src="https://user-images.githubusercontent.com/57245344/102016707-8e3a0f80-3da5-11eb-9f59-47b7467a6bb4.png">

お部屋詳細表示画面

<img width="600" alt="スクリーンショット 2020-12-14 0 43 45" src="https://user-images.githubusercontent.com/57245344/102016709-9003d300-3da5-11eb-9672-859aefac5c96.png">

マイページ

いいねした物件がリスト表示される

<img width="600" alt="スクリーンショット 2020-12-14 0 43 19" src="https://user-images.githubusercontent.com/57245344/102016704-89755b80-3da5-11eb-8c74-27316ad1adf3.png">

ログアウト

<img width="600" alt="スクリーンショット 2020-12-14 0 44 07" src="https://user-images.githubusercontent.com/57245344/102016711-909c6980-3da5-11eb-9abf-ae0e0f2f13bd.png">


## ER図

<img width="756" alt="スクリーンショット 2020-12-14 1 18 42" src="https://user-images.githubusercontent.com/57245344/102017466-72853800-3daa-11eb-849e-ff3718344d18.png">


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
