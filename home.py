import streamlit as st
from Utils.GitHubHelper import g_Helper
from Utils.PosterHelper import PosterHelper


# 创建需要获取的信息
data = {
    "Owner":[]
}



"""
# GitHub Poster

Welcome! It's a tool to help you Share Your GitHub Repos!
""" 


# 创建链接获取GitHub仓库
github_url = "https://github.com/"
github_repo = st.text_input("Please type GitHub Repo's Url here",f"{github_url}L4Walk/GitHubPoster")

if github_repo:
    #检查是否为有效URL
    repo_name = github_repo[len(github_url):]
    if st.button("GeneratePoster"):
        if(repo_name):
            poster = PosterHelper(repo_name)
            st.success("已经保存")
        

       

        