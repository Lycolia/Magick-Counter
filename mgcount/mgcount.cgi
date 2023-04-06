#!/usr/local/bin/perl

#┌─────────────────────────────────
#│ Magick Counter : mgcount.cgi - 2011/05/14
#│ Copyright (c) KentWeb
#│ http://www.kent-web.com/
#└─────────────────────────────────

# モジュール宣言
use strict;
use Image::Magick;

# 設定データ認識
require "./init.cgi";
my %cf = &init;

# 時間取得
my $time = time;

# 二重アクセスチェック
my $flg;
if ($cf{limit_time} > 0) {

	# クッキー取得
	my $cook_time = &get_cookie;

	# 二重アクセスチェック
	if ($cook_time && $cook_time > $time) {
		$flg++;
	}
}

# データ読込
open(DAT,"+< $cf{datfile}");
eval "flock(DAT, 2);";
my $data = <DAT>;

# 重複なしの場合カウントアップ
if (!$flg) {
	seek(DAT, 0, 0);
	print DAT ++$data;
	truncate(DAT, tell(DAT));
}
close(DAT);

# クッキー格納
&set_cookie if (!$flg && $cf{limit_time} > 0);

# 桁数調整
while ( length($data) < $cf{digit} ) {
	$data = '0' . $data;
}

# Magick起動
my $img = Image::Magick -> new;

# 画像読込
foreach ( split(//, $data) ) {
	$img -> Read("$cf{gifdir}/$_.gif");
}

# 画像連結
$img = $img -> Append(stack => 'false');

# 画像表示
print "Content-type: image/gif\n\n";
binmode(STDOUT);
$img -> Write('gif:-');
exit;

#-------------------------------------------------
#  クッキー発行
#-------------------------------------------------
sub set_cookie {
	# 有効時間定義
	my $gtime = $time += $cf{limit_time} * 60;

	# 国際標準時取得
	my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = gmtime($gtime);
	my @mon  = qw|Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec|;
	my @week = qw|Sun Mon Tue Wed Thu Fri Sat|;

	# 有効期限をフォーマット
	my $gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
						$week[$wday], $mday, $mon[$mon], $year + 1900, $hour, $min, $sec);

	# クッキー発行
	print "Set-Cookie: mgcounter=$time; expires=$gmt\n";
}

#-------------------------------------------------
#  クッキー取得
#-------------------------------------------------
sub get_cookie {
	# クッキーを取得
	my $cook = $ENV{HTTP_COOKIE};

	# クッキーデータ抽出
	my $cook_data;
	foreach ( split(/;/, $cook) ) {
		my ($key, $val) = split(/=/);
		$key =~ s/\s//g;

		if ($key eq 'mgcounter') {
			$cook_data = $val;
			last;
		}
	}
	return $cook_data;
}

