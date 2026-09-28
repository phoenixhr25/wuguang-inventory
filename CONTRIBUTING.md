# 参与贡献

感谢你帮助改进物光。

## 提交问题前

1. 搜索是否已有相同 Issue；
2. 确认问题可在最新版复现；
3. 不要上传真实物品照片、完整备份、地址、收纳位置或其他个人信息；
4. 安全问题请按 `SECURITY.md` 私下报告。

## 本地开发

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

主要文件：

- `streamlit_app.py`：Streamlit 承载层；
- `inventory.html`：页面、IndexedDB 数据和交互逻辑；
- `docs/`：产品、架构、路线和隐私说明。

## Pull Request

- 一次 PR 只解决一个明确问题；
- 说明触发条件、修改后的行为和验证方式；
- 涉及数据格式时说明向后兼容与备份恢复；
- 涉及照片或外部 API 时说明数据流、权限和失败处理；
- 不要提交密钥、用户数据或生成的备份文件。

低影响的文案与样式修改可以附人工检查结果。存储、备份、恢复和数据迁移必须提供可复现的验证步骤。

