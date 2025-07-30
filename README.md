# VersionHub

## Installation

```bash
git clone https://github.com/yourusername/versionhub.git
cd versionhub
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver