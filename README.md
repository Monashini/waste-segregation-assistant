♻️ Smart Waste Segregation Assistant (Granite + Ollama + Streamlit)
📌 Project Overview

Improper waste segregation is one of the biggest reasons for poor recycling efficiency, overflowing landfills, and increased environmental pollution. Many people are unsure whether an item should go into wet waste, dry waste, hazardous waste, or e-waste, which leads to mixing of waste and unsafe disposal practices.

This project is an AI-powered Waste Segregation Assistant that helps users classify everyday waste items and provides the correct bin recommendation along with safe disposal instructions and sustainability tips. The system uses IBM Granite model (via Ollama local inference) and provides an interactive Streamlit UI for a smooth user experience.

This project is aligned with the UN Sustainable Development Goals (SDGs) and is built as part of the 1M1B AI for Sustainability Virtual Internship (in collaboration with IBM SkillsBuild & AICTE).

🎯 Problem Statement

Waste segregation is often ignored or done incorrectly because:

People don’t know which waste category an item belongs to

Multi-layer plastic, sanitary waste, and e-waste are frequently mixed with regular waste

Incorrect disposal reduces recycling and increases landfill load

Hazardous waste (masks, medicines, batteries, syringes) can harm sanitation workers

A simple and accessible AI assistant can help people make better disposal decisions instantly, improving recycling rates and reducing environmental impact.

🌍 SDG Alignment

This project supports the following Sustainable Development Goals:

SDG 12: Responsible Consumption and Production (Primary SDG)

SDG 11: Sustainable Cities and Communities

SDG 13: Climate Action

💡 Solution Description

The Smart Waste Segregation Assistant provides:
✅ Waste classification into one of the following categories:

Wet Waste

Dry Waste (Recyclable)

Dry Waste (Non-Recyclable)

Hazardous Waste

E-Waste

✅ Correct bin recommendation using common bin color mapping:

Green → Wet Waste

Blue → Dry Waste

Red → Hazardous Waste

Yellow → E-Waste

✅ Disposal instruction for safe handling
✅ Sustainability tip to encourage eco-friendly habits
✅ Confidence score (High / Medium / Low) to indicate reliability

🧠 AI Component (IBM Granite)

This project uses IBM Granite, a generative AI model, to:

Understand the waste item input using Natural Language Processing (NLP)

Categorize the item into the correct waste class

Generate short, clear disposal instructions

Provide awareness-based sustainability tips

Granite is executed locally using Ollama, and the assistant is accessed through an OpenAI-compatible API endpoint.

🖥️ Key Features
🔹 1. Single Item Classification

Users can enter any waste item (example: banana peel, battery, chips packet) and get:

Category

Bin recommendation

Disposal instruction

Sustainability tip

Confidence level

🔹 2. Bulk Waste Classification

Users can input multiple waste items (one per line), and the assistant classifies all of them at once.

🔹 3. Classification History

The system maintains a session-based history of all classified items for tracking.

🔹 4. Analytics Dashboard

The assistant provides a basic visualization of waste distribution by category using a bar chart.

🔹 5. CSV Export

Users can download the results as a CSV file for documentation and reporting.

🏗️ System Workflow (Architecture)

Step 1: User enters waste item(s)
Step 2: Streamlit UI sends input to Ollama local API
Step 3: IBM Granite processes the request using the prompt workflow
Step 4: Assistant returns structured output
Step 5: Results are stored in history + shown in table
Step 6: Analytics + CSV download are generated

🛠️ Technologies Used

IBM Granite Model (granite4)

Ollama (Local model inference)

Streamlit (UI development)

Python

Requests (API calls)

Pandas (data handling)

Matplotlib (visualization)

⚙️ Installation & Setup
✅ Prerequisites

Make sure you have:

Python 3.9+ installed

Ollama installed

granite4 model downloaded

1️⃣ Install Ollama

Download and install Ollama from the official website.

Check installation:

ollama --version

2️⃣ Download IBM Granite Model
ollama pull granite4


Check models:

ollama list

3️⃣ Install Python Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run app.py

🧪 Example Inputs

Try these in the app:

banana peel

plastic bottle

chips packet

used mask

battery

medicine strip

tube light

old mobile phone

broken glass

cardboard

📌 Sample Output Format

The assistant returns structured output like:

Category: Wet Waste
Bin: Green
Recyclable: No
Instruction: Place it in the wet waste bin for composting.
Tip: Composting reduces landfill waste.
Confidence: High

🛡️ Responsible AI Considerations

This project follows Responsible AI principles:

Privacy: No personal or sensitive data is collected

Transparency: Output includes clear category + bin mapping

Safety: Hazardous and e-waste outputs include safe disposal instructions

Limitations: Waste rules vary by location; low-confidence outputs advise checking local municipal rules

Bias Reduction: Suggestions are generic and do not target any community or group unfairly

📈 Expected Impact

If implemented at scale, this project can:

Improve correct waste segregation habits

Increase recycling efficiency

Reduce landfill waste and pollution

Improve safety for sanitation workers

Build awareness about responsible consumption and sustainability

🚀 Future Enhancements

Planned improvements include:

Image-based waste classification using Computer Vision

Location-based waste rules using real municipal datasets

Full RAG pipeline using policy documents and vector databases

Multi-language support (Tamil / Hindi / English)

Mobile-friendly deployment for public use
