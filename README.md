# Sagemaker Studio AutoShutdownのセットアップ方法

## 前提

次のバージョンで動作確認をしています。

- sagemaker_studio_autoshutdown
  - 0.1.5
- JupyterLab
  - 3.3.4

## 参考資料

- [自動シャットダウン拡張機能を利用した Amazon SageMaker Studio のコスト削減方法](https://aws.amazon.com/jp/blogs/news/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/)
  - AWS公式の資料
- [Sagemaker-Studio-Autoshutdown-Extension](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension)
  - 導入する拡張機能のGitHub リポジトリ
- [JupyterLab extensions](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html)
  - JupyterLab 公式

## Sagemkaer Studio を起動

## ターミナルを起動

`File -> New -> Terminal` からターミナルを起動します。

## conda を起動

以下のコマンドをコピペして実行します。

```bash
conda activate studio
```

## JupyterLabのバージョンを確認

以下のコマンドをコピペして実行します。

```bash
jupyter lab --version
```

バージョンが`3.3.4`であることを確認します。

## GitHub からリポジトリを取得

```bash
git clone https://github.com/ymd65536/sagemaker-auto-shutdown.git
```

カレントディレクトリを変更します。

```bash
cd sagemaker-auto-shutdown
```

## auto-shutdownのextensionをセットアップ - シェルスクリプトを実行

以下のコマンドをコピペして実行します。

```bash
cp ./on-jupyter-server-start.sh ../
cp ./check_idle_timeout_configuration.py ../
cd ..
chmod 557 ./on-jupyter-server-start.sh
./on-jupyter-server-start.sh
```

実行が終わると現在利用しているターミナルが閉じます。

## ターミナルを新しく起動する

`File -> New -> Terminal` からターミナルを起動します。

## タイムアウト時間を設定 - シェルスクリプトを実行

以下のコマンドをコピペして実行します。

```bash
conda activate studio
./.auto-shutdown/set-time-interval.sh
```

実行すると次のように実行結果が表示されます。

```bash
sagemaker-user@studio$ conda activate studio
(studio) sagemaker-user@studio$ ./.auto-shutdown/set-time-interval.sh
Succeeded, idle timeout set to 180 minutes
(studio) sagemaker-user@studio$
```

なお、デフォルトのタイムアウト時間は180分に設定していますが、この`set-time-interval.sh`を修正して再度このコマンドを実行することで
タイムアウト時間（秒単位）の再設定が可能です。

`set-time-interval.sh`は`on-jupyter-server-start.sh`によって自動で作成されるファイルです。
一時的にタイムアウト時間を変更する場合は`set-time-interval.sh`の`TIMEOUT`変数を修正するようにしてください。

## 設定されているかどうかの確認

以下のコマンドをコピペして実行します。

```bash
python check_idle_timeout_configuration.py
```

実行すると次のように実行結果が表示されます。

```bash
(studio) sagemaker-user@studio$ python check_idle_timeout_configuration.py
<Response [200]>
{‘idle_time’: 10800, ‘keep_terminals’: False, ‘count’: 10}
(studio) sagemaker-user@studio$
```

これで設定は以上になります。

## 切り戻し手順

ここから先はうまくいかなかった時のリセット手順です。

### カレントディレクトリの確認

以下のコマンドをコピペして実行します。

```bash
pwd
```

実行すると次のように実行結果が表示されます。

```bash
(studio) sagemaker-user@studio$ pwd
/home/sagemaker-user
(studio) sagemaker-user@studio$
```

カレントディレクトリが`/home/sagemaker-user`であることを確認します。

### ディレクトリの削除

以下のコマンドをコピペして実行します。

```bash
rm -rf .auto-shutdown
rm -rf check_idle_timeout_configuration.py
rm -rf on-jupyter-server-start.sh
```

これでインストール前の状態に戻りました。
