import streamlit as st
import json

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
        padding: 12px 18px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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

# 顯示被選擇的課別標籤 (高亮醒目區塊)
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

# ================= 語音播放控制器 (HTML5 + Web Speech API) =================
# 將當前課別的所有單字資料轉為 JSON 給 JavaScript 使用
dataset_json = json.dumps(current_dataset, ensure_ascii=False)

player_code = f"""
<div style="background:#E8D8C8; padding:15px; border-radius:10px; text-align:center; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
    <div style="margin-bottom: 10px; font-weight: bold; color: #4A403A;">🔊 全課自動連續朗讀控制器</div>
    <button id="playAllBtn" style="background:#4A403A; color:#F4EAD3; border:none; padding:10px 20px; border-radius:6px; font-weight:bold; cursor:pointer; font-size:16px; margin-right:8px;">
        ▶️ 從頭自動連續朗讀全課
    </button>
    <button id="stopBtn" style="background:#D9534F; color:white; border:none; padding:10px 20px; border-radius:6px; font-weight:bold; cursor:pointer; font-size:16px;">
        ⏹️ 停止朗讀
    </button>
    <div id="statusText" style="margin-top:10px; font-size:14px; color:#6B5B52; font-weight:bold;">狀態：待命</div>
</div>

<script>
    const dataset = {dataset_json};
    let isPlaying = false;
    let wordIndex = 0;
    
    const playAllBtn = document.getElementById('playAllBtn');
    const stopBtn = document.getElementById('stopBtn');
    const statusText = document.getElementById('statusText');

    function updateStatus(text) {{
        statusText.innerText = "狀態：" + text;
    }}

    function speakText(text, onEndCallback) {{
        if (!isPlaying) return;
        window.speechSynthesis.cancel();
        
        const msg = new SpeechSynthesisUtterance(text);
        msg.lang = 'ja-JP';
        msg.rate = 0.85;
        
        msg.onend = function() {{
            if (isPlaying && onEndCallback) {{
                setTimeout(onEndCallback, 400); // 句與句之間停頓 0.4 秒
            }}
        }};
        
        msg.onerror = function() {{
            if (isPlaying && onEndCallback) {{
                onEndCallback();
            }}
        }};
        
        window.speechSynthesis.speak(msg);
    }}

    function playItemSequence(index) {{
        if (!isPlaying || index >= dataset.length) {{
            isPlaying = false;
            updateStatus("全課朗讀完成！");
            return;
        }}

        const item = dataset[index];
        updateStatus("正在朗讀 第 " + (index + 1) + " / " + dataset.length + " 個單字：" + item.word);

        // 步驟 1: 讀單字
        speakText(item.word, function() {{
            // 步驟 2: 讀例句 1
            speakText(item.ex1_kana, function() {{
                // 步驟 3: 讀例句 2
                speakText(item.ex2_kana, function() {{
                    // 步驟 4: 自動前進至下一個單字
                    wordIndex++;
                    playItemSequence(wordIndex);
                }});
            }});
        }});
    }}

    playAllBtn.onclick = function() {{
        window.speechSynthesis.cancel();
        isPlaying = true;
        wordIndex = 0;
        playItemSequence(wordIndex);
    }};

    stopBtn.onclick = function() {{
        isPlaying = false;
        window.speechSynthesis.cancel();
        updateStatus("已手動停止");
    }};
</script>
"""

st.components.v1.html(player_code, height=130)

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
