## 创建新仓库push到github上

```bash
cd 项目目录下
git init
git add  .
git commit -m "first commit"
git branch -M main
git remote add origin github项目地址
git push -u origin main
```



## 将已有仓库push到github上

```bash
git remote add origin github项目地址
git branch -M main
git push -u origin main
```





```bash
# 本地分支重命名
git branch -m old new

git pull origin main 
git pull github项目地址 --allow-unrelated-histories

git remote -v
```

