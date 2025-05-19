import requests as rq
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# .env 파일 불러오기
load_dotenv() 

# Supabase 프로젝트 정보 입력
supa_url = os.getenv("SUPABASE_URL")  # Supabase 프로젝트 URL
supa_key = os.getenv("SUPABASE_KEY")  # Supabase API 키


url = 'https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&sectionid2=258'

data = rq.get(url)

html = BeautifulSoup(data.text, 'html.parser')
html_select = html.select('dl > dd.articleSubject > a')


supabase: Client = create_client(supa_url, supa_key)

for i in html_select:

    title = i.get_text(strip=True)
    supabase.table("news").insert({"title": title}).execute()




