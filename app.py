import io
import os
import threading
import time
import tkinter as tk
from gtts import gTTS
import pygame

# 初始化音訊模組
pygame.mixer.init()


class ModeSelector:
    """ 啟動時的主類別選擇視窗 """
    def __init__(self, root):
        self.root = root
        self.root.title("日文綜合學習大師 - 選擇單字類別")
        self.root.geometry("580x880")
        
        # 採用牛皮紙色系風格
        self.bg_color = "#D8C3A5"
        self.root.configure(bg=self.bg_color)

        # 標題
        lbl_title = tk.Label(
            self.root,
            text="日文單字學習",
            font=("Arial", 22, "bold"),
            fg="#4A403A",
            bg=self.bg_color
        )
        lbl_title.pack(pady=(20, 5))

        lbl_subtitle = tk.Label(
            self.root,
            text="請選擇您想學習的類別",
            font=("Arial", 14),
            fg="#6B5B52",
            bg=self.bg_color
        )
        lbl_subtitle.pack(pady=(0, 10))

        # 朗讀間隔時間設定區塊（預設 4 秒）
        frame_setting = tk.Frame(self.root, bg=self.bg_color)
        frame_setting.pack(pady=(0, 15))

        lbl_setting = tk.Label(
            frame_setting,
            text="連續朗讀單字間隔：",
            font=("Arial", 13, "bold"),
            fg="#4A403A",
            bg=self.bg_color
        )
        lbl_setting.pack(side=tk.LEFT)

        self.entry_pause = tk.Entry(
            frame_setting,
            font=("Arial", 13, "bold"),
            width=5,
            justify="center"
        )
        self.entry_pause.insert(0, "4")
        self.entry_pause.pack(side=tk.LEFT, padx=3)

        lbl_unit = tk.Label(
            frame_setting,
            text="秒",
            font=("Arial", 13, "bold"),
            fg="#4A403A",
            bg=self.bg_color
        )
        lbl_unit.pack(side=tk.LEFT)

        # 食物與水果按鈕
        btn_food = tk.Button(
            self.root,
            text="食物與水果單字(共50個)",
            font=("Arial", 16, "bold"),
            bg="#D9534F",
            fg="white",
            activebackground="#C9302C",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("food")
        )
        btn_food.pack(pady=3)

        # 動物及魚類按鈕
        btn_animal = tk.Button(
            self.root,
            text="動物與魚類單字(共50個)",
            font=("Arial", 16, "bold"),
            bg="#4682B4",
            fg="white",
            activebackground="#36648B",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("animal")
        )
        btn_animal.pack(pady=3)

        # 生活日常用品按鈕
        btn_daily = tk.Button(
            self.root,
            text="生活日常用品(共50個)",
            font=("Arial", 16, "bold"),
            bg="#556B2F",
            fg="white",
            activebackground="#455624",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("daily")
        )
        btn_daily.pack(pady=3)

        # 自然天氣按鈕
        btn_nature = tk.Button(
            self.root,
            text="自然天氣單字(共35個)",
            font=("Arial", 16, "bold"),
            bg="#CD853F",
            fg="white",
            activebackground="#B87333",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("nature")
        )
        btn_nature.pack(pady=3)

        # 學校學科按鈕
        btn_subject = tk.Button(
            self.root,
            text="學校學科單字(共25個)",
            font=("Arial", 16, "bold"),
            bg="#6A5ACD",
            fg="white",
            activebackground="#5848B8",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("subject")
        )
        btn_subject.pack(pady=3)

        # 家族稱謂按鈕
        btn_family = tk.Button(
            self.root,
            text="家族稱謂單字(共40個)",
            font=("Arial", 16, "bold"),
            bg="#8B5A2B",
            fg="white",
            activebackground="#7A4F24",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("family")
        )
        btn_family.pack(pady=3)

        # 心情情緒按鈕
        btn_emotion = tk.Button(
            self.root,
            text="心情情緒單字(共30個)",
            font=("Arial", 16, "bold"),
            bg="#C06C84",
            fg="white",
            activebackground="#A3586D",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("emotion")
        )
        btn_emotion.pack(pady=3)

        # 方向與位置按鈕
        btn_direction = tk.Button(
            self.root,
            text="方向與位置單字(共30個)",
            font=("Arial", 16, "bold"),
            bg="#4A6B82",
            fg="white",
            activebackground="#395A71",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=lambda: self.start_app("direction")
        )
        btn_direction.pack(pady=3)

        # 結束程式按鈕
        btn_exit = tk.Button(
            self.root,
            text="結束程式",
            font=("Arial", 14),
            bg="#B85B56",
            fg="white",
            activebackground="#A04A45",
            activeforeground="white",
            relief=tk.FLAT,
            width=26,
            pady=6,
            command=self.close_app
        )
        btn_exit.pack(pady=(12, 10))

    def start_app(self, mode):
        try:
            pause_sec = float(self.entry_pause.get())
            if pause_sec < 0:
                pause_sec = 4.0
        except ValueError:
            pause_sec = 4.0

        self.root.destroy()
        main_root = tk.Tk()
        JapaneseMasterApp(main_root, initial_mode=mode, pause_seconds=pause_sec)
        main_root.mainloop()

    def close_app(self):
        self.root.destroy()


