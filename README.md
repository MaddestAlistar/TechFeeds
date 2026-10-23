# 良友科技资讯订阅库 · TechFeeds

[← 返回良友资源中心](https://maddestalistar.github.io/LiangYou-ResourceHub/) · 维护日期：2026-10-23

按 **苹果生态 / NAS 与自建服务 / 播放器影音 / 独立开发** 分类，收集公开的 RSS/Atom 资讯源，并导出能被主流阅读器导入的 **OPML 2.0**。

## 一键导入

- **[完整订阅清单（OPML）](https://raw.githubusercontent.com/MaddestAlistar/TechFeeds/main/opml/all.opml)** — 11 个来源。
- [苹果生态](https://raw.githubusercontent.com/MaddestAlistar/TechFeeds/main/opml/apple.opml)
- [NAS 与自建服务](https://raw.githubusercontent.com/MaddestAlistar/TechFeeds/main/opml/nas.opml)
- [播放器与影音科技](https://raw.githubusercontent.com/MaddestAlistar/TechFeeds/main/opml/players.opml)
- [独立开发与科技](https://raw.githubusercontent.com/MaddestAlistar/TechFeeds/main/opml/indie.opml)

在 Reeder、NetNewsWire、Feedly、Inoreader 等支持 OPML 的软件里选择「导入 OPML」，使用下载的文件。部分阅读器不支持直接输入远程 OPML URL，需先保存文件。

## 文件与维护

- `feeds.json`：唯一的来源清单，含分类、站点与 Feed URL。
- `opml/`：按分类导出的 OPML 和合集。
- `scripts/build_opml.py`：纯 Python 标准库的离线生成脚本；更新 JSON 后运行 `python3 scripts/build_opml.py`。
- `scripts/check_feeds.py`：可选的在线可达性检查，不承诺服务始终可访问。

**注意：** 内容、更新频率与接入可用性由各站点控制。部分网站可能变更 RSS 地址、启用防爬验证或需要代理；这里的来源并非经过持续在线监控，遇到失效请提交 Issue。分类属于人工编辑意见，不代表对应站点专门运营该分类的独立频道。

## 来源参考

OPML 标准：https://opml.org/spec2.opml 。文章版权归原发布者，仓库只储存 RSS 订阅入口。
