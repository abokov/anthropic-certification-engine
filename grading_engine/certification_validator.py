import json
import re

class AnthropicGTMValidator:
    """
    Automates the technical certification of GTM new hires by validating 
    their Claude API implementation against production standards.
    """
    
    def __init__(self, submission_file):
        with open(submission_file, 'r') as f:
            self.data = json.load(f)
        self.results = {"pass": True, "feedback": []}

    def validate_json_mode(self):
        """Ensures the hire knows how to force Claude into strict JSON output."""
        content = self.data.get("response_body", "")
        try:
            json.loads(content)
            self.results["feedback"].append("✅ Lab 1 (JSON Mode): Passed.")
        except ValueError:
            self.results["pass"] = False
            self.results["feedback"].append("❌ Lab 1: Output is not valid JSON. Ensure 'System Prompt' enforces JSON.")

    def check_token_efficiency(self, threshold=500):
        """Ensures the hire understands cost-optimization/token-frugality."""
        tokens = self.data.get("usage", {}).get("output_tokens", 0)
        if tokens < threshold:
            self.results["feedback"].append(f"✅ Lab 2 (Efficiency): Passed ({tokens} tokens).")
        else:
            self.results["pass"] = False
            self.results["feedback"].append(f"❌ Lab 2: Output too verbose ({tokens} tokens). Use 'Max Tokens' to limit cost.")

    def run_grading(self):
        print("🤖 Initializing Technical Certification Grading...")
        self.validate_json_mode()
        self.check_token_efficiency()
        
        status = "CERTIFIED" if self.results["pass"] else "RETRY REQUIRED"
        print(f"\n--- Final Result: {status} ---")
        for comment in self.results["feedback"]:
            print(comment)

# Example Usage
if __name__ == "__main__":
    # In production, this would be an automated GitHub Action triggered by a new hire's PR
    validator = AnthropicGTMValidator("candidate_submission.json")
    validator.run_grading()
