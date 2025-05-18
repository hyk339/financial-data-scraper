from supabase import create_client, Client
import os
from dotenv import load_dotenv

# .env 파일 불러오기
load_dotenv() 

# Supabase 프로젝트 정보 입력
url = os.getenv("SUPABASE_URL")  # Supabase 프로젝트 URL
key = os.getenv("SUPABASE_KEY")  # Supabase API 키

supabase: Client = create_client(url, key)

