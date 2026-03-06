import streamlit as st

# ------------------------------------------------------------
# Налаштування сторінки
# ------------------------------------------------------------
st.set_page_config(
    page_title="Панель менеджера дзвінків",
    page_icon="📞",
    layout="wide",  # Wide layout згідно вимог
)

# ------------------------------------------------------------
# URL-и інструментів (легко змінювати в одному місці)
# ------------------------------------------------------------
TOOL_1_URL = "https://fgm-report-mamfjktx277oqtvhgeqdwm.streamlit.app/#9367593b"
TOOL_2_URL = "https://distribution-of-applications.streamlit.app/"
TOOL_3_URL = "https://costories.streamlit.app/"

# Опис інструментів у структурі даних, щоб було легко додавати нові
TOOLS = [
    {
        "name": "Звіт за день",
        "description": "Формування звіту менеджера за день",
        "emoji": "📊",
        "url": TOOL_1_URL,
    },
    {
        "name": "Розподіл заявок",
        "description": "Автоматичний розподіл заявок між менеджера по обраному напрямку",
        "emoji": "⚙️",
        "url": TOOL_2_URL,
    },
    {
        "name": "Кошторис",
        "description": "Формування прорахунку для клієнта за допомогою кошторису",
        "emoji": "🤑",
        "url": TOOL_3_URL,
    },
]

# ------------------------------------------------------------
# Стилі для великих "карток" та читабельного інтерфейсу
# ------------------------------------------------------------
st.markdown(
    """
    <style>
      .tool-card {
        border: 1px solid #e6e6e6;
        border-radius: 12px;
        padding: 20px;
        min-height: 220px;
        background-color: #000000;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
      }
      .tool-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
      }
      .tool-description {
        color: #ffffff;
        margin-bottom: 1rem;
      }
      .stLinkButton > a {
        width: 100%;
        text-align: center;
        font-size: 1rem;
        padding: 0.7rem 1rem;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Заголовок і підзаголовок
# ------------------------------------------------------------
st.title("Панель менеджера дзвінків")
st.caption("Оберіть інструмент для роботи")

st.divider()

# ------------------------------------------------------------
# Відображення інструментів у колонках
# ------------------------------------------------------------
columns = st.columns(len(TOOLS), gap="large")

for col, tool in zip(columns, TOOLS):
    with col:
        st.markdown(
            f"""
            <div class="tool-card">
              <div class="tool-title">{tool['emoji']} {tool['name']}</div>
              <div class="tool-description">{tool['description']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Кнопка переходу у відповідний Streamlit інструмент
        st.link_button("Відкрити інструмент", tool["url"], use_container_width=True)

st.divider()

# Підказка для майбутнього масштабування
st.info("Щоб додати новий інструмент, додайте новий словник у список TOOLS.")
