# Result Express

Result Express is a Python-based tool designed to fetch university results using a student’s USN, bypass captchas, and send the results via WhatsApp. It automates the entire process, saving time and effort.

## Features

- Automated result fetching
- Captcha bypass using Easy-OCR
- WhatsApp integration to deliver results
- SGPA calculator

## Installation and Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Atharv-A2/Result-Express.git
```

### 2. Set Up a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd Result-Express
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scriptsctivate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Modify Student USNs

Update the `usn_list.txt` file with the USNs of the students for whom you want to fetch results.

### 5. Create Text Files

Create two additional text files:

- `name_list.txt`: Include the students’ names in this format:
  ```text
  <Name>
  ```
- `receiver_list.txt`: Include the corresponding phone numbers (with country code) in this format:
  ```text
  +91XXXXXXXXXX
  ```

### 6. Run the Script

Start the script by running:

```bash
python results.py
```

Sit back and let the script handle everything from fetching results to sending them via WhatsApp.

## Captcha Bypass

The script uses **Easy-OCR** to read and solve captchas. You can adjust the `captcha_to_text.py` script for different captcha formats as needed.

## License

This project is licensed under the MIT License.
