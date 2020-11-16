# apartment_hunting

# 前提事項
- Macでの開発を前提としています。
- Docker Desktop for Macをインストールしておいてください。

# 環境構築手順
### リポジトリのクローン
- このリポジトリをforkする。
- forkしたリポジトリをローカルにcloneする。
### Djangoプロジェクト用Dockerイメージの作成

clone したディレクトリに移動して、その直下にある Dockerfile から Docker イメージを作成します。
```command
$ cd apartment_hunting/
$ docker build -t apartment_hunting .
```
### Dockerコンテナの実行
作成したイメージを使ってDockerコンテナを作成、実行し、bashを起動します。
$(pwd)の部分はクローンしたリポジトリのPATHを指定してください。

```command
$ docker run --rm -it -p 8000:8000 -v $(pwd):/root/apartment_hunting apartment_hunting
```

### サーバーの起動
起動したコンテナのbashからDjangoサーバーを立ち上げます。
```command
(container) $ python3 manage.py runserver 0.0.0.0:8000
```

### 動作確認

ブラウザから http://localhost:8000 にアクセスすることで確認できます。

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
