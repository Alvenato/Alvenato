import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric

# --- CONFIGURAÇÃO DE AMBIENTE HÍBRIDA ---
# Tenta o caminho do seu PC. Se não existir, usa o arquivo temporário do GitHub.
local_key_path = r"C:\Users\Cristiano A. Barbosa\OneDrive\Desktop\unidade-visual-code-studio-9dbbd743890a.json"

if os.path.exists(local_key_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = local_key_path
else:
    # O GitHub Actions criará este arquivo automaticamente a partir da Secret
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# ID da sua propriedade do GA4
property_id = "473359623"

def get_full_analytics():
    print("🚀 Iniciando extração de dados do Google Analytics...")
    
    try:
        client = BetaAnalyticsDataClient()

        # Requisitando dimensões completas (Data, Cidade, País, Dispositivo e Página)
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[
                Dimension(name="date"), 
                Dimension(name="city"), 
                Dimension(name="country"),
                Dimension(name="deviceCategory"),
                Dimension(name="pageTitle")
            ],
            metrics=[Metric(name="activeUsers")],
            date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
        )

        response = client.run_report(request)
        
        report_data = []
        
        # Processando os dados da resposta
        if not response.rows:
            print("⚠️ Nenhum dado encontrado no período selecionado.")
        
        for row in response.rows:
            report_data.append({
                "date": row.dimension_values[0].value,
                "city": row.dimension_values[1].value,
                "country": row.dimension_values[2].value,
                "device": row.dimension_values[3].value,
                "page": row.dimension_values[4].value,
                "users": int(row.metric_values[0].value)
            })

        # Salvando o JSON na raiz do repositório
        # O GitHub Action usará este arquivo para fazer o Push
        with open('analytics_data.json', 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ Sucesso! {len(report_data)} linhas de dados foram salvas em analytics_data.json.")

    except Exception as e:
        print(f"❌ ERRO CRÍTICO no pipeline: {str(e)}")
        # Levanta o erro para que o GitHub Actions marque a tarefa como falha
        raise e

if __name__ == "__main__":
    get_full_analytics()
