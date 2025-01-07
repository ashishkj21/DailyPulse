from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
from langchain_community.utilities.github import GitHubAPIWrapper
from app.core.config import settings

def get_github_toolkit():
    github = GitHubAPIWrapper(
        app_id=settings.GITHUB_APP_ID,
        private_key=settings.GITHUB_APP_PRIVATE_KEY,
        repository=settings.GITHUB_REPOSITORY
    )
    toolkit = GitHubToolkit.from_github_api_wrapper(github)
    return toolkit

def get_commits():
    toolkit = get_github_toolkit()
    get_commits_tool = [tool for tool in toolkit.get_tools() if tool.name == "Get Issues"][0]
    return get_commits_tool.run()

def get_pull_requests():
    toolkit = get_github_toolkit()
    get_prs_tool = [tool for tool in toolkit.get_tools() if tool.name == "List open pull requests (PRs)"][0]
    return get_prs_tool.run()
