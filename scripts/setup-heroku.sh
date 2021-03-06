#!/bin/bash
ENV_NAME="fantasybooking"


unset PYTHONDONTWRITEBYTECODE
source `which virtualenvwrapper.sh`


workon $ENV_NAME
heroku create $ENV_NAME-prod
heroku buildpacks:add https://github.com/cyberdelia/heroku-geo-buildpack.git#1.3 -a $ENV_NAME-prod
heroku buildpacks:add heroku/nodejs -a $ENV_NAME-prod
heroku buildpacks:add heroku/python -a $ENV_NAME-prod

heroku addons:create sendgrid --app $ENV_NAME-prod

heroku addons:create heroku-redis:hobby-dev --app $ENV_NAME-prod
heroku addons:add heroku-postgresql --app $ENV_NAME-prod
heroku config:set ALLOWED_HOSTS="*" --app $ENV_NAME-prod
heroku config:set PYTHONHASHSEED=random --app $ENV_NAME-prod
heroku config:set AWS_SECRET_ACCESS_KEY="" --app $ENV_NAME-prod
heroku config:set AWS_ACCESS_KEY_ID="" --app $ENV_NAME-prod
heroku config:set AWS_STORAGE_BUCKET_NAME=$ENV_NAME-prod --app $ENV_NAME-prod
heroku config:set STRIPE_PUBLIC_KEY="" --app $ENV_NAME-prod
heroku config:set STRIPE_SECRET_KEY="" --app $ENV_NAME-prod
heroku config:set SECRET_KEY=`python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'` --app $ENV_NAME-prod
heroku config:set DJANGO_SETTINGS_MODULE=$ENV_NAME.$ENV_NAME.settings.heroku --app $ENV_NAME-prod

git remote add prod git@heroku.com:$ENV_NAME-prod.git
git push prod master
heroku run python manage.py migrate --app $ENV_NAME-prod

heroku fork --to $ENV_NAME-staging --from $ENV_NAME-prod
heroku fork --to $ENV_NAME-dev --from $ENV_NAME-prod

git remote add staging git@heroku.com:$ENV_NAME-staging.git
git remote add dev git@heroku.com:$ENV_NAME-staging.git

heroku config:set SECRET_KEY=`python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'` --app $ENV_NAME-dev
heroku config:set SECRET_KEY=`python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'` --app $ENV_NAME-staging

heroku config:set PYTHONHASHSEED=random --app $ENV_NAME-dev
heroku config:set AWS_SECRET_ACCESS_KEY="" --app $ENV_NAME-dev
heroku config:set AWS_ACCESS_KEY_ID="" --app $ENV_NAME-dev
heroku config:set AWS_STORAGE_BUCKET_NAME=$ENV_NAME-dev --app $ENV_NAME-dev
heroku config:set STRIPE_PUBLIC_KEY="" --app $ENV_NAME-dev
heroku config:set STRIPE_SECRET_KEY="" --app $ENV_NAME-dev

heroku config:set PYTHONHASHSEED=random --app $ENV_NAME-staging
heroku config:set AWS_SECRET_ACCESS_KEY="" --app $ENV_NAME-staging
heroku config:set AWS_ACCESS_KEY_ID="" --app $ENV_NAME-staging
heroku config:set AWS_STORAGE_BUCKET_NAME=$ENV_NAME-staging --app $ENV_NAME-staging
heroku config:set STRIPE_PUBLIC_KEY="" --app $ENV_NAME-staging
heroku config:set STRIPE_SECRET_KEY="" --app $ENV_NAME-staging

heroku config:set DJANGO_SETTINGS_MODULE=$ENV_NAME.$ENV_NAME.settings.heroku --app $ENV_NAME-dev
heroku config:set DJANGO_SETTINGS_MODULE=$ENV_NAME.$ENV_NAME.settings.heroku --app $ENV_NAME-staging

heroku dyno:type hobby --app $ENV_NAME-prod
heroku dyno:type hobby --app $ENV_NAME-staging
heroku dyno:type hobby --app $ENV_NAME-dev

heroku apps:transfer lightmatter --app $ENV_NAME-dev
heroku apps:transfer lightmatter --app $ENV_NAME-staging
heroku apps:transfer lightmatter --app $ENV_NAME-prod

heroku git:remote -r dev -a $ENV_NAME-dev
heroku git:remote -r staging -a $ENV_NAME-staging
