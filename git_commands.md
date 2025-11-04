# 🧠 Git Команди: Шпаргалка

## 🔧 Ініціалізація та конфігурація

### 📁 Ініціалізувати новий репозиторій
```
git init
```
### ⚙️ Налаштування користувача
```
git config --global user.name "Твоє Ім’я"
git config --global user.email "email@example.com"
```
## 📂 Робота з файлами
### ➕ Додати файл до індексу (staging area)
```
git add filename
```
### ➕ Додати всі зміни
```
git add .
```
### ❌ Видалити файл з індексу
```
git rm --cached filename
```
## 💾 Фіксація змін
### ✅ Зробити коміт
```
git commit -m "Опис змін"
```
### 📝 Змінити останній коміт
```
git commit --amend
```
## 🔍 Перегляд стану та історії
### 📌 Перевірити статус
```
git status
```
### 📜 Переглянути історію комітів
```
git log
```
### 🧾 Короткий лог
```
git log --oneline
```
## 🌿 Гілки
### ➕ Створити нову гілку
```
git branch new-branch
```
### 🔀 Перейти на гілку
```
git checkout new-branch
```
### 🔄 Створити та перейти одразу
```
git checkout -b new-branch
```
### ❌ Видалити гілку
```
git branch -d branch-name
```
## 🔗 Віддалені репозиторії
### 🔗 Додати віддалений репозиторій
```
git remote add origin https://github.com/user/repo.git
```
### 📥 Отримати зміни з віддаленого репозиторію
```
git fetch
```
### 🔄 Завантажити та об’єднати зміни
```
git pull
```
### 📤 Надіслати зміни
```
git push origin main
```
## 🔄 Злиття та ребейз
### 🔀 Злити гілку
```
git merge branch-name
```
### 🔁 Ребейз гілки
```
git rebase branch-name
```
## 🧹 Відкат змін
### ↩️ Відкотити файл до останнього коміту
```
git checkout -- filename
```
### ⏪ Скасувати останній коміт (залишити зміни)
```
git reset --soft HEAD~1
```
### ⏮️ Скасувати коміт і зміни
```
git reset --hard HEAD~1
```
## 🧪 Інше
### 🧪 Перевірити різницю між файлами
```
git diff
```
### 🧪 Перевірити різницю між комітами
```
git diff commit1 commit2
```
### 🧪 Перевірити різницю між гілками
```
git diff branch1..branch2
```