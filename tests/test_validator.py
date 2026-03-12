import pytest
import json
import os
from grading_engine.certification_validator import AnthropicGTMValidator

# 🛠️ Fixtures: Creating temporary submission files for testing
@pytest.fixture
def valid_submission(tmp_path):
    d = tmp_path / "samples"
    d.mkdir()
    file = d / "valid.json"
    content = {
        "response_body": "{\"sentiment\": \"positive\", \"score\": 0.9}",
        "usage": {"output_tokens": 150}
    }
    file.write_text(json.dumps(content))
    return str(file)

@pytest.fixture
def invalid_submission(tmp_path):
    d = tmp_path / "samples"
    d.mkdir(exist_ok=True)
    file = d / "invalid.json"
    content = {
        "response_body": "This is not JSON",
        "usage": {"output_tokens": 1000}
    }
    file.write_text(json.dumps(content))
    return str(file)

# ✅ Test Case 1: Perfect Submission
def test_validator_pass_criteria(valid_submission):
    validator = AnthropicGTMValidator(valid_submission)
    result = validator.run_grading()
    
    assert result["status"] == "CERTIFIED"
    assert "✅ Lab 1 (JSON Mode): Passed." in result["logs"]

# ❌ Test Case 2: Multi-Failure (Bad JSON + High Tokens)
def test_validator_fail_criteria(invalid_submission):
    validator = AnthropicGTMValidator(invalid_submission)
    result = validator.run_grading()
    
    assert result["status"] == "RETRY REQUIRED"
    assert any("❌ Lab 1" in log for log in result["logs"])
    assert any("❌ Lab 2" in log for log in result["logs"])
