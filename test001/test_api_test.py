import requests

# 1. 最简单的GET请求测试
def test_get_request():
    """测试GET请求"""
    url = "https://www.baidu.com/"

    # 发送GET请求
    response = requests.get(url)

    # 断言验证
    assert response.status_code == 200, f"状态码错误: {response.status_code}"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # 解析JSON响应
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

    print("✓ GET请求测试通过")
    print(f"响应数据: {data}")


# 2. 带参数的GET请求测试
def test_get_with_params():
    """测试带参数的GET请求"""
    url = "https://jsonplaceholder.typicode.com/posts"

    # 添加查询参数
    params = {"userId": 1}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

    print("✓ 带参数GET请求测试通过")


# 3. POST请求测试
def test_post_request():
    """测试POST请求"""
    url = "https://jsonplaceholder.typicode.com/posts"

    # 请求体数据
    payload = {
        "title": "测试标题",
        "body": "测试内容",
        "userId": 1
    }

    # 发送POST请求
    response = requests.post(url, json=payload)

    assert response.status_code == 201  # 创建成功
    data = response.json()
    assert data["title"] == "测试标题"

    print("✓ POST请求测试通过")


# 4. 异常处理测试
def test_error_handling():
    """测试错误处理"""
    url = "https://jsonplaceholder.typicode.com/posts/99999"  # 不存在的资源

    try:
        response = requests.get(url)
        # 404应该被正常处理
        if response.status_code == 404:
            print("✓ 404错误处理正常")
        else:
            print(f"收到状态码: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")


# 运行所有测试
if __name__ == "__main__":
    print("开始接口测试...")
    print("-" * 40)

    try:
        test_get_request()
        # test_get_with_params()
        # test_post_request()
        # test_error_handling()

        print("-" * 40)
        print("所有测试通过！🎉")

    except Exception as e:
        print(f"测试失败: {e}")
        import traceback

        traceback.print_exc()

        import requests
        import json

def test_login_basic():
            """基础登录测试"""
    url = "http://your-api-domain.com/api/login"

            # 测试数据
        test_cases = [
            {
                    "name": "正确用户名密码",
                    "data": {"username": "admin", "password": "123456"},
                    "expected_status": 200,
                    "expected_msg": "登录成功"
            },
            {
                    "name": "错误密码",
                    "data": {"username": "admin", "password": "wrong"},
                    "expected_status": 401,
                    "expected_msg": "密码错误"
            },
            {
                    "name": "用户不存在",
                    "data": {"username": "notexist", "password": "123456"},
                    "expected_status": 404,
                    "expected_msg": "用户不存在"
            },
            {
                    "name": "空密码",
                    "data": {"username": "admin", "password": ""},
                    "expected_status": 400,
                    "expected_msg": "密码不能为空"
            }
        ]

            print("开始登录接口测试...")
            print("=" * 50)

            for case in test_cases:
                print(f"测试用例: {case['name']}")
                print(f"请求数据: {case['data']}")

                try:
                    # 发送登录请求
                    response = requests.post(url, json=case['data'])

                    # 验证状态码
                    actual_status = response.status_code
                    assert actual_status == case['expected_status'], \
                        f"状态码错误: 期望 {case['expected_status']}, 实际 {actual_status}"

                    # 解析响应
                    if response.text:  # 防止空响应
                        response_data = response.json()

                        # 验证返回消息
                        if "message" in response_data:
                            assert case['expected_msg'] in response_data["message"], \
                                f"消息不匹配: 期望包含 '{case['expected_msg']}', 实际 '{response_data.get('message', '')}'"

                        # 验证登录成功的返回（如果有token）
                        if actual_status == 200:
                            assert "token" in response_data, "登录成功但未返回token"
                            assert "user_id" in response_data, "登录成功但未返回user_id"
                            assert len(response_data["token"]) > 0, "token为空"
                            print(f"✓ 登录成功，获取到token: {response_data['token'][:20]}...")

                    print(f"✓ 测试通过: {case['name']}")

                except AssertionError as e:
                    print(f"✗ 测试失败: {e}")
                except requests.exceptions.RequestException as e:
                    print(f"✗ 请求异常: {e}")
                except json.JSONDecodeError:
                    print(f"✗ 响应不是有效的JSON: {response.text}")

                print("-" * 30)