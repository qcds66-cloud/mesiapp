import streamlit as st
import streamlit.components.v1 as components

# ================= 頁面基礎設定 =================
st.set_page_config(
    page_title="日文綜合學習大師",
    page_icon="📚",
    layout="centered"
)

# 套用莫蘭迪/牛皮紙視覺風格 CSS
st.markdown("""
<style>
    .stApp {
        background-color: #D8C3A5;
        color: #4A403A;
    }
    .card {
        background-color: #E8D8C8;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .category-highlight {
        background-color: #4A403A;
        color: #F4EAD3;
        padding: 10px 15px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        text-align: center;
        margin-bottom: 15px;
    }
    .word-title {
        font-size: 28px;
        font-weight: bold;
        color: #4A403A;
        margin-bottom: 4px;
    }
    .meaning {
        font-size: 18px;
        color: #6B5B52;
        margin-bottom: 16px;
    }
    .ex-kanji {
        font-size: 20px;
        font-weight: bold;
        color: #4A403A;
    }
    .ex-kana {
        font-size: 16px;
        color: #4A90E2;
        margin-bottom: 4px;
    }
    .ex-cn {
        font-size: 16px;
        color: #6B5B52;
        margin-bottom: 12px;
    }
    .particle {
        color: #D9534F;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ================= 瀏覽器原生 TTS 工具函式 =================
def speak_js(text_list):
    """ 支援單一文字或字串陣列的連續朗讀 """
    if isinstance(text_list, str):
        text_list = [text_list]
    
    # 建立 JS 陣列
    js_array = str(text_list)
    
    js_code = f"""
    <script>
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel(); // 先停止當前語音
            var texts = {js_array};
            
            texts.forEach(function(text) {{
                if (text && text.trim() !== "") {{
                    var msg = new SpeechSynthesisUtterance(text);
                    msg.lang = 'ja-JP';
                    msg.rate = 0.85; // 語速稍慢，適合學習
                    window.speechSynthesis.speak(msg);
                }}
            }});
        }}
    </script>
    """
    components.html(js_code, height=0, width=0)

# ================= 資料庫載入 =================
@st.cache_data
def load_all_data():
    food_data = [
        {"word": "ごはん", "kanji": "ご飯", "meaning": "白飯 / 餐點", "ex1_kanji": "3時間ごとにお腹が空いて ご飯を食べます。", "ex1_kana": "さんじかんごとにおなかがすいてごはんをたべます", "ex1_cn": "每隔三小時肚子就會餓，然後吃飯。", "ex2_kanji": "温かいご飯を食べます。", "ex2_kana": "あたたかいごはんをたべます", "ex2_cn": "吃熱騰騰的白飯。"},
        {"word": "パン", "kanji": "パン", "meaning": "麵包", "ex1_kanji": "朝ごはんに バターをぬった パンを食べます。", "ex1_kana": "あさごはんにばたーをぬったぱんをたべます", "ex1_cn": "早餐吃抹了奶油的麵包。", "ex2_kanji": "美味しいパンを買います。", "ex2_kana": "おいしいぱんをかいます", "ex2_cn": "買好吃的麵包。"},
        {"word": "にく", "kanji": "肉", "meaning": "肉", "ex1_kanji": "焼き肉の 匂いが 食欲を そそります。", "ex1_kana": "やきにくのにおいがしょくよくをそそります", "ex1_cn": "烤肉的香味勾起人的食欲。", "ex2_kanji": "肉を料理します。", "ex2_kana": "にくをりょうりします", "ex2_cn": "料理肉品。"},
        {"word": "たまご", "kanji": "卵", "meaning": "雞蛋", "ex1_kanji": "朝ごはんに 目玉焼き用の 卵を 割ります。", "ex1_kana": "あさごはんにめだまやきようのたまごをわれます", "ex1_cn": "早餐把做荷包蛋用的雞蛋打開。", "ex2_kanji": "新鮮な卵を買います。", "ex2_kana": "しんせんなたまごをかいます", "ex2_cn": "買新鮮的雞蛋。"},
        {"word": "やさい", "kanji": "野菜", "meaning": "蔬菜", "ex1_kanji": "健康のため、毎日 新鮮な 野菜を 食べます。", "ex1_kana": "けんこうのためまいにちしんせんなやさいをたべます", "ex1_cn": "為了健康，每天都吃新鮮蔬菜。", "ex2_kanji": "野菜をたくさん食べます。", "ex2_kana": "やさいをたくさんたべます", "ex2_cn": "吃很多蔬菜。"}
    ]

    animal_data = [
        {"word": "いぬ", "kanji": "犬", "meaning": "狗", "ex1_kanji": "公園で 犬の 散歩を します。", "ex1_kana": "こうえんでいぬのさんぽをします", "ex1_cn": "在公園遛狗。", "ex2_kanji": "可愛い犬を飼っています。", "ex2_kana": "かわいいいぬをかっています", "ex2_cn": "養了可愛的狗狗。"},
        {"word": "ねこ", "kanji": "猫", "meaning": "貓", "ex1_kanji": "猫が 日向ぼっこを しています。", "ex1_kana": "ねこがひなたぼっこをしています", "ex1_cn": "貓咪正在曬太陽。", "ex2_kanji": "猫が魚を食べます。", "ex2_kana": "ねこがさかなをたべます", "ex2_cn": "貓吃魚。"}
    ]

    daily_data = [
        {"word": "つくえ", "kanji": "机", "meaning": "書桌、桌子 (Desk)", "ex1_kanji": "机の上に本があります。", "ex1_kana": "つくえのうえにほんがあります", "ex1_cn": "桌上有書本。", "ex2_kanji": "机をきれいに拭きます。", "ex2_kana": "つくえをきれいにふきます", "ex2_cn": "把桌子擦拭乾淨。"},
        {"word": "いす", "kanji": "椅子", "meaning": "椅子 (Chair)", "ex1_kanji": "椅子に座って休みます。", "ex1_kana": "いすにすわってやすみます", "ex1_cn": "坐在椅子上休息。", "ex2_kanji": "新しい椅子を買いました。", "ex2_kana": "あたらしいいすをかいました", "ex2_cn": "買了一把新椅子。"}
    ]

    return {
        "食物與水果": food_data,
        "動物與魚類": animal_data,
        "生活日常用品": daily_data
    }

CATEGORIES = load_all_data()

# ================= 工具函式 =================
def highlight_particles(text):
    multi_particles = {"から", "より", "まで"}
    single_particles = {"を", "に", "で", "が", "の", "へ", "と", "は", "も", "や", "て"}
    
    tokens = text.split(" ")
    highlighted = []
    for token in tokens:
        if token in multi_particles or token in single_particles:
            highlighted.append(f'<span class="particle">{token}</span>')
        else:
            highlighted.append(token)
    return " ".join(highlighted)

# ================= Session State 初始化 =================
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# ================= 側邊欄控制區 =================
st.sidebar.title("📖 學習課別選單")

category_name = st.sidebar.selectbox("請選擇課別：", list(CATEGORIES.keys()))
current_dataset = CATEGORIES[category_name]

# 切換類別時自動重置索引
if "last_category" not in st.session_state or st.session_state.last_category != category_name:
    st.session_state.current_index = 0
    st.session_state.last_category = category_name

st.sidebar.markdown("---")
if st.sidebar.button("🔄 重置到本課第一個單字"):
    st.session_state.current_index = 0
    st.rerun()

# ================= 主畫面 UI =================
st.title("日文綜合學習大師")

# 顯示被選擇的課別標籤 (高亮區塊)
st.markdown(f"""
<div class="category-highlight">
    🎯 當前選取課別：【{category_name}】（共 {len(current_dataset)} 個單字）
