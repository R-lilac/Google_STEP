【問】キャッシュの管理をほぼO(1)で実現できるデータ構造を考える
目標：もっとも直近にアクセスされた上位X個の<URL, Web ページ>の組が保存できるデータ構造を作ればよい

【答】
ハッシュテーブルと連結リストを組み合わせることで実現できると考える。方法は考え中

【考えたこと・調べたこと】
<URL, Web ページ>の組を保存したい。（X個と決まっている）
if <URL, Web ページ>の組が入力されたとき、その組がすでに保存されている。
(Yes)-> キャッシュ内で順序の入れ替えを行う。入力されたURLを一番最新のものにする。
(No)-> 一番前にアクセスされたものを消し、新たに保存。

ハッシュテーブル
Key: URL　Value: Webページ
検索、追加、削除がほぼO(1)の時間計算量で行われる。
保存順序が維持されない。

アクセス順を保存する必要性がある。
線形のデータ構造と組み合わせる？

線形データ構造　
配列、リスト、スタック、キューなど

* 配列
  メモリ上に連続して配置された、同じ種類のデータの集合
  インデックスを指定することで中間の要素でもO(1)でアクセスできる。
  一つずらす操作が必要なため、追加や削除に時間がかかる。
* リスト（連結リスト）
  非連続なデータの集合
  ポインタをたどることで次の要素へアクセスする。
  ポインタをたどる必要があるため中間のデータにすぐにアクセスすることはできない。
  ポインタを更新することで、追加や削除をO(1)で行うことができる。
* スタック
  最後に入れたデータを最初に取り出すデータ構造（Last-In-First-Out）
  中間のデータにはアクセスできない。
* キュー
  最初に入れたデータを最初に取り出すデータ構造（First-In-First-Out）
  中間のデータにはアクセスできない。

参考
「[データ構造入門：基本概念と主要なデータ構造を理解しよう](https://zenn.dev/brainyblog/articles/data-structures-beginners-guide)」
「[配列と連結リストの線形探索における計算速度とキャッシュメモリの重要性](https://tech.connehito.com/entry/2023/10/16/115909#%E5%9B%BA%E5%AE%9A%E9%95%B7)」

連結リストを使い、ポインタのつなぎ方を更新することでアクセス順を保存する。O(1)で可能。

どのように組み合わせるのか。ハッシュテーブルも連結リストも非連続。
Hash値をつなぐ？