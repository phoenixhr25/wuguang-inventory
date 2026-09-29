# 物光 Wuguang

[English README](README_EN.md) · 中文

> 先看见拥有，再决定购买。

物光是一个照片优先、数据本地保存的个人物品盘点工具。它帮助用户逐步建立物品库、记录购买金额与使用情况，并用已有衣物生成基础搭配。

**在线体验：** https://wuguang-inventory.streamlit.app/

## 为什么做

我们常常不是没有东西，而是看不清自己已经拥有什么。传统库存工具像 ERP，字段多、维护累，刚开始就容易放弃。

物光希望把入口变得尽量简单：从今天常用的一件东西、一张照片开始，不必一次整理完整个家。

当前版本仍需要人工填写名称和分类。它首先验证完整闭环；未来再通过视觉模型把“逐项录入”变成“看一眼、改一下、确认入库”。

## 当前功能

- 拍照或选择多张照片，逐张确认入库；
- 名称、大品类、具体分类、数量、单价、颜色和收纳位置；
- 按衣物、家居、数码筛选；
- 物品数量和已记录购买金额汇总；
- 单件使用记录；
- 从上装、下装、连衣裙、外套、鞋履、包袋和配饰中生成基础组合；
- “今天穿了这套”与最近使用历史；
- 按实际穿搭记录统计单品出现率和完整组合出现率；
- 包含照片的 JSON 完整备份与恢复；
- 页面内“反馈建议”入口，兼顾公众号用户与 GitHub Issue；
- 只读 WebMCP 工具 `read_inventory_summary`（在兼容环境中启用）。

## 当前限制

- 尚未接入 AI 图片识别；
- 不是专业造型建议；
- 数据和照片只保存在当前浏览器的 IndexedDB 中；
- 换设备、清理浏览器数据或更换浏览器后，记录不会自动同步；
- Streamlit 页面通过 iframe 承载前端，微信内置浏览器的存储与下载行为需要真机验证；
- 当前没有用户账户、云端数据库或多人协作。

使用前请阅读[隐私与数据说明](docs/PRIVACY.md)，录入一批物品后及时导出备份。

## 本地运行

需要 Python 3.10 或更高版本。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Windows PowerShell 激活环境：

```powershell
.venv\Scripts\Activate.ps1
```

## 部署到 Streamlit Community Cloud

1. Fork 或复制本仓库；
2. 在 Streamlit Community Cloud 创建应用；
3. 选择目标仓库和 `main` 分支；
4. Main file path 填写 `streamlit_app.py`；
5. 部署后用手机、微信和无痕浏览器分别检查。

当前版本不需要任何 Secrets。未来接入 AI 时，API key 必须保存在服务端 Secrets 中，不能写进 `inventory.html`。

## 数据边界

浏览器负责保存物品、照片和使用记录，Streamlit Python 服务只读取并嵌入仓库中的静态 HTML。当前版本不会把用户选择的照片发送到 Python 服务或第三方 AI。

备份文件格式为 `wuguang-backup` JSON，包含照片、物品和使用记录。备份可能含有敏感生活信息，请勿公开上传到 Issue 或聊天群。

## 产品与技术路线

- [产品说明](docs/PRODUCT.md)
- [技术架构](docs/ARCHITECTURE.md)
- [路线图与时间预估](docs/ROADMAP.md)
- [隐私与数据说明](docs/PRIVACY.md)

下一阶段优先验证：

1. 单件照片的 AI 结构化识别；
2. 天气、场合与真实库存结合的穿搭；
3. 相似物品与重复购买提醒；
4. 出现持续使用后再建设账户和云同步。

## 反馈与贡献

- 遇到错误：提交 Bug report；
- 有产品建议：提交 Feature request；
- 涉及安全或个人数据：按照 [SECURITY.md](SECURITY.md) 私下报告，不要公开上传数据和备份。

提交代码前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 开源许可

本项目采用 [MIT License](LICENSE)。

## 致谢

产品与技术研究参考了以下开源项目的公开工作流：

- [Hangar](https://github.com/Gurshaan-Deol/Hangar)：AI 衣物识别、天气穿搭与 Provider 抽象；
- [HomeBox](https://github.com/sysadminsmedia/homebox)：家庭库存与物品生命周期；
- [Libre Closet](https://github.com/Lazztech/Libre-Closet)：数字衣橱与组合交互；
- [Grocy](https://github.com/grocy/grocy)：家庭消耗品和库存管理。

当前仓库没有复制这些项目的代码。未来如引入第三方代码，将按相应许可证保留版权和许可声明。
