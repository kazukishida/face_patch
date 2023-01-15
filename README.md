# Face Patch
入力した画像から人物の顔を検出し、顔文字に置き換える。

Streamlit Cloudでデプロイしようとしたが、face_recognitionモジュール（というか依存しているdlib）のインストール時にリソース制限?でエラーになるためできなかった。（[参考](https://discuss.streamlit.io/t/error-in-installing-the-face-recognition-facing-errors/30011)）

コマンドラインで実行する場合
--
下記実行後、localhostにアクセスする。

$ streamlit run main.py

