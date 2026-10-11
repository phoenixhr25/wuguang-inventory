# 物光图片识别评测集（入门版）

这个目录用于学习第一个 MLE 闭环：先定义正确答案，再评估模型。当前不会连接任何 AI，也不会上传照片。

## 先理解三个词

- **样本（sample）**：一张待识别照片。
- **标准答案（ground truth）**：你人工确认的名称、分类、数量和颜色。
- **指标（metric）**：模型答案与标准答案相差多少。

模型看起来“挺聪明”不等于可用。固定评测集可以让不同模型、提示词和版本在相同照片上比较。

## 隐私边界

真实照片放在 `private_images/`，真实标注保存为 `private_labels.csv`。两者已加入 `.gitignore`，不会随正常 Git 提交进入公开仓库。

拍摄时仍应避免：

- 人脸、镜面反射和家庭成员；
- 门牌、地址、快递单和身份证件；
- 设备序列号、二维码、票据和账号信息；
- 能精确判断住址或日常行程的背景。

提交前始终运行：

```bash
git status --short
```

若输出中出现真实照片或 `private_labels.csv`，立即停止提交并检查 `.gitignore`。

## 30 张照片怎么分配

| 难度 | 张数 | 拍摄方式 |
|---|---:|---|
| `single-clear` | 15 | 单件物品、主体完整、光线正常 |
| `multi-item` | 5 | 一张图里有 2–4 件可区分物品 |
| `occluded` | 5 | 物品有部分遮挡，但人仍能判断 |
| `low-light` | 5 | 光线较暗或背景较复杂 |

尽量覆盖衣物、物品和数码三个大类。第一轮不追求均衡训练集，因为这些照片只用于评测，不用于训练。

## 第一步：建立私人目录

在仓库根目录执行：

```bash
mkdir -p ml/eval/private_images
cp ml/eval/labels_template.csv ml/eval/private_labels.csv
```

把照片改名为：

```text
001.jpg
002.jpg
...
030.jpg
```

照片编号不表达分类，避免无意中把答案泄露给未来程序。

## 第二步：人工填写标准答案

用 Numbers、Excel 或文本编辑器打开 `private_labels.csv`。一张照片中有几件目标物品，就填写几行；用 `item_index` 从 1 开始编号。

例如，`016.jpg` 中有一件衬衫和一条裤子：

```csv
image_id,item_index,name,major,category,quantity,color,difficulty,notes
016.jpg,1,浅蓝色长袖衬衫,衣物,上装,1,浅蓝,multi-item,
016.jpg,2,黑色直筒裤,衣物,下装,1,黑色,multi-item,
```

### 标注原则

1. 只写照片中能够确认的事实，不猜品牌、价格和材质。
2. `name` 使用普通人能复核的名称，不追求商品标题。
3. `quantity` 是该行同类物品的可见数量。
4. `color` 填主要颜色；无法判断时写 `未知`。
5. 多物品照片按从左到右、从上到下编号。
6. 同一套规则应用于全部照片，不为某个模型修改答案。

完整字段与枚举见 [SCHEMA.md](SCHEMA.md)。

## 第三步：检查标注

```bash
python3 ml/eval/validate_labels.py \
  ml/eval/private_labels.csv \
  --images-dir ml/eval/private_images
```

成功时会显示照片数、物品行数和难度分布。错误会指出具体行号。

## 第四步：以后再评估模型

未来模型输出也保存为同样的 CSV 主键：`image_id + item_index`。然后运行：

```bash
python3 ml/eval/score_predictions.py \
  --truth ml/eval/private_labels.csv \
  --predictions ml/eval/private_predictions-v1.csv
```

首轮指标：

- **字段准确率**：名称、大类、二级分类、数量、颜色分别答对多少；
- **完整物品准确率**：一件物品的五个字段是否全部正确；
- **分类 Macro F1**：每个二级分类一视同仁，避免大类样本掩盖小类错误；
- **平均需修改字段数**：用户每确认一件物品平均要改几处；
- **覆盖率**：模型是否遗漏标准答案中的物品。

延迟和调用成本要等真正调用模型后记录，不能从标注文件推断。

## 完成标准

第一阶段完成不要求运行模型。满足以下条件即可：

- 30 张照片完成去敏检查；
- 四种难度都有规定数量；
- 三个大类都有样本；
- 标注检查脚本通过；
- 随机抽 5 张，隔一天重新标注，结果基本一致。

做到这里，你已经完成了 MLE 的第一项基础工作：建立可重复的离线评测基准。
