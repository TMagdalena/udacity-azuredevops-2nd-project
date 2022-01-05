mkdir ci-cd-repo
cd ci-cd-repo/
git init
git clone git@github.com:TMagdalena/udacity-azuredevops-2nd-project.git

python3 -m venv ~/.ci-cd
source ~/.ci-cd/bin/activate
make all

az webapp up -n myappservice6

git status
git add README.md
git commit -m "update README.md"
git push

chmod +x make_predict_azure_app.sh
./make_predict_azure_app.sh
az webapp log tail
