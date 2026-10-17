# fours Agent

基于 AWS [Once Upon Agentic AI](https://github.com/aws-samples/sample-once-upon-agentic-ai) 工作坊，使用 Strands SDK 逐步开发 AI Agent。

## 开发环境

- Python：3.13.5（由 `.python-version` 固定，与工作坊一致）
- 包管理器：uv
- 虚拟环境：项目内 `.venv`
- 依赖：`pyproject.toml` 声明，`uv.lock` 锁定可复现版本

首次安装 uv 请参考 [官方安装说明](https://docs.astral.sh/uv/getting-started/installation/)。macOS / Linux：

```bash
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/ArisLiWind/fours-agent.git
cd fours-agent
uv python install
uv sync --locked
source .venv/bin/activate
python scripts/check_environment.py
```

Windows PowerShell 激活命令：`.venv\Scripts\Activate.ps1`。

每次打开新终端，需要重新进入项目目录并激活虚拟环境；也可以直接使用 `uv run python scripts/check_environment.py`。

环境检查只验证 Python、虚拟环境和依赖导入，不调用模型，也不需要 AWS 凭证。正式调用工作坊默认的 Amazon Bedrock 模型前，需要配置 AWS 凭证和对应模型访问权限，请勿将凭证提交到 Git。

## 开发路线

当前阶段：第 1–7 章代码已完成，清理说明和本地 Web 测试流程已整理。

1. 第 1 章：在 `1_strands_basics/simple_agent.py` 创建首个智能体，设置系统提示词和调用入口。
2. 第 2 章：`http_request` 查询 D&D 5e API；奖励任务加入受 HumanInTheLoop 保护的文件和 shell 工具。
3. 第 3 章：`@tool` 自定义 `roll_dice`，用 4d6 drop lowest 生成能力值。
4. 第 4 章：用 FastMCP 暴露远程 `roll_dice` 服务，并由 Strands MCP 客户端连接。
5. 第 5 章：Rules Agent、Character Agent 通过 A2A 暴露，Game Master 负责协调。
6. 第 6 章：通过 [Web 测试指南](docs/CHAPTER_6_WEB_TESTING.md) 连接本地协调器。
7. 第 7 章：Harness 版本启用 MCP、A2A、命名会话和结构化输出。

核心章节代码已完成；后续可在现有工具、代理和 Web API 上继续扩展。当前本地工具验证通过不代表云端模型调用已经验证。

## 上游来源

保留上游 Git 历史与许可证。`origin` 指向本项目；本地 `upstream` 指向 AWS 示例仓库。原始工作坊说明保存在 [docs/UPSTREAM_README.md](docs/UPSTREAM_README.md)，其中路径相对于仓库根目录。
