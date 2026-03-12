# 🚀 Anthropic GTM Technical Productivity Framework

This repository serves as a functional prototype for a **Technical Sales Onboarding Factory**. It is designed to solve the "Technical Fluency Gap" for global Go-To-Market (GTM) teams scaling in high-growth AI environments.

---

## 🎯 The Strategic Problem
As AI models like Claude evolve, GTM teams (Sales, Customer Success, Applied AI) must move beyond high-level pitches to deep technical mastery of APIs, Tool Use, and Context Management. Manual onboarding and certification cannot scale at Anthropic’s velocity. 

This framework automates the "Human-in-the-loop" bottleneck of technical enablement, ensuring every hire is "Claude-Fluent" from day one.


---

## 🛠️ Core Components

### 1. Tiered Curriculum (`/curriculum_labs`)
A hands-on, API-first lab series designed for different technical personas. These modules transition hires from basic prompting to complex JSON-mode extractions and Tool Use.
* **AE Track:** Focus on reasoning, prompt engineering, and "Constitutional AI" basics.
* **SA Track:** Focus on structured JSON output, system prompt engineering, and developer-first workflows.
* **CS Track:** Focus on token efficiency, latency optimization, and enterprise TCO reduction.

### 🤖 2. Automated Validation Engine (`/grading_engine`)
A Python-based **Certification Validator** that removes the need for manual grading by Subject Matter Experts (SMEs). This engine programmatically enforces production standards for every certification submission, checking for JSON schema validity and token constraints.

### 📊 3. Continuous Improvement Analytics (`/analytics`)
The **Program Health Dashboard** analyzes certification data to identify curriculum friction. This closes the loop between "Enablement" and "Productivity," allowing for data-driven curriculum iterations based on real-world candidate performance.

---

## 📈 Expected Business Impact

| Metric | Before Framework | With Framework |
| :--- | :--- | :--- |
| **SME Time Spent Grading** | 4-6 Hours / Hire | **0 Hours (Automated)** |
| **Time-to-Productivity** | 4 Weeks | **2 Weeks** |
| **Technical Accuracy** | Variable (Manual) | **Standardized (Programmatic)** |

---

## 🚀 Getting Started

1. **Clone the Framework:**
   ```bash
   git clone [https://github.com/abokov/anthropic-gtm-enablement-lab.git](https://github.com/abokov/anthropic-gtm-enablement-lab.git)
   ```

2. ** Initialize Environment:**

```bash
pip install -r requirements.txt
```


3. ** Execute a Certification Run:**

```bash
python grading_engine/certification_validator.py --file samples/submission_01.json
```

4. ** View Program Analytics:**

```bash
python analytics/onboarding_metrics_tracker.py
```
