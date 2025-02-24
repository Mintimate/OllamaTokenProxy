# Flask API 网关

本项目是一个使用 Flask 实现的简单 API 网关。它作为中间件，用于验证令牌并将请求转发到目标服务。用于避免 Ollama 暴露在公网，而没有鉴权。

Ollama API 的调用参考: [Ollama API 使用指南](https://github.com/datawhalechina/handy-ollama/blob/main/docs/C4/1.%20Ollama%20API%20%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md)

## 功能
- **令牌验证**：在处理任何请求之前，验证 `Authorization` 令牌。
- **请求转发**：将原始请求转发到目标服务，并将响应返回给客户端。
- **灵活的路由**：支持多种 HTTP 方法（`GET`、`POST`、`PUT`、`DELETE`、`PATCH`）用于保护路由。

## 安装
1. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```
2**运行应用**：
   ```bash
   python main.py
   ```

## 使用方法

### 令牌验证

API 网关期望在请求头中包含 `Authorization` 字段，并使用 Bearer 令牌。令牌必须为 `TDP` 才能通过验证。

示例：
```bash
curl -H "Authorization: Bearer TDP" http://localhost:5000/api/protected
```

### 请求转发

网关将请求转发到预定义的目标 URL（`https://www.example.com/`）。你可以修改代码中的 `target_url` 变量，将其指向你所需的服务。

### 示例请求

- **GET 请求**：
  ```bash
  curl -X GET -H "Authorization: Bearer TDP" http://localhost:5000/api/protected
  ```

- **POST 请求**：
  ```bash
  curl -X POST -H "Authorization: Bearer TDP" -d '{"key":"value"}' http://localhost:5000/api/protected
  ```

- **PUT 请求**：
  ```bash
  curl -X PUT -H "Authorization: Bearer TDP" -d '{"key":"value"}' http://localhost:5000/api/protected
  ```

- **DELETE 请求**：
  ```bash
  curl -X DELETE -H "Authorization: Bearer TDP" http://localhost:5000/api/protected
  ```

- **PATCH 请求**：
  ```bash
  curl -X PATCH -H "Authorization: Bearer TDP" -d '{"key":"value"}' http://localhost:5000/api/protected
  ```

## 配置

- **目标 URL**：修改 `protected_route` 函数中的 `target_url` 变量，将其指向你所需的服务。
- **令牌**：如果需要使用其他令牌，可以修改 `validate_token` 函数中的令牌验证逻辑。

## 错误处理

- **未授权访问**：如果令牌无效，返回 `401 Unauthorized` 错误。
- **请求转发失败**：如果请求转发失败，返回 `502 Bad Gateway` 错误。

## 贡献

欢迎贡献代码！如果有任何改进或 bug 修复，请提交 issue 或 pull request。

## 许可证

本项目基于 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。