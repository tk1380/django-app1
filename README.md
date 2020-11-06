## ファイル作成1  
touch .env  

<ファイル内記述例>  
DEBUG=0
SECRET_KEY=hoge
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_DB=django_db
DATABASE_USER=test
DATABASE_PASSWORD=test
DATABASE_HOST=postgres
DATABASE_PORT=5432
DATABASE=postgres

## 実行
docker-compose up -d --build


## コマンド集
本番起動用  
docker-compose -f docker-compose.prod.yml down -v  
docker-compose -f docker-compose.prod.yml up -d --build  
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput  
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear  
.env.developmentの記述：VUE_APP_ROOT_API=http://127.0.0.1:1337/api/v1/  

開発起動用  
docker-compose -f docker-compose.yml exec django python manage.py makemigrations  
docker-compose -f docker-compose.yml exec django python manage.py migrate --noinput  
.env.developmentの記述：VUE_APP_ROOT_API=http://127.0.0.1:8000/api/v1/  


## 画面イメージ
<img src="https://user-images.githubusercontent.com/61681360/98380895-8abbb600-208c-11eb-8a17-963ce000e40c.png">
<img src="https://user-images.githubusercontent.com/61681360/98381026-aa52de80-208c-11eb-87b7-be1c4f4a7ad4.png">
<img src="https://user-images.githubusercontent.com/61681360/98381070-b5a60a00-208c-11eb-85bf-91f9e9b32f1d.png">
<img src="https://user-images.githubusercontent.com/61681360/98381126-ca829d80-208c-11eb-949d-cfb4f77a76c7.png">


<!-- 
コマンド集

単体テスト実行
python manage.py test app.test

SCSSファイル変更
python manage.py sass static/app/index.scss static/css/index.css

本番起動用
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear
.env.developmentの記述：VUE_APP_ROOT_API=http://127.0.0.1:1337/api/v1/

開発起動用
docker-compose -f docker-compose.yml exec django python manage.py makemigrations
docker-compose -f docker-compose.yml exec django python manage.py migrate --noinput
VUE_APP_ROOT_API=http://127.0.0.1:8000/api/v1/

コンテナ未使用時
python manage.py runserver --setting=config.settings.local
 -->