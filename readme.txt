... или создайте новый репозиторий в командной строке
echo "# GB_Pyton" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Romarom81/GB_Pyton.git
git push -u origin main
... или отправьте существующий репозиторий из командной строки
git remote add origin https://github.com/Romarom81/GB_Pyton.git
git branch -M main
git push -u origin main