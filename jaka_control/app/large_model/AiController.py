import requests

from jaka_control.infra.constant.ServerConstant import ServerConstant


class AiController:
    def __init__(self, aiUrl):
        self.aiUrl = aiUrl

    def sendMessage(self, message):
        # 请求的JSON数据
        data = {
            "model": "llama3",
            "prompt": message,
            "stream": False
        }

        # 发送POST请求
        response = requests.post(self.aiUrl, json=data)

        # 确保请求成功
        if response.status_code == 200:
            # 解析JSON响应
            response_data = response.json()
            # 获取并返回'response'字段的内容
            if 'response' in response_data:
                return response_data['response']
            else:
                return "dailog failed."
        else:
            return f"Request failed with status code {response.status_code}."

if __name__ == "__main__":
    aiController = AiController(ServerConstant.aiUrl)
    while True:
        message = input("send to ai: (input '/bye' to quit)\n")
        if (message == '/bye'):
            print("bye")
            break
        response = aiController.sendMessage(message)
        print("\nai:")
        print(response)
        print()