class JapaneseMasterApp:

    def __init__(self, root, initial_mode="food", pause_seconds=4.0):
        self.root = root
        self.current_mode = initial_mode
        self.pause_seconds = pause_seconds
        
        mode_titles = {
            "food": "食物與水果",
            "animal": "動物及魚類",
            "daily": "生活日常用品",
            "nature": "自然天氣",
            "subject": "學校學科",
            "family": "家族稱謂",
            "emotion": "心情情緒",
            "direction": "方向與位置"
        }
        mode_title_str = mode_titles.get(self.current_mode, "方向與位置")

        self.root.title(f"日文綜合學習大師 ({mode_title_str})")
        self.root.geometry("820x780")

        # 配色定義（牛皮紙色背景 + 莫蘭迪色系按鈕與文字）
        self.bg_color = "#D8C3A5"
        self.top_bg = "#C3B091"
        self.card_bg = "#E8D8C8"
        self.text_color = "#4A403A"
        self.kana_color = "#4A90E2"  # 假名句淺藍色
        self.btn_bg = "#8E9A86"
        self.btn_fg = "#FFFFFF"
        self.btn_active = "#7A8672"
        self.audio_btn_bg = "#9A8C98"
        self.audio_btn_active = "#837581"
        self.loop_btn_bg = "#708090"
        self.loop_btn_active = "#5A6875"
        self.particle_color = "#D9534F"  # 助詞淺紅色

        self.root.configure(bg=self.bg_color)

        # 初始化所有資料庫
        self.init_food_data()
        self.init_animal_data()
        self.init_daily_data()
        self.init_nature_data()
        self.init_subject_data()
        self.init_family_data()
        self.init_emotion_data()
        self.init_direction_data()

        self.current_index = 0
        self.is_looping = False

        self.setup_ui()
        self.load_word()

    def init_food_data(self):
        self.food_data = [
            {"word": "ごはん", "kanji": "ご飯", "meaning": "白飯 / 餐點", "ex1_kanji": "3時間ごとにお腹が空いて ご飯を食べます。", "ex1_kana": "さんじかんごとにおなかがすいてごはんをたべます", "ex1_cn": "每隔三小時肚子就會餓，然後吃飯。", "ex2_kanji": "温かいご飯を食べます。", "ex2_kana": "あたたかいごはんをたべます", "ex2_cn": "吃熱騰騰的白飯。"},
            {"word": "パン", "kanji": "パン", "meaning": "麵包", "ex1_kanji": "朝ごはんに バターをぬった パンを食べます。", "ex1_kana": "あさごはんにばたーをぬったぱんをたべます", "ex1_cn": "早餐吃抹了奶油的麵包。", "ex2_kanji": "美味しいパンを買います。", "ex2_kana": "おいしいぱんをかいます", "ex2_cn": "買好吃的麵包。"},
            {"word": "にく", "kanji": "肉", "meaning": "肉", "ex1_kanji": "焼き肉の 匂いが 食欲を そそります。", "ex1_kana": "やきにくのにおいがしょくよくをそそります", "ex1_cn": "烤肉的香味勾起人的食欲。", "ex2_kanji": "肉を料理します。", "ex2_kana": "にくをりょうりします", "ex2_cn": "料理肉品。"},
            {"word": "たまご", "kanji": "卵", "meaning": "雞蛋", "ex1_kanji": "朝ごはんに 目玉焼き用の 卵を 割ります。", "ex1_kana": "あさごはんにめだまやきようのたまごをわれます", "ex1_cn": "早餐把做荷包蛋用的雞蛋打開。", "ex2_kanji": "新鮮な卵を買います。", "ex2_kana": "しんせんなたまごをかいます", "ex2_cn": "買新鮮的雞蛋。"},
            {"word": "やさい", "kanji": "野菜", "meaning": "蔬菜", "ex1_kanji": "健康のため、毎日 新鮮な 野菜を 食べます。", "ex1_kana": "けんこうのためまいにちしんせんなやさいをたべます", "ex1_cn": "為了健康，每天都吃新鮮蔬菜。", "ex2_kanji": "野菜をたくさん食べます。", "ex2_kana": "やさいをたくさんたべます", "ex2_cn": "吃很多蔬菜。"},
            {"word": "とうふ", "kanji": "豆腐", "meaning": "豆腐", "ex1_kanji": "冷やし 豆腐に 生姜と 醤油を かけます。", "ex1_kana": "ひやしとうふにしょうがとしょうゆをかけます", "ex1_cn": "在冰豆腐上淋上薑末與醬油。", "ex2_kanji": "豆腐の味噌汁を作ります。", "ex2_kana": "とうふのみそしるをつくります", "ex2_cn": "做豆腐味噌湯。"},
            {"word": "なっとう", "kanji": "納豆", "meaning": "納豆", "ex1_kanji": "納豆を よくかきまぜて ごはんの上に出します。", "ex1_kana": "なっとうをよくかきまぜてごはんのうえにだします", "ex1_cn": "把納豆充分攪拌後端上白飯。", "ex2_kanji": "健康のために納豆を食べます。", "ex2_kana": "けんこうのためになっとうをたべます", "ex2_cn": "為了健康而吃納豆。"},
            {"word": "みそしる", "kanji": "味噌汁", "meaning": "味噌湯", "ex1_kanji": "熱い 味味噌汁を 飲むと ほっとします。", "ex1_kana": "あついみそしるをのむとほっとします", "ex1_cn": "喝熱熱的味噌湯會讓人感到放鬆。", "ex2_kanji": "朝は必ず味噌汁を飲みます。", "ex2_kana": "あさはかならずみそしるをのみます", "ex2_cn": "早上一定喝味噌湯。"},
            {"word": "すし", "kanji": "寿司", "meaning": "壽司", "ex1_kanji": "回る 寿司屋で 好きな 皿を 取ります。", "ex1_kana": "まわるすしやですきなさらをとります", "ex1_cn": "在迴轉壽司店拿取喜歡的盤子。", "ex2_kanji": "美味しい寿司を食べます。", "ex2_kana": "おいしいすしをたべます", "ex2_cn": "吃美味的壽司。"},
            {"word": "さしみ", "kanji": "刺身", "meaning": "生魚片", "ex1_kanji": "鮮度の 高い 刺身を わさびと 一緒に 食べます。", "ex1_kana": "せんどのたかいさしみをわさびといっしょにたべます", "ex1_cn": "將新鮮度高的生魚片搭配芥末一起吃。", "ex2_kanji": "新鮮な刺身が好きです。", "ex2_kana": "しんせんなさしみがすきです", "ex2_cn": "喜歡新鮮的生魚片。"},
            {"word": "てんぷら", "kanji": "天婦羅", "meaning": "天婦羅", "ex1_kanji": "サクサクの 天ぷら粉で 揚げた 海老が 美味しいです。", "ex1_kana": "さくさくのてんぷらこであげたえびがおいしいです", "ex1_cn": "用酥脆天婦羅粉炸的蝦子很好吃。", "ex2_kanji": "野菜の天婦羅を食べます。", "ex2_kana": "やさいのてんぷらをたべます", "ex2_cn": "吃蔬菜天婦羅。"},
            {"word": "うどん", "kanji": "烏龍麵", "meaning": "烏龍麵", "ex1_kanji": "出汁の 利いた 温かい うどんを 食べます。", "ex1_kana": "だしのきいたあたたかいうどんをたべます", "ex1_cn": "吃一碗充滿高湯香味的熱烏龍麵。", "ex2_kanji": "手打ちうどんを作ります。", "ex2_kana": "てうちうどんをつくります", "ex2_cn": "做手打烏龍麵。"},
            {"word": "ラーメン", "kanji": "拉麵", "meaning": "拉麵", "ex1_kanji": "豚骨スープの 濃厚な ラーメンを 注文します。", "ex1_kana": "とんこつすｰぷののうこうならｰめんをちゅうもんします", "ex1_cn": "點一碗豚骨湯頭濃郁的拉麵。", "ex2_kanji": "熱いラーメンを食べます。", "ex2_kana": "あついらｰめんをたべます", "ex2_cn": "吃熱拉麵。"},
            {"word": "カレーライス", "kanji": "咖哩飯", "meaning": "咖哩飯", "ex1_kanji": "特製の スパイスが 効いた カレーライスを 作ります。", "ex1_kana": "とくせいのすぱいすがきいたかれｰらいすをつくります", "ex1_cn": "做一份充滿特製香料味的咖哩飯。", "ex2_kanji": "辛いカレーライスが好きです。", "ex2_kana": "からいかれｰらいすがすきです", "ex2_cn": "喜歡辣咖哩飯。"},
            {"word": "ぎゅうどん", "kanji": "牛丼", "meaning": "牛丼", "ex1_kanji": "お腹が 空いた時、早くて 安い 牛丼を 食べます。", "ex1_kana": "おなかがすいたときはやくてやすいぎゅうどんをたべます", "ex1_cn": "肚子餓時，吃份又快又便宜的牛丼。", "ex2_kanji": "美味しい牛丼を食べます。", "ex2_kana": "おいしいぎゅうどんをたべます", "ex2_cn": "吃好吃的牛丼。"},
            {"word": "ぎょうざ", "kanji": "餃子", "meaning": "餃子 / 煎餃", "ex1_kanji": "パリッとした 焼き餃子を タレに つけて 食べます。", "ex1_kana": "ぱりっとしたやきぎょうざをたれにつけてたべます", "ex1_cn": "把煎得酥脆的煎餃沾醬汁吃。", "ex2_kanji": "熱い餃子を食べます。", "ex2_kana": "あついぎょうざをたべます", "ex2_cn": "吃熱餃子。"},
            {"word": "おべんとう", "kanji": "便當", "meaning": "便當", "ex1_kanji": "母が 愛情を 込めて 作ってくれた お弁当を 開けます。", "ex1_kana": "ははがあいじょうをこめてつくってくれたおべんとうをあけます", "ex1_cn": "打開母親充滿愛意所製作的便當。", "ex2_kanji": "美味しいお弁当を食べます。", "ex2_kana": "おいしいおべんとうをたべます", "ex2_cn": "吃美味的便當。"},
            {"word": "おにぎり", "kanji": "飯糰", "meaning": "飯糰", "ex1_kanji": "海苔を 巻いた 梅味の おにぎりを 握ります。", "ex1_kana": "のりをまいたうめあじのおにぎりをにぎります", "ex1_cn": "捏一個包著海苔的梅子口味飯糰。", "ex2_kanji": "おにぎりを作ります。", "ex2_kana": "おにぎりをつくります", "ex2_cn": "做飯糰。"},
            {"word": "サラダ", "kanji": "沙拉", "meaning": "沙拉", "ex1_kanji": "ドレッシングを かけた 生菜サラダを 食べます。", "ex1_kana": "どれっしんぐをかけたせいさいさらだをたべます", "ex1_cn": "吃淋上沙拉醬的生菜沙拉。", "ex2_kanji": "新鮮なサラダを食べます。", "ex2_kana": "しんせんなさらだをたべます", "ex2_cn": "吃新鮮的沙拉。"},
            {"word": "サンドイッチ", "kanji": "三明治", "meaning": "三明治", "ex1_kanji": "ハムと チーズを 挟んだ サンドイッチを 頬張ります。", "ex1_kana": "はむとちｰずをはさんださんどいっちをほうばります", "ex1_cn": "大口咬下夾著火腿與起司的三明治。", "ex2_kanji": "朝食にサンドイッチを食べます。", "ex2_kana": "ちょうしょくにさんどいっちをたべます", "ex2_cn": "早餐吃三明治。"},
            {"word": "ハンバーガー", "kanji": "漢堡", "meaning": "漢堡", "ex1_kanji": "ジューシーな パティの ハンバーガーを セットで 頼みます。", "ex1_kana": "じゅｰしｰなぱてぃのはんばｰがｰをせっとでたのみます", "ex1_cn": "點一份多汁肉餅的漢堡套餐。", "ex2_kanji": "大きなハンバーガーを食べます。", "ex2_kana": "おおきなはんばｰがｰをたべます", "ex2_cn": "吃大漢堡。"},
            {"word": "フライドポテト", "kanji": "薯條", "meaning": "薯條", "ex1_kanji": "揚げたてで 熱々の フライドポテトを つまみます。", "ex1_kana": "あげたてであつあつのふらいどぽてとをつまみます", "ex1_cn": "抓幾根剛炸好、熱騰騰的薯條來吃。", "ex2_kanji": "フライドポテトが好きです。", "ex2_kana": "ふらいどぽてとがすきです", "ex2_cn": "喜歡薯條。"},
            {"word": "スパゲッティ", "kanji": "義大利麵", "meaning": "義大利麵", "ex1_kanji": "トマトソースの スパゲッティを フォークで 巻いて 食べます。", "ex1_kana": "とまとそｰすのすぱげってぃをふぉｰくでまいてたべます", "ex1_cn": "用叉子捲起番茄肉醬義大利麵來吃。", "ex2_kanji": "美味しいスパゲッティを作ります。", "ex2_kana": "おいしいすぱげってぃをつくります", "ex2_cn": "做美味的義大利麵。"},
            {"word": "スープ", "kanji": "濃湯", "meaning": "湯 / 濃湯", "ex1_kanji": "コーンの 甘みが 広がる 温かい スープを 飲む。", "ex1_kana": "こｰんのあまみがひろがるあたたかいすｰぷをのむ", "ex1_cn": "喝一碗充滿玉米甜味的溫暖濃湯。", "ex2_kanji": "温かいスープを飲みます。", "ex2_kana": "あたたかいすｰぷをのみます", "ex2_cn": "喝熱湯。"},
            {"word": "クッキー", "kanji": "餅乾", "meaning": "餅乾", "ex1_kanji": "香ばしい 焼き色の クッキーを お茶と 一緒に 食べます。", "ex1_kana": "こうばしいやきいろのくっきｰをおちゃといっしょにたべます", "ex1_cn": "吃著烤得香氣四溢的餅乾，並配上一杯茶。", "ex2_kanji": "甘いクッキーを食べます。", "ex2_kana": "あまいくっきｰをたべます", "ex2_cn": "吃甜餅乾。"},
            {"word": "りんご", "kanji": "林檎", "meaning": "蘋果", "ex1_kanji": "赤くて 水々しい りんごを シャリッと 噛み締めます。", "ex1_kana": "あかくてみずみずしいりんごをしゃりっとかみしめます", "ex1_cn": "喀滋一聲咬下紅潤又水分多的蘋果。", "ex2_kanji": "新鮮なりんごを食べます。", "ex2_kana": "しんせんなりんごをたべます", "ex2_cn": "吃新鮮的蘋果。"},
            {"word": "みかん", "kanji": "蜜柑", "meaning": "橘子", "ex1_kanji": "こたつに 入りながら 甘い みかんを 剥いて 食べます。", "ex1_kana": "こたつにはいりながらあまいみかんをむいてたべます", "ex1_cn": "一邊窩在暖桌裡一邊剝著甜橘子吃。", "ex2_kanji": "美味しいみかんを食べます。", "ex2_kana": "おいしいみかんをたべます", "ex2_cn": "吃好吃的橘子。"},
            {"word": "すいか", "kanji": "西瓜", "meaning": "西瓜", "ex1_kanji": "夏の 暑い 日に 冷えた すいかにかぶりつきます。", "ex1_kana": "なつのあついひにひえたすいかにかぶりつきます", "ex1_cn": "在大熱天裡大口咬下冰涼的西瓜。", "ex2_kanji": "甘いすいかを食べます。", "ex2_kana": "あまいすいかをたべます", "ex2_cn": "吃甜西瓜。"},
            {"word": "ぶどう", "kanji": "葡萄", "meaning": "葡萄", "ex1_kanji": "一房の 紫色の ぶどうを 一粒ずつ 味わいます。", "ex1_kana": "ひとふさのむらさきいろのぶどうをひとつぶずつあじわいます", "ex1_cn": "一顆顆品嚐著一整串紫色的葡萄。", "ex2_kanji": "新鮮なぶどうを買います。", "ex2_kana": "しんせんなぶどうをかいます", "ex2_cn": "買新鮮的葡萄。"},
            {"word": "もも", "kanji": "桃", "meaning": "水蜜桃", "ex1_kanji": "香りが よくて 柔らかい ももを 口に 入れます。", "ex1_kana": "かおりがよくてやわらかいももをくちにいれます", "ex1_cn": "把香氣撲鼻又柔軟的水蜜桃放入口中。", "ex2_kanji": "甘いももを食べます。", "ex2_kana": "あまいももをたべます", "ex2_cn": "吃甜水蜜桃。"},
            {"word": "いちご", "kanji": "苺", "meaning": "草莓", "ex1_kanji": "甘酸っぱい 鮮紅色の いちごに 練乳を かけます。", "ex1_kana": "あまずっぱいせんこうしょくのいちごにれんにゅうをかけます", "ex1_cn": "在酸甜鮮紅的草莓上淋上煉乳。", "ex2_kanji": "大きい苺を食べます。", "ex2_kana": "おおきいいちごをたべます", "ex2_cn": "吃大草莓。"},
            {"word": "バナナ", "kanji": "香蕉", "meaning": "香蕉", "ex1_kanji": "手で 簡単に 皮が 剥ける 栄養満点の バナナを 食べます。", "ex1_kana": "てでかんたんにかわがむけるえいようまんてんのばななをたべます", "ex1_cn": "吃一根用手就能輕鬆剝皮、營養滿分的香蕉。", "ex2_kanji": "毎日バナナを食べます。", "ex2_kana": "まいにちばななをたべます", "ex2_cn": "每天吃香蕉。"},
            {"word": "なし", "kanji": "梨", "meaning": "梨子", "ex1_kanji": "シャキシャキとした 食感の みずみずしい なしが 好きです。", "ex1_kana": "しゃきしゃきとしたしょっかんのみずみずしいなしがすきです", "ex1_cn": "我喜歡口感爽脆又多汁的梨子。", "ex2_kanji": "甘いなしを食べます。", "ex2_kana": "あまいなしをたべます", "ex2_cn": "吃甜梨子。"},
            {"word": "かき", "kanji": "柿", "meaning": "柿子", "ex1_kanji": "秋の 味覚である 熟した 甘い かきを 剥きます。", "ex1_kana": "あきのみかくであるじゅくしたあまいかきをむきます", "ex1_cn": "削一顆屬於秋季美味、熟透且香甜的柿子。", "ex2_kanji": "熟した柿を食べます。", "ex2_kana": "じゅくしたかきをたべます", "ex2_cn": "吃熟柿子。"},
            {"word": "レモン", "kanji": "檸檬", "meaning": "檸檬", "ex1_kanji": "爽やかで 酸っぱい レモンを 絞って 唐揚げに かけます。", "ex1_kana": "さわやかですっぱいれもんをしぼってからあげにかけます", "ex1_cn": "擠出清爽又酸的檸檬汁淋在炸雞塊上。", "ex2_kanji": "レモン水を飲みます。", "ex2_kana": "れもんすいをのみます", "ex2_cn": "喝檸檬水。"},
            {"word": "パパイヤ", "kanji": "木瓜", "meaning": "木瓜", "ex1_kanji": "南国の 豊潤な 香りが する パパイヤを カットします。", "ex1_kana": "なんごくのほうじゅんなかおりがするぱぱいやをかっとします", "ex1_cn": "切開散發南國醇厚香氣的木瓜。", "ex2_kanji": "甘いパパイヤを食べます。", "ex2_kana": "あまいパパイヤをたべます", "ex2_cn": "吃甜木瓜。"},
            {"word": "マンゴー", "kanji": "芒果", "meaning": "芒果", "ex1_kanji": "トロピカルな 甘さが 特徴の 完熟 マンゴーを 頬張ります。", "ex1_kana": "とろぴかるなあまさがとくちょうのかんじゅくまんごｰをほうばります", "ex1_cn": "大口品嚐以熱帶甜味為特色的完熟芒果。", "ex2_kanji": "マンゴーアイスを食べます。", "ex2_kana": "まんごｰあいすをたべます", "ex2_cn": "吃芒果冰淇淋。"},
            {"word": "キウイ", "kanji": "奇異果", "meaning": "奇異果", "ex1_kanji": "ビタミンCが 豊富な グリーン キウイを スプーンで 掬って 食べます。", "ex1_kana": "びたみんしｰがほうふなぐりｰんきういをすぷｰんですくってたべます", "ex1_cn": "用湯匙挖著富含維生素C的綠奇異果吃。", "ex2_kanji": "キウイフルーツが好きです。", "ex2_kana": "きういふるｰつがすきです", "ex2_cn": "喜歡奇異果。"},
            {"word": "パイナップル", "kanji": "鳳梨", "meaning": "鳳梨", "ex1_kanji": "輪切りに した ジューシーな パイナップルを デザートに 出します。", "ex1_kana": "わぎりにしたじゅｰしｰなぱいなっぷるをでざｰとにだします", "ex1_cn": "把切成圓片、多汁的鳳梨作為甜點端上桌。", "ex2_kanji": "パイナップルを食べます。", "ex2_kana": "ぱいなっぷるをたべます", "ex2_cn": "吃鳳梨。"},
            {"word": "メロン", "kanji": "哈密瓜", "meaning": "哈密瓜 / 香瓜", "ex1_kanji": "高級感の ある 甘みが 特徴の メロンを 贅沢に 食べます。", "ex1_kana": "こうきゅうかんのあるあまみがとくちょうのめろんをぜいたくにたべます", "ex1_cn": "奢侈地品嚐帶有高級甜味特色的哈密瓜。", "ex2_kanji": "高いメロンを食べます。", "ex2_kana": "たかいめろんをたべます", "ex2_cn": "吃昂貴的哈密瓜。"},
            {"word": "さくらんぼ", "kanji": "櫻桃", "meaning": "櫻桃", "ex1_kanji": "小さくて 愛らしい 真っ赤な さくらんぼを 飾ります。", "ex1_kana": "ちいさくてあいらしいまっかなさくらんぼをかざります", "ex1_cn": "裝飾著嬌小可愛且通紅的櫻桃。", "ex2_kanji": "可愛いさくらんぼを食べます。", "ex2_kana": "かわいいさくらんぼをたべます", "ex2_cn": "吃可愛的櫻桃。"},
            {"word": "すもも", "kanji": "李子", "meaning": "李子", "ex1_kanji": "甘酸っぱさが クセに なる 新鮮な すももを 味わいます。", "ex1_kana": "あまずっぱさがくせになるしんせんなすももをあじわいます", "ex1_cn": "品嚐那酸甜滋味讓人上癮的新鮮李子。", "ex2_kanji": "新鮮なすももを食べます。", "ex2_kana": "しんせんなすももをたべます", "ex2_cn": "吃新鮮的李子。"},
            {"word": "いちじく", "kanji": "無花果", "meaning": "無花果", "ex1_kanji": "独自の 食感が 楽しめる いちじくを サラダに 添えます。", "ex1_kana": "どくとくのしょっかんがたのしめないちじくをさらだにそえます", "ex1_cn": "將能享受到獨特口感的無花果點綴在沙拉裡。", "ex2_kanji": "美味しいいちじくを食べます。", "ex2_kana": "おいしいいちじくをたべます", "ex2_cn": "吃美味的無花果。"},
            {"word": "ざくろ", "kanji": "石榴", "meaning": "石榴", "ex1_kanji": "粒々とした 美しい ざくろの 実を 一粒ずつ 取り出します。", "ex1_kana": "つぶつぶとしたうつくしいざくろのみをひとつぶずつとりだします", "ex1_cn": "把一顆顆粒粒分明且美麗的石榴果實挑出來。", "ex2_kanji": "珍しいざくろを食べます。", "ex2_kana": "めずらしいざくろをたべます", "ex2_cn": "吃罕見的石榴。"},
            {"word": "ブルーベリー", "kanji": "藍莓", "meaning": "藍莓", "ex1_kanji": "ヨーグルトに たっぷり ブルーベリーを トッピングします。", "ex1_kana": "よｰぐるとにたっぷりぶるｰべりｰをとっぷんぐします", "ex1_cn": "在優格上鋪上滿滿的藍莓。", "ex2_kanji": "ブルーベリーを食べます。", "ex2_kana": "ぶるｰべりｰをたべます", "ex2_cn": "吃藍莓。"},
            {"word": "ラズベリー", "kanji": "覆盆子", "meaning": "覆盆子 / 紅莓", "ex1_kanji": "甘酸っぱい ラズベリーを ケーキの 飾りに 使用します。", "ex1_kana": "あまずっぱいらずべりｰをけｰきのかざりにしようします", "ex1_cn": "將酸甜的覆盆子用來裝飾蛋糕。", "ex2_kanji": "甘酸っぱいラズベリーを食べます。", "ex2_kana": "あまずっぱいらずべりｰをたべます", "ex2_cn": "吃酸甜的覆盆子。"},
            {"word": "ようなし", "kanji": "西洋梨", "meaning": "西洋梨", "ex1_kanji": "とろけるような 食感の 熟した 洋梨を 切ります。", "ex1_kana": "とろけるようなしょっかんのじゅくしたようなしをきります", "ex1_cn": "切開口感入口即化、熟透的西洋梨。", "ex2_kanji": "甘い西洋梨を食べます。", "ex2_kana": "あまいようなしをたべます", "ex2_cn": "吃甜西洋梨。"},
            {"word": "ゆず", "kanji": "柚子", "meaning": "柚子", "ex1_kanji": "爽やかな 香りが する ゆずを お風呂に 浮かべます。", "ex1_kana": "さわやかなかおりがするゆずをおふろにうかべます", "ex1_cn": "把散發清爽香氣的柚子放入浴缸中泡澡。", "ex2_kanji": "柚子の香りが好きです。", "ex2_kana": "ゆずのかおりがすきです", "ex2_cn": "喜歡柚子的香味。"},
            {"word": "スターフルーツ", "kanji": "楊桃", "meaning": "楊桃", "ex1_kanji": "横に 切ると 星型に なる スターフルーツを 盛り付けます。", "ex1_kana": "よこにきるとほしがたになるすたｰふるｰつをもりつけます", "ex1_cn": "將橫切後會變成星星形狀的楊桃擺盤。", "ex2_kanji": "珍しいスターフルーツを食べます。", "ex2_kana": "めずらしいすたｰふるｰつをたべます", "ex2_cn": "吃罕見的楊桃。"},
            {"word": "ドラゴンフルーツ", "kanji": "火龍果", "meaning": "火龍果", "ex1_kanji": "鮮烈な 見た目が 特徴の ドラゴンフルーツを カットします。", "ex1_kana": "せんれつなみた目がとくちょうのどらごんふるｰつをかっとします", "ex1_cn": "切開外觀鮮烈為特色的火龍果。", "ex2_kanji": "赤いドラゴンフルーツを食べます。", "ex2_kana": "あかいどらごんふるｰつをたべます", "ex2_cn": "吃紅火龍果。"}
        ]

    def init_animal_data(self):
        self.animal_data = [
            {"word": "いぬ", "kanji": "犬", "meaning": "狗", "ex1_kanji": "公園で 犬の 散歩を します。", "ex1_kana": "こうえんでいぬのさんぽをします", "ex1_cn": "在公園遛狗。", "ex2_kanji": "可愛い犬を飼っています。", "ex2_kana": "かわいいいぬをかっています", "ex2_cn": "養了可愛的狗狗。"},
            {"word": "ねこ", "kanji": "猫", "meaning": "貓", "ex1_kanji": "猫が 日向ぼっこを しています。", "ex1_kana": "ねこがひなたぼっこをしています", "ex1_cn": "貓咪正在曬太陽。", "ex2_kanji": "猫が魚を食べます。", "ex2_kana": "ねこがさかなをたべます", "ex2_cn": "貓吃魚。"},
            {"word": "うさぎ", "kanji": "兎", "meaning": "兔子", "ex1_kanji": "白い うさぎは とても 可愛いです。", "ex1_kana": "しろいうさぎはとてもかわいいです", "ex1_cn": "白色的兔子非常可愛。", "ex2_kanji": "うさぎが跳ねます。", "ex2_kana": "うさぎがはねます", "ex2_cn": "兔子跳躍。"},
            {"word": "とり", "kanji": "鳥", "meaning": "鳥", "ex1_kanji": "朝 早く 鳥が 鳴いています。", "ex1_kana": "あさはやくとりがないています", "ex1_cn": "清晨有鳥兒在鳴叫。", "ex2_kanji": "空を鳥が飛んでいます。", "ex2_kana": "そらをとりがとんでいます", "ex2_cn": "鳥兒在空中飛翔。"},
            {"word": "くま", "kanji": "熊", "meaning": "熊", "ex1_kanji": "森で 熊に 注意して ください。", "ex1_kana": "もりでくまにちゅういしてください", "ex1_cn": "在森林裡請小心熊。", "ex2_kanji": "大きな熊を見ました。", "ex2_kana": "おおきなくまをみました", "ex2_cn": "看到了大熊。"},
            {"word": "ぞう", "kanji": "象", "meaning": "大象", "ex1_kanji": "動物園で 象を 見ました。", "ex1_kana": "どうぶつえんでぞうをみました", "ex1_cn": "在動物園看了大象。", "ex2_kanji": "象の鼻が長いです。", "ex2_kana": "ぞうのはながながいです", "ex2_cn": "大象的鼻子很長。"},
            {"word": "とら", "kanji": "虎", "meaning": "老虎", "ex1_kanji": "虎は とても 強そうです。", "ex1_kana": "とらはとてもつよそうです", "ex1_cn": "老虎看起來非常強壯。", "ex2_kanji": "動物園で虎を見ます。", "ex2_kana": "どうぶつえんでとらをみます", "ex2_cn": "在動物園看老虎。"},
            {"word": "さる", "kanji": "猿", "meaning": "猴子", "ex1_kanji": "猿が バナナを 食べます。", "ex1_kana": "さるがばななをたべます", "ex1_cn": "猴子吃香蕉。", "ex2_kanji": "木に猿がいます。", "ex2_kana": "きにさるがいます", "ex2_cn": "樹上有猴子。"},
            {"word": "うま", "kanji": "馬", "meaning": "馬", "ex1_kanji": "牧場で 馬に 乗りました。", "ex1_kana": "ぼくじょうでうまにのりました", "ex1_cn": "在牧場騎了馬。", "ex2_kanji": "馬が速く走ります。", "ex2_kana": "うまがはやくはしります", "ex2_cn": "馬跑得很快。"},
            {"word": "うし", "kanji": "牛", "meaning": "牛", "ex1_kanji": "牛から 牛乳を 絞ります。", "ex1_kana": "うしからぎゅうにゅうをしぼります", "ex1_cn": "從牛身上擠牛奶。", "ex2_kanji": "牧場に牛がいます。", "ex2_kana": "ぼくじょうにうしがいます", "ex2_cn": "牧場裡有牛。"},
            {"word": "ぶた", "kanji": "豚", "meaning": "豬", "ex1_kanji": "子豚が 寝ています。", "ex1_kana": "こぶたがねています", "ex1_cn": "小豬正在睡覺。", "ex2_kanji": "可愛い豚を見ました。", "ex2_kana": "かわいいぶたをみました", "ex2_cn": "看到了可愛的豬。"},
            {"word": "ひつじ", "kanji": "羊", "meaning": "羊", "ex1_kanji": "羊の 毛は フワフワです。", "ex1_kana": "ひつじのけはふわふわです", "ex1_cn": "羊毛毛茸茸的。", "ex2_kanji": "牧場に羊がいます。", "ex2_kana": "ぼくじょうにひつじがいます", "ex2_cn": "牧場裡有羊。"},
            {"word": "しか", "kanji": "鹿", "meaning": "鹿", "ex1_kanji": "奈良には 鹿が たくさんいます。", "ex1_kana": "ならにはしかがたくさんいます", "ex1_cn": "奈良有很多鹿。", "ex2_kanji": "鹿にせんべいをあげます。", "ex2_kana": "しかにせんべいをあげます", "ex2_cn": "餵鹿吃仙貝。"},
            {"word": "きつね", "kanji": "狐", "meaning": "狐狸", "ex1_kanji": "きつねが 走って いきました。", "ex1_kana": "きつねがはしっていきました", "ex1_cn": "狐狸跑過去了。", "ex2_kanji": "森で狐を見ました。", "ex2_kana": "もりできつねをみました", "ex2_cn": "在森林裡看到了狐狸。"},
            {"word": "たぬき", "kanji": "狸", "meaning": "狸貓", "ex1_kanji": "道で たぬきを 見かけました。", "ex1_kana": "みちでたぬきをみかけました", "ex1_cn": "在路上看見了狸貓。", "ex2_kanji": "夜にたぬきが出ます。", "ex2_kana": "よるにたぬきがでます", "ex2_cn": "晚上狸貓會出現。"},
            {"word": "おおかみ", "kanji": "狼", "meaning": "狼", "ex1_kanji": "狼が 月に 吠えます。", "ex1_kana": "おおかみがつきにほえます", "ex1_cn": "狼對著月亮嚎叫。", "ex2_kanji": "遠くで狼が鳴きます。", "ex2_kana": "とおくでおおかみがないきます", "ex2_cn": "遠處有狼在叫。"},
            {"word": "ねずみ", "kanji": "鼠", "meaning": "老鼠", "ex1_kanji": "ねずみが チーズを 食べています。", "ex1_kana": "ねずみがちｰずをたべています", "ex1_cn": "老鼠正在吃起司。", "ex2_kanji": "家の中にねずみがいます。", "ex2_kana": "いえのなかにねずみがいます", "ex2_cn": "家裡有老鼠。"},
            {"word": "かめ", "kanji": "亀", "meaning": "烏龜", "ex1_kanji": "亀が ゆっくり 歩いています。", "ex1_kana": "かめがゆっくりあるいています", "ex1_cn": "烏龜正慢慢地走著。", "ex2_kanji": "池に亀がいます。", "ex2_kana": "いけにかめがいます", "ex2_cn": "池塘裡有烏龜。"},
            {"word": "へび", "kanji": "蛇", "meaning": "蛇", "ex1_kanji": "草の 中に 蛇が います。", "ex1_kana": "くさのなかにへびがいます", "ex1_cn": "草叢裡有蛇。", "ex2_kanji": "山で蛇に気をつけます。", "ex2_kana": "やまでへびにきをつけます", "ex2_cn": "在山上小心蛇。"},
            {"word": "カエル", "kanji": "蛙", "meaning": "青蛙", "ex1_kanji": "雨の 日は カエルが 鳴きます。", "ex1_kana": "あめのひはかえるがないきます", "ex1_cn": "下雨天青蛙會叫。", "ex2_kanji": "田んぼでカエルが鳴きます。", "ex2_kana": "たんぼでかえるがないきます", "ex2_cn": "稻田裡青蛙在叫。"},
            {"word": "キリン", "kanji": "麒麟", "meaning": "長頸鹿", "ex1_kanji": "キリンは 首が 長いです。", "ex1_kana": "きりんはくびがながいです", "ex1_cn": "長頸鹿的脖子很長。", "ex2_kanji": "動物園でキリンを見ます。", "ex2_kana": "どうぶつえんできりんをみます", "ex2_cn": "在動物園看長頸鹿。"},
            {"word": "ライオン", "kanji": "獅子", "meaning": "獅子", "ex1_kanji": "ライオンは 百獣の 王です。", "ex1_kana": "らいおんはひゃくじゅうのおうです", "ex1_cn": "獅子是百獸之王。", "ex2_kanji": "強いライオンを見ました。", "ex2_kana": "つよいらいおんをみました", "ex2_cn": "看到了強壯的獅子。"},
            {"word": "パンダ", "kanji": "熊猫", "meaning": "熊貓", "ex1_kanji": "パンダが 笹を 食べています。", "ex1_kana": "ぱんだがささをたべています", "ex1_cn": "熊貓正在吃竹葉。", "ex2_kanji": "人気のパンダを見ます。", "ex2_kana": "にんきのぱんだをみます", "ex2_cn": "去看人氣熊貓。"},
            {"word": "ペンギン", "kanji": "-", "meaning": "企鵝", "ex1_kanji": "水族館の ペンギンが 可愛いです。", "ex1_kana": "すいぞくかんのぺんぎんがかわいいです", "ex1_cn": "水族館裡的企鵝很可愛。", "ex2_kanji": "ペンギンが泳ぎます。", "ex2_kana": "ぺんぎんがおよぎます", "ex2_cn": "企鵝在游泳。"},
            {"word": "カンガルー", "kanji": "-", "meaning": "袋鼠", "ex1_kanji": "カンガルーの 赤ちゃんが 袋に います。", "ex1_kana": "かんがるｰのあかちゃんがふくろにいます", "ex1_cn": "袋鼠寶寶在育兒袋裡。", "ex2_kanji": "動物園でカンガルーを見ます。", "ex2_kana": "どうぶつえんでかんがるｰをみます", "ex2_cn": "在動物園看袋鼠。"},
            {"word": "しゃけ", "kanji": "鮭", "meaning": "鮭魚", "ex1_kanji": "朝食に 焼き鮭を 食べます。", "ex1_kana": "ちょうしょくにやきじゃけをたべます", "ex1_cn": "早餐吃烤鮭魚。", "ex2_kanji": "美味しい鮭を焼きます。", "ex2_kana": "おいしいしゃけをやきます", "ex2_cn": "烤好吃的鮭魚。"},
            {"word": "まぐろ", "kanji": "鮪", "meaning": "鮪魚", "ex1_kanji": "まぐろの お寿司が 好きです。", "ex1_kana": "まぐろのおすしがすきです", "ex1_cn": "我喜歡吃鮪魚壽司。", "ex2_kanji": "新鮮なまぐろを食べます。", "ex2_kana": "しんせんなまぐろをたべます", "ex2_cn": "吃新鮮的鮪魚。"},
            {"word": "たい", "kanji": "鯛", "meaning": "鯛魚", "ex1_kanji": "お祝いの 日に たいを 焼きます。", "ex1_kana": "おいわいのひにたいをやきます", "ex1_cn": "慶祝的日子會烤鯛魚。", "ex2_kanji": "めでたい日に鯛を食べます。", "ex2_kana": "めでたいひにたいをたべます", "ex2_cn": "在值得慶賀的日子吃鯛魚。"},
            {"word": "さば", "kanji": "鯖", "meaning": "鯖魚", "ex1_kanji": "さばの 塩焼きを 注文しました。", "ex1_kana": "さばのしおやきをちゅうもんしました", "ex1_cn": "點了鹽烤鯖魚。", "ex2_kanji": "美味しいさばを食べます。", "ex2_kana": "おいしいさばをたべます", "ex2_cn": "吃好吃的鯖魚。"},
            {"word": "あじ", "kanji": "鯵", "meaning": "竹筴魚", "ex1_kanji": "あじの フライは サクサクです。", "ex1_kana": "あじのふらいはさくさくです", "ex1_cn": "炸竹筴魚非常酥脆。", "ex2_kanji": "新鮮なあじを料理します。", "ex2_kana": "しんせんなあじをりょうりします", "ex2_cn": "料理新鮮的竹筴魚。"},
            {"word": "いわし", "kanji": "鰯", "meaning": "沙丁魚", "ex1_kanji": "いわしは 栄養が 満点です。", "ex1_kana": "いわしはえいようがまんてんです", "ex1_cn": "沙丁魚營養滿分。", "ex2_kanji": "いわしを焼いて食べます。", "ex2_kana": "いわしをやいてたべます", "ex2_cn": "烤沙丁魚來吃。"},
            {"word": "うなぎ", "kanji": "鰻", "meaning": "鰻魚", "ex1_kanji": "夏は うなぎを 食べて 元気を 出します。", "ex1_kana": "なつはうなぎをたべてげんきをだします", "ex1_cn": "夏天吃鰻魚來補充體力。", "ex2_kanji": "美味しい鰻を食べます。", "ex2_kana": "おいしいうなぎをたべます", "ex2_cn": "吃好吃的鰻魚。"},
            {"word": "ぶり", "kanji": "鰤", "meaning": "鰤魚 (青甘)", "ex1_kanji": "ぶり大根は 冬の 料理です。", "ex1_kana": "ぶりだいこんはふゆのりょうりです", "ex1_cn": "鰤魚燉蘿蔔是冬天的料理。", "ex2_kanji": "新鮮なぶりを食べます。", "ex2_kana": "しんせんなぶりをたべます", "ex2_cn": "吃新鮮的鰤魚。"},
            {"word": "かつお", "kanji": "鰹", "meaning": "鰹魚", "ex1_kanji": "かつおの たたきが 美味しいです。", "ex1_kana": "かつおのたたきがおいしいです", "ex1_cn": "炙烤鰹魚生魚片很好吃。", "ex2_kanji": "旬のかつおを食べます。", "ex2_kana": "しゅんのかつおをたべます", "ex2_cn": "吃當季的鰹魚。"},
            {"word": "たら", "kanji": "鱈", "meaning": "鱈魚", "ex1_kanji": "お鍋に たらを 入れます。", "ex1_kana": "おなべにたらをいれます", "ex1_cn": "把鱈魚放進火鍋裡。", "ex2_kanji": "鍋料理にたらを使います。", "ex2_kana": "なべりょうりにたらをつかいます", "ex2_cn": "火鍋料理會使用鱈魚。"},
            {"word": "ひらめ", "kanji": "鮃", "meaning": "比目魚", "ex1_kanji": "ひらめの 刺身を 頼みました。", "ex1_kana": "ひらめのさしみをたのみました", "ex1_cn": "點了比目魚的生魚片。", "ex2_kanji": "新鮮なひらめを食べます。", "ex2_kana": "しんせんなひらめをたべます", "ex2_cn": "吃新鮮的比目魚。"},
            {"word": "さんま", "kanji": "秋刀魚", "meaning": "秋刀魚", "ex1_kanji": "秋の さんまは 脂が のっています。", "ex1_kana": "あきのさんまはあぶらがのっています", "ex1_cn": "秋天的秋刀魚油脂豐富。", "ex2_kanji": "塩焼きのさんまを食べます。", "ex2_kana": "しおやきのさんまをたべます", "ex2_cn": "吃鹽烤秋刀魚。"},
            {"word": "かれい", "kanji": "鰈", "meaning": "鰈魚", "ex1_kanji": "かれいの 煮付を 作ります。", "ex1_kana": "かれいのにつけをつくります", "ex1_cn": "來做紅燒鰈魚。", "ex2_kanji": "美味しいかれいを食べます。", "ex2_kana": "おいしいかれいをたべます", "ex2_cn": "吃好吃的鰈魚。"},
            {"word": "すずき", "kanji": "鱸", "meaning": "鱸魚", "ex1_kanji": "すずきの ムニエルは おしゃれな 料理です。", "ex1_kana": "すずきのむにえるはおしゃれなりょうりです", "ex1_cn": "法式乾煎鱸魚是一道時髦的料理。", "ex2_kanji": "新鮮なすずきを料理します。", "ex2_kana": "しんせんなすずきをりょうりします", "ex2_cn": "料理新鮮的鱸魚。"},
            {"word": "きす", "kanji": "鱚", "meaning": "沙鮻 (沙梭魚)", "ex1_kanji": "きすの 天ぷらは 絶品です。", "ex1_kana": "きすのてんぷらはぜっぴんです", "ex1_cn": "炸沙鮻天婦羅是絕品。", "ex2_kanji": "サクサクのきすを食べます。", "ex2_kana": "さくさくのきすをたべます", "ex2_cn": "吃酥脆的沙鮻。"},
            {"word": "あゆ", "kanji": "鮎", "meaning": "香魚", "ex1_kanji": "川で 釣った あゆを 焼いて 食べます。", "ex1_kana": "かわでつったあゆをやいてたべます", "ex1_cn": "把河裡釣到的香魚烤來吃。", "ex2_kanji": "塩焼きのあゆを食べます。", "ex2_kana": "しおやきのあゆをたべます", "ex2_cn": "吃鹽烤香魚。"},
            {"word": "さわら", "kanji": "鰆", "meaning": "土魠魚 (馬鮫魚)", "ex1_kanji": "さわらの 西京焼きが 大好きです。", "ex1_kana": "さわらのさいきょうやきがだいすきです", "ex1_cn": "我最喜歡吃西京燒土魠魚。", "ex2_kanji": "美味しいさわらを食べます。", "ex2_kana": "おいしいさわらをたべます", "ex2_cn": "吃好吃的土魠魚。"},
            {"word": "ふぐ", "kanji": "河豚", "meaning": "河豚", "ex1_kanji": "ふぐは 高級な 魚です。", "ex1_kana": "ふぐはこうきゅうなさかなです", "ex1_cn": "河豚是高級的魚類。", "ex2_kanji": "高級なふぐ料理を食べます。", "ex2_kana": "こうきゅうなふぐりょうりをたべます", "ex2_cn": "吃高級的河豚料理。"},
            {"word": "あなご", "kanji": "穴子", "meaning": "星鰻", "ex1_kanji": "あなごの 握り寿司を 頼みます。", "ex1_kana": "あなごのにぎりずしをたのみます", "ex1_cn": "點了星鰻握壽司。", "ex2_kanji": "美味しいあなごを食べます。", "ex2_kana": "おいしいあなごをたべます", "ex2_cn": "吃好吃的星鰻。"},
            {"word": "はまち", "kanji": "魬", "meaning": "幼鰤魚 (青甘幼魚)", "ex1_kanji": "はまちは とても 人気があります。", "ex1_kana": "はまちはとてもにんきがあります", "ex1_cn": "幼鰤魚非常受歡迎。", "ex2_kanji": "新鮮なはまちを食べます。", "ex2_kana": "しんせんなはまちをたべます", "ex2_cn": "吃新鮮的幼鰤魚。"},
            {"word": "たちうお", "kanji": "太刀魚", "meaning": "白帶魚", "ex1_kanji": "たちうおは ピカピカ 光っています。", "ex1_kana": "たちうおはぴかぴかひかっています", "ex1_cn": "白帶魚閃閃發光。", "ex2_kanji": "塩焼きのたちうおを食べます。", "ex2_kana": "しおやきのたちうおをたべます", "ex2_cn": "吃鹽烤白帶魚。"},
            {"word": "あんこう", "kanji": "鮟鱇", "meaning": "鮟鱇魚", "ex1_kanji": "冬の あんこう鍋は 最高です。", "ex1_kana": "ふゆのあんこうなべはさいこうです", "ex1_cn": "冬天的鮟鱇魚火鍋最棒了。", "ex2_kanji": "温かいあんこう鍋を食べます。", "ex2_kana": "あたたかいあんこうなべをたべます", "ex2_cn": "吃溫暖的鮟鱇魚火鍋。"},
            {"word": "こい", "kanji": "鯉", "meaning": "鯉魚", "ex1_kanji": "池に 大きな こいが 泳いでいます。", "ex1_kana": "いけにおおきなこいがおよいでいます", "ex1_cn": "池塘裡有大鯉魚在游水。", "ex2_kanji": "池の鯉を見ます。", "ex2_kana": "いけのこいをみます", "ex2_cn": "看池塘裡的鯉魚。"},
            {"word": "どじょう", "kanji": "泥鰌", "meaning": "泥鰍", "ex1_kanji": "どじょう汁は 昔から ある 料理です。", "ex1_kana": "どじょうじるはむかしからあるりょうりです", "ex1_cn": "泥鰍汁是自古就有的料理。", "ex2_kanji": "伝統的などじょう料理を食べます。", "ex2_kana": "でんとうてきなどじょうりょうりをたべます", "ex2_cn": "吃傳統的泥鰍料理。"},
            {"word": "さめ", "kanji": "鮫", "meaning": "鯊魚", "ex1_kanji": "さめの フカヒレは 高級 食材です。", "ex1_kana": "さめのふかひれはこうきゅうしょくざいです", "ex1_cn": "鯊魚的魚翅是高級食材。", "ex2_kanji": "水族館で大きなさめを見ます。", "ex2_kana": "すいぞくかんでおおきなさめをみます", "ex2_cn": "在水族館看大鯊魚。"}
        ]

    def init_daily_data(self):
        self.daily_data = [
            {"word": "つくえ", "kanji": "机", "meaning": "書桌、桌子 (Desk)", "ex1_kanji": "机の上に本があります。", "ex1_kana": "つくえのうえにほんがあります", "ex1_cn": "桌上有書本。", "ex2_kanji": "机をきれいに拭きます。", "ex2_kana": "つくえをきれいにふきます", "ex2_cn": "把桌子擦拭乾淨。"},
            {"word": "いす", "kanji": "椅子", "meaning": "椅子 (Chair)", "ex1_kanji": "椅子に座って休みます。", "ex1_kana": "いすにすわってやすみます", "ex1_cn": "坐在椅子上休息。", "ex2_kanji": "新しい椅子を買いました。", "ex2_kana": "あたらしいいすをかいました", "ex2_cn": "買了一把新椅子。"},
            {"word": "とけい", "kanji": "時計", "meaning": "時鐘、手錶 (Clock / Watch)", "ex1_kanji": "壁に時計をかけます。", "ex1_kana": "かべにとけいをかけます", "ex1_cn": "把時鐘掛在牆上。", "ex2_kanji": "腕時計を見ます。", "ex2_kana": "うでどけいをみます", "ex2_cn": "看手錶。"},
            {"word": "かばん", "kanji": "鞄", "meaning": "包包、皮包 (Bag)", "ex1_kanji": "鞄の中に財布を入れます。", "ex1_kana": "かばんのなかにさいふをいれます", "ex1_cn": "把錢包放進包包裡。", "ex2_kanji": "重い鞄を持ちます。", "ex2_kana": "おもいかばんをもちます", "ex2_cn": "提著沈重的包包。"},
            {"word": "かさ", "kanji": "傘", "meaning": "雨傘 (Umbrella)", "ex1_kanji": "雨が降るので傘をさします。", "ex1_kana": "あめがふるのでかさをさします", "ex1_cn": "因為下雨所以撐傘。", "ex2_kanji": "電車に傘を忘れました。", "ex2_kana": "でんしゃにかさをわすれました", "ex2_cn": "把雨傘忘在電車上了。"},
            {"word": "めがね", "kanji": "眼鏡", "meaning": "眼鏡 (Glasses)", "ex1_kanji": "眼鏡をかけて本を読みます。", "ex1_kana": "めがねをかけてほんをよみます", "ex1_cn": "戴著眼鏡讀書。", "ex2_kanji": "新しい眼鏡を作ります。", "ex2_kana": "あたらしいめがねをつくります", "ex2_cn": "配一副新眼鏡。"},
            {"word": "さいふ", "kanji": "財布", "meaning": "錢包 (Wallet)", "ex1_kanji": "財布からお金を出します。", "ex1_kana": "さいふからおかねをだします", "ex1_cn": "從錢包裡拿出錢。", "ex2_kanji": "財布を忘れてしまいました。", "ex2_kana": "さいふをわすれてしまいました", "ex2_cn": "把錢包給忘了。"},
            {"word": "かぎ", "kanji": "鍵", "meaning": "鑰匙 (Key)", "ex1_kanji": "ドアの鍵を閉めます。", "ex1_kana": "どあのかぎをしめます", "ex1_cn": "鎖上門的鑰匙。", "ex2_kanji": "鍵をなくして困ります。", "ex2_kana": "かぎをなくしてこまります", "ex2_cn": "弄丟鑰匙很困擾。"},
            {"word": "ほん", "kanji": "本", "meaning": "書本 (Book)", "ex1_kanji": "図書館で本を借ります。", "ex1_kana": "としょかんでほんをかります", "ex1_cn": "在圖書館借書。", "ex2_kanji": "面白い本を読みます。", "ex2_kana": "おもしろいほんをよみます", "ex2_cn": "讀有趣的書。"},
            {"word": "ノート", "kanji": "ノート", "meaning": "筆記本 (Notebook)", "ex1_kanji": "ノートに漢字を書き込みます。", "ex1_kana": "のーとにかんじをかきこみます", "ex1_cn": "把漢字寫在筆記本裡。", "ex2_kanji": "新しいノートを開きます。", "ex2_kana": "あたらしいのーとをひらきます", "ex2_cn": "翻開一本新筆記本。"},
            {"word": "ペン", "kanji": "ペン", "meaning": "原子筆、筆 (Pen)", "ex1_kanji": "赤いペンで名前を書きます。", "ex1_kana": "あかいぺんでなまえをかきます", "ex1_cn": "用紅筆寫名字。", "ex2_kanji": "インクのペンを使います。", "ex2_kana": "いんくのぺんをつかいます", "ex2_cn": "使用墨水筆。"},
            {"word": "けしゴム", "kanji": "消しゴム", "meaning": "橡皮擦 (Eraser)", "ex1_kanji": "消しゴムで文字を消します。", "ex1_kana": "けしごむでもじをけします", "ex1_cn": "用橡皮擦擦掉文字。", "ex2_kanji": "消しゴムを落としました。", "ex2_kana": "けしごむをおとしました", "ex2_cn": "把橡皮擦弄掉了。"},
            {"word": "はさみ", "kanji": "鋏", "meaning": "剪刀 (Scissors)", "ex1_kanji": "はさみで紙を切ります。", "ex1_kana": "はさみでかみをきります", "ex1_cn": "用剪刀剪紙。", "ex2_kanji": "安全なはさみを使います。", "ex2_kana": "あんぜんなはさみをつかいます", "ex2_cn": "使用安全的剪刀。"},
            {"word": "タオル", "kanji": "タオル", "meaning": "毛巾 (Towel)", "ex1_kanji": "お風呂の後にタオルで拭きます。", "ex1_kana": "おふろのあとにたおるでふきます", "ex1_cn": "洗完澡後用毛巾擦拭。", "ex2_kanji": "白いタオルを洗います。", "ex2_kana": "しろいたおるをあらいます", "ex2_cn": "洗白毛巾。"},
            {"word": "せっけん", "kanji": "石鹸", "meaning": "肥皂 (Soap)", "ex1_kanji": "石鹸で手をきれいに洗います。", "ex1_kana": "せっけんでてをきれいにあらいます", "ex1_cn": "用肥皂把手洗乾淨。", "ex2_kanji": "良い香りの石鹸です。", "ex2_kana": "よいかおりのせっけんです", "ex2_cn": "是香味很好的肥皂。"},
            {"word": "シャンプー", "kanji": "シャンプー", "meaning": "洗髮精 (Shampoo)", "ex1_kanji": "シャンプーで頭を洗います。", "ex1_kana": "しゃんぷーであたまをあらいます", "ex1_cn": "用洗髮精洗頭。", "ex2_kanji": "新しいシャンプーを買います。", "ex2_kana": "あたらしいしゃんぷーをかいます", "ex2_cn": "買新的洗髮精。"},
            {"word": "はみがき", "kanji": "歯磨き", "meaning": "牙膏、刷牙 (Toothpaste / Brushing teeth)", "ex1_kanji": "歯磨き粉をつけて歯を磨きます。", "ex1_kana": "はみがきこをつけてはをみがきます", "ex1_cn": "擠上牙膏刷牙。", "ex2_kanji": "毎朝歯磨きをします。", "ex2_kana": "まいあさはみがきをします", "ex2_cn": "每天早上刷牙。"},
            {"word": "ドライヤー", "kanji": "ドライヤー", "meaning": "吹風機 (Hair dryer)", "ex1_kanji": "ドライヤーで髪を乾かします。", "ex1_kana": "どらいやーでかみをかわかします", "ex1_cn": "用吹風機吹乾頭髮。", "ex2_kanji": "ドライヤーの風が強いです。", "ex2_kana": "どらいやーのかぜがつよいです", "ex2_cn": "吹風機風力很強。"},
            {"word": "コップ", "kanji": "コップ", "meaning": "杯子 (Cup / Glass)", "ex1_kanji": "コップに水を注ぎます。", "ex1_kana": "こっぷにみずをそそぎます", "ex1_cn": "往杯子裡倒水。", "ex2_kanji": "ガラスのコップを割ります。", "ex2_kana": "がらすのこっぷをわります", "ex2_cn": "打破玻璃杯。"},
            {"word": "おわん", "kanji": "お椀", "meaning": "碗、飯碗 (Bowl)", "ex1_kanji": "お椀でお味噌汁を飲みます。", "ex1_kana": "おわんでおみそしるをのみます", "ex1_cn": "用碗喝味噌湯。", "ex2_kanji": "木のお椀を使います。", "ex2_kana": "きのおわんをつかいます", "ex2_cn": "使用木碗。"},
            {"word": "はし", "kanji": "箸", "meaning": "筷子 (Chopsticks)", "ex1_kanji": "箸でご飯を食べます。", "ex1_kana": "はしでごはんをたべます", "ex1_cn": "用筷子吃飯。", "ex2_kanji": "新しい箸を揃えます。", "ex2_kana": "あたらしいはしをそろえます", "ex2_cn": "備齊新筷子。"},
            {"word": "スプーン", "kanji": "スプーン", "meaning": "湯匙 (Spoon)", "ex1_kanji": "スプーンでスープをすくいます。", "ex1_kana": "すぷーんですーぷをすくいます", "ex1_cn": "用湯匙舀湯。", "ex2_kanji": "銀のスプーンを使います。", "ex2_kana": "ぎんのすぷーんをつかいます", "ex2_cn": "使用銀湯匙。"},
            {"word": "ふとん", "kanji": "布団", "meaning": "棉被、日式床鋪 (Futon / Bedding)", "ex1_kanji": "夜に布団に入って寝ます。", "ex1_kana": "よるにふとんにはいってねます", "ex1_cn": "晚上鑽進被窩睡覺。", "ex2_kanji": "晴れた日に布団を干します。", "ex2_kana": "はれたひにふとんをほします", "ex2_cn": "在晴天曬棉被。"},
            {"word": "まくら", "kanji": "枕", "meaning": "枕頭 (Pillow)", "ex1_kanji": "柔らかい枕を使います。", "ex1_kana": "やわらかいまくらをつかいます", "ex1_cn": "使用柔軟的枕頭。", "ex2_kanji": "枕の高さを調整します。", "ex2_kana": "まくらのたかさをちょうせいします", "ex2_cn": "調整枕頭的高度。"},
            {"word": "ゴミばこ", "kanji": "ゴミ箱", "meaning": "垃圾桶 (Trash can)", "ex1_kanji": "ゴミをゴミ箱に捨てます。", "ex1_kana": "ごみをごみばこにすてます", "ex1_cn": "把垃圾丟進垃圾桶。", "ex2_kanji": "新しいゴミ箱を買います。", "ex2_kana": "あたらしいごみばこをかいます", "ex2_cn": "買一個新的垃圾桶。"},
            {"word": "かみそり", "kanji": "剃刀", "meaning": "刮鬍刀、剃刀 (Razor)", "ex1_kanji": "剃刀でヒゲをそります。", "ex1_kana": "かみそりでひげをそります", "ex1_cn": "用刮鬍刀刮鬍子。", "ex2_kanji": "新しい剃刀を交換します。", "ex2_kana": "あたらしいかみそりをこうかんします", "ex2_cn": "更換新的刮鬍刀。"},
            {"word": "ハンガー", "kanji": "ハンガー", "meaning": "衣架 (Hanger)", "ex1_kanji": "シャツをハンガーにかけます。", "ex1_kana": "しゃつをはんがーにかめます", "ex1_cn": "把襯衫掛在衣架上。", "ex2_kanji": "木製のハンガーを使います。", "ex2_kana": "もくせいのはんがーをつかいます", "ex2_cn": "使用木製衣架。"},
            {"word": "まど", "kanji": "窓", "meaning": "窗戶 (Window)", "ex1_kanji": "朝に窓を開けて換気をします。", "ex1_kana": "あさにまどをあけてかんきをします", "ex1_cn": "早上打開窗戶換氣。", "ex2_kanji": "窓から外の景色を見ます。", "ex2_kana": "まどからそとのけしきをみます", "ex2_cn": "從窗戶看外面的風景。"},
            {"word": "カーテン", "kanji": "カーテン", "meaning": "窗簾 (Curtain)", "ex1_kanji": "カーテンを閉めて部屋を暗くします。", "ex1_kana": "かーてんをしめてへやをくらくします", "ex1_cn": "拉上窗簾把房間變暗。", "ex2_kanji": "白いカーテンを洗います。", "ex2_kana": "しろいかーてんをあらいます", "ex2_cn": "洗白窗簾。"},
            {"word": "まほうびん", "kanji": "魔法瓶", "meaning": "保溫瓶 (Thermos flask)", "ex1_kanji": "魔法瓶にお湯を入れます。", "ex1_kana": "まほうびんにおゆをいれます", "ex1_cn": "把熱水裝進保溫瓶裡。", "ex2_kanji": "魔法瓶の冷めないお茶です。", "ex2_kana": "まほうびんのさめないおちゃです", "ex2_cn": "是保溫瓶裡不會變涼的茶。"},
            {"word": "ぞうきん", "kanji": "雑巾", "meaning": "抹布 (Cleaning cloth / Rag)", "ex1_kanji": "雑巾で床を拭きます。", "ex1_kana": "ぞうきんでゆかをふきます", "ex1_cn": "用抹布擦地板。", "ex2_kanji": "汚れた雑巾を洗います。", "ex2_kana": "よごれたぞうきんをあらいます", "ex2_cn": "清洗髒抹布。"},
            {"word": "ほうき", "kanji": "箒", "meaning": "掃帚 (Broom)", "ex1_kanji": "ほうきで床を掃きます。", "ex1_kana": "ほうきでゆかをはきます", "ex1_cn": "用掃帚掃地板。", "ex2_kanji": "玄関をほうきで掃除します。", "ex2_kana": "げんかんをほうきでそうじします", "ex2_cn": "用掃帚打掃玄關。"},
            {"word": "ちりとり", "kanji": "塵取り", "meaning": "畚箕、垃圾鏟 (Dustpan)", "ex1_kanji": "ほうきとちりとりを使います。", "ex1_kana": "ほうきとちりとりをつかいます", "ex1_cn": "使用掃帚和畚箕。", "ex2_kanji": "ゴミをちりとりに入れます。", "ex2_kana": "ごみをちりとりにいれます", "ex2_cn": "把垃圾掃進畚箕裡。"},
            {"word": "つめきり", "kanji": "爪切り", "meaning": "指甲剪 (Nail clipper)", "ex1_kanji": "爪切りで爪を切ります。", "ex1_kana": "つめきりでつめをきります", "ex1_cn": "用指甲剪剪指甲。", "ex2_kanji": "小さな爪切りを持ち歩きます。", "ex2_kana": "ちいさなつめきりをもちあるきます", "ex2_cn": "隨身攜帶小指甲剪。"},
            {"word": "たいおんけい", "kanji": "体温計", "meaning": "體溫計 (Thermometer)", "ex1_kanji": "体温計で熱を測ります。", "ex1_kana": "たいおんけいでねつをはかります", "ex1_cn": "用體溫計量體溫。", "ex2_kanji": "新しい体温計を買いました。", "ex2_kana": "あたらしいたいおんけいをかいました", "ex2_cn": "買了一支新體溫計。"},
            {"word": "くるま", "kanji": "車", "meaning": "汽車 (Car)", "ex1_kanji": "週末に車でドライブをします。", "ex1_kana": "しゅうまつにくるまでどらいぶをします", "ex1_cn": "週末開車去兜風。", "ex2_kanji": "赤い車を運転します。", "ex2_kana": "あかいくるまをうんてんします", "ex2_cn": "開紅色的車子。"},
            {"word": "でんしゃ", "kanji": "電車", "meaning": "電車、火車 (Train)", "ex1_kanji": "毎朝電車で会社へ行きます。", "ex1_kana": "まいあさでんしゃでかいしゃへいきます", "ex1_cn": "每天早上坐電車去公司。", "ex2_kanji": "終電の電車に間に合います。", "ex2_kana": "しゅうでんのでんしゃにまにあいます", "ex2_cn": "趕上了末班電車。"},
            {"word": "バス", "kanji": "バス", "meaning": "公車、巴士 (Bus)", "ex1_kanji": "停留所でバスを待ちます。", "ex1_kana": "ていりゅうじょでばすをまちます", "ex1_cn": "在公車站牌等公車。", "ex2_kanji": "バスに乗って街へ行きます。", "ex2_kana": "ばすにのってまちへいきます", "ex2_cn": "搭公車去市區。"},
            {"word": "じてんしゃ", "kanji": "自転車", "meaning": "腳踏車、單車 (Bicycle)", "ex1_kanji": "自転車で学校に通います。", "ex1_kana": "じてんしゃでがっこうにかよいます", "ex1_cn": "騎腳踏車上學。", "ex2_kanji": "新しい自転車を買いました。", "ex2_kana": "あたらしいじてんしゃをかいました", "ex2_cn": "買了一輛新腳踏車。"},
            {"word": "ちかてつ", "kanji": "地下鉄", "meaning": "地鐵 (Subway)", "ex1_kanji": "地下鉄に乗って移動します。", "ex1_kana": "ちかてつにのっていどうします", "ex1_cn": "搭乘地鐵移動。", "ex2_kanji": "東京の地下鉄は便利です。", "ex2_kana": "とうきょうのちかてつはべんりです", "ex2_cn": "東京的地鐵很方便。"},
            {"word": "ひこうき", "kanji": "飛行機", "meaning": "飛機 (Airplane)", "ex1_kanji": "飛行機で日本へ旅行します。", "ex1_kana": "ひこうきでにほんにりょこうします", "ex1_cn": "坐飛機去日本旅行。", "ex2_kanji": "空を飛ぶ飛行機を見ます。", "ex2_kana": "そらをとぶひこうきをみます", "ex2_cn": "看飛在空中的飛機。"},
            {"word": "しんかんせん", "kanji": "新幹線", "meaning": "新幹線 (Shinkansen / Bullet train)", "ex1_kanji": "新幹線はとても速いです。", "ex1_kana": "しんかんせんはとてもはやいです", "ex1_cn": "新幹線非常快。", "ex2_kanji": "新幹線の切符を予約します。", "ex2_kana": "しんかんせんのきっぷをよやくします", "ex2_cn": "預約新幹線車票。"},
            {"word": "タクシー", "kanji": "タクシー", "meaning": "計程車 (Taxi)", "ex1_kanji": "雨なのでタクシーを拾います。", "ex1_kana": "あめなのでたくしーをひろいます", "ex1_cn": "因為下雨所以攔計程車。", "ex2_kanji": "ホテルまでタクシーに乗ります。", "ex2_kana": "ほてるまでたくしーにのります", "ex2_cn": "搭計程車到飯店。"},
            {"word": "バイク", "kanji": "バイク", "meaning": "機車、摩托車 (Motorcycle)", "ex1_kanji": "バイクで通勤する人が多いです。", "ex1_kana": "ばいくでつうきんするひとがおおいです", "ex1_cn": "騎機車通勤的人很多。", "ex2_kanji": "ヘルメットをかぶってバイクに乗ります。", "ex2_kana": "へるめっとをかぶってばいくにのります", "ex2_cn": "戴上安全帽騎機車。"},
            {"word": "ふね", "kanji": "船", "meaning": "船 (Ship / Boat)", "ex1_kanji": "大きな船で海を渡ります。", "ex1_kana": "おおきなふねでうみをわたります", "ex1_cn": "搭乘大船橫渡大海。", "ex2_kanji": "港に船がたくさん停まっています。", "ex2_kana": "みなとにたくさんのふねがとまっています", "ex2_cn": "港口停泊了許多船隻。"},
            {"word": "オートバイ", "kanji": "自動二輪", "meaning": "重機、摩托車 (Motorcycle)", "ex1_kanji": "オートバイでツーリングをします。", "ex1_kana": "おーとばいでつーりんぐをします", "ex1_cn": "騎重機進行長途旅遊。", "ex2_kanji": "かっこいいオートバイですね。", "ex2_kana": "かっこいいおーとばいですね", "ex2_cn": "好帥的重機呢。"},
            {"word": "こうそくバス", "kanji": "高速バス", "meaning": "高速巴士、長途客運 (Highway bus)", "ex1_kanji": "高速バスで遠くへ行きます。", "ex1_kana": "こうそくばすでとおくへいきます", "ex1_cn": "搭高速巴士去遠方。", "ex2_kanji": "夜行の高速バスを予約します。", "ex2_kana": "やこうのこうそくばすをよやくします", "ex2_cn": "預約夜間高速巴士。"},
            {"word": "ロープウェー", "kanji": "索道", "meaning": "纜車 (Cable car / Ropeway)", "ex1_kanji": "ロープウェーで山頂に登ります。", "ex1_kana": "ろーぷうぇーでさんちょうにのぼります", "ex1_cn": "搭乘纜車登上山頂。", "ex2_kanji": "ロープウェーから景色を一望します。", "ex2_kana": "ろーぷうぇーからけしきをいちぼうします", "ex2_cn": "從纜車上一覽美景。"},
            {"word": "ヘリコプター", "kanji": "直升機", "meaning": "直升機 (Helicopter)", "ex1_kanji": "ヘリコプターが空を飛んでいます。", "ex1_kana": "へりこぷたーがそらをとんでいます", "ex1_cn": "直升機在空中飛翔。", "ex2_kanji": "救助用のヘリコプターが出動します。", "ex2_kana": "きゅうじょようのへりこぷたーがしゅつどうします", "ex2_cn": "救援用直升機出動。"},
            {"word": "パトカー", "kanji": "巡邏車", "meaning": "警車、巡邏車 (Police car)", "ex1_kanji": "パトカーがサイレンを鳴らします。", "ex1_kana": "ぱとかーがさいれんをならします", "ex1_cn": "警車鳴響警笛。", "ex2_kanji": "街をパトカーが巡回しています。", "ex2_kana": "まちをぱとかーがじゅんかいしています", "ex2_cn": "警車正在街上巡邏。"}
        ]

    def init_nature_data(self):
        self.nature_data = [
            {"word": "てんき", "kanji": "天気", "meaning": "天氣 (Weather)", "ex1_kanji": "今日の天気はとても良いです。", "ex1_kana": "きょうのてんきはとてもよいです", "ex1_cn": "今天的天氣非常好。", "ex2_kanji": "天気が変わります。", "ex2_kana": "てんきがかわります", "ex2_cn": "天氣變化了。"},
            {"word": "あめ", "kanji": "雨", "meaning": "雨 (Rain)", "ex1_kanji": "外で雨が降っています。", "ex1_kana": "そとであめがふっています", "ex1_cn": "外面正在下雨。", "ex2_kanji": "雨の日は家にいます。", "ex2_kana": "あめのひはいえにいます", "ex2_cn": "下雨天待在家裡。"},
            {"word": "ゆき", "kanji": "雪", "meaning": "雪 (Snow)", "ex1_kanji": "冬に雪が降ります。", "ex1_kana": "ふゆにゆきがふります", "ex1_cn": "冬天會下雪。", "ex2_kanji": "雪景色が綺麗です。", "ex2_kana": "ゆきげしきがきれいです", "ex2_cn": "雪景很漂亮。"},
            {"word": "かぜ", "kanji": "風", "meaning": "風 (Wind)", "ex1_kanji": "強い風が吹いています。", "ex1_kana": "つよいかぜがふいています", "ex1_cn": "正吹著強風。", "ex2_kanji": "風が涼しいです。", "ex2_kana": "かぜがすずしいです", "ex2_cn": "風很涼爽。"},
            {"word": "はれ", "kanji": "晴れ", "meaning": "晴天、晴朗 (Sunny / Clear)", "ex1_kanji": "明日は晴れでしょう。", "ex1_kana": "あしたははれでしょう", "ex1_cn": "明天應該會是晴天吧。", "ex2_kanji": "晴れの日に散歩します。", "ex2_kana": "はれのひにさんぽします", "ex2_cn": "在晴天時散步。"},
            {"word": "くもり", "kanji": "曇り", "meaning": "陰天 (Cloudy)", "ex1_kanji": "空が曇りになりました。", "ex1_kana": "そらがくもりになりました", "ex1_cn": "天空變陰天了。", "ex2_kanji": "今日は曇りの天気です。", "ex2_kana": "きょうはくもりのてんきです", "ex2_cn": "今天是陰天。"},
            {"word": "あつい", "kanji": "暑い", "meaning": "熱 (Hot)", "ex1_kanji": "夏の日はとても暑いです。", "ex1_kana": "なつのひはとてもあついです", "ex1_cn": "夏天的日子非常熱。", "ex2_kanji": "部屋の中が暑いです。", "ex2_kana": "へやのなかがあついです", "ex2_cn": "房間裡面很熱。"},
            {"word": "さむい", "kanji": "寒い", "meaning": "冷 (Cold)", "ex1_kanji": "冬の朝は寒いです。", "ex1_kana": "ふゆのあさはさむいです", "ex1_cn": "冬天的早晨很冷。", "ex2_kanji": "外は風が吹いて寒いです。", "ex2_kana": "そとはかぜがふいてさむいです", "ex2_cn": "外面吹著風很冷。"},
            {"word": "はる", "kanji": "春", "meaning": "春季 (Spring)", "ex1_kanji": "春に桜が咲きます。", "ex1_kana": "はるにさくらがさきます", "ex1_cn": "春天櫻花盛開。", "ex2_kanji": "春の季節が好きです。", "ex2_kana": "はるのきせつがすきです", "ex2_cn": "喜歡春天的季節。"},
            {"word": "なつ", "kanji": "夏", "meaning": "夏季 (Summer)", "ex1_kanji": "夏に海へ行きます。", "ex1_kana": "なつにうみへいきます", "ex1_cn": "夏天要去海邊。", "ex2_kanji": "夏休みが楽しみです。", "ex2_kana": "なつやすみがたのしみです", "ex2_cn": "很期待暑假。"},
            {"word": "あき", "kanji": "秋", "meaning": "秋季 (Autumn / Fall)", "ex1_kanji": "秋に紅葉を見ます。", "ex1_kana": "あきにこうようをみます", "ex1_cn": "秋天看紅葉。", "ex2_kanji": "秋の風が心地よいです。", "ex2_kana": "あきのかぜがここちよいです", "ex2_cn": "秋天的風很舒服。"},
            {"word": "ふゆ", "kanji": "冬", "meaning": "冬季 (Winter)", "ex1_kanji": "冬になると寒くなります。", "ex1_kana": "ふゆになるとさむくなります", "ex1_cn": "一到冬天就會變冷。", "ex2_kanji": "冬にスキーをします。", "ex2_kana": "ふゆにすきーをします", "ex2_cn": "冬天會滑雪。"},
            {"word": "やま", "kanji": "山", "meaning": "山 (Mountain)", "ex1_kanji": "週末に山に登ります。", "ex1_kana": "しゅうまつにやまにのぼります", "ex1_cn": "週末去爬山。", "ex2_kanji": "高い山が見えます。", "ex2_kana": "たかいやまがみえます", "ex2_cn": "看得見高山。"},
            {"word": "かわ", "kanji": "川", "meaning": "河川 (River)", "ex1_kanji": "川の水が冷たいです。", "ex1_kana": "かわのみずがつめたいです", "ex1_cn": "河水很冰涼。", "ex2_kanji": "川沿いを散歩します。", "ex2_kana": "かわぞいをさんぽします", "ex2_cn": "沿着河邊散步。"},
            {"word": "うみ", "kanji": "海", "meaning": "海 (Sea)", "ex1_kanji": "夏に海で泳ぎます。", "ex1_kana": "なつにうみでおよぎます", "ex1_cn": "夏天在海里游泳。", "ex2_kanji": "青い海が美しいです。", "ex2_kana": "あおいうみがうつくしいです", "ex2_cn": "蔚藍的大海非常美麗。"},
            {"word": "ほし", "kanji": "星", "meaning": "星星 (Star)", "ex1_kanji": "夜空に星が輝いています。", "ex1_kana": "よぞらにほしがかがやいています", "ex1_cn": "夜空中星星在閃耀。", "ex2_kanji": "流れ星を見ました。", "ex2_kana": "ながれぼしをみました", "ex2_cn": "我看到了流星。"},
            {"word": "つき", "kanji": "月", "meaning": "月亮 (Moon)", "ex1_kanji": "今夜の月はとても明るいです。", "ex1_kana": "こんやのつきはとてもあかるいです", "ex1_cn": "今晚的月亮非常明亮。", "ex2_kanji": "月が綺麗ですね。", "ex2_kana": "つきがきれいですね", "ex2_cn": "月色真美呢。"},
            {"word": "そら", "kanji": "空", "meaning": "天空 (Sky)", "ex1_kanji": "青い空に雲が浮かんでいます。", "ex1_kana": "あおいそらにくもがうかんんでいます", "ex1_cn": "藍色天空上飄著雲朵。", "ex2_kanji": "夕方の空が赤いです。", "ex2_kana": "ゆうがたのそらがあかいです", "ex2_cn": "傍晚的天空是紅色的。"},
            {"word": "にじ", "kanji": "虹", "meaning": "彩虹 (Rainbow)", "ex1_kanji": "雨の後に虹が出ました。", "ex1_kana": "あめのあとににじがでました", "ex1_cn": "雨後出現了彩虹。", "ex2_kanji": "空に大きな虹が見えます。", "ex2_kana": "そらにおおきなにじがみえます", "ex2_cn": "天空看得見巨大的彩虹。"},
            {"word": "もり", "kanji": "森", "meaning": "森林 (Forest)", "ex1_kanji": "森の中を散歩します。", "ex1_kana": "もりのなかをさんぽします", "ex1_cn": "在森林中散步。", "ex2_kanji": "森にたくさんの木があります。", "ex2_kana": "もりにたくさんのきがあります", "ex2_cn": "森林裡有很多樹木。"},
            {"word": "はな", "kanji": "花", "meaning": "花 (Flower)", "ex1_kanji": "庭に綺麗な花が咲いています。", "ex1_kana": "にわにきれいなはながさいています", "ex1_cn": "庭院裡開著美麗的花朵。", "ex2_kanji": "赤い花が好きです。", "ex2_kana": "あかいはながすきです", "ex2_cn": "我喜歡紅色的花。"},
            {"word": "くも", "kanji": "雲", "meaning": "雲 (Cloud)", "ex1_kanji": "空に白い雲が見えます。", "ex1_kana": "そらにしろいくもがみえます", "ex1_cn": "天空看得見白雲。", "ex2_kanji": "雲が多くて日が隠れました。", "ex2_kana": "くもがおおくてひがかくれました", "ex2_cn": "雲很多把太陽遮住了。"},
            {"word": "たいよう", "kanji": "太陽", "meaning": "太陽 (Sun)", "ex1_kanji": "太陽が明るく輝いています。", "ex1_kana": "たいようがあかるくかがやいています", "ex1_cn": "太陽明亮地閃耀著。", "ex2_kanji": "太陽が沈みます。", "ex2_kana": "たいようがしずみます", "ex2_cn": "太陽下山了。"},
            {"word": "いけ", "kanji": "池", "meaning": "池塘 (Pond)", "ex1_kanji": "池に魚が泳いでいます。", "ex1_kana": "いけにさかながおよいでいます", "ex1_cn": "池塘裡有魚兒在游泳。", "ex2_kanji": "公園の池は広いです。", "ex2_kana": "こうえんのいけはひろいです", "ex2_cn": "公園的池塘很寬敞。"},
            {"word": "くさ", "kanji": "草", "meaning": "草 (Grass)", "ex1_kanji": "庭の草を刈ります。", "ex1_kana": "にわのくさをかります", "ex1_cn": "修剪庭院的草。", "ex2_kanji": "緑の草が茂っています。", "ex2_kana": "みどりのくすがしげっています", "ex2_cn": "綠色的草很茂盛。"},
            {"word": "かみなり", "kanji": "雷", "meaning": "雷、閃電 (Thunder)", "ex1_kanji": "雷が鳴っています。", "ex1_kana": "かみなりがなっています", "ex1_cn": "雷聲大作 / 正在打雷。", "ex2_kanji": "雷が怖いです。", "ex2_kana": "かみなりがこわいです", "ex2_cn": "我覺得打雷很可怕。"},
            {"word": "きり", "kanji": "霧", "meaning": "霧 (Fog)", "ex1_kanji": "朝に霧が出ました。", "ex1_kana": "あさにきりがでました", "ex1_cn": "早晨起霧了。", "ex2_kanji": "霧で前が見えません。", "ex2_kana": "きりでまえがみえません", "ex2_cn": "因為起霧看不見前方。"},
            {"word": "あらし", "kanji": "嵐", "meaning": "暴風雨、風暴 (Storm)", "ex1_kanji": "嵐が近づいています。", "ex1_kana": "あらしがちかづいています", "ex1_cn": "風暴正在靠近。", "ex2_kanji": "嵐で木が倒れました。", "ex2_kana": "あらしできがたおれました", "ex2_cn": "風暴吹倒了樹木。"},
            {"word": "ほしぞら", "kanji": "星空", "meaning": "星空 (Starry sky)", "ex1_kanji": "今夜は綺麗な星空です。", "ex1_kana": "こんやはきれいなほしぞらです", "ex1_cn": "今晚是美麗的星空。", "ex2_kanji": "星空を見上げて願い事をします。", "ex2_kana": "ほしぞらをみあげてねがいごとをします", "ex2_cn": "仰望星空許願。"},
            {"word": "なみ", "kanji": "波", "meaning": "波浪、浪 (Wave)", "ex1_kanji": "海の波が高いです。", "ex1_kana": "うみのなみがたかいです", "ex1_cn": "海浪很高。", "ex2_kanji": "波の音が聞こえます。", "ex2_kana": "なみのおとがきこえます", "ex2_cn": "聽得到海浪的聲音。"},
            {"word": "すなはま", "kanji": "砂浜", "meaning": "沙灘 (Sandy beach)", "ex1_kanji": "砂浜を歩きます。", "ex1_kana": "すなはまをあるきます", "ex1_cn": "在沙灘上散步。", "ex2_kanji": "白い砂浜が続きます。", "ex2_kana": "しろいすなはまがつづきます", "ex2_cn": "白色的沙灘綿延不斷。"},
            {"word": "たき", "kanji": "滝", "meaning": "瀑布 (Waterfall)", "ex1_kanji": "山の中に大きな滝があります。", "ex1_kana": "やまのなかにおおきなたきがあります", "ex1_cn": "山裡有大瀑布。", "ex2_kanji": "滝の水が冷たいです。", "ex2_kana": "たきのみずがつめたいです", "ex2_cn": "瀑布的水很冰涼。"},
            {"word": "たに", "kanji": "谷", "meaning": "山谷 (Valley)", "ex1_kanji": "深い谷を通ります。", "ex1_kana": "ふかいたにをとおります", "ex1_cn": "通過深谷。", "ex2_kanji": "谷川の水が綺麗です。", "ex2_kana": "たにがわのみずがきれいです", "ex2_cn": "谷川的水很清澈。"},
            {"word": "どうくつ", "kanji": "洞窟", "meaning": "洞穴、洞窟 (Cave)", "ex1_kanji": "暗い洞窟を探検します。", "ex1_kana": "くらいどうくつをたんけんします", "ex1_cn": "探索黑暗的洞窟。", "ex2_kanji": "洞窟の中に水があります。", "ex2_kana": "どうくつのなかにみずがあります", "ex2_cn": "洞窟裡面有水。"},
            {"word": "こおり", "kanji": "氷", "meaning": "冰 (Ice)", "ex1_kanji": "水が凍って氷になりました。", "ex1_kana": "みずがこおってこおりになりました", "ex1_cn": "水結成了冰。", "ex2_kanji": "飲み物に氷を入れます。", "ex2_kana": "のみものにこおりをいれます", "ex2_cn": "飲料裡加冰塊。"}
        ]

    def init_subject_data(self):
        self.subject_data = [
            {"word": "すうがく", "kanji": "数学", "meaning": "數學 (Mathematics)", "ex1_kanji": "私は数学の勉強が好きです。", "ex1_kana": "わたしはすうがくのべんきょうがすきです", "ex1_cn": "我喜歡學習數學。", "ex2_kanji": "数学の問題を解きます。", "ex2_kana": "すうがくのもんだいをときます", "ex2_cn": "解答數學問題。"},
            {"word": "えいご", "kanji": "英語", "meaning": "英語 (English)", "ex1_kanji": "毎日英語を話します。", "ex1_kana": "まいにちえいごをはなします", "ex1_cn": "每天說英語。", "ex2_kanji": "英語の辞書を買いました。", "ex2_kana": "えいごのじしょをかいました", "ex2_cn": "買了一本英語辭典。"},
            {"word": "こくご", "kanji": "国語", "meaning": "國語 (Japanese)", "ex1_kanji": "国語の授業を受けます。", "ex1_kana": "こくごのじゅぎょうをうけます", "ex1_cn": "上國語課。", "ex2_kanji": "国語の本を読みます。", "ex2_kana": "こくごのほんをよみます", "ex2_cn": "讀國語課本。"},
            {"word": "りか", "kanji": "理科", "meaning": "理科、科學 (Science)", "ex1_kanji": "理科の実験をします。", "ex1_kana": "りかのじっけんをします", "ex1_cn": "做理科實驗。", "ex2_kanji": "理科室へ行きます。", "ex2_kana": "りかしつへいきます", "ex2_cn": "去理科教室。"},
            {"word": "れきし", "kanji": "歴史", "meaning": "歷史 (History)", "ex1_kanji": "歴史の勉強が面白いです。", "ex1_kana": "れきしのべんきょうがおもしろいです", "ex1_cn": "歷史學習很有趣。", "ex2_kanji": "古い歴史を調べます。", "ex2_kana": "ふるいれきしをしらべます", "ex2_cn": "調查悠久的歷史。"},
            {"word": "ちり", "kanji": "地理", "meaning": "地理 (Geography)", "ex1_kanji": "地理の地図を見ます。", "ex1_kana": "ちりのちずをみます", "ex1_cn": "看地理地圖。", "ex2_kanji": "世界の地理を学びます。", "ex2_kana": "せかいのちりをまなびます", "ex2_cn": "學習世界地理。"},
            {"word": "おんがく", "kanji": "音楽", "meaning": "音樂 (Music)", "ex1_kanji": "音楽を聞くのが好きです。", "ex1_kana": "おんがくをきくのがすきです", "ex1_cn": "喜歡聽音樂。", "ex2_kanji": "音楽の歌を歌います。", "ex2_kana": "おんがくのうたをうたいます", "ex2_cn": "唱音樂課的歌。"},
            {"word": "びじゅつ", "kanji": "美術", "meaning": "美術 (Art)", "ex1_kanji": "美術の時間に絵を描きます。", "ex1_kana": "びじゅつのじかんにえをかきます", "ex1_cn": "在美術課上畫畫。", "ex2_kanji": "美術の展覧会に行きます。", "ex2_kana": "びじゅつのてんらんかいにいきます", "ex2_cn": "去看美術展覽會。"},
            {"word": "たいいく", "kanji": "体育", "meaning": "體育 (Physical Education)", "ex1_kanji": "体育の授業で走ります。", "ex1_kana": "たいいくのじゅぎょうではしります", "ex1_cn": "在體育課跑步。", "ex2_kanji": "体育館でバスケをします。", "ex2_kana": "たいいくかんでばすけをします", "ex2_cn": "在體育館打籃球。"},
            {"word": "ぶつり", "kanji": "物理", "meaning": "物理 (Physics)", "ex1_kanji": "物理の法則を学びます。", "ex1_kana": "ぶつりのほうそくをまなびます", "ex1_cn": "學習物理定律。", "ex2_kanji": "物理の計算は難しいです。", "ex2_kana": "ぶつりのけいさんはむずかしいです", "ex2_cn": "物理的計算很難。"},
            {"word": "かがく", "kanji": "化学", "meaning": "化學 (Chemistry)", "ex1_kanji": "化学の薬を混ぜます。", "ex1_kana": "かがくのくすりをまぜます", "ex1_cn": "混合化學藥劑。", "ex2_kanji": "化学の元素を覚えます。", "ex2_kana": "かがくのげんそをおぼえます", "ex2_cn": "背誦化學元素。"},
            {"word": "せいぶつ", "kanji": "生物", "meaning": "生物學 (Biology)", "ex1_kanji": "生物の観察をします。", "ex1_kana": "せいぶつのかんさつをします", "ex1_cn": "進行生物觀察。", "ex2_kanji": "植物の生物を勉強します。", "ex2_kana": "しょくぶつのせいぶつをべんきょうします", "ex2_cn": "學習植物生物學。"},
            {"word": "しゃかい", "kanji": "社会", "meaning": "社會 (Social Studies)", "ex1_kanji": "社会のテストを受けます。", "ex1_kana": "しゃかいのてすとをうけます", "ex1_cn": "參加社會科考試。", "ex2_kanji": "社会の教科書を開きます。", "ex2_kana": "しゃかいのきょうかしょをひらきます", "ex2_cn": "翻開社會課本。"},
            {"word": "こうがく", "kanji": "工学", "meaning": "工程學、工學 (Engineering)", "ex1_kanji": "大学で工学を専攻します。", "ex1_kana": "だいがくでこうがくをせんこうします", "ex1_cn": "在大學主修工學。", "ex2_kanji": "新しい工学技術を発明します。", "ex2_kana": "あたらしいこうがくぎじゅつをはつめいします", "ex2_cn": "發明新的工程技術。"},
            {"word": "けいざい", "kanji": "経済", "meaning": "經濟學 (Economics)", "ex1_kanji": "経済の仕組みを理解します。", "ex1_kana": "けいざいのしくみをりかいします", "ex1_cn": "理解經濟的運作機制。", "ex2_kanji": "経済の本を読んでいます。", "ex2_kana": "けいざいのほんをよんでいます", "ex2_cn": "正在讀經濟學的書。"},
            {"word": "せいじ", "kanji": "政治", "meaning": "政治學 (Politics)", "ex1_kanji": "政治のニュースを見ます。", "ex1_kana": "せいじのにゅーすをみます", "ex1_cn": "看政治新聞。", "ex2_kanji": "政治のシステムを学びます。", "ex2_kana": "せいじのしすてむをまなびます", "ex2_cn": "學習政治系統。"},
            {"word": "てつがく", "kanji": "哲学", "meaning": "哲學 (Philosophy)", "ex1_kanji": "哲学の考え方は深いです。", "ex1_kana": "てつがくのかんがえかたはふかいです", "ex1_cn": "哲學的思考方式很深奧。", "ex2_kanji": "古代の哲学を研究します。", "ex2_kana": "こだいのてつがくをけんきゅうします", "ex2_cn": "研究古代哲學。"},
            {"word": "ぶんがく", "kanji": "文学", "meaning": "文學 (Literature)", "ex1_kanji": "日本文学を読みます。", "ex1_kana": "にほんぶんがくをよみます", "ex1_cn": "閱讀日本文學。", "ex2_kanji": "文学賞を受賞しました。", "ex2_kana": "ぶんがくしょうをじゅしょうしました", "ex2_cn": "獲得了文學獎。"},
            {"word": "じょうほう", "kanji": "情報", "meaning": "資訊、電腦科學 (Information Technology)", "ex1_kanji": "情報の授業でプログラミングをします。", "ex1_kana": "じょうほうのじゅぎょうでぷろぐらみんぐをします", "ex1_cn": "在資訊課上寫程式。", "ex2_kanji": "パソコンで情報を集めます。", "ex2_kana": "ぱそこんでじょうほうをあつめます", "ex2_cn": "用電腦蒐集資訊。"},
            {"word": "かていか", "kanji": "家庭科", "meaning": "家政課 (Home Economics)", "ex1_kanji": "家庭科で料理を作ります。", "ex1_kana": "かていかでりょうりをつくります", "ex1_cn": "在家政課做料理。", "ex2_kanji": "家庭科の宿題で服を縫います。", "ex2_kana": "かていかのしゅくだいでふくをぬいます", "ex2_cn": "做家政作業縫衣服。"},
            {"word": "しょどう", "kanji": "書道", "meaning": "書法 (Calligraphy)", "ex1_kanji": "書道で漢字を書きます。", "ex1_kana": "しょどうでかんじをかきます", "ex1_cn": "用書法寫漢字。", "ex2_kanji": "書道の展覧会に出品します。", "ex2_kana": "しょどうのてんらんかいにしゅっぴんします", "ex2_cn": "參加書法展覽會。"},
            {"word": "かんご", "kanji": "看護", "meaning": "護理學 (Nursing)", "ex1_kanji": "看護の勉強は忙しいです。", "ex1_kana": "かんごのべんきょうはいそがしいです", "ex1_cn": "護理學的學習很忙碌。", "ex2_kanji": "将来は看護師になります。", "ex2_kana": "しょうらいはかんごしになります", "ex2_cn": "將來要成為護理師。"},
            {"word": "ぎじゅつ", "kanji": "技術", "meaning": "技術課、工藝 (Technology)", "ex1_kanji": "技術の時間に木工をします。", "ex1_kana": "ぎじゅつのじかんにもっこうをします", "ex1_cn": "在技術課做木工。", "ex2_kanji": "新しい技術を学びます。", "ex2_kana": "あたらしいぎじゅつをまなびます", "ex2_cn": "學習新技術。"},
            {"word": "ちがく", "kanji": "地学", "meaning": "地質學、地球科學 (Earth Science)", "ex1_kanji": "地学で岩石を調べます。", "ex1_kana": "ちがくでがんせきをしらべます", "ex1_cn": "在地科課調查岩石。", "ex2_kanji": "地学の授業で星を観察します。", "ex2_kana": "ちがくのじゅぎょうでほしをかんさつします", "ex2_cn": "在地科課觀察星星。"},
            {"word": "ほうがく", "kanji": "法学", "meaning": "法學 (Law)", "ex1_kanji": "大学で法学を勉強します。", "ex1_kana": "だいがくでほうがくをべんきょうします", "ex1_cn": "在大學學習法學。", "ex2_kanji": "法律の本を読みます。", "ex2_kana": "ほうりつのほんをよみます", "ex2_cn": "閱讀法律書籍。"}
        ]

    def init_family_data(self):
        self.family_data = [
            {"word": "そふ", "kanji": "祖父", "meaning": "爺爺、外公 【對自己人的稱呼／自稱】", "ex1_kanji": "私の祖父は元気です。", "ex1_kana": "わたしのそふはげんきです", "ex1_cn": "我爺爺很有精神。", "ex2_kanji": "祖父から時計をもらいました。", "ex2_kana": "そふからとけいをもらいました", "ex2_cn": "從爺爺那裡收到了手錶。"},
            {"word": "おじいさん", "kanji": "お爺さん", "meaning": "爺爺、外公 【對別人的稱呼／尊稱】", "ex1_kanji": "おじいさんはお元気ですか。", "ex1_kana": "おじいさんはおげんきですか", "ex1_cn": "您的爺爺身體好嗎？", "ex2_kanji": "田中さんのおじいさんに会いました。", "ex2_kana": "たなかさんのおじいさんにあいました", "ex2_cn": "遇到了田中先生的爺爺。"},
            {"word": "そぼ", "kanji": "祖母", "meaning": "奶奶、外婆 【對自己人的稱呼／自稱】", "ex1_kanji": "私の祖母は料理が上手です。", "ex1_kana": "わたしのそぼはりょうりがじょうずです", "ex1_cn": "我奶奶很擅長做菜。", "ex2_kanji": "祖母に電話をかけます。", "ex2_kana": "そぼにでんわをかけます", "ex2_cn": "給奶奶打電話。"},
            {"word": "おばあさん", "kanji": "お婆さん", "meaning": "奶奶、外婆 【對別人の稱呼／尊稱】", "ex1_kanji": "おばあさんに手紙を書きます。", "ex1_kana": "おばあさんにてがみをかきます", "ex1_cn": "給奶奶寫信。", "ex2_kanji": "佐藤さんのおばあさんは親切です。", "ex2_kana": "さとうさんのおばあさんはしんせつです", "ex2_cn": "佐藤同學的奶奶很親切。"},
            {"word": "ちち", "kanji": "父", "meaning": "父親 【對自己人的稱呼／自稱】", "ex1_kanji": "父は会社員です。", "ex1_kana": "ちちはかいしゃいんです", "ex1_cn": "我父親是公司職員。", "ex2_kanji": "父と一緒にドライブに行きます。", "ex2_kana": "ちちといっしょにどらいぶにいきます", "ex2_cn": "我和父親一起去兜風。"},
            {"word": "おとうさん", "kanji": "お父さん", "meaning": "父親 【對別人的稱呼／尊稱】", "ex1_kanji": "お父さんのお仕事は何ですか。", "ex1_kana": "おとうさんのおしごとはなんですか", "ex1_cn": "您父親的工作是什麼？", "ex2_kanji": "お父さんによろしくお伝えください。", "ex2_kana": "おとうさんによろしくおつたえください", "ex2_cn": "請代我向您父親問好。"},
            {"word": "はは", "kanji": "母", "meaning": "母親 【對自己人的稱呼／自稱】", "ex1_kanji": "母は花が好きです。", "ex1_kana": "ははははながすきです", "ex1_cn": "我母親喜歡花。", "ex2_kanji": "母にプレゼントをあげます。", "ex2_kana": "ははにぷれぜんとをあげます", "ex2_cn": "送禮物給母親。"},
            {"word": "おかあさん", "kanji": "お母さん", "meaning": "母親 【對別人的稱呼／尊稱】", "ex1_kanji": "お母さんは料理が上手ですね。", "ex1_kana": "おかあさんはりょうりがじょうずですね", "ex1_cn": "您母親做菜很棒呢。", "ex2_kanji": "お母さんと買い物をします。", "ex2_kana": "おかあさんとかいものをします", "ex2_cn": "和媽媽一起去買東西。"},
            {"word": "おじ", "kanji": "叔父", "meaning": "叔伯、舅舅 【對自己人的稱呼／自稱】", "ex1_kanji": "私の叔父は東京に住んでいます。", "ex1_kana": "わたしのおじはとうきょうにすんでいます", "ex1_cn": "我的叔叔住在東京。", "ex2_kanji": "叔父から本をもらいました。", "ex2_kana": "おじからほんをもらいました", "ex2_cn": "從叔叔那裡收到了書。"},
            {"word": "おじさん", "kanji": "おじさん", "meaning": "叔伯、舅舅 【對別人的稱呼／尊稱】", "ex1_kanji": "山田さんのおじさんは医者です。", "ex1_kana": "やまださんのおじさんはいしゃです", "ex1_cn": "山田先生的叔叔是醫生。", "ex2_kanji": "おじさんによろしくね。", "ex2_kana": "おじさんによろしくね", "ex2_cn": "向叔叔問好喔。"},
            {"word": "おば", "kanji": "叔母", "meaning": "姑姑、阿姨、嬸嬸 【對自己人的稱呼／自稱】", "ex1_kanji": "叔母は看護師です。", "ex1_kana": "おばはかんごしです", "ex1_cn": "我阿姨是護理師。", "ex2_kanji": "週末に叔母の家へ行きます。", "ex2_kana": "しゅうまつにおばのいえへいきます", "ex2_cn": "週末要去阿姨家。"},
            {"word": "おばさん", "kanji": "おばさん", "meaning": "姑姑、阿姨、嬸嬸 【對別人的稱呼／尊稱】", "ex1_kanji": "おばさんはお元気ですか。", "ex1_kana": "おばさんはおげんきですか", "ex1_cn": "您阿姨身體好嗎？", "ex2_kanji": "鈴木さんのおばさんに会いました。", "ex2_kana": "すずきさんのおばさんにあいました", "ex2_cn": "遇到了鈴木同學的阿姨。"},
            {"word": "おっと", "kanji": "夫", "meaning": "丈夫 【對自己人的稱呼／自稱】", "ex1_kanji": "夫は今出張中です。", "ex1_kana": "おっとはいましゅっちょうちゅうです", "ex1_cn": "我先生現在出差中。", "ex2_kanji": "夫と買い物に行きます。", "ex2_kana": "おっととかいものにいきます", "ex2_cn": "我和丈夫去買東西。"},
            {"word": "ごしゅじん", "kanji": "ご主人", "meaning": "丈夫 【對別人的稱呼／尊稱】", "ex1_kanji": "ご主人はお元気ですか。", "ex1_kana": "ごしゅじんはおげんきですか", "ex1_cn": "您先生身體好嗎？", "ex2_kanji": "ご主人と一緒に来てください。", "ex2_kana": "ごしゅじんといっしょにきてください", "ex2_cn": "請和您先生一起來。"},
            {"word": "つま", "kanji": "妻", "meaning": "妻子 【對自己人的稱呼／自稱】", "ex1_kanji": "妻は銀行で働いています。", "ex1_kana": "つまはぎんこうではたらいています", "ex1_cn": "我妻子在銀行工作。", "ex2_kanji": "妻に指輪を贈ります。", "ex2_kana": "つまにゆびわをおくります", "ex2_cn": "送戒指給妻子。"},
            {"word": "おくさん", "kanji": "奥さん", "meaning": "妻子 【對別人的稱呼／尊稱】", "ex1_kanji": "奥さんはおきれいですね。", "ex1_kana": "おくさんはおきれいですね", "ex1_cn": "您太太真漂亮呢。", "ex2_kanji": "林さんの奥さんに会いました。", "ex2_kana": "はやしさんのおくさんにあいました", "ex2_cn": "遇到了林先生的太太。"},
            {"word": "あに", "kanji": "兄", "meaning": "哥哥 【對自己人的稱呼／自稱】", "ex1_kanji": "兄は大学生です。", "ex1_kana": "あにはだいがくせいです", "ex1_cn": "我哥哥是大學生。", "ex2_kanji": "兄と一緒にサッカーをします。", "ex2_kana": "あにといっしょにさっかーをします", "ex2_cn": "我和哥哥一起踢足球。"},
            {"word": "おにいさん", "kanji": "お兄さん", "meaning": "哥哥 【對別人的稱呼／尊稱】", "ex1_kanji": "高橋さんのお兄さんは背が高いです。", "ex1_kana": "たかはしさんのおにいさんはせがたかいです", "ex1_cn": "高橋同學的哥哥身材很高大。", "ex2_kanji": "お兄さんは何歳ですか。", "ex2_kana": "おにいさんはなんさいですか", "ex2_cn": "您哥哥幾歲呢？"},
            {"word": "あね", "kanji": "姉", "meaning": "姐姐 【對自己人的稱呼／自稱】", "ex1_kanji": "姉は英語の先生です。", "ex1_kana": "あねはえいごのせんせいです", "ex1_cn": "我姐姐是英文老師。", "ex2_kanji": "姉に服を借ります。", "ex2_kana": "あねにふくをかります", "ex2_cn": "向姐姐借衣服。"},
            {"word": "おねえさん", "kanji": "お姉さん", "meaning": "姐姐 【對別人的稱呼／尊稱】", "ex1_kanji": "お姉さんはピアノが上手ですね。", "ex1_kana": "おねえさんはぴあのがじょうずですね", "ex1_cn": "您姐姐彈鋼琴很厲害呢。", "ex2_kanji": "渡辺さんのお姉さんに会いました。", "ex2_kana": "わたなべさんのおねえさんにあいました", "ex2_cn": "遇到了渡邊同學的姐姐。"},
            {"word": "おとうと", "kanji": "弟", "meaning": "弟弟 【對自己人的稱呼／自稱】", "ex1_kanji": "弟は高校生です。", "ex1_kana": "おとうとはこうこうせいです", "ex1_cn": "我弟弟是高中生。", "ex2_kanji": "弟にゲームを教えます。", "ex2_kana": "おとうとにげーむをおしえます", "ex2_cn": "教弟弟玩遊戲。"},
            {"word": "おとうとさん", "kanji": "弟さん", "meaning": "弟弟 【對別人的稱呼／尊稱】", "ex1_kanji": "弟さんは何年生ですか。", "ex1_kana": "おとうとさんはなんねんせいですか", "ex1_cn": "您弟弟讀幾年級？", "ex2_kanji": "中村さんの弟さんは元気です。", "ex2_kana": "なかむらさんのおとうとさんはげんきです", "ex2_cn": "中村同學的弟弟很有活力。"},
            {"word": "いもうと", "kanji": "妹", "meaning": "妹妹 【對自己人的稱呼／自稱】", "ex1_kanji": "妹は歌が好きです。", "ex1_kana": "いもうとはうたがすきです", "ex1_cn": "我妹妹喜歡唱歌。", "ex2_kanji": "妹と一緒に公園へ行きます。", "ex2_kana": "いもうとといっしょにこうえんへいきます", "ex2_cn": "和妹妹一起去公園。"},
            {"word": "いもうとさん", "kanji": "妹さん", "meaning": "妹妹 【對別人的稱呼／尊稱】", "ex1_kanji": "妹さんは可愛いですね。", "ex1_kana": "いもうとさんはかわいいですね", "ex1_cn": "您妹妹真可愛呢。", "ex2_kanji": "小林さんの妹さんに会いました。", "ex2_kana": "こばやしさんのいもうとさんにあいました", "ex2_cn": "遇到了小林同學的妹妹。"},
            {"word": "むすこ", "kanji": "息子", "meaning": "兒子 【對自己人的稱呼／自稱】", "ex1_kanji": "息子は今年の春に就職しました。", "ex1_kana": "むすこはことしのはるにしゅうしょくしました", "ex1_cn": "我兒子今年春天就業了。", "ex2_kanji": "息子と野球をします。", "ex2_kana": "むすことやきゅうをします", "ex2_cn": "和兒子打棒球。"},
            {"word": "むすこさん", "kanji": "息子さん", "meaning": "兒子 【對別人的稱呼／尊稱】", "ex1_kanji": "息子さんはお元気ですか。", "ex1_kana": "むすこさんはおげんきですか", "ex1_cn": "您兒子近來好嗎？", "ex2_kanji": "加藤さんの息子さんは頭が良いです。", "ex2_kana": "かとうさんのむすこさんはあたまがよいです", "ex2_cn": "加藤先生的兒子很聰明。"},
            {"word": "むすめ", "kanji": "娘", "meaning": "女兒 【對自己人的稱呼／自稱】", "ex1_kanji": "娘は絵を描くのが好きです。", "ex1_kana": "むすめはえをかくのがすきです", "ex1_cn": "我女兒喜歡畫畫。", "ex2_kanji": "娘に新しい靴を買います。", "ex2_kana": "むすめにあたらしいくつをかいます", "ex2_cn": "給女兒買新鞋。"},
            {"word": "むすめさん", "kanji": "娘さん", "meaning": "女兒 【對別人的稱呼／尊稱】", "ex1_kanji": "娘さんは何歳になりましたか。", "ex1_kana": "むすめさんはなんさいになりましたか", "ex1_cn": "您女兒滿幾歲了？", "ex2_kanji": "吉田さんの娘さんは親切です。", "ex2_kana": "よしださんのむすめさんはしんせつです", "ex2_cn": "吉田先生的女兒很親切。"},
            {"word": "まご", "kanji": "孫", "meaning": "孫子、孫女 【對自己人的稱呼／自稱】", "ex1_kanji": "私の孫は小学生です。", "ex1_kana": "わたしのまごはしょうがくせいです", "ex1_cn": "我的孫子是小學生。", "ex2_kanji": "孫と公園で遊びます。", "ex2_kana": "まごとこうえんであそびます", "ex2_cn": "和孫子在公園玩。"},
            {"word": "おまごさん", "kanji": "お孫さん", "meaning": "孫子、孫女 【對別人的稱呼／尊稱】", "ex1_kanji": "お孫さんは何歳ですか。", "ex1_kana": "おまごさんはなんさいですか", "ex1_cn": "您的孫子幾歲呢？", "ex2_kanji": "山田さんのお孫さんに会いました。", "ex2_kana": "やまださんのおまごさんにあいました", "ex2_cn": "遇到了山田先生的孫子。"},
            {"word": "りょうしん", "kanji": "両親", "meaning": "父母、雙親 【對自己人的稱呼／自稱】", "ex1_kanji": "両親と一緒に住んでいます。", "ex1_kana": "りょうしんといっしょにすんでいます", "ex1_cn": "和父母住在一起。", "ex2_kanji": "両親に感謝しています。", "ex2_kana": "りょうしんにかんしゃしています", "ex2_cn": "感謝父母。"},
            {"word": "ごりょうしん", "kanji": "ご両親", "meaning": "父母、雙親 【對別人的稱呼／尊稱】", "ex1_kanji": "ご両親はお元気ですか。", "ex1_kana": "ごりょうしんはおげんきですか", "ex1_cn": "您的父母身體好嗎？", "ex2_kanji": "ご両親に相談してください。", "ex2_kana": "ごりょうしんにそうだんしてください", "ex2_cn": "請和您的父母商量。"},
            {"word": "きょうだい", "kanji": "兄弟", "meaning": "兄弟姊妹 【對自己人的稱呼／自稱】", "ex1_kanji": "私は三人兄弟です。", "ex1_kana": "わたしはさんにんきょうだいです", "ex1_cn": "我們是三兄弟姊妹。", "ex2_kanji": "兄弟と仲が良いです。", "ex2_kana": "きょうだいとなかがよいです", "ex2_cn": "和兄弟姊妹感情很好。"},
            {"word": "ごきょうだい", "kanji": "ご兄弟", "meaning": "兄弟姊妹 【對別人的稱呼／尊稱】", "ex1_kanji": "ご兄弟はいますか。", "ex1_kana": "ごきょうだいはいますか", "ex1_cn": "您有兄弟姊妹嗎？", "ex2_kanji": "ご兄弟と旅行に行きますか。", "ex2_kana": "ごきょうだいとりょこうにいきますか", "ex2_cn": "要和您的兄弟姊妹去旅行嗎？"},
            {"word": "こども", "kanji": "子供", "meaning": "小孩、子女 【對自己人的稱呼／自稱】", "ex1_kanji": "私の子供は二人います。", "ex1_kana": "わたしのこどもはふたりいます", "ex1_cn": "我有兩個小孩。", "ex2_kanji": "子供とアニメを見ます。", "ex2_kana": "こどもとあにめをみます", "ex2_cn": "和孩子一起看動畫。"},
            {"word": "おこさん", "kanji": "お子さん", "meaning": "小孩、子女 【對別人的稱呼／尊稱】", "ex1_kanji": "お子さんはお幾つですか。", "ex1_kana": "おこさんはおいくつですか", "ex1_cn": "您的孩子幾歲了？", "ex2_kanji": "田中さんのお子さんは可愛いです。", "ex2_kana": "たなかさんのおこさんはかわいいです", "ex2_cn": "田中先生的孩子真可愛。"},
            {"word": "しんせき", "kanji": "親戚", "meaning": "親戚 【對自己人的稱呼／自稱】", "ex1_kanji": "親戚の家に行きます。", "ex1_kana": "しんせきのいえにいきます", "ex1_cn": "去親戚家。", "ex2_kanji": "お正月に親戚が集まります。", "ex2_kana": "おしょうがつにしんせきがあつまります", "ex2_cn": "過年時親戚聚在一起。"},
            {"word": "ごしんせき", "kanji": "ご親戚", "meaning": "親戚 【對別人的稱呼／尊稱】", "ex1_kanji": "ご親戚はどちらにいますか。", "ex1_kana": "ごしんせきはどちらにいますか", "ex1_cn": "您的親戚在哪裡呢？", "ex2_kanji": "ご親戚によろしくお伝えください。", "ex2_kana": "ごしんせきによろしくおつたえください", "ex2_cn": "請代我向您的親戚問好。"},
            {"word": "かぞく", "kanji": "家族", "meaning": "家人、家族 【對自己人的稱呼／自稱】", "ex1_kanji": "私の家族は四人です。", "ex1_kana": "わたしのかぞくはよにんです", "ex1_cn": "我一家有四個人。", "ex2_kanji": "家族で旅行に行きます。", "ex2_kana": "かぞくでりょこうにいきます", "ex2_cn": "全家一起去旅行。"},
            {"word": "ごかぞく", "kanji": "ご家族", "meaning": "家人、家族 【對別人的稱呼／尊稱】", "ex1_kanji": "ご家族はお元気ですか。", "ex1_kana": "ごかぞくはおげんきですか", "ex1_cn": "您的家人身體好嗎？", "ex2_kanji": "ご家族によろしくお伝えください。", "ex2_kana": "ごかぞくによろしくおつたえください", "ex2_cn": "請代我向您的家人問好。"}
        ]

    def init_emotion_data(self):
        self.emotion_data = [
            {"word": "うれしい", "kanji": "嬉しい", "meaning": "高興、開心 (Happy / Glad)", "ex1_kanji": "合格の 知らせを 聞いて とても 嬉しいです。", "ex1_kana": "ごうかくのしらせをきいてとてもうれしいです", "ex1_cn": "聽到合格的消息非常高興。", "ex2_kanji": "プレゼントを もらって 嬉しいです。", "ex2_kana": "ぷれぜんとをもらってうれしいです", "ex2_cn": "收到禮物很開心。"},
            {"word": "かなしい", "kanji": "悲しい", "meaning": "悲傷、難過 (Sad)", "ex1_kanji": "大好きな 映画を 見て 悲しくなりました。", "ex1_kana": "だいすきなえいがをみてかなしくなりました", "ex1_cn": "看了最喜歡的電影後感到很悲傷。", "ex2_kanji": "別れは いつも 悲しいです。", "ex2_kana": "わかれはいつもかなしいです", "ex2_cn": "離別總是令人難過的。"},
            {"word": "たのしい", "kanji": "楽しい", "meaning": "快樂、愉快 (Fun / Enjoyable)", "ex1_kanji": "友達と 旅行に 行くのは とても 楽しいです。", "ex1_kana": "ともだちとりょこうにいくのはとてもたのしいです", "ex1_cn": "和朋友去旅行非常快樂。", "ex2_kanji": "日本語の 勉強は 楽しいです。", "ex2_kana": "にほんごのべんきょうはたのしいです", "ex2_cn": "學習日文很有趣／很愉快。"},
            {"word": "さびしい", "kanji": "寂しい", "meaning": "寂寞、孤單 (Lonely)", "ex1_kanji": "一人で 暮らすのは 時々 寂しいです。", "ex1_kana": "ひとりでおくらすのはときどきさびしいです", "ex1_cn": "一個人生活偶爾會感到寂寞。", "ex2_kanji": "友達が 帰って 寂しいです。", "ex2_kana": "ともだちがかえってさびしいです", "ex2_cn": "朋友回去後覺得很孤單。"},
            {"word": "おこる", "kanji": "怒る", "meaning": "發怒、生氣 (Angry)", "ex1_kanji": "約束を 破られて 彼は 激しく 怒りました。", "ex1_kana": "やくそくをやぶられてかれははげしくおこりました", "ex1_cn": "因為被打破約定，他非常生氣。", "ex2_kanji": "理由もなく 怒らないでください。", "ex2_kana": "りゆうもなくおこらないでください", "ex2_cn": "請不要無緣無故生氣。"},
            {"word": "しあわせ", "kanji": "幸せ", "meaning": "幸福 (Happy / Blessed)", "ex1_kanji": "家族と 過ごす 時間が 一番 幸せです。", "ex1_kana": "かぞくとすごすじかんがいちばんしあわせです", "ex1_cn": "和家人共度的時光是最幸福的。", "ex2_kanji": "末永く お幸せに。", "ex2_kana": "すえながくおしあわせに", "ex2_cn": "祝您永遠幸福。"},
            {"word": "つらい", "kanji": "辛い", "meaning": "痛苦、辛苦 (Painful / Tough)", "ex1_kanji": "リハビリの 練習は 大変 つらいです。", "ex1_kana": "りはびりのれんしゅうはたいへんつらいです", "ex1_cn": "復健的練習非常痛苦。", "ex2_kanji": "辛い 練習を 乗り越えます。", "ex2_kana": "つらいれんしゅうをのりこえます", "ex2_cn": "克服艱辛的練習。"},
            {"word": "こわい", "kanji": "怖い", "meaning": "害怕、恐怖 (Scared / Afraid)", "ex1_kanji": "夜の 暗い 道を 一人で 歩くのは 怖いです。", "ex1_kana": "よるのくらいみちをひとりであるくのはこわいです", "ex1_cn": "晚上一個人走黑暗的路很害怕。", "ex2_kanji": "ホラー映画が 怖いです。", "ex2_kana": "ほらーえいががこわいです", "ex2_cn": "覺得恐怖電影很可怕。"},
            {"word": "おどろく", "kanji": "驚く", "meaning": "吃驚、驚訝 (Surprised / Shocked)", "ex1_kanji": "予想外の ニュースに とても 驚きました。", "ex1_kana": "よそうがいのにゅーすにとてもおどろきました", "ex1_cn": "對意料之外的新聞感到非常驚訝。", "ex2_kanji": "大きな 音に 驚きます。", "ex2_kana": "おおきなおとにおどろきます", "ex2_cn": "被巨大的聲音嚇了一跳。"},
            {"word": "しんぱい", "kanji": "心配", "meaning": "擔心、憂慮 (Worried / Anxious)", "ex1_kanji": "テストの 結果が 心配で 寝られません。", "ex1_kana": "てすとのけっかがしんぱいでねられません", "ex1_cn": "因為擔心考試結果而睡不著。", "ex2_kanji": "どうぞ ご心配なく。", "ex2_kana": "どうぞごしんぱいなく", "ex2_cn": "請別擔心。"},
            {"word": "あんしん", "kanji": "安心", "meaning": "放心、安心 (Relieved / Reassured)", "ex1_kanji": "無事に 到着したと 聞いて 安心しました。", "ex1_kana": "ぶじにとうちゃくしたときいてあんしんしました", "ex1_cn": "聽到平安抵達的消息就放心了。", "ex2_kanji": "医者の 言葉を 聞いて 安心します。", "ex2_kana": "いしゃのことばをきいてあんしんします", "ex2_cn": "聽了醫生的話感到安心。"},
            {"word": "はずかしい", "kanji": "恥ずかしい", "meaning": "害羞、不好意思 (Embarrassed / Ashamed)", "ex1_kanji": "みんなの前で 転んで 恥ずかしかったです。", "ex1_kana": "みんなのまえでころんではずかしかったです", "ex1_cn": "在大家面前摔倒覺得很不好意思。", "ex2_kanji": "褒められて 恥ずかしいです。", "ex2_kana": "ほめられてはずかしいです", "ex2_cn": "被稱讚感到很害羞。"},
            {"word": "うらやましい", "kanji": "羨ましい", "meaning": "羨慕 (Envious / Jealous)", "ex1_kanji": "彼女の 綺麗な 歌声が 羨ましいです。", "ex1_kana": "かのじょのきれいなうたごえがうらやましいです", "ex1_cn": "很羨慕她美麗的歌聲。", "ex2_kanji": "長い 休みが 取れて 羨ましいです。", "ex2_kana": "ながいやすみがとれてうらやましいです", "ex2_cn": "能拿到長假真讓人羨慕。"},
            {"word": "なつかしい", "kanji": "懐かしい", "meaning": "懷念、令人懷念 (Nostalgic)", "ex1_kanji": "昔の 写真を 見て 懐かしく 思います。", "ex1_kana": "むかしのしゃしんをみてなつかしくおもいます", "ex1_cn": "看著以前的照片覺得令人懷念。", "ex2_kanji": "懐かしい 歌を 聴きます。", "ex2_kana": "なつかしいうたをききます", "ex2_cn": "聆聽令人懷念的歌曲。"},
            {"word": "くやしい", "kanji": "悔しい", "meaning": "不甘心、悔恨 (Frustrated / Mortified)", "ex1_kanji": "試合に 負けて とても 悔しいです。", "ex1_kana": "しあいにまけてとてもくやしいです", "ex1_cn": "比賽輸了非常不甘心。", "ex2_kanji": "一分差で 逃して 悔しいです。", "ex2_kana": "いっぷんさでのがしてくやしいです", "ex2_cn": "差一分鐘而錯過，真令人沮喪。"},
            {"word": "いらいら", "kanji": "イライラ", "meaning": "焦躁、煩躁 (Irritated / Annoyed)", "ex1_kanji": "渋滞で 車が 進まず イライラします。", "ex1_kana": "じゅうたいでくるまがすすまずいらいらします", "ex1_cn": "因為塞車車子動不了而感到焦躁。", "ex2_kanji": "イライラせずに 落ち着いてください。", "ex2_kana": "いらいらせずにおちついてください", "ex2_cn": "請不要煩躁，冷靜下來。"},
            {"word": "どきどき", "kanji": "ドキドキ", "meaning": "緊張、心跳加速 (Pounding heart / Nervous)", "ex1_kanji": "発表の 前で 胸が ドキドキしています。", "ex1_kana": "はっぴょうのまえでむねがどきどきしています", "ex1_cn": "發表前心裡砰砰直跳。", "ex2_kanji": "緊張して 心臓が ドキドキします。", "ex2_kana": "きんちょうしてしんぞうがどきどきします", "ex2_cn": "緊張得心跳加速。"},
            {"word": "わくわく", "kanji": "ワクワク", "meaning": "興奮、期待 (Excited / Thrilled)", "ex1_kanji": "明日からの 旅行に 胸が ワクワクします。", "ex1_kana": "あしたからのりょこうにむねがわくわくします", "ex1_cn": "對明天開始的旅行感到雀躍興奮。", "ex2_kanji": "ワクワクしながら 待っています。", "ex2_kana": "わくわくしながらまっています", "ex2_cn": "懷著興奮的心情等待著。"},
            {"word": "すっきり", "kanji": "スッキリ", "meaning": "舒暢、神清氣爽 (Refreshed / Relieved)", "ex1_kanji": "部屋を 掃除して 気持ちが スッキリしました。", "ex1_kana": "へやをそうじしてきもちがすっきりしました", "ex1_cn": "打掃完房間後心情變得很舒暢。", "ex2_kanji": "シャワーを 浴びて スッキリします。", "ex2_kana": "しゃわーをあびてすっきりします", "ex2_cn": "洗個澡神清氣爽。"},
            {"word": "がっかり", "kanji": "ガッカリ", "meaning": "失望、沮喪 (Disappointed)", "ex1_kanji": "期待していた 映画が つまらなくて ガッカリしました。", "ex1_kana": "きたいしていたえいががつまらなくてがっかりしました", "ex1_cn": "期待的電影很無聊，感到很失望。", "ex2_kanji": "そんなに ガッカリしないでください。", "ex2_kana": "そんなにがっかりしないでください", "ex2_cn": "請不要那麼沮喪。"},
            {"word": "ふあん", "kanji": "不安", "meaning": "不安、不踏實 (Uneasy / Anxious)", "ex1_kanji": "将来の ことについて 不安を 感じます。", "ex1_kana": "しょうらいのことについてふあんをかんじます", "ex1_cn": "對將來的事感到不安。", "ex2_kanji": "一人で 行くのは 不安です。", "ex2_kana": "ひとりで行くのはふあんです", "ex2_cn": "一個人去讓人感到不踏實。"},
            {"word": "とまどう", "kanji": "戸惑う", "meaning": "困惑、不知所措 (Bewildered / Confused)", "ex1_kanji": "新しい 環境に 慣れず 戸惑っています。", "ex1_kana": "あたらしいかんきょうになれずとまどっています", "ex1_cn": "還沒習慣新環境，感到有些不知所措。", "ex2_kanji": "急な 質問に 戸惑いました。", "ex2_kana": "きゅうなしつもんとまどいました", "ex2_cn": "對突如其來的提問感到困惑。"},
            {"word": "かんどう", "kanji": "感動", "meaning": "感動 (Moved / Touched)", "ex1_kanji": "素晴らしい 演奏に 深く 感動しました。", "ex1_kana": "すばらしいえんそうにふかくかんどうしました", "ex1_cn": "被精彩的演奏深深感動了。", "ex2_kanji": "感動して 涙が 出ました。", "ex2_kana": "かんどうしてなみだがでました", "ex2_cn": "感動得流下了眼淚。"},
            {"word": "めんどうくさい", "kanji": "面倒くさい", "meaning": "麻煩、提不起勁 (Bothersome / Troublesome)", "ex1_kanji": "部屋の 掃除をするのが 面倒くさいです。", "ex1_kana": "へやのそうじをするのがめんどうくさいです", "ex1_cn": "打掃房間覺得好麻煩。", "ex2_kanji": "手続きが 面倒くさいです。", "ex2_kana": "てつづきがめんどうくさいです", "ex2_cn": "手續非常麻煩。"},
            {"word": "つかれる", "kanji": "疲れる", "meaning": "疲累、疲倦 (Tired / Exhausted)", "ex1_kanji": "一日中 働いて とても 疲れました。", "ex1_kana": "いちにちじゅうはたらいてとてもつかれました", "ex1_cn": "工作了一整天感到非常疲累。", "ex2_kanji": "疲れた時は ゆっくり 休みます。", "ex2_kana": "つかれたときはゆっくりやすみます", "ex2_cn": "累的時候就好好休息。"},
            {"word": "あきる", "kanji": "飽きる", "meaning": "厭倦、膩了 (Bored of / Tired of)", "ex1_kanji": "毎日 同じ 料理で 飽きてしまいました。", "ex1_kana": "まいにちおなじりょうりであきてしまいました", "ex1_cn": "每天吃同樣的料理都吃膩了。", "ex2_kanji": "この ゲームには もう 飽きました。", "ex2_kana": "このげーむにはもうあきました", "ex2_cn": "這個遊戲我已經玩膩了。"},
            {"word": "あせる", "kanji": "焦る", "meaning": "焦急、著急 (Impatient / Panic)", "ex1_kanji": "時間が なくなって 焦って しまいました。", "ex1_kana": "じかんがなくなってあせってしまいました", "ex1_cn": "時間不夠了，變得非常焦急。", "ex2_kanji": "焦らずに 順番に やりましょう。", "ex2_kana": "あせずにつんばんにやりましょう", "ex2_cn": "不要著急，按順序來做吧。"},
            {"word": "こまる", "kanji": "困る", "meaning": "困擾、為難 (Troubled / In a fix)", "ex1_kanji": "財布を 落として 困っています。", "ex1_kana": "さいふをおとしてこまっています", "ex1_cn": "弄丟了錢包，現在非常困擾。", "ex2_kanji": "返事に 困ります。", "ex2_kana": "へんじにこまります", "ex2_cn": "難以做出回答 / 感到為難。"},
            {"word": "むかむか", "kanji": "ムカムカ", "meaning": "生氣、胃部不適 (Sick / Disgusted / Angry)", "ex1_kanji": "彼の 失礼な 態度に ムカムカします。", "ex1_kana": "かれのしつれいなたいどにむかむかします", "ex1_cn": "對他無禮的態度感到非常生氣。", "ex2_kanji": "食べすぎて 胃が ムカムカします。", "ex2_kana": "たべすぎていがむかむかします", "ex2_cn": "吃太多了，胃裡感到不舒服。"},
            {"word": "たのしむ", "kanji": "楽しむ", "meaning": "享受、樂在其中 (Enjoy oneself)", "ex1_kanji": "週末は 趣味の 時間を 楽しみます。", "ex1_kana": "しゅうまつはしゅみのじかんをたのしみます", "ex1_cn": "週末享受個人興趣的時間。", "ex2_kanji": "パーティを 心から 楽しみます。", "ex2_kana": "ぱーてぃをこころからたのしみます", "ex2_cn": "打從心底享受派對。"}
        ]

    def init_direction_data(self):
        self.direction_data = [
            {"word": "うえ", "kanji": "上", "meaning": "上面、上方 (位置名詞)", "ex1_kanji": "机の上に本があります。", "ex1_kana": "つくえのうえにほんがあります", "ex1_cn": "桌子上面有書。", "ex2_kanji": "上を見ます。", "ex2_kana": "うえをみます", "ex2_cn": "往上看。"},
            {"word": "した", "kanji": "下", "meaning": "下面、下方 (位置名詞)", "ex1_kanji": "机の下に猫がいます。", "ex1_kana": "つくえのしたにねこがいます", "ex1_cn": "桌子下面有貓。", "ex2_kanji": "下を見てください。", "ex2_kana": "したをみてください", "ex2_cn": "請往下看。"},
            {"word": "まえ", "kanji": "前", "meaning": "前面 (位置名詞)", "ex1_kanji": "駅の前で友達と会います。", "ex1_kana": "えきのまえでともだちにあいます", "ex1_cn": "在車站前面跟朋友見面。", "ex2_kanji": "前を向いて歩きます。", "ex2_kana": "まえをむいてあるきます", "ex2_cn": "朝向前看著走。"},
            {"word": "うしろ", "kanji": "後ろ", "meaning": "後面、後方 (位置名詞)", "ex1_kanji": "車の後ろに人がいます。", "ex1_kana": "くるまのうしろにひとがいます", "ex1_cn": "車子後面有人。", "ex2_kanji": "後ろを振り返ります。", "ex2_kana": "うしろをふりかえります", "ex2_cn": "向後看。"},
            {"word": "みぎ", "kanji": "右", "meaning": "右邊 (位置名詞)", "ex1_kanji": "右に曲がってください。", "ex1_kana": "みぎにまがってください", "ex1_cn": "請向右轉。", "ex2_kanji": "右手でペンを持ちます。", "ex2_kana": "みぎてでぺんをもちます", "ex2_cn": "用右手拿筆。"},
            {"word": "ひだり", "kanji": "左", "meaning": "左邊 (位置名詞)", "ex1_kanji": "左に交番があります。", "ex1_kana": "ひだりにこうばんがあります", "ex1_cn": "左邊有派出所。", "ex2_kanji": "左を見て確認します。", "ex2_kana": "ひだりをみてかくにんします", "ex2_cn": "看向左邊確認。"},
            {"word": "なか", "kanji": "中", "meaning": "裡面、內部 (位置名詞)", "ex1_kanji": "箱の中に何がありますか。", "ex1_kana": "はおのなかになにがありますか", "ex1_cn": "盒子裡面有什麼？", "ex2_kanji": "部屋の中に入ります。", "ex2_kana": "へやのなかにはいります", "ex2_cn": "進入房間裡面。"},
            {"word": "そと", "kanji": "外", "meaning": "外面、室外 (位置名詞)", "ex1_kanji": "外はとても寒いです。", "ex1_kana": "そとはとてもさむいです", "ex1_cn": "外面非常冷。", "ex2_kanji": "外で遊びましょう。", "ex2_kana": "そとであそびましょう", "ex2_cn": "去外面玩吧。"},
            {"word": "となり", "kanji": "隣", "meaning": "隔壁、旁邊 (同類緊鄰) (位置名詞)", "ex1_kanji": "銀行の隣にスーパーがあります。", "ex1_kana": "ぎんこうのとなりにすーぱーがあります", "ex1_cn": "銀行隔壁有超市。", "ex2_kanji": "隣の席に座ります。", "ex2_kana": "となりのせきにすわります", "ex2_cn": "坐在隔壁的座位。"},
            {"word": "よこ", "kanji": "横", "meaning": "旁邊、兩側 (位置名詞)", "ex1_kanji": "ベッドの横に時計があります。", "ex1_kana": "べっどのよこにとけいがあります", "ex1_cn": "床邊有鐘。", "ex2_kanji": "横を向きます。", "ex2_kana": "よこをむきます", "ex2_cn": "轉向側邊。"},
            {"word": "ちかく", "kanji": "近く", "meaning": "附近、近處 (位置名詞)", "ex1_kanji": "家の近くに公園があります。", "ex1_kana": "いえのちかくにこうえんがあります", "ex1_cn": "家附近有公園。", "ex2_kanji": "近くで買い物をします。", "ex2_kana": "ちかくでかいものをします", "ex2_cn": "在附近購物。"},
            {"word": "そば", "kanji": "側", "meaning": "身旁、近側 (位置名詞)", "ex1_kanji": "私のそばにいてください。", "ex1_kana": "わたしのそばにいてください", "ex1_cn": "請待在我的身邊。", "ex2_kanji": "川のそばを歩きます。", "ex2_kana": "かわのそばをあるきます", "ex2_cn": "在河邊散步。"},
            {"word": "むかい", "kanji": "向かい", "meaning": "對面 (位置名詞)", "ex1_kanji": "郵便局の向かいに病院があります。", "ex1_kana": "ゆうびんきょくのむかいにびょういんがあります", "ex1_cn": "郵局對面有醫院。", "ex2_kanji": "駅の向かい側にビルがあります。", "ex2_kana": "えきのむかいがわにびるがあります", "ex2_cn": "車站對面有大樓。"},
            {"word": "あいだ", "kanji": "間", "meaning": "中間、兩者之間 (位置名詞)", "ex1_kanji": "本屋と薬局の間にあります。", "ex1_kana": "ほんやとやっきょくのあいだにあります", "ex1_cn": "在書店和藥局之間。", "ex2_kanji": "AとBの間を選びます。", "ex2_kana": "えーとびーのあいだをえらびます", "ex2_cn": "在A與B之間選擇。"},
            {"word": "うら", "kanji": "裏", "meaning": "背面、裏面 (位置名詞)", "ex1_kanji": "紙の裏に名前を書きます。", "ex1_kana": "かみのうらになまえをかきます", "ex1_cn": "在紙的背面寫名字。", "ex2_kanji": "ビルの裏に駐車場があります。", "ex2_kana": "びるのうらにちゅうしゃじょうがあります", "ex2_cn": "大樓後面有停車場。"},
            {"word": "おもて", "kanji": "表", "meaning": "正面、表面 (位置名詞)", "ex1_kanji": "表に大きな看板があります。", "ex1_kana": "おもてにおおきなかんばんがあります", "ex1_cn": "正面有很大的看板。", "ex2_kanji": "服の表と裏を確認します。", "ex2_kana": "ふくのおもてとうらをかくにんします", "ex2_cn": "確認衣服的正面和背面。"},
            {"word": "まんなか", "kanji": "真ん中", "meaning": "正中央 (位置名詞)", "ex1_kanji": "テーブルの真ん中に花を置きます。", "ex1_kana": "てーぶるのまんなかにはなをおきます", "ex1_cn": "在桌子正中央擺花。", "ex2_kanji": "部屋の真ん中に立ちます。", "ex2_kana": "へやのまんなかにたちます", "ex2_cn": "站在房間正中央。"},
            {"word": "すみ", "kanji": "隅", "meaning": "角落 (室內或內部角落) (位置名詞)", "ex1_kanji": "部屋の隅にゴミ箱があります。", "ex1_kana": "へやのすみにごみばこがあります", "ex1_cn": "房間角落有垃圾桶。", "ex2_kanji": "隅に座ります。", "ex2_kana": "すみにすわります", "ex2_cn": "坐在角落。"},
            {"word": "かど", "kanji": "角", "meaning": "轉角、街角 (外部轉角) (位置名詞)", "ex1_kanji": "次の角を右に曲がります。", "ex1_kana": "つぎのかどをみぎにまがります", "ex1_cn": "在下一個轉角向右轉。", "ex2_kanji": "角の店でパンを買いました。", "ex2_kana": "かどのみせでぱんをかいました", "ex2_cn": "在轉角的店買了麵包。"},
            {"word": "おく", "kanji": "奥", "meaning": "深處、內部 (位置名詞)", "ex1_kanji": "店の奥にトイレがあります。", "ex1_kana": "みせのおくにといれがあります", "ex1_cn": "店內深處有洗手間。", "ex2_kanji": "奥の席へどうぞ。", "ex2_kana": "おくのせきへどうぞ", "ex2_cn": "請往裡面的座位走。"},
            {"word": "てまえ", "kanji": "手前", "meaning": "近前、眼前、這側 (位置名詞)", "ex1_kanji": "信号の手前で止まります。", "ex1_kana": "しんごうのてまえでとまります", "ex1_cn": "在紅綠燈前停下。", "ex2_kanji": "駅の手前にカフェがあります。", "ex2_kana": "えきのてまえにかふぇがあります", "ex2_cn": "車站前有一家咖啡廳。"},
            {"word": "むこう", "kanji": "向こう", "meaning": "對岸、另一側、遠處 (位置名詞)", "ex1_kanji": "川の向こうに公園が見えます。", "ex1_kana": "かわのむこうにこうえんがみえます", "ex1_cn": "看得見河對岸的公園。", "ex2_kanji": "向こうへ行きましょう。", "ex2_kana": "むこうへいきましょう", "ex2_cn": "往那邊走吧。"},
            {"word": "ひがし", "kanji": "東", "meaning": "東邊 (方位名詞)", "ex1_kanji": "太陽は東から昇ります。", "ex1_kana": "たいようはひがしからのおぼります", "ex1_cn": "太陽從東邊升起。", "ex2_kanji": "東京は日本の東にあります。", "ex2_kana": "とうきょうはにほんのひがしにあります", "ex2_cn": "東京在日本的東部。"},
            {"word": "にし", "kanji": "西", "meaning": "西邊 (方位名詞)", "ex1_kanji": "太陽は西に沈みます。", "ex1_kana": "たいようはにしにしずみます", "ex1_cn": "太陽在西邊落下。", "ex2_kanji": "関西は日本の西側にあります。", "ex2_kana": "かんさいはにほんのにしがわにあります", "ex2_cn": "關西在日本的西側。"},
            {"word": "みなみ", "kanji": "南", "meaning": "南邊 (方位名詞)", "ex1_kanji": "南の島へ旅行に行きます。", "ex1_kana": "みなみのしまへりょこうにいきます", "ex1_cn": "去南方的島嶼旅行。", "ex2_kanji": "部屋の窓は南に面しています。", "ex2_kana": "へやのまどはみなみにめんしています", "ex2_cn": "房間的窗戶朝向南方。"},
            {"word": "きた", "kanji": "北", "meaning": "北邊 (方位名詞)", "ex1_kanji": "北海道は日本の北にあります。", "ex1_kana": "ほっかいどうはにほんのきたにあります", "ex1_cn": "北海道在日本的北方。", "ex2_kanji": "風が北から吹いています。", "ex2_kana": "かぜがきたからふいています", "ex2_cn": "風從北方吹來。"},
            {"word": "ほう", "kanji": "方", "meaning": "方向、方面 (位置名詞)", "ex1_kanji": "あちらの方へ歩きます。", "ex1_kana": "あちらのほうへあるきます", "ex1_cn": "朝那個方向走。", "ex2_kanji": "北の方角は寒いです。", "ex2_kana": "きたのほうがくはさむいです", "ex2_cn": "北方比較冷。"},
            {"word": "まわり", "kanji": "周り", "meaning": "周圍、四周 (位置名詞)", "ex1_kanji": "池の周りを散歩します。", "ex1_kana": "いけのまわりをさんぽします", "ex1_cn": "在池塘周圍散步。", "ex2_kanji": "周りの人に聞きます。", "ex2_kana": "まわりのひとにききます", "ex2_cn": "詢問周圍的人。"},
            {"word": "きたぐち", "kanji": "北口", "meaning": "北出口 (位置名詞)", "ex1_kanji": "北口の改札で待ち合わせます。", "ex1_kana": "きたぐちのかいさつでまちあわせます", "ex1_cn": "在北口剪票口集合。", "ex2_kanji": "北口を出てください。", "ex2_kana": "きたぐちをでてください", "ex2_cn": "請從北口出去。"},
            {"word": "みなみぐち", "kanji": "南口", "meaning": "南出口 (位置名詞)", "ex1_kanji": "南口にバス乗り場があります。", "ex1_kana": "みなみぐちにばすのりばがあります", "ex1_cn": "南口有公車搭乘處。", "ex2_kanji": "南口から出ます。", "ex2_kana": "みなみぐちからでます", "ex2_cn": "從南口出去。"}
        ]

    def get_current_data(self):
        modes = {
            "food": self.food_data,
            "animal": self.animal_data,
            "daily": self.daily_data,
            "nature": self.nature_data,
            "subject": self.subject_data,
            "family": self.family_data,
            "emotion": self.emotion_data,
            "direction": self.direction_data
        }
        return modes.get(self.current_mode, self.direction_data)

    def setup_ui(self):
        top_bar = tk.Frame(self.root, bg=self.top_bg, height=50)
        top_bar.pack(side=tk.TOP, fill=tk.X)

        # 返回主選單按鈕
        btn_back = tk.Button(
            top_bar,
            text="返回主選單",
            font=("Arial", 14, "bold"),
            bg="#556B2F",
            fg="white",
            activebackground="#455624",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.return_to_selector,
            padx=15,
            pady=3,
        )
        btn_back.pack(side=tk.LEFT, padx=15, pady=8)

        # 結束程式按鈕
        exit_btn = tk.Button(
            top_bar,
            text="結束程式",
            font=("Arial", 14),
            bg="#B85B56",
            fg="white",
            activebackground="#A04A45",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.close_app,
            padx=15,
            pady=3,
        )
        exit_btn.pack(side=tk.RIGHT, padx=15, pady=8)

        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(side=tk.BOTTOM, pady=15)

        self.btn_prev = tk.Button(
            btn_frame,
            text="上一單字",
            font=("Arial", 16),
            bg=self.btn_bg,
            fg=self.btn_fg,
            activebackground=self.btn_active,
            activeforeground=self.btn_fg,
            relief=tk.FLAT,
            command=self.prev_word,
            padx=18,
            pady=5,
        )
        self.btn_prev.pack(side=tk.LEFT, padx=15)

        self.lbl_count = tk.Label(
            btn_frame,
            text="",
            font=("Arial", 12),
            fg=self.text_color,
            bg=self.bg_color,
        )
        self.lbl_count.pack(side=tk.LEFT, padx=15)

        self.btn_next = tk.Button(
            btn_frame,
            text="下一單字",
            font=("Arial", 16),
            bg=self.btn_bg,
            fg=self.btn_fg,
            activebackground=self.btn_active,
            activeforeground=self.btn_fg,
            relief=tk.FLAT,
            command=self.next_word,
            padx=20,
            pady=5,
        )
        self.btn_next.pack(side=tk.LEFT, padx=15)

        container = tk.Frame(self.root, bg=self.bg_color)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.canvas = tk.Canvas(container, bg=self.card_bg, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)

        self.main_frame = tk.Frame(self.canvas, bg=self.card_bg, padx=25, pady=15)

        self.main_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        def _on_canvas_configure(event):
            self.canvas.itemconfig(self.canvas_window, width=event.width)
        self.canvas.bind("<Configure>", _on_canvas_configure)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lbl_word = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 20, "bold"),
            fg=self.text_color,
            bg=self.card_bg,
            anchor="w",
            justify=tk.LEFT,
        )
        self.lbl_word.pack(fill=tk.X, pady=4)

        self.lbl_meaning = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 12),
            fg=self.text_color,
            bg=self.card_bg,
            anchor="w",
            justify=tk.LEFT,
        )
        self.lbl_meaning.pack(fill=tk.X, pady=4)

        sep = tk.Frame(self.main_frame, bg="#C0B0A0", height=1)
        sep.pack(fill=tk.X, pady=8)

        # ================= 例句 1 區塊 =================
        ex1_box = tk.Frame(self.main_frame, bg=self.card_bg)
        ex1_box.pack(fill=tk.X, pady=4)

        self.txt_ex1_kanji = self.create_particle_text_widget(ex1_box, 13, "bold", self.text_color)
        self.txt_ex1_kanji.pack(side=tk.TOP, anchor="w", fill=tk.X)

        self.txt_ex1_kana = self.create_particle_text_widget(ex1_box, 12, "normal", self.kana_color)
        self.txt_ex1_kana.pack(side=tk.TOP, anchor="w", fill=tk.X, pady=(1, 0))

        self.lbl_ex1_cn = tk.Label(
            ex1_box,
            text="",
            font=("Arial", 12),
            fg="#6B5B52",
            bg=self.card_bg,
            anchor="w",
            justify=tk.LEFT,
        )
        self.lbl_ex1_cn.pack(side=tk.TOP, anchor="w", fill=tk.X, pady=(1, 0))

        # ================= 水平分隔線 =================
        sep_between = tk.Frame(self.main_frame, bg="#B0A090", height=2)
        sep_between.pack(fill=tk.X, pady=10)

        # ================= 例句 2 區塊 =================
        ex2_box = tk.Frame(self.main_frame, bg=self.card_bg)
        ex2_box.pack(fill=tk.X, pady=4)

        self.txt_ex2_kanji = self.create_particle_text_widget(ex2_box, 13, "bold", self.text_color)
        self.txt_ex2_kanji.pack(side=tk.TOP, anchor="w", fill=tk.X)

        self.txt_ex2_kana = self.create_particle_text_widget(ex2_box, 12, "normal", self.kana_color)
        self.txt_ex2_kana.pack(side=tk.TOP, anchor="w", fill=tk.X, pady=(1, 0))

        self.lbl_ex2_cn = tk.Label(
            ex2_box,
            text="",
            font=("Arial", 12),
            fg="#6B5B52",
            bg=self.card_bg,
            anchor="w",
            justify=tk.LEFT,
        )
        self.lbl_ex2_cn.pack(side=tk.TOP, anchor="w", fill=tk.X, pady=(1, 0))

        audio_btn_frame = tk.Frame(self.main_frame, bg=self.card_bg)
        audio_btn_frame.pack(side=tk.TOP, anchor="w", pady=(12, 0))

        btn_tts = tk.Button(
            audio_btn_frame,
            text="朗讀例句",
            font=("Arial", 16),
            bg=self.audio_btn_bg,
            fg="white",
            activebackground=self.audio_btn_active,
            activeforeground="white",
            relief=tk.FLAT,
            command=self.trigger_tts,
            padx=15,
            pady=4,
        )
        btn_tts.pack(side=tk.LEFT, padx=(0, 10))

        self.btn_loop = tk.Button(
            audio_btn_frame,
            text="連續朗讀",
            font=("Arial", 16),
            bg=self.loop_btn_bg,
            fg="white",
            activebackground=self.loop_btn_active,
            activeforeground="white",
            relief=tk.FLAT,
            command=self.trigger_loop_tts,
            padx=15,
            pady=4,
        )
        self.btn_loop.pack(side=tk.LEFT)

    def return_to_selector(self):
        """ 返回主選擇視窗 """
        self.is_looping = False
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        except Exception:
            pass
        self.root.destroy()
        new_root = tk.Tk()
        ModeSelector(new_root)
        new_root.mainloop()

    def create_particle_text_widget(self, parent, size, weight, default_fg):
        txt = tk.Text(
            parent,
            height=1,
            bd=0,
            highlightthickness=0,
            bg=self.card_bg,
            fg=default_fg,
            font=("Arial", size, weight),
            wrap="word",
        )
        txt.tag_config("normal", foreground=default_fg)
        txt.tag_config("particle", foreground=self.particle_color)
        return txt

    def set_particle_text(self, text_widget, text_str):
        """ 支援雙字與單字助詞的標色匹配 """
        text_widget.config(state="normal")
        text_widget.delete("1.0", tk.END)

        multi_particles = {"から", "より", "まで"}
        single_particles = {"を", "に", "で", "が", "の", "へ", "と", "は", "も", "や", "て"}

        i = 0
        n = len(text_str)
        while i < n:
            # 優先比對雙字助詞
            if i + 1 < n and text_str[i:i+2] in multi_particles:
                text_widget.insert(tk.END, text_str[i:i+2], "particle")
                i += 2
            # 次之比對單字助詞
            elif text_str[i] in single_particles:
                text_widget.insert(tk.END, text_str[i], "particle")
                i += 1
            else:
                text_widget.insert(tk.END, text_str[i], "normal")
                i += 1

        text_widget.update_idletasks()
        dlines = text_widget.count("1.0", "end", "displaylines")
        actual_lines = dlines[0] if dlines and dlines[0] > 0 else 1
        
        text_widget.config(height=actual_lines)
        text_widget.config(state="disabled")

    def load_word(self):
        data_list = self.get_current_data()
        data = data_list[self.current_index]
        
        kanji_str = f" ({data['kanji']})" if data['kanji'] != "-" else ""
        self.lbl_word.config(text=f"{data['word']}{kanji_str}")
        self.lbl_meaning.config(text=f"{data['meaning']}")

        # 例句 1
        self.set_particle_text(self.txt_ex1_kanji, data["ex1_kanji"])
        ex1_kana_str = data.get("ex1_kana", data.get("ex1_ttstext", ""))
        self.set_particle_text(self.txt_ex1_kana, ex1_kana_str)
        self.lbl_ex1_cn.config(text=data["ex1_cn"])

        # 例句 2
        self.set_particle_text(self.txt_ex2_kanji, data["ex2_kanji"])
        ex2_kana_str = data.get("ex2_kana", data.get("ex2_ttstext", data.get("ex2_kanji", "")))
        self.set_particle_text(self.txt_ex2_kana, ex2_kana_str)
        self.lbl_ex2_cn.config(text=data["ex2_cn"])

        total = len(data_list)
        self.lbl_count.config(text=f"{self.current_index + 1} / {total}")

        self.main_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def prev_word(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_word()

    def next_word(self):
        data_list = self.get_current_data()
        if self.current_index < len(data_list) - 1:
            self.current_index += 1
            self.load_word()

    def trigger_tts(self):
        threading.Thread(target=self.speak_worker_single, daemon=True).start()

    def speak_worker_single(self):
        data_list = self.get_current_data()
        data = data_list[self.current_index]
        tts_texts = [
            data.get("ex1_ttstext", data.get("ex1_kana", "")),
            data.get("ex2_ttstext", data.get("ex2_kana", ""))
        ]
        for text in tts_texts:
            if text:
                self.play_audio_text(text)

    def trigger_loop_tts(self):
        if self.is_looping:
            self.is_looping = False
            self.btn_loop.config(text="連續朗讀", bg=self.loop_btn_bg)
            return

        self.is_looping = True
        self.btn_loop.config(text="停止朗讀", bg="#B85B56")
        threading.Thread(target=self.loop_all_words, daemon=True).start()

    def loop_all_words(self):
        data_list = self.get_current_data()
        while self.is_looping and self.current_index < len(data_list):
            self.root.after(0, self.load_word)
            
            data = data_list[self.current_index]
            tts_texts = [
                data.get("word", ""),
                data.get("ex1_ttstext", data.get("ex1_kana", "")),
                data.get("ex2_ttstext", data.get("ex2_kana", ""))
            ]

            for text in tts_texts:
                if not self.is_looping:
                    break
                if text:
                    self.play_audio_text(text)

            if not self.is_looping:
                break

            if self.current_index < len(data_list) - 1:
                # 依據主目錄設定的 pause_seconds 進行動態等待
                sleep_steps = int(self.pause_seconds * 10)
                for _ in range(sleep_steps):
                    if not self.is_looping:
                        break
                    time.sleep(0.1)
                self.current_index += 1
            else:
                break

        self.is_looping = False
        self.root.after(0, lambda: self.btn_loop.config(text="連續朗讀", bg=self.loop_btn_bg))

    def play_audio_text(self, text):
        """ 使用 BytesIO 將音訊保留在記憶體中，徹底解決實體檔案鎖定問題 """
        for _ in range(3):
            try:
                pygame.mixer.music.unload()
                fp = io.BytesIO()
                tts = gTTS(text=text, lang="ja", slow=False)
                tts.write_to_fp(fp)
                fp.seek(0)
                
                pygame.mixer.music.load(fp)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(0.05)

                pygame.mixer.music.unload()
                time.sleep(0.1)
                break
            except Exception:
                time.sleep(0.2)

    def close_app(self):
        self.is_looping = False
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        except Exception:
            pass
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    selector = ModeSelector(root)
    root.mainloop()