</div>
""", unsafe_allow_html=True)

# 安全索引防護
if st.session_state.current_index >= len(current_dataset):
    st.session_state.current_index = 0

item = current_dataset[st.session_state.current_index]

# 渲染單字卡片
kanji_text = f" ({item['kanji']})" if item['kanji'] != "-" else ""
ex1_highlighted = highlight_particles(item['ex1_kanji'])
ex2_highlighted = highlight_particles(item['ex2_kanji'])

st.markdown(f"""
<div class="card">
    <div class="word-title">{item['word']}{kanji_text}</div>
    <div class="meaning">{item['meaning']}</div>
    <hr>
    <div><b>例句 1：</b></div>
    <div class="ex-kanji">{ex1_highlighted}</div>
    <div class="ex-kana">{item['ex1_kana']}</div>
    <div class="ex-cn">{item['ex1_cn']}</div>
    <hr>
    <div><b>例句 2：</b></div>
    <div class="ex-kanji">{ex2_highlighted}</div>
    <div class="ex-kana">{item['ex2_kana']}</div>
    <div class="ex-cn">{item['ex2_cn']}</div>
</div>
""", unsafe_allow_html=True)

# ================= 語音控制區 =================
st.markdown("### 🔊 語音朗讀功能")

# 第一排：一鍵連續朗讀
if st.button("▶️ 連續朗讀（單字 ➔ 例句1 ➔ 例句2）", use_container_width=True, type="primary"):
    speak_js([item["word"], item["ex1_kana"], item["ex2_kana"]])

# 第二排：分段朗讀
col_audio1, col_audio2, col_audio3 = st.columns(3)
with col_audio1:
    if st.button("🔊 僅讀單字", use_container_width=True):
        speak_js(item["word"])

with col_audio2:
    if st.button("🔊 僅讀例句 1", use_container_width=True):
        speak_js(item["ex1_kana"])

with col_audio3:
    if st.button("🔊 僅讀例句 2", use_container_width=True):
        speak_js(item["ex2_kana"])

# ================= 切換與進度控制 =================
st.markdown("---")
col_prev, col_info, col_next = st.columns([1, 2, 1])

with col_prev:
    if st.button("⬅️ 上一單字", use_container_width=True):
        if st.session_state.current_index > 0:
            st.session_state.current_index -= 1
            st.rerun()

with col_info:
    st.markdown(f"<h4 style='text-align: center;'>{st.session_state.current_index + 1} / {len(current_dataset)}</h4>", unsafe_allow_html=True)

with col_next:
    if st.button("下一單字 ➡️", use_container_width=True):
        if st.session_state.current_index < len(current_dataset) - 1:
            st.session_state.current_index += 1
            st.rerun()
