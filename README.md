# Magick-Nekomimi-Counter

[KENT-WEB](https://www.kent-web.com/)で配布されている[Magick Counter](https://www.kent-web.com/count/mgcount.html)のフォークです。\
本家のものは改行コードを変更しないと動かせませんが、こちらはあらかじめパーミッションを変えるだけで使えるようにしています。

その他変更点は以下の変更点を参照ください。

## 変更点

| 項目         | 変更前               | 変更後             |
| ------------ | -------------------- | ------------------ |
| 文字コード   | Shift-JIS            | UTF8               |
| 改行コード   | CRLF                 | LF                 |
| カウンタ画像 | 黒背景白文字デジタル | ねこみみカウンター |

## 設置方法

[詳細は公式ページにも書かれています。](https://www.kent-web.com/count/mgcount.html)

### サーバーへの配置方法

サーバーに配置してパーミッションを変更するだけです。
下図の `[]` はパーミッションを表しています。
必要に応じて `init.cgi` を編集することで設定を変更することができます。
カウント数は `data/mgcount.dat` の一行目に 10 進数整数で記述することで設定できます。

```
mgcount
  ├─data/
  │  └─mgcount.dat [666 or 606 or 600]
  ├─gif/
  ├─check.cgi   [755 or 705 or 701 or 700]
  ├─init.cgi    [644 or 604 or 601 or 600]
  └─mgcount.cgi [755 or 705 or 701 or 700]
```

### HTML への埋め込み方法

次のように `mgcount.cgi` を参照する形で `img` 要素を記述します。

```html
<img src="path/to/mgcount.cgi" alt="" />
```

## カウンタ画像参考

![0](mgcount/gif/0.gif)![1](mgcount/gif/1.gif)![2](mgcount/gif/2.gif)![3](mgcount/gif/3.gif)![4](mgcount/gif/4.gif)![5](mgcount/gif/5.gif)![6](mgcount/gif/6.gif)![7](mgcount/gif/7.gif)![8](mgcount/gif/8.gif)![9](mgcount/gif/9.gif)

## 著作権表示

-   CGI プログラムの著作権は[KENT-WEB](https://www.kent-web.com/)様に帰属します。
    -   本リポジトリの内容をフォークなどし、再配布を行う場合、[KENT-WEB 様の再配布規定](https://www.kent-web.com/pubc/saihaifu.html)をご一読ください
-   カウンタ画像の著作権は[日下こかげ](https://www.pixiv.net/users/11807)様に帰属します。
