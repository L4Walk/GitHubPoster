from dotenv import load_dotenv
from github import Github
from github import Auth
import os

class GitHubHelper:
    def __init__(self):
        # 获取GitHubToken
        env_file = os.path.join(os.getcwd(), '.env')

        # 加载 .env 文件中的环境变量
        load_dotenv()

        # 获取GitHub Token
        github_token = os.getenv('Github_Token')

        # 进行Access认证
        auth = Auth.Token(github_token)

        # 启动实例
        self.G = Github(auth=auth)



# 创建全局实例
g_Helper = GitHubHelper()