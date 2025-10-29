# 🌐 CamSnare Radar

Developed by Anjali Patlan |

# 🛰️ Overview

CamSnare Radar is a personal project developed with Elevate Labs, designed to detect and visualize potential hidden surveillance devices using an interactive web interface.
Built with Python (FastAPI), HTML/CSS/JavaScript, and a radar-style animation dashboard, it combines visual awareness with real-time scanning functionality.
The project aims to evolve into a fully functional online system offering secure and intelligent camera detection for personal and civic privacy applications.

---

# 🚀 Features

- 🧭 *Radar Visualization* — Displays detected devices in an interactive radar animation.
-🔍 *Hidden Camera Detection* — Scans for potential surveillance devices via Bluetooth and Wi-Fi signals.
-🌍 *World Map Awareness View* — Integrates geographical visualizations for global or room-level detection.
-🛡️ *Privacy-first Interface* — No personal data is stored or shared.
-💻 *Web-Ready Deployment* — Hosted via Render for live online access.

# 📁 Project Structure
Camsnare/
│
├── app.py\                        # Main Flask/FastAPI application entry point\
├── Fusion_Engine.py\              # Core backend fusion logic for device detection\\
│
├── bluetooth_scan.py\             # Bluetooth-based camera signal detection
├── wifi_scan.py\                  # Wi-Fi scanning and analysis module\
│
├── requirements.txt\              # Project dependencies\
├── LICENSE\                       # MIT License file\
├── README.md\                     # Project documentation\
│
├── static/\                       # Frontend static assets\
│   ├── css/\
│   │   └── style.css\             # Custom styles for layout and visuals\
│   │
│   ├── js/\
│   │   └── script.js\             # JavaScript for radar animation and interactivity\
│   │
│   └── images/\
│       ├── hero_image.png\        # Homepage hero banner image\
│       ├── shaded_bar.jpeg\       # Gradient divider / visual bar element\
│       ├── world_map.png\         # World map background for detection visualization\
│       └── Digital Security Image.png\  # Sidebar illustration for security concept\
│
├── templates/\                    # HTML templates rendered by Flask\
│   └── index.html\                # Main webpage structure and content\
│
└── data/\                         # (Optional) Folder for scan results or databases\
    └── detections.db\             # Future database for detected devices\



# 🧰 Tech Stack

| Layer               | Technology              |
| ------------------- | ----------------------- |
| **Backend**         | Python (FastAPI)        |
| **Frontend**        | HTML5, CSS3, JavaScript |
| **Visualization**   | Canvas-based Radar UI   |
| **Deployment**      | Render Cloud            |
| **Version Control** | GitHub                  |


# 🌐 Deployment

*Live Deployment (Render):*
   Deployed via Render using FastAPI.
   Start Command:
       uvicorn app:app --host 0.0.0.0 --port 10000
   Runtime: Python 3.x
   Automatic redeploy on GitHub push.

## 📦 Use Cases

| Scenario                      | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| 🏨 **Room Security**          | Detect possible hidden cameras in hotel rooms or rentals. |
| 🏙️ **Civic Transparency**    | Map surveillance device density in public spaces.          |
| 🧳 **Traveler Safety**        | Scan new environments for unauthorized surveillance.      |
| 🔬 **Research & Development** | Explore privacy and AI ethics in real-world contexts.     |


# 🔮 Future Roadmap
🌐 Integration with mobile devices for live scanning.
🔥 Enhanced AI-based camera signal detection.
🧠 Voice alert and notification system.
🛰️ 3D radar and thermal visualization interface.
☁️ Secure cloud-based scan storage.

# ⚖️ Ethical Statement

CamSnare Radar is an educational and awareness-based tool.
It must only be used for ethical, personal, and research purposes.
Unauthorized scanning or interference with others' devices is strictly prohibited.

# 👩‍💻 Author

Anjali Patlan
Student | Developer | AI Enthusiast
Collaborating with Elevate Labs

“Don’t just guess — scan with confidence.”


# 📜 License

This project is licensed under the MIT License.
See the LICENSE file for details.
