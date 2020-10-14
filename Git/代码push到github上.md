## 创建新仓库push到github上

```bash
cd 项目目录下
git init
git add  .
git commit -m "first commit"
git branch -M master
git remote add origin github项目地址
git push -u origin master
```



## 将已有仓库push到github上

```bash
git remote add origin github项目地址
git branch -M master
git push -u master
```

