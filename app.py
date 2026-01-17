import streamlit as st
import requests
import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL_NAME = "granite4"

SYSTEM_PROMPT = """
You are a Smart Waste Segregation Assistant for India.

Classify the given item into ONE category:
- Wet Waste
- Dry Waste (Recyclable)
- Dry Waste (Non-Recyclable)
- Hazardous Waste
- E-Waste

Bin color mapping:
Green = Wet Waste
Blue = Dry Waste
Red = Hazardous Waste
Yellow = E-Waste

Return output in this exact format:

Category: <one category>
Bin: <Green/Blue/Red/Yellow>
Recyclable: <Yes/No/Depends>
Instruction: <1 short disposal instruction>
Tip: <1 sustainability tip>
Confidence: <High/Medium/Low>

Rules:
- Keep the response short and clear.
- If unsure, Confidence: Low and say "Check local municipal rules".
- Do NOT ask for personal data.
"""

def ask_granite(item):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Item: {item}"}
        ],
        "temperature": 0.2
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=180)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def parse_output(text):
    fields = ["Category", "Bin", "Recyclable", "Instruction", "Tip", "Confidence"]
    data = {f: "" for f in fields}
    for f in fields:
        match = re.search(rf"{f}:\s*(.*)", text)
        if match:
            data[f] = match.group(1).strip()
    return data

def classify_item(item):
    raw = ask_granite(item)
    parsed = parse_output(raw)
    parsed["Item"] = item
    parsed["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parsed["Raw_Output"] = raw
    return parsed

# ---------------- UI ----------------
st.set_page_config(page_title="Waste Segregation Assistant", page_icon="♻️", layout="wide")

st.title("♻️ Smart Waste Segregation Assistant (Granite + Ollama)")
st.caption("SDG 12: Responsible Consumption & Production | AI-powered waste classification and disposal guidance")

# session state to store history
if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔍 Single Item Classification")
    item = st.text_input("Enter a waste item (example: banana peel, battery, chips packet):")

    if st.button("Classify Item"):
        if item.strip() == "":
            st.warning("Please enter an item name.")
        else:
            with st.spinner("Classifying using Granite..."):
                try:
                    result = classify_item(item)
                    st.session_state.history.append(result)

                    st.success("Classification Completed ✅")
                    st.write(f"**Category:** {result['Category']}")
                    st.write(f"**Bin:** {result['Bin']}")
                    st.write(f"**Recyclable:** {result['Recyclable']}")
                    st.write(f"**Instruction:** {result['Instruction']}")
                    st.write(f"**Tip:** {result['Tip']}")
                    st.write(f"**Confidence:** {result['Confidence']}")

                except Exception as e:
                    st.error("Error: Make sure Ollama is running and granite4 is available.")
                    st.code(str(e))

with col2:
    st.subheader("📦 Bulk Classification")
    bulk_text = st.text_area(
        "Enter multiple items (one per line):",
        value="banana peel\nplastic bottle\nchips packet\nbattery\nused mask",
        height=180
    )

    if st.button("Classify Bulk Items"):
        items = [x.strip() for x in bulk_text.split("\n") if x.strip()]
        if len(items) == 0:
            st.warning("Please enter at least one item.")
        else:
            with st.spinner("Classifying bulk items..."):
                for it in items:
                    try:
                        result = classify_item(it)
                        st.session_state.history.append(result)
                    except Exception as e:
                        st.error(f"Failed for item: {it}")
                        st.code(str(e))
            st.success("Bulk classification completed ✅")

st.markdown("---")

st.subheader("📜 Classification History")
if len(st.session_state.history) == 0:
    st.info("No classifications yet. Try classifying an item above.")
else:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df[["Timestamp", "Item", "Category", "Bin", "Recyclable", "Confidence"]], use_container_width=True)

    # Download CSV
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Results CSV", data=csv_data, file_name="waste_segregation_results.csv", mime="text/csv")

    st.subheader("📊 Analytics")
    category_counts = df["Category"].value_counts()

    fig, ax = plt.subplots()
    category_counts.plot(kind="bar", ax=ax)
    ax.set_title("Waste Category Distribution")
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.markdown("---")
st.subheader("🛡️ Responsible AI Notes")
st.write("""
- This assistant does not collect personal user data.  
- Output may vary by city rules; users should verify local municipal guidelines.  
- Provides safe handling instructions for hazardous and e-waste items.  
""")
