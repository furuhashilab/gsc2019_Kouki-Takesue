# フリーデジタル地図における過疎地域の更新頻度向上とその解決策の提案

### Update history
  
* 今年５月に決めたときの初期構想↓  https://medium.com/furuhashilab/%E3%82%88%E3%82%8A%E8%89%AF%E3%81%84%E5%9C%B0%E5%9B%B3%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AB%E3%81%A7%E3%81%8D%E3%82%8B%E3%81%93%E3%81%A8-ef423d7c88c4?source=friends_link&sk=1c77cd3fa9a4846dbce4be1221c20a5e

* それを受け7月に作ったOSM UPDATE CHECKERの構想案↓  
https://prezi.com/view/M8nHjgqN17z1Ta9sj9te/

* 11月の初頭にSotM Asia 2019で使ったプレゼン資料（スクリプトなし）↓  
https://docs.google.com/presentation/d/1OsO54yhrfZswJOOY3bfYDDKxPPcuIW9K-VhtrGD4Tkg/edit?usp=sharing

### 現在の進捗
  
* SQLにタイムスタンプまで保存することに成功し、期間を検索できるようにした。
![screenshot1](https://github.com/kouki-T/imagebox/blob/master/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202019-11-29%2017.47.26.png)

* Herokuのチュートリアルを勉強しながらローカル・オンラインでの動き方を確認した

  https://still-hamlet-40150.herokuapp.com/
  
  コピペ元→https://qiita.com/Rowing0914/items/de16bc2676705bd94d24
  ありがとうございます。
    
* 一旦無視してpyエンジンをあげてみたらエラーログでプログラムが動くやべーのができた。
  
  https://boiling-mountain-83235.herokuapp.com/
  ![screenshot2](https://github.com/kouki-T/imagebox/blob/master/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202019-12-02%2013.32.23.png)
  
  原因はreturn先がhtmlになってなかったからぽい。Flaskのテンプレートに上手く組み込めないか試験中←イマココ

* とりあえず内容はGitHubwikiでいいかなぁと思案中。<br>
スタートページできたよー。

* とりあえず書き始めたよー
https://docs.google.com/document/d/1IKFoF_jw6Ew8CO1M2sh2xnmQOdk7aPO5GglsygWl1RM/edit?usp=sharing

pg_dump --table sotsurontest4 test > sotsurontest.sql
psql herokudb < sotsurontest.sql
