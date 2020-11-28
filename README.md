# apartment_hunting

# 前提事項
- Dockerがインストール済みであること。

# 環境構築手順
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

### 動作確認

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

# GitFlowの予備知識

- master
  - プロダクトとしてリリースするためのブランチ。リリースしたらタグ付けする。
- develop
  - 開発ブランチ。コードが安定し、リリース準備ができたら master へマージする。リリース前はこのブランチが最新バージョンとなる。
- feature
  - 機能の追加。 develop から分岐し、 develop にマージする。
- release
  - プロダクトリリースの準備。develop ブランチにリリース予定の機能やバグフィックスがほぼ反映した状態で develop から分岐する。 リリース準備が整ったら, master にマージし、タグをつける。次に develop にマージする。
- hotfix
  - リリース後のクリティカルなバグフィックスなど、 現在のプロダクトのバージョンに対する変更用。 master から分岐し、 master にマージし、タグをつける。次に develop にマージする。

<img src="https://user-images.githubusercontent.com/46508203/77295789-e4ec4e80-6d29-11ea-8608-1f24618d6b0f.png" width="500px">

- [git初心者への道 - お仕事で困らないレベルまでググっとします。 · GitHub](https://gist.github.com/yatemmma/6486028)
- [ Branchについて](https://havelog.ayumusato.com/develop/git/e513-git_branch_model.html)
