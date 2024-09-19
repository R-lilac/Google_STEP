巡回セールスパーソン問題 (TSP) とは、
与えられた座標を持つ地点すべてを一度ずつめぐるとき、移動コストが最小のものを求める最適化問題である。
[巡回セールスマン問題](https://ja.wikipedia.org/wiki/%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC%E3%83%AB%E3%82%B9%E3%83%9E%E3%83%B3%E5%95%8F%E9%A1%8C)

NP困難と呼ばれる問題のクラスに属し、最適解を見つけることは現状難しいためなるべく近い解 (近似解) を探す。

ヒューリスティクスとは、必ずしも正しい答えを導けるとは限らないがある程度のレベルで正解に近い解を得ることができる方法である。
[ヒューリスティクス](https://ja.wikipedia.org/wiki/%E3%83%92%E3%83%A5%E3%83%BC%E3%83%AA%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF)
[メタヒューリスティクス](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%BF%E3%83%92%E3%83%A5%E3%83%BC%E3%83%AA%E3%82%B9%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9) (特定の計算問題に依存しないヒューリスティクス)

探索アルゴリズム / 局所探索法 / 2-opt,3-opt

【課題】TSPを実際に実装する

【方針】　以下の論文を参考に2-optと3-optを組み合わせた実装を行う。

第一段階　greedy+2opt
第二段階　greedy+2-3opt

【結果】

| challenge     | 0       | 1       | 2       | 3       | 4        | 5 | 6 | 7 |
| ------------- | ------- | ------- | ------- | ------- | -------- | - | - | - |
| greedy+2opt   | 3418.10 | 3832.29 | 5232.96 | 9261.01 | 11591.84 |   |   |   |
| greedy+2-3opt | 3291.62 | 3778.72 | 4494.42 | 8473.88 | 11057.08 |   |   |   |

【参考】
[
    巡回セールスマン問題における n-opt 法適用の検討](https://www.cst.nihon-u.ac.jp/research/gakujutu/58/pdf/L-56.pdf)[巡回セールスマン問題をいろんな近似解法で解く
	](https://qiita.com/take314/items/dc2e6cf6d97889923c8b)[Algorithms with Python / 巡回セールスマン問題 [3] - NCT](http://www.nct9.ne.jp/m_hiroi/light/pyalgo64.html)

    2-optに関して[
    　2-opt法によるTSP](https://paiza.jp/works/mondai/tsp_problems/tsp_problems__tsp_2-opt)[
    　2-optの実装](https://qiita.com/hotpepsi/items/424f9491e7baaa63b6ce)[
    　巡回セールスマン問題の近似解法と 2-opt 改善法](https://qiita.com/hotpepsi/items/424f9491e7baaa63b6ce)[
    　2-opt (Wikipedia)](https://ja.wikipedia.org/wiki/2-opt)

   3-optに関して
	[巡回セールスマン問題(TSP)の基本的な解き方(ILS)
	](https://future-architect.github.io/articles/20211201a/#2-3-opt)[tsp3opt](https://github.com/ozanyerli/tsp3opt)
	[3optに関するGitHubリポジトリ
	](https://github.com/topics/3opt)[発見的解放：収集/配送経路問題への適用](https://orsj.org/wp-content/corsj/or54-12/or54_12_721.pdf)
