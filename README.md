# ♻️ Smart Waste Segregation Assistant  
### IBM Granite + Ollama + Streamlit | SDG 12 Sustainability Project

![Status](https://img.shields.io/badge/Status-Completed-success)
![AI](https://img.shields.io/badge/Model-IBM%20Granite-blue)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![SDG](https://img.shields.io/badge/SDG-12%20Responsible%20Consumption%20%26%20Production-green)

---

## 📌 Project Overview
Improper waste segregation is one of the major reasons for **low recycling efficiency**, **increased landfill waste**, and **environmental pollution**. Many people are unsure whether an item belongs to **wet waste**, **dry waste**, **hazardous waste**, or **e-waste**, leading to incorrect disposal.

This project is an **AI-powered Waste Segregation Assistant** that helps users classify daily waste items and provides:
- ✅ Correct **waste category**
- ✅ Recommended **bin color**
- ✅ Safe **disposal instruction**
- ✅ Sustainability **eco-tip**
- ✅ Confidence score (**High / Medium / Low**)

Built using **IBM Granite (via Ollama local inference)** and deployed through an interactive **Streamlit UI**.

---

## 🎯 Problem Statement
Waste is often disposed incorrectly because:
- People do not know how to segregate waste properly
- Multi-layer plastic, sanitary waste, and e-waste get mixed with normal waste
- Recycling becomes difficult due to contamination
- Hazardous items can harm sanitation workers

A simple AI assistant can guide users instantly to improve segregation habits and reduce pollution.

---

## 🌍 SDG Alignment
This project supports:

✅ **SDG 12: Responsible Consumption and Production** *(Primary)*  
✅ **SDG 11: Sustainable Cities and Communities**  
✅ **SDG 13: Climate Action**

---

## 💡 Solution Summary
The assistant classifies waste into:

- **Wet Waste**
- **Dry Waste (Recyclable)**
- **Dry Waste (Non-Recyclable)**
- **Hazardous Waste**
- **E-Waste**

### 🗑️ Bin Color Mapping
| Category | Bin Color |
|---------|----------|
| Wet Waste | 🟩 Green |
| Dry Waste | 🟦 Blue |
| Hazardous Waste | 🟥 Red |
| E-Waste | 🟨 Yellow |

---

## 🧠 AI Component (IBM Granite)
This system uses **IBM Granite** to:
- Understand the waste item (NLP)
- Classify it into the correct category
- Generate disposal instructions and sustainability tips

Granite runs locally through **Ollama** using an OpenAI-compatible API.

---

## ✨ Key Features
✅ **Single Item Classification**  
Enter one waste item and get category + bin + disposal instruction.

✅ **Bulk Classification**  
Classify multiple waste items (one per line).

✅ **History Tracking**  
Stores all classifications in a session table.

✅ **Analytics Dashboard**  
Shows a bar chart of waste category distribution.

✅ **CSV Export**  
Download classification results for reports and documentation.

---

## 🏗️ System Workflow (Architecture)
```text
User Input (Item Name)
        ↓
Streamlit UI
        ↓
Ollama Local API (localhost:11434)
        ↓
IBM Granite Model (granite4)
        ↓
Structured Output (Category + Bin + Tips)
        ↓
History + Analytics + CSV Download

````md

♻️ Smart Waste Segregation Assistant
 IBM Granite + Ollama + Streamlit | SDG 12 Sustainability Project

---

 🛠️ Tech Stack
- IBM Granite (granite4)
- Ollama (Local inference)
- Streamlit (UI)
- Python
- Requests
-Pandas
- Matplotlib

---

⚙️ Installation & Setup

✅ 1) Install Ollama
Download and install Ollama.

Check:
```bash
ollama --version
````

---

### ✅ 2) Download Granite Model

```bash
ollama pull granite4
```

Verify:

```bash
ollama list
```

---

### ✅ 3) Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ 4) Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Inputs

Try these items in the UI:

* banana peel
* plastic bottle
* chips packet
* used mask
* battery
* medicine strip
* tube light
* old mobile phone
* broken glass
* cardboard

---

## 📌 Sample Output

```text
Category: Wet Waste
Bin: Green
Recyclable: No
Instruction: Place the banana peel in the green bin for composting.
Tip: Composting reduces landfill waste and methane emissions.
Confidence: High
```

---

## 🛡️ Responsible AI Considerations

This project follows responsible AI practices:

* 🔒 **Privacy:** No personal user data is collected
* 🔍 **Transparency:** Clear category + bin mapping is provided
* ⚠️ **Safety:** Hazardous and e-waste include safe handling instructions
* 📍 **Limitations:** Local disposal rules may vary; low confidence suggests checking municipal rules
* ⚖️ **Fairness:** Outputs are general and do not target any group unfairly

---

## 📈 Expected Impact

If used in homes/hostels/campuses, this assistant can:

* Improve correct waste segregation habits
* Increase recycling efficiency
* Reduce landfill waste and pollution
* Improve sanitation worker safety
* Promote sustainability awareness

---

## 🚀 Future Enhancements

Planned improvements:

* 📷 Image-based classification using Computer Vision
* 📍 Location-based municipal waste rules
* 📚 Full RAG pipeline with waste policy documents
* 🌐 Multi-language support (Tamil / Hindi / English)
* 📱 Mobile-friendly deployment

```
```
