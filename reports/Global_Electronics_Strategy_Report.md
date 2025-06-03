from docx import Document

# Create a Word document for strategy recommendations
doc = Document()
doc.add_heading('📌 Strategic Recommendations for Global Electronics', 0)

sections = {
    "🎯 Marketing Strategy Optimization": [
        "**Insight:** Sales and customer data show concentration in specific product lines (e.g., desktop PCs) and regions (e.g., Victoria, South Australia), with a majority of customers aged 30–60.",
        "**Recommendation:**",
        "- Launch geo-targeted campaigns in top-performing states using demographic-specific messaging.",
        "- Personalize offers based on age/gender segments to improve engagement.",
        "- Retarget loyal, high-spending customers for upselling and loyalty programs."
    ],
    "📦 Inventory Management Optimization": [
        "**Insight:** Sales trends show a few products driving a large share of revenue, while many others underperform. Seasonality is visible in monthly sales peaks.",
        "**Recommendation:**",
        "- Focus inventory planning on best-selling SKUs in 'Computers' and 'Audio'.",
        "- De-stock slow-moving items through clearance or bundling.",
        "- Adjust inventory levels to align with seasonal demand peaks."
    ],
    "📈 Sales Forecasting Support": [
        "**Insight:** Sales are skewed and seasonal; stores and currencies vary in revenue contribution.",
        "**Recommendation:**",
        "- Use separate forecasting models per product category and region.",
        "- Integrate time series models to factor in seasonal trends.",
        "- Monitor high-value orders to reduce distortion in forecasts."
    ],
    "🌍 International Pricing Strategy": [
        "**Insight:** Multiple currencies used; USD dominates but others show variability.",
        "**Recommendation:**",
        "- Implement dynamic pricing models based on exchange rates.",
        "- Offer geo-specific promotions based on local purchasing power.",
        "- Normalize revenue for global performance comparison."
    ],
    "🏬 Store Expansion & Optimization": [
        "**Insight:** Sales do not strongly correlate with store size; some states outperform others.",
        "**Recommendation:**",
        "- Expand into top-performing states, not necessarily based on store size.",
        "- Focus on medium-sized stores with high operational efficiency.",
        "- Monitor store-level KPIs beyond square meters and age."
    ]
}

for section, content in sections.items():
    doc.add_heading(section, level=1)
    for line in content:
        if line.startswith("**Insight:**"):
            doc.add_paragraph(line.replace("**", ""), style='Intense Quote')
        elif line.startswith("**Recommendation:**"):
            doc.add_paragraph(line.replace("**", ""), style='List Bullet')
        else:
            doc.add_paragraph(line, style='List Bullet 2')

# Add Summary Table
doc.add_heading('✅ Summary Focus Areas', level=1)
table = doc.add_table(rows=1, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Area'
hdr_cells[1].text = 'Strategic Action'

rows = [
    ("🎯 Marketing", "Segment campaigns by top states, age, and loyalty"),
    ("📦 Inventory", "Prioritize bestsellers, reduce dead stock"),
    ("📈 Forecasting", "Model by region and category with seasonality in mind"),
    ("🌍 Pricing Strategy", "Localized pricing and reporting using exchange rate data"),
    ("🏬 Store Expansion", "Expand where performance is strongest, not largest size"),
]

for area, action in rows:
    row_cells = table.add_row().cells
    row_cells[0].text = area
    row_cells[1].text = action

# Save Word document
docx_path = "/mnt/data/Global_Electronics_Strategy_Report.docx"
doc.save(docx_path)



