# Next-gen Health Management System (NHMS)

A modular Django-based platform delivering end-to-end healthcare support—from patient and clinic onboarding to AI-powered diagnostics, home remedy suggestions, organ donation tracking, and interactive mapping of healthcare facilities.

---

## Table of Contents

1. [Overview](#overview)  
2. [Tech Stack](#tech-stack)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Setup](#installation--setup)  
5. [Configuration](#configuration)  
6. [Project Structure](#project-structure)  
7. [Usage](#usage)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Contact](#contact)

---

## Overview

NHMS is designed to streamline healthcare workflows and empower users with intelligent tools:

- **User & Clinic Authentication**  
  Secure signup/login for patients, clinics, and hospitals.

- **AI-Powered Diagnostics**  
  Image- and data-driven disease prediction (ECG arrhythmia, cataracts, tuberculosis, diabetes risk, tumor segmentation, simulated AIDS biomarkers).

- **Home Remedy Recommendations**  
  Natural treatment suggestions based on user symptoms.

- **Organ Donation & Search**  
  Donor registration, blood-type matching, proximity-based donor lookup.

- **Facility Mapping & Routing**  
  Compute shortest driving routes to hospitals using real road-network graphs (Mizoram, India).

---

## Tech Stack

- **Backend**: Python 3.x, Django 3.x  
- **AI/ML**: PyTorch, TorchScript models  
- **Data Processing**: OpenCV, PIL, GeoPandas, NetworkX, OSMnx  
- **Frontend**: Django Templates (HTML5, CSS3, JavaScript, Bootstrap optional)  
- **Database**: SQLite (development)  
- **Deployment**: Procfile (Heroku)

---

## Prerequisites

- Python 3.8+  
- pip (or Pipenv)  
- Git

---

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/ganapathi1578/Next-gen_health_management_system.git

# 2. Change into project directory
cd Next-gen_health_management_system

# 3. (Optional) Create & activate virtual environment
python3 -m venv env
# macOS/Linux:
source env/bin/activate
# Windows:
env\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Create media directory for uploads
mkdir -p media uploads

# 7. Run development server
python manage.py runserver

# 8. Open in browser:
#    http://127.0.0.1:8000/
```

---

## Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Open `.env` and set the following variables:

```ini
SECRET_KEY=<your-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,<your-domain.com>
```

> **Note:** For production, update the `DATABASES` setting in `medcare/settings.py` to use PostgreSQL, MySQL, or another production-grade database.

---

## Project Structure

```text
Next-gen_health_management_system/
├── medcare/                 # Core Django project (settings, URLs)
├── landingpage/             # Auth & landing pages
├── diseaseprediction/       # AI inference endpoints & forms
├── homeremedies/            # Symptom → remedy lookup
├── organavailability/       # Donor registration & search
├── mapthings/               # OSMnx & NetworkX routing scripts
├── templates/               # Shared HTML templates
├── static/                  # CSS, JS, images
├── media/                   # Uploaded files for prediction
├── manage.py                # Django CLI entrypoint
├── requirements.txt         # Python dependencies
└── Procfile                 # Deployment config (Heroku)
```

---

## Usage

### Signup & Login

1. Visit `/signup/` to create a Patient, Clinic, or Hospital account.  
2. Secure login at `/login/`.

### AI Diagnostics

- Go to `/diseaseprediction/`, choose modality (ECG, X‑ray, etc.), upload your image/data, and view results.

### Home Remedies

- Navigate to `/homeremedies/`, enter symptoms, and receive natural remedy suggestions.

### Organ Search

- Open `/organavailability/`, filter by organ & blood group, and find the nearest donor.

### Routing to Facilities

- Use the built-in map interface to calculate shortest driving routes to registered hospitals.

---

## Contributing

1. Fork the repository.  
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

Please follow PEP8 guidelines and include tests for any new functionality.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

**Author**: Lakshmi Ganapathi Kodi  
**Email**: ganapathi1578@example.com

