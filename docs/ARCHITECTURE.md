# 技术架构

## 当前结构

```text
Streamlit Community Cloud
└── streamlit_app.py
    └── iframe: inventory.html
        ├── 页面与交互
        ├── 图片压缩
        ├── IndexedDB
        │   ├── 物品
        │   ├── 压缩照片并转换为 Data URL
        │   └── 使用记录
        ├── JSON 备份与恢复
        └── 可选的只读 WebMCP 工具
```

Streamlit Python 服务不接收用户照片。照片由浏览器读取、压缩并保存到当前站点的 IndexedDB。

## 数据结构

物品主要字段：

```json
{
  "id": "uuid",
  "name": "蓝白条纹衬衫",
  "major": "衣物",
  "cat": "上装",
  "qty": 1,
  "price": 399,
  "color": "蓝白",
  "location": "卧室衣柜",
  "photo": "data:image/jpeg;base64,...",
  "createdAt": "ISO-8601"
}
```

使用事件记录物品 ID、类型与时间。照片压缩后以 Data URL 保存到 IndexedDB，并直接写入 JSON 备份；导入前会校验格式、字段范围、ID、日期和图片类型。旧版本保存的 Blob 会在页面启动时自动转换。

## 为什么当前使用本地存储

- 不需要账号和服务器数据库；
- 照片默认不离开设备；
- 适合验证产品闭环；
- 部署和运维成本低。

代价是不能跨设备同步，浏览器清理数据后可能丢失，家庭共享也无法实现。

## AI 版本的边界

API 密钥不能写入 `inventory.html`。AI 识别至少需要一个服务端代理：

```text
浏览器压缩照片
→ 服务端认证、限额和安全校验
→ 视觉模型
→ 结构化候选结果
→ 用户确认
→ 正式写入物品库
```

AI 输出必须经过 Schema 校验；低置信度字段需要明确提示。模型不得直接覆盖用户数据。

## 正式版本建议

- 前端：响应式 Web/PWA；
- API：FastAPI、Next.js API 或同等服务；
- 数据库：PostgreSQL；
- 图片：S3、R2 或 Supabase Storage；
- 异步任务：队列与有上限的失败重试；
- AI：Provider 抽象，支持 OpenAI 兼容接口；
- 相似检索：图片 embedding 与结构化字段混合召回；
- 可观测性：成功率、延迟、费用和用户修正字段；
- 安全：认证、对象权限、速率限制、导出与删除。
