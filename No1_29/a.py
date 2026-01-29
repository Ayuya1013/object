import matplotlib
import matplotlib.pyplot as plt

# データ集計
pref_count_dict = {}
with open('visitor_record_test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        date, pref, num_adult, num_children = line.strip().split(',')
        num_all = int(num_adult) + int(num_children)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

# 訪問者数で降順ソート
pref_count_sorted = sorted(pref_count_dict.items(), key=lambda x: x[1], reverse=True)

# ラベルと値の準備
labels = [item[0] for item in pref_count_sorted]
values = [item[1] for item in pref_count_sorted]

# グラフ描画設定
matplotlib.use('Agg')  # GUIなし環境でも保存できるように
plt.rcParams['font.family'] = 'Noto Sans CJK JP'  # 日本語フォント
plt.rcParams['axes.unicode_minus'] = False
plt.xticks(rotation=270)  # ラベルを縦書きに

# 棒グラフ作成
plt.bar(range(len(labels)), values, tick_label=labels)
plt.title('都道府県別訪問者数')
plt.ylabel('人数')
plt.tight_layout()
plt.savefig('graph_test.png')  # グラフ画像として保存
