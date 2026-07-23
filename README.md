  # UI & API Test Automation Demonstration Project

A fragment of a real automated testing project.

### 🛠 Stack
*   **Language:** Python 3.12+
*   **UI Testing:** Selenium WebDriver 4.x
*   **API Testing:** Requests 2.x
*   **Test Runner:** PyTest 9.x
*   **Test Data Generation:** Faker
*   **Reporting:** Allure Report

### 🎯 Test Scope
*   **UI Tests:**
    *   End-to-end positive and negative scenarios for form submissions.
*   **API Tests:**
    *   Verifying the availability and functionality of all active course links using Requests library.

### 🚀 Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/hetken/amrita-training-center
   cd amrita-training-center
   ```
2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run tests:**
   ```bash
   pytest --alluredir=allure-results
   ```
5. **Generate Allure Report** (requires Allure CLI installed):
   ```bash
   allure serve allure-results
   ```

