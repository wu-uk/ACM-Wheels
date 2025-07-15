#!/usr/bin/env python3
# update_readme.py

import os
import argparse
import re

# 可配置的需要排除的文件夹或文件名
EXCLUDE_NAMES = {'.git', 'bin'}

def build_list(dir_path: str, root_dir: str, github_base: str, indent: int = 0) -> list[str]:
    """
    递归生成 dir_path 下的文件/目录的 markdown 无序列表，每行以 '-' 开头并缩进。
    """
    try:
        entries = sorted(
            [e for e in os.listdir(dir_path)
             if not e.startswith('.') and e not in EXCLUDE_NAMES]
        )
    except PermissionError:
        return []

    lines = []
    for name in entries:
        path = os.path.join(dir_path, name)
        rel_path = os.path.relpath(path, root_dir).replace('\\', '/')
        is_dir = os.path.isdir(path)
        display = f"{name}/" if is_dir else name
        kind = 'tree' if is_dir else 'blob'
        url = f"{github_base}/{kind}/main/{rel_path}" if github_base else (
            f"./{rel_path}/" if is_dir else f"./{rel_path}"
        )
        lines.append(f"{'  ' * indent}- [{display}]({url})")
        if is_dir:
            lines.extend(build_list(path, root_dir, github_base, indent + 1))
    return lines


def generate_structure_block(root_dir: str, github_base: str, root_name: str = None) -> str:
    """
    生成整个项目结构的 markdown 无序列表文本，不含代码块标记。
    """
    if root_name is None:
        root_name = os.path.basename(os.path.abspath(root_dir))
    header = f"- {root_name}/"
    lines = [header]
    lines += build_list(root_dir, root_dir, github_base, indent=1)
    return "\n".join(lines)


def replace_structure_in_readme(readme_path: str, new_block: str) -> None:
    """
    将 README.md 中 “## 项目结构” 小节内的内容替换为 new_block。
    匹配“## 项目结构”到下一个二级标题之间的所有内容。
    """
    content = open(readme_path, encoding="utf-8").read()
    pattern = re.compile(
        r"(## 项目结构[\s\S]*?)(?=\n## )",
        re.MULTILINE
    )
    replacement = f"## 项目结构\n\n{new_block}\n"
    new_content, count = pattern.subn(replacement, content, count=1)
    if count == 0:
        raise RuntimeError("未在 README.md 中找到 '## 项目结构' 区块，请检查文档格式。")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    parser = argparse.ArgumentParser(description="自动更新 README.md 中的项目结构目录树，Markdown 无序列表格式")
    parser.add_argument(
        "--root", "-r", default=".",
        help="项目根目录路径，默认为当前目录"
    )
    parser.add_argument(
        "--readme", "-m", default="README.md",
        help="README 文件路径，默认为当前目录下的 README.md"
    )
    parser.add_argument(
        "--github-base", "-g",
        default="https://github.com/wu-uk/ACM-Wheels/blob/main",
        help="GitHub 仓库链接根，默认为 https://github.com/wu-uk/ACM-Wheels/blob/main"
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
