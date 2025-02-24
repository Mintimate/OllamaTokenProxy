"""
@author: Mintimate
@date: 2025-02-24
@desc:
"""

from flask import Flask, request, make_response
import requests

app = Flask(__name__)


@app.before_request
def validate_token():
    """
    验证Token是否有效
    :return:
    """
    # 从请求头中提取Token
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]

    # 验证Token是否有效
    if token != 'TDP':
        return {"error": "Unauthorized, invalid token"}, 401


@app.route('/api/protected', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def protected_route():
    """
    保护路由，转发原始请求到目标服务
    :return:
    """
    # 目标URL（固定或动态构造）
    target_url = 'https://www.example.com/'  # 固定目标
    # 或动态路径：target_url = f'https://www.example.com{request.full_path}'

    # 构造请求头（移除Host避免冲突）
    headers = {key: value for key, value in request.headers if key.lower() != 'host'}

    try:
        # 使用requests转发原始请求
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            data=request.get_data(),
            params=request.args,
            cookies=request.cookies,
            allow_redirects=False
        )
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to forward request: {str(e)}"}, 502

    # 将目标服务的响应返回给客户端
    response = make_response(resp.content)
    response.status_code = resp.status_code
    for header_key, header_value in resp.headers.items():
        if header_key.lower() not in ('content-length', 'content-encoding', 'transfer-encoding'):
            response.headers[header_key] = header_value
    return response


if __name__ == '__main__':
    app.run(debug=True)