#!/usr/bin/env python3
"""Validate Wuguang's private image-evaluation labels with no dependencies."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


CATEGORIES = {
    "衣物": {"上装", "下装", "连衣裙", "外套", "鞋履", "包袋", "配饰", "其他衣物"},
    "物品": {"个人护理", "运动户外", "书籍文具", "兴趣收藏", "工具器材", "生活用品", "其他"},
    "数码": {"手机", "电脑", "平板", "摄影摄像", "影音设备", "智能设备", "游戏设备", "数码配件", "其他数码"},
}
DIFFICULTIES = {"single-clear", "multi-item", "occluded", "low-light"}
FIELDS = [
    "image_id",
    "item_index",
    "name",
    "major",
    "category",
    "quantity",
    "color",
    "difficulty",
    "notes",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("labels", type=Path, help="CSV ground-truth file")
    parser.add_argument("--images-dir", type=Path, help="Directory containing private images")
    return parser.parse_args()


def validate(path: Path, images_dir: Path | None = None) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    rows: list[dict[str, str]] = []
    if not path.is_file():
        return rows, [f"找不到标注文件：{path}"]

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            return rows, [f"表头必须严格为：{','.join(FIELDS)}"]
        seen_keys: set[tuple[str, int]] = set()
        indexes: dict[str, list[int]] = defaultdict(list)
        image_difficulty: dict[str, str] = {}
        for line_number, raw in enumerate(reader, start=2):
            row = {key: (value or "").strip() for key, value in raw.items()}
            rows.append(row)
            prefix = f"第 {line_number} 行"
            image_id = row["image_id"]
            if not image_id or Path(image_id).name != image_id:
                errors.append(f"{prefix}：image_id 必须是文件名")
            elif Path(image_id).suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".heic"}:
                errors.append(f"{prefix}：不支持的图片扩展名 {Path(image_id).suffix}")
            try:
                item_index = int(row["item_index"])
                if item_index < 1:
                    raise ValueError
            except ValueError:
                errors.append(f"{prefix}：item_index 必须是从 1 开始的整数")
                item_index = -1
            key = (image_id, item_index)
            if key in seen_keys:
                errors.append(f"{prefix}：重复主键 {image_id} + {item_index}")
            seen_keys.add(key)
            indexes[image_id].append(item_index)
            if not row["name"]:
                errors.append(f"{prefix}：name 不能为空")
            major = row["major"]
            if major not in CATEGORIES:
                errors.append(f"{prefix}：major 必须是衣物、物品或数码")
            elif row["category"] not in CATEGORIES[major]:
                errors.append(f"{prefix}：{row['category']} 不属于大类 {major}")
            try:
                quantity = int(row["quantity"])
                if quantity < 1:
                    raise ValueError
            except ValueError:
                errors.append(f"{prefix}：quantity 必须是正整数")
            if not row["color"]:
                errors.append(f"{prefix}：color 不能为空；无法判断时填“未知”")
            difficulty = row["difficulty"]
            if difficulty not in DIFFICULTIES:
                errors.append(f"{prefix}：difficulty 值无效")
            previous = image_difficulty.setdefault(image_id, difficulty)
            if previous != difficulty:
                errors.append(f"{prefix}：同一图片的 difficulty 必须一致")
            if images_dir and image_id and not (images_dir / image_id).is_file():
                errors.append(f"{prefix}：图片不存在 {images_dir / image_id}")

    for image_id, values in indexes.items():
        expected = list(range(1, len(values) + 1))
        if sorted(values) != expected:
            errors.append(f"{image_id}：item_index 应连续为 {expected}")
    return rows, errors


def main() -> int:
    args = parse_args()
    rows, errors = validate(args.labels, args.images_dir)
    if errors:
        print("标注检查失败：")
        for error in errors:
            print(f"- {error}")
        return 1
    image_difficulties = {row["image_id"]: row["difficulty"] for row in rows}
    print("标注检查通过")
    print(f"- 图片：{len(image_difficulties)} 张")
    print(f"- 物品：{len(rows)} 行")
    print(f"- 大类：{dict(Counter(row['major'] for row in rows))}")
    print(f"- 难度：{dict(Counter(image_difficulties.values()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
