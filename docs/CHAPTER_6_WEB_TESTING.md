# 第 6 章：Web 界面测试

第 6 章没有新的 Python 代码，它验证第 5 章的 Game Master API 是否能被浏览器调用。请先准备 AWS 凭证和 Bedrock 模型权限，再启动以下服务。

## 启动服务

在仓库根目录执行，每个服务占用一个终端：

```bash
source .venv/bin/activate
python 4_mcp_integration/dice_roll_mcp_server.py
```

```bash
source .venv/bin/activate
python 5_a2a_integration/agents/rules_agent/rules_agent.py
```

```bash
source .venv/bin/activate
python 5_a2a_integration/agents/character_agent/character_agent.py
```

```bash
source .venv/bin/activate
python 5_a2a_integration/agents/gamemaster_orchestrator/gamemaster_orchestrator.py
```

Rules Agent、Character Agent、骰子 MCP 服务和协调器分别监听 `8000`、`8001`、`8002`、`8009`。协调器必须在前三个服务之后启动。

## API 测试

先检查协调器：

```bash
curl http://127.0.0.1:8009/health
```

再发送一轮游戏请求：

```bash
curl -X POST http://127.0.0.1:8009/inquire \
  -H 'Content-Type: application/json' \
  -d '{"question":"Create a character named Thorin, a Dwarf Fighter. Roll his ability scores."}'
```

也可以打开 [Workshop Web UI](https://aws-samples.github.io/sample-once-upon-agentic-ai/)，将 Server URL 设置为 `http://127.0.0.1:8009`。日志应显示 Game Master 调用了 A2A 代理和骰子 MCP 服务。

## 第 7 章

停止第 5 章的协调器后，可以用同样的 MCP、Rules Agent 和 Character Agent 服务启动：

```bash
python 7_strands_harness/gamemaster_harness.py
```

Harness 版本也监听 `8009`，会在 `.agent/` 保存会话和记忆。该目录已被 Git 忽略，不要提交到仓库。

## 停止和清理

每个服务所在终端按 `Ctrl+C` 停止。运行时生成的 `.agent/`、`dnd_knowledge_base/`、PDF 和 Python 缓存可以删除；`.venv/` 和 `uv.lock` 建议保留以便继续开发。仓库中已有的角色数据文件属于项目状态，删除前请先确认不再需要。
