#!/usr/bin/env python3
# update_readme.py

import os
import argparse
import re

# 可配置的需要排除的文件夹或文件名
EXCLUDE_NAMES = {'.git', 'bin'}


def build_tree(dir_path: str, root_dir: str, github_base: str | None, prefix: str = "") -> list[str]:
    """
    递归生成 dir_path 下的文件/目录树，输出 markdown 格式的链接。
    跳过以 '.' 开头的隐藏文件/文件夹及 EXCLUDE_NAMES 内的名称。
    github_base: GitHub 仓库链接根，如 'https://github.com/user/repo', 不含尾部 '/'.
    """
    try:
        entries = sorted(
            [e for e in os.listdir(dir_path)
             if not e.startswith('.') and e not in EXCLUDE_NAMES]
        )
    except PermissionError:
        return []

    lines = []
    for idx, name in enumerate(entries):
        path = os.path.join(dir_path, name)
        rel_path = os.path.relpath(path, root_dir).replace('\\', '/')
        is_dir = os.path.isdir(path)
        connector = "└── " if idx == len(entries) - 1 else "├── "
        display = f"{name}/" if is_dir else name
        if github_base:
            # 仓库页面链接，目录指向 tree，文件指向 blob
            kind = 'tree' if is_dir else 'blob'
            link = f"{github_base}/{kind}/main/{rel_path}"
        else:
            # 本地相对链接
            link = f"./{rel_path}/" if is_dir else f"./{rel_path}"
        md = f"[{display}]({link})"
        lines.append(f"{prefix}{connector}{md}")
        if is_dir:
            extension = "    " if idx == len(entries) - 1 else "│   "
            lines.extend(build_tree(path, root_dir, github_base, prefix + extension))
    return lines


def generate_structure_block(root_dir: str, github_base: str | None, root_name: str = None) -> str:
    """
    生成整个项目结构的 markdown 代码块文本（含 ```）。
    github_base: GitHub 仓库根链接或 None。
    """
    if root_name is None:
        root_name = os.path.basename(os.path.abspath(root_dir))
    header = f"{root_name}/"
    tree_lines = [header]
    tree_lines += build_tree(root_dir, root_dir, github_base)
    return "```\n" + "\n".join(tree_lines) + "\n```"


def replace_structure_in_readme(readme_path: str, new_block: str) -> None:
    """
    将 README.md 中 “## 项目结构” 下的第一个 ```...``` 区块替换为 new_block。
    """
    content = open(readme_path, encoding="utf-8").read()
    pattern = re.compile(
        r"(## 项目结构\s*)(```[\s\S]*?```)",
        re.MULTILINE
    )
    new_content, count = pattern.subn(r"\1" + new_block, content, count=1)
    if count == 0:
        raise RuntimeError("未在 README.md 中找到 '## 项目结构' 及其代码块，请检查文档格式。")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    parser = argparse.ArgumentParser(description="自动更新 README.md 中的项目结构目录树，支持 GitHub 链接格式")
    parser.add_argument(
        "--root", "-r", default=".",
        help="项目根目录路径，默认为当前目录"
    )
    parser.add_argument(
        "--readme", "-m", default="README.md",
        help="README 文件路径，默认为当前目录下的 README.md"
    )
    parser.add_argument(
        "--github-base", "-g", default="https://github.com/wu-uk/ACM-Wheels/tree/main",
        help="GitHub 仓库链接根，如 'https://github.com/user/repo'，不含尾部 '/'，提供后生成在线 URL"
    )
    args = parser.parse_args()

    root_dir = args.root
    readme_path = args.readme
    github_base = args.github_base

    if not os.path.isdir(root_dir):
        print(f"错误：指定的根目录不存在：{root_dir}")
        return
    if not os.path.isfile(readme_path):
        print(f"错误：未找到 README 文件：{readme_path}")
        return

    print("正在生成项目结构……")
    new_block = generate_structure_block(root_dir, github_base)
    print("正在更新 README.md……")
    replace_structure_in_readme(readme_path, new_block)
    print("✅ README.md 更新完成！")

if __name__ == "__main__":
    main()
