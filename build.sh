echo "Building project..."
pip install -r requirements.txt
echo "Making migrations..."
python3.11 manage.py makemigrations --noinput
python3.11 manage.py migrate --noinput
echo "Collection statics..."
python3.11 manage.py collectstatic --noinput --clear
