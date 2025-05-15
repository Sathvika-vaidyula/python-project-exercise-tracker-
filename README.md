# 🏋️‍♀️ Exercise Tracker

This Python project uses the **Nutritionix API** to understand natural language descriptions of workouts and logs them to a **Google Sheet** using the **Sheety API**.

---

## 🚀 Features

- Take exercise descriptions in natural language (e.g., "I jogged for 30 minutes")
- Get structured data: duration, calories, exercise type
- Log exercise info (date, time, name, calories, duration) to a Google Sheet
- Uses Basic Authentication for secure sheet access

---

## 🛠️ Tech Stack

- Python
- [Nutritionix API](https://developer.nutritionix.com/docs/v2)
- [Sheety API](https://sheety.co)
- Google Sheets (via Sheety)
- Requests library

---

## 📥 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/exercise-tracker.git
cd exercise-tracker
prompt:
Enter the exercise:

input:
I did 20 minutes of walking
| Date       | Time     | Exercise | Duration | Calories |
| ---------- | -------- | -------- | -------- | -------- |
| 15/05/2025 | 18:42:33 | walking  | 20       | 252      |


