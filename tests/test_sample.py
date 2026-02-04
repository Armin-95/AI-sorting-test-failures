import pytest
import time
import random

# -------------------------
# Authentication failures
# -------------------------

def test_login_invalid_credentials():
    assert False, "Login failed: invalid username or password"

def test_login_token_expired():
    assert False, "Authentication error: access token has expired"

def test_login_missing_token():
    assert False, "Authentication error: no token provided"

# -------------------------
# Timeout / performance issues
# -------------------------

def test_login_timeout():
    time.sleep(0.1)
    raise TimeoutError("Login request timed out after 30 seconds")

def test_payment_timeout():
    time.sleep(0.1)
    raise TimeoutError("Payment service did not respond in time")

def test_search_api_slow_response():
    raise TimeoutError("Search API response exceeded timeout threshold")

# -------------------------
# Authorization / permission issues
# -------------------------

def test_payment_unauthorized():
    assert False, "Payment API returned 401 Unauthorized"

def test_admin_access_forbidden():
    assert False, "Access denied: user does not have admin privileges"

# -------------------------
# Data / database issues
# -------------------------

def test_order_count_mismatch():
    expected = 5
    actual = 7
    assert actual == expected, "Database error: order count mismatch"

def test_user_record_not_found():
    assert False, "Database error: user record not found"

def test_duplicate_record_error():
    assert False, "Database constraint violation: duplicate key value"

# -------------------------
# UI / frontend issues
# -------------------------

def test_submit_button_missing():
    assert False, "UI error: Submit button not found on page"

def test_login_field_not_visible():
    assert False, "UI error: Username input field is not visible"

def test_modal_not_loaded():
    assert False, "UI error: confirmation modal did not load"

# -------------------------
# API validation issues
# -------------------------

def test_invalid_response_schema():
    assert False, "API error: response schema validation failed"

def test_missing_required_field():
    assert False, "API error: required field 'email' is missing"

def test_unexpected_status_code():
    assert False, "API error: expected status 200 but received 500"

# -------------------------
# Flaky / intermittent failures
# -------------------------

def test_random_network_issue():
    assert random.choice([True, False]), "Intermittent network failure"

def test_intermittent_ui_render():
    assert random.choice([True, False]), "UI rendering failed intermittently"
