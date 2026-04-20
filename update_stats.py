import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric

# --- LOGICA DE CREDENCIAIS ---
local_key = r"C:\Users\Cristiano A. Barbosa\OneDrive\Desktop\unidade-visual-code-studio-9dbbd743890a.json"

if os.path.exists(local_key):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = local_key
    print("🏠 Rodando em ambiente local.")
else:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
    print("🤖 Rodando no GitHub Actions.")

property_id = "513962275"

def get_full_analytics():
    try:
        client = BetaAnalyticsDataClient()

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
        for row in response.rows:
            report_data.append({
                "date": row.dimension_values[0].value,
                "city": row.dimension_values[1].value,
                "country": row.dimension_values[2].value,
                "device": row.dimension_values[3].value,
                "page": row.dimension_values[4].value,
                "users": int(row.metric_values[0].value)
            })

        # Salva o JSON com suporte a caracteres acentuados (UTF-8)
        with open('analytics_data.json', 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ Sucesso: {len(report_data)} registros atualizados.")

    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        raise e

if __name__ == "__main__":
    get_full_analytics()
