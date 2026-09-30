# AI Agent

## 初回セットアップ

### Ollama起動

```bash
docker compose -f docker-compose.dev.yaml up -d ollama
```

### モデルダウンロード

```bash
docker compose -f docker-compose.dev.yaml exec ollama ollama pull llama3.2
```

### Python環境ビルド

```bash
docker compose -f docker-compose.dev.yaml build agent
```

## AIエージェント実行

```bash
docker compose -f docker-compose.dev.yaml run --rm agent python agent.py
```

## Ollama停止

```bash
docker compose -f docker-compose.dev.yaml stop ollama
```