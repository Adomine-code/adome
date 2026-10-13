# adome

`adome` Python 包。

## 本地安装和打包

在项目目录执行，将 `ADOME_PYTHON` 替换为你的 Python 解释器绝对路径：

```bash
ADOME_PYTHON="/absolute/path/to/python"
"$ADOME_PYTHON" -m pip install --no-deps -e .
"$ADOME_PYTHON" -m pip install build twine
"$ADOME_PYTHON" -m build
"$ADOME_PYTHON" -m twine check --strict dist/*
```

构建产物位于 `dist/`，包含源码包和 wheel。

## 发布到 PyPI

[GitHub 仓库](https://github.com/Adomine-code/adome)通过
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/)发布到
[PyPI](https://pypi.org/project/adome/)。

PyPI 的 Publishing 设置与工作流对应如下：

| 设置 | 值 |
| --- | --- |
| Owner | `Adomine-code` |
| Repository name | `adome` |
| Workflow name | `publish.yml` |
| Environment name | `pypi` |

发布步骤：

1. 完成代码和说明，更新 `pyproject.toml` 中的 `version`，使用高于 PyPI 最新版本的未发布版本号。
2. 提交并推送到 GitHub。在 Actions 中手动运行 **Publish to PyPI**，检查构建结果；手动运行只构建，不上传到 PyPI。
3. 在 GitHub 创建并发布 Release，标签使用 `v<版本号>`，指向准备好的提交。工作流会构建、检查并上传到 PyPI。

普通提交、推送和 Release 草稿不会触发 PyPI 发布。
