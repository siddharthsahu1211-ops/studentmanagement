##################### API Observation Via Codespace URL
##################### API Observation Via Hopscotch
##################### API Observation Via CURL

# A. Get All Students
curl -X GET "https://urban-broccoli-p7p7wjq5v7qhr96v-8000.app.github.dev/api/students"

# B. Get One Student
curl -X GET "https://urban-broccoli-p7p7wjq5v7qhr96v-8000.app.github.dev/api/students/1"

# C. Create Student
curl -X POST "https://urban-broccoli-p7p7wjq5v7qhr96v-8000.app.github.dev/api/students" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "aloic@example.com",
    "course": "Computer ",
    "year": 44
  }'

# D. Update Student
curl -X PUT "https://urban-broccoli-p7p7wjq5v7qhr96v-8000.app.github.dev/api/students/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Updated",
    "email": "alice_new@example.com",
    "course": "Data Science",
    "year": 3
  }'

# E. Delete Student
curl -X DELETE "https://fantastic-orbit-x57r7j9g4477h9x4-8000.app.github.dev//api/students/1"


##################### DB Observation Via SQLite Web
- install https://github.com/coleifer/sqlite-web
- pip install sqlite-web
- sqlite_web students.db