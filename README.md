# Magick-Nekomimi-Counter

[KENT-WEB](https://www.kent-web.com/)で配布されている[Magick Counter](https://www.kent-web.com/count/mgcount.html)のフォークです。\
本家のものは改行コードを変更しないと動かせませんが、こちらはあらかじめパーミッションを変えるだけで使えるようにしています。

その他変更点は以下の変更点を参照ください。

## 変更点

### 文字コードの変更

| 項目         | 変更前               | 変更後             |
| ------------ | -------------------- | ------------------ |
| 文字コード   | Shift-JIS            | UTF8               |
| 改行コード   | CRLF                 | LF                 |
| カウンタ画像 | 黒背景白文字デジタル | ねこみみカウンター |

### 過剰カウント防止機能の追加

クローラーを始めたBOTや、海外からのアクセスをカウントしない機能を追加しています。

https://github.com/Lycolia/Magick-Nekomimi-Counter/commit/fceb3cb15c1ca9dfa38a2de0f2adb9c8ae6a4b6d

## ファイルの内容

| ファイル           | 内容                     |
| ------------------ | ------------------------ |
| mpcount.cgi        | カウンタプログラム本体   |
| init.cgi           | 設定ファイル             |
| check.cgi          | 設定チェック用プログラム |
| data/mpcount.dat   | カウント値記録ファイル   |
| gif/0.gif .. 9.gif | カウンタ画像             |

## 設置方法

[公式ページにも書かれています](https://www.kent-web.com/count/mgcount.html)

### サーバーへの配置方法

1. このリポジトリの内容を取得し、`./mgcount`配下の内容をCGIが動作する場所に配置する
2. 必要に応じて、`mgcount.cgi`の一行目にある`#!/usr/local/bin/perl`をPerlのパスにする
3. 必要に応じて、`data/mgcount.dat`の一行目に初期カウント値を設定する
4. 以下の表を基に、各ファイルに適切なパーミッションを設定する（左から順に試していくとよい）

| ファイル         | 一般サーバー | suExec環境、CGIWrap環境 |
| ---------------- | ------------ | ----------------------- |
| data/mpcount.dat | 666 or 606   | 600                     |
| check.cgi        | 755 or 705   | 701 or 700              |
| init.cgi         | 644 or 604   | 601 or 600              |
| mgcount.cgi      | 755 or 705   | 701 or 700              |

### 設定方法

init.cgiで行える設定について

| 設定項目        | 内容                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| $cf{limit_time} | 同一訪問者の重複アクセスを排除する設定です。再訪問までの排除時間を分単位で指定します。この機能を使用しない場合は`0`を指定します |
| $cf{digit}      | 表示するカウンタの最小桁数を指定します。例えば、これを「6」と指定した場合、カウント数が「12」の場合は「000012」と表示されます   |
| $cf{datfile}    | `mgcount.dat`へのパス                                                                                                           |
| $cf{gifdir}     | カウンタ画像へのパス。`./path/to/dir`形式で記述する                                                                             |

### HTML への埋め込み方法

次のように`mgcount.cgi`を参照する形で`img`要素を記述します。

```html
<img src="path/to/mgcount.cgi" alt="">
```

## 動かないとき

以下の事柄を試すことで、動かない原因をある程度掴めます。

- ブラウザから`check.cgi`にアクセスしてエラーがないか
- SSHやターミナルから`check.cgi`を叩いてみてエラーがないか

## カウンタ画像参考

![0](mgcount/gif/0.gif)![1](mgcount/gif/1.gif)![2](mgcount/gif/2.gif)![3](mgcount/gif/3.gif)![4](mgcount/gif/4.gif)![5](mgcount/gif/5.gif)![6](mgcount/gif/6.gif)![7](mgcount/gif/7.gif)![8](mgcount/gif/8.gif)![9](mgcount/gif/9.gif)

## 著作権表示

- CGIプログラムの著作権は[KENT-WEB](https://www.kent-web.com/)様に帰属します。
  - 本リポジトリの内容をフォークなどし、再配布を行う場合、[KENT-WEB 様の再配布規定](https://www.kent-web.com/pubc/saihaifu.html)をご一読ください
- カウンタ画像の著作権は[日下こかげ](https://www.pixiv.net/users/11807)様に帰属します。
