import csv
from collections import Counter

class GTMProductivityTracker:
    """
    Analyzes onboarding data to identify friction points in the 
    Technical Sales curriculum and drive continuous improvement.
    """

    def __init__(self, log_file):
        self.log_file = log_file
        self.data = []

    def load_data(self):
        # Simulating reading from a system log or GitHub Action output
        with open(self.log_file, 'r') as f:
            reader = csv.DictReader(f)
            self.data = list(reader)

    def calculate_kpis(self):
        total_hires = len(self.data)
        passed = sum(1 for row in self.data if row['status'] == 'PASS')
        
        # Identify "The Gap": Which lab is causing the most friction?
        failures = [row['fail_reason'] for row in self.data if row['status'] == 'FAIL']
        common_bottleneck = Counter(failures).most_common(1)

        print("📊 --- GTM Technical Productivity Dashboard ---")
        print(f"Total New Hires: {total_hires}")
        print(f"Certification Rate: {(passed/total_hires)*100:.1f}%")
        
        if common_bottleneck:
            reason, count = common_bottleneck[0]
            print(f"⚠️ Primary Friction Point: '{reason}' ({count} occurrences)")
            print(f"💡 Recommendation: Update Lab '{reason}' documentation or add a refresher session.")

# Example CSV Structure for log_file (onboarding_results.csv)
# name,role,lab_id,status,fail_reason
# "John Doe","Sales",1,"PASS",""
# "Jane Smith","Success",2,"FAIL","JSON_MODE"
# "Bob Ross","Sales",2,"FAIL","JSON_MODE"

if __name__ == "__main__":
    # In practice, this runs weekly to provide data for the GTM Leadership meeting
    tracker = GTMProductivityTracker("onboarding_results.csv")
    # Generating mock data report
    tracker.data = [
        {"name": "Alice", "status": "PASS", "fail_reason": ""},
        {"name": "Bob", "status": "FAIL", "fail_reason": "JSON_MODE"},
        {"name": "Charlie", "status": "FAIL", "fail_reason": "JSON_MODE"},
        {"name": "Dave", "status": "PASS", "fail_reason": ""}
    ]
    tracker.calculate_kpis()
