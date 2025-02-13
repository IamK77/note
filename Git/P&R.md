# Pull & Request

Pull & Request 是一种开源协作方式, 是一种通过提交代码来参与项目的方式。

## Fork

Fork 是 GitHub 对一个项目的拷贝, 拷贝后的项目会出现在你的仓库中.    
Fork 项目的目的是为了让你可以在不影响原项目的情况下进行修改.    

Fork 在 GitHub 上的操作是点击项目右上角的 Fork 按钮.

## Pull

Pull 是指从一个项目中获取最新的更改, 这个操作会将原项目的更改同步到你的项目中.

第一次拉取项目时, 需要先将项目克隆到本地, 然后再进行拉取操作.

```
git clone https://github.com/username/repo.git
```

之后拉取项目的最新更改, 只需要在项目目录下执行以下命令.

```
git pull
```

## Request

Request 是指将你的更改提交到原项目中, 这个操作需要通过 Pull Request 来完成.

在本地修改完项目后, 需要将更改提交到 GitHub 上.

```
git add .

git commit -m "Your commit message"

git push
```

然后在 GitHub 上你Fork出的仓库中, 点击 Pull Request 按钮, 填写相关信息后提交即可.
