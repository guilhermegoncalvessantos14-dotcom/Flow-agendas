from dotenv import load_dotenv
import os
from supabase import create_client
load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
print('URL:', url)
print('KEY começa com:', (key or '')[:25], '...')
print('Tamanho da KEY:', len(key or ''))
try:
    c = create_client(url, key)
    r = c.table('instituicao').select('*').limit(5).execute()
    print('✅ Conexão OK')
    print('Registros:', r.data)
except Exception as e:
    print('❌ Erro:', type(e).__name__, '-', e)
