```
 _              _
| | _____ _   _| |__  _ __
| |/ / _ \ | | | '_ \| '__|
|   <  __/ |_| | |_) | |
|_|\_\___|\__, |_.__/|_|
          |___/

  type. learn. master.
  打字 · 学习 · 精通
```

# keybr-tui ⌨️

终端打字练习工具，自适应学习算法 + 实时中文翻译。

A terminal typing trainer with adaptive learning and real-time Chinese translation.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![MSRV](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org)

---

## 功能 / Features

- **自适应文本生成** — 基于英语语音 Markov 链生成练习文本，忠实复刻 keybr.com 算法
- **整键置信度追踪** — 指数平滑反应时间，实时评估每个键的掌握程度
- **渐进式字母解锁** — 从 6 个字母开始，达标后自动解锁新字母
- **中文翻译** — 光标所在单词下方显示中文释义，边打字边背单词（7697 个词条）
- **自动备份** — 每次保存前自动备份旧存档（`stats.json.bak`），不怕崩档
- **持久进度** — 跨会话保存，重启不丢
- **两种纠错模式** — Forgive（容错前进）/ Stop（停在原地）
- **练习总结** — 每轮显示 WPM、准确率、最弱键
- **统计面板** — 查看各键详细数据
- **可配置** — 目标速度、纠错模式、文本长度均可调

---

## 安装 / Install

```bash
cargo install --git https://github.com/Edwin-Shao/keybr-tui
```

需要 [Rust](https://rustup.rs/) 1.75+。

或从源码安装：

```bash
git clone https://github.com/Edwin-Shao/keybr-tui.git
cd keybr-tui
cargo install --path .
```

---

## 使用 / Usage

```bash
keybr-tui
```

### 选项 / Options

| Flag | Description |
|------|-------------|
| `--target-wpm <N>` | 目标速度 WPM（默认 35） |
| `--error-mode <MODE>` | `move-on` 容错 / `stop-on-error` 精准 |
| `--reset` | 清除存档，重新开始 |
| `--data-dir` | 打印数据目录路径 |
| `--help` / `--version` | 帮助 / 版本 |

### 快捷键 / Shortcuts

| Key | Action |
|-----|--------|
| `Esc` | 返回菜单 / 退出 |
| `Enter` | 确认 / 开始练习 |
| `Tab` | 切换纠错模式 |
| `↑↓` | 导航菜单 |
| `←→` | 调整设置值 |
| `Ctrl+C` | 强制退出 |

---

## 自适应算法 / Algorithm

1. **字母调度**：从 6 个字母开始，追踪每个键的反应时间
2. **解锁机制**：当前所有字母达标后，按词频顺序解锁下一个
3. **聚焦键**：最弱的键在练习文本中出现频率最高
4. **文本生成**：用英语语音规律生成可读的伪单词（或从 10000 真实单词词典中抽取）
5. **追踪反馈**：每次击键时间被记录、滤波、平滑，更新统计

---

## 存档位置 / Data

```
macOS:  ~/Library/Application Support/keybr-tui/
Linux:  ~/.local/share/keybr-tui/
Windows:  C:\Users\<User>\AppData\Roaming\keybr-tui\
```

| 文件 | 说明 |
|------|------|
| `stats.json` | 练习统计 |
| `stats.json.bak` | 自动备份 |
| `config.toml` | 配置文件 |

---

## 开发 / Development

```bash
cargo build
cargo test
cargo fmt --all
cargo clippy --all-targets -- -D warnings
```

## 致谢 / Credits

- 算法源自 [keybr.com](https://www.keybr.com) by [aradzie](https://github.com/aradzie/keybr.com)
- 原项目 [y0sif/keybr-tui](https://github.com/y0sif/keybr-tui)
- 中文词典 [ECDICT](https://github.com/skywind3000/ECDICT)
- 基于 [ratatui](https://ratatui.rs/) + [crossterm](https://github.com/crossterm-rs/crossterm)

## License

[MIT](LICENSE)
