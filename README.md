# 物光 Streamlit 试用部署包

## 方案

独立部署一个物光应用，不修改现有资产评估工具。Streamlit 只承载网页，现有物光的照片、物品和使用记录继续在浏览器 IndexedDB 中保存。未使用 st.file_uploader，所以物品照片不会通过 Python 上传到服务器；应用代码没有云端物品库或 AI 调用。

## 部署

1. 将本目录内容上传至单独的 GitHub 仓库（包含 .streamlit 目录）。
2. 在已有 Streamlit Community Cloud 账户选择 Create app，选对应仓库和分支。
3. 入口填写 streamlit_app.py；建议 Python 3.12。依赖由 requirements.txt 安装。
4. 为物光选择独立子域名并确认允许公众访问。应用实际网址以部署成功后显示为准。
5. 用未登录浏览器和微信真机检查，再放入公众号「服务 → 物品盘点」。

部署过程参照：https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## 本地启动

建议用独立虚拟环境，安装 requirements.txt 后运行：

    streamlit run streamlit_app.py

固定 1.55.0 以保持已知 iframe 接口行为；此版本为 PyPI 已发布版本。此包没有把主机已有的旧版 Streamlit 全局升级。

## 需要了解

- 这是低成本小范围试用方案。Community Cloud 托管免费，但无流量 12 小时可能休眠；官方目前称所有应用托管在美国，国内微信访问需要实际测试。
- 不是跨设备云同步。不要把 Session State 或 Community Cloud 本地文件当作持久用户数据库。
- 浏览器存储在 iframe 内能否长期保留，需要目标 iPhone/Android 微信实测；浏览器策略可能限制存储或下载。页面存储失败会提示，不会假装入库成功。
- iframe 高度固定为 1050px 并允许滚动，手机可能出现内外两层滚动。
- 从旧本地 HTML 迁移时，先导出备份，再在新网址导入；不同网址不会自动共享数据。
- API 识图尚未接入。不是“上传就自动识别”的版本。

## 验证范围

原始前端已检查照片持久化、编辑、搭配记录和备份恢复。Streamlit 入口已做 Python 编译及本机 1.37.1 的 AppTest 包装层冒烟检查；它不执行 iframe 内 JavaScript。requirements.txt 固定的 1.55.0 尚未在此机器安装验证，线上部署、iframe 持久化与微信真机仍需测试。
