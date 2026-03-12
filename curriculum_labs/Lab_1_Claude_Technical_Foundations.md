# Lab 1: Technical Foundations & JSON Mode

**Objective:** Equip GTM new hires with the ability to leverage Claude for structured data extraction—a key use case for our enterprise clients.

---

### Phase 1: The Account Executive (AE) Challenge
**Task:** Use the Claude API to summarize a client call transcript into three bullet points.
* **Goal:** Understand Claude's reasoning capabilities and "Constitutional AI" guardrails.
* **Success Metric:** High-quality, safe, and professional summary.

### Phase 2: The Solutions Architect (SA) Challenge 
**Task:** Configure a System Prompt to ensure Claude *only* returns a valid JSON object.
* **Why this matters:** Our customers integrate Claude into their apps; if the output isn't valid JSON, their app crashes.
* **Required Keys:** `sentiment`, `next_steps`, `urgency_score`.

### Phase 3: The Customer Success (CS) Challenge
**Task:** Use the `max_tokens` parameter to force a concise response.
* **Goal:** Optimize for cost and latency (TCO optimization).
* **Validation:** Submissions exceeding 200 tokens will be flagged by the `certification_validator.py`.

---

## 🛠️ Submission Instructions
1. Run your prompt in the **Anthropic Console**.
2. Save the raw JSON response as `candidate_submission.json`.
3. Run the automated grader:
   ```bash
   python grading_engine/certification_validator.py --file candidate_submission.json
