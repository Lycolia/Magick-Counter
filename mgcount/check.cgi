#!/usr/local/bin/perl

#┌─────────────────────────────────
#│ Magick Counter : check.cgi - 2011/05/14
#│ Copyright (c) KentWeb
#│ http://www.kent-web.com/
#└─────────────────────────────────

# モジュール宣言
use strict;

# 設定データ認識
require "./init.cgi";
my %cf = &init;

print <<EOM;
Content-type: text/html

<html>
<head>
<meta charset="utf-8">
<title>Magick Counter チェックプログラム</title>
</head>
<body>
<h1>Magick Counter チェックプログラム</h1>
バージョン: $cf{version}<br>
EOM

# Image-Magick動作確認
eval { require Image::Magick; };
if ($@) {
	print "Image-Magick動作: NG → $@<br>\n";
} else {
	print "Image-Magick動作: OK<br>\n";
}

# データファイルチェック
if (-f $cf{datfile}) {
	print "データファイル位置: OK<br>\n";

	if (-r $cf{datfile} && -w $cf{datfile}) {
		print "データファイルパーミッション: OK<br>\n";
	} else {
		print "データファイルパーミッション: NG<br>\n";
	}
} else {
	print "データファイル位置: NG<br>\n";
}

# 環境変数チェック
if (defined $ENV{REMOTE_HOST}) {
	print "環境変数「REMOTE_HOST」の取得: OK<br>\n";
} else {
	print "環境変数「REMOTE_HOST」の取得: NG。内部処理でDNS lookupを行います。<br>\n";
}
if (defined $ENV{REMOTE_ADDR}) {
	print "環境変数「REMOTE_ADDR」の取得: OK<br>\n";
} else {
	print "環境変数「REMOTE_ADDR」の取得: NG<br>\n";
}
if (defined $ENV{HTTP_USER_AGENT}) {
	print "環境変数「HTTP_USER_AGENT」の取得: OK<br>\n";
} else {
	print "環境変数「HTTP_USER_AGENT」の取得: NG<br>\n";
}

# 画像ファイルチェック
foreach (0 .. 9) {
	if (-f "$cf{gifdir}/$_.gif") {
		print "$_ 画像の位置: OK<br>\n";
	} else {
		print "$_ 画像の位置: NG<br>\n";
	}
}

print "</body></html>\n";
exit;

