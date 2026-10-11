#!/usr/bin/env python3
"""Score model CSV predictions against Wuguang ground truth."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


KEY_FIELDS = ("image_id", "item_index")
SCORED_FIELDS = ("name", "major", "category", "quantity", "color")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--truth", required=True, type=Path)
    parser.add_argument("--predictions", required=True, type=Path)
    return parser.parse_args()


def load(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    required = set(KEY_FIELDS + SCORED_FIELDS)
    if not rows:
        raise ValueError(f"{path} 没有数据")
    if not required.issubset(rows[0]):
        raise ValueError(f"{path} 缺少字段：{sorted(required - set(rows[0]))}")
    result: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        clean = {key: (value or "").strip() for key, value in row.items()}
        key = (clean["image_id"], clean["item_index"])
        if key in result:
            raise ValueError(f"{path} 存在重复主键：{key}")
        result[key] = clean
    return result


def macro_f1(truth: list[str], predicted: list[str]) -> float:
    labels = sorted(set(truth) | set(predicted))
    scores: list[float] = []
    for label in labels:
        tp = sum(t == label and p == label for t, p in zip(truth, predicted))
        fp = sum(t != label and p == label for t, p in zip(truth, predicted))
        fn = sum(t == label and p != label for t, p in zip(truth, predicted))
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        scores.append(2 * precision * recall / (precision + recall) if precision + recall else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


def main() -> int:
    args = parse_args()
    truth = load(args.truth)
    predictions = load(args.predictions)
    matched = sorted(set(truth) & set(predictions))
    if not matched:
        raise ValueError("标准答案与预测没有可匹配的 image_id + item_index")

    print("物光离线评测")
    print(f"- 标准答案物品数：{len(truth)}")
    print(f"- 成功匹配物品数：{len(matched)}")
    print(f"- 覆盖率：{len(matched) / len(truth):.1%}")

    total_differences = 0
    exact_items = 0
    for field in SCORED_FIELDS:
        correct = sum(truth[key][field] == predictions[key][field] for key in matched)
        print(f"- {field} 准确率：{correct / len(matched):.1%}")
    for key in matched:
        differences = sum(truth[key][field] != predictions[key][field] for field in SCORED_FIELDS)
        total_differences += differences
        exact_items += differences == 0
    print(f"- 完整物品准确率：{exact_items / len(truth):.1%}")
    print(f"- 平均需修改字段数：{total_differences / len(matched):.2f}")
    print(
        "- category Macro F1："
        f"{macro_f1([truth[key]['category'] for key in matched], [predictions[key]['category'] for key in matched]):.3f}"
    )

    missing = sorted(set(truth) - set(predictions))
    extra = sorted(set(predictions) - set(truth))
    if missing:
        print(f"- 遗漏物品：{len(missing)}")
    if extra:
        print(f"- 多报物品：{len(extra)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
