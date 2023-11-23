# Melingo Tarnslator Task
This web app allows users to see the translation of words into Spanish with some examples.

## Getting Started
### Using Code
note: installation may change a bit on different operating systems 

1. Clone the repository:
```
git clone https://github.com/AmyRayDroui/melingo-tarnslator-task.git
```
2. Install Backend dependencies:
```
cd backend
pip install django django-cors-headers
```
3. Initialize Backend DB:
```
python manage.py import_csv Entriesnodu.csv Examples.csv
```
4. Run Backend:
```
python manage.py runserver
```
5. Install the dependencies for the Frontend:
```
cd frontend
npm install
```
6. Run the Frontend:
```
npm run start
```
### Using Docker Images

1. Clone the images:
```
docker pull amyray/melingo-api
docker pull amyray/melingo-web
```
2. Run images, either by Docker Desktop with melingo-api port:8000 and  melingo-web port:3000 or:
```
docker run -p 8000:8000 amyray/melingo-api
docker run -p 3000:3000 amyray/melingo-web
```

### Using Docker Compose

1. Clone the repository:
```
git clone https://github.com/AmyRayDroui/melingo-tarnslator-task.git
```
2. Run docker-compose:
```
docker-compose up
```


The server will be available at http://localhost:8000.

The web app will be available at http://localhost:3000.

## Dependencies
### DB
* SQLite
### Backend
* Django
### Frontend
* React
* TailwindCSS
