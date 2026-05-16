import { readFile, writeFile } from "node:fs/promises";
import { Workbook, SpreadsheetFile } from "file:///C:/Users/lucky/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const root = new URL("../", import.meta.url);
const summary = JSON.parse(await readFile(new URL("dashboard/dashboard_summary.json", root), "utf8"));
const outputPath = new URL("dashboard/sales_dashboard_mockup.xlsx", root);

const workbook = Workbook.create();
const dashboard = workbook.worksheets.add("Dashboard");
const monthly = workbook.worksheets.add("Monthly Trend");
const breakdowns = workbook.worksheets.add("Breakdowns");

const currency = (value) => Number(value || 0);
const pct = (value) => Number(value || 0);

dashboard.showGridLines = false;
dashboard.getRange("A1").values = [["Sales Performance Dashboard"]];
dashboard.getRange("A2").values = [["Task 2 static dashboard mock-up built from the cleaned Task 1 sales dataset"]];

dashboard.getRange("A4:J7").values = [
  ["Total Revenue", "Completed Orders", "Average Order Value", "Return Rate", "Cancellation Rate"],
  [
    currency(summary.kpis.total_revenue),
    summary.kpis.completed_orders,
    currency(summary.kpis.avg_order_value),
    pct(summary.kpis.return_rate),
    pct(summary.kpis.cancel_rate),
  ],
  ["KPI Meaning", "Completed sales only", "Revenue / completed orders", "Returned / all orders", "Cancelled / all orders"],
  ["Business Use", "Track sales size", "Track demand quality", "Track buying value", "Track fulfillment risk", "Track lost orders"],
];

monthly.getRange("A1").values = [["Order Month", "Revenue"]];
monthly.getRange("A2").write(summary.monthly_revenue.map((row) => [row.order_month, currency(row.revenue)]));

breakdowns.getRange("A1").values = [["Product", "Revenue", "Orders", "Units"]];
breakdowns.getRange("A2").write(summary.product_revenue.map((row) => [row.product, currency(row.revenue), row.orders, row.units]));
breakdowns.getRange("F1").values = [["Region", "Revenue", "Orders"]];
breakdowns.getRange("F2").write(summary.region_revenue.map((row) => [row.region, currency(row.revenue), row.orders]));
breakdowns.getRange("J1").values = [["Sales Channel", "Revenue", "Orders"]];
breakdowns.getRange("J2").write(summary.channel_revenue.map((row) => [row.sales_channel, currency(row.revenue), row.orders]));
breakdowns.getRange("N1").values = [["Customer Segment", "Revenue", "Average Order Value", "Orders"]];
breakdowns.getRange("N2").write(summary.segment_revenue.map((row) => [row.customer_segment, currency(row.revenue), currency(row.avg_order_value), row.orders]));

dashboard.getRange("A10").values = [["Top Products by Revenue"]];
dashboard.getRange("A11:D17").write([
  ["Product", "Revenue", "Orders", "Units"],
  ...summary.product_revenue.slice(0, 6).map((row) => [row.product, currency(row.revenue), row.orders, row.units]),
]);
dashboard.getRange("F10").values = [["Revenue by Region"]];
dashboard.getRange("F11:H17").write([
  ["Region", "Revenue", "Orders"],
  ...summary.region_revenue.map((row) => [row.region, currency(row.revenue), row.orders]),
]);
dashboard.getRange("J10").values = [["Revenue by Channel"]];
dashboard.getRange("J11:L15").write([
  ["Channel", "Revenue", "Orders"],
  ...summary.channel_revenue.map((row) => [row.sales_channel, currency(row.revenue), row.orders]),
]);

const titleFormat = {
  font: { bold: true, size: 18, color: "#16324F" },
};
const subtitleFormat = {
  font: { italic: true, size: 10, color: "#607080" },
};
const headerFormat = {
  fill: "#16324F",
  font: { bold: true, color: "#FFFFFF" },
  horizontalAlignment: "center",
  verticalAlignment: "center",
};

dashboard.getRange("A1:E1").format = titleFormat;
dashboard.getRange("A2:E2").format = subtitleFormat;
dashboard.getRange("A4:E4").format = headerFormat;
dashboard.getRange("A11:D11").format = headerFormat;
dashboard.getRange("F11:H11").format = headerFormat;
dashboard.getRange("J11:L11").format = headerFormat;
monthly.getRange("A1:B1").format = headerFormat;
breakdowns.getRange("A1:D1").format = headerFormat;
breakdowns.getRange("F1:H1").format = headerFormat;
breakdowns.getRange("J1:L1").format = headerFormat;
breakdowns.getRange("N1:Q1").format = headerFormat;

dashboard.getRange("A5:E5").format = {
  fill: "#EAF3F8",
  font: { bold: true, size: 13, color: "#16324F" },
  horizontalAlignment: "center",
};
dashboard.getRange("A4:E7").format.borders = { preset: "all", style: "thin", color: "#B8C7D3" };
dashboard.getRange("A11:D17").format.borders = { preset: "all", style: "thin", color: "#D1D5DB" };
dashboard.getRange("F11:H17").format.borders = { preset: "all", style: "thin", color: "#D1D5DB" };
dashboard.getRange("J11:L15").format.borders = { preset: "all", style: "thin", color: "#D1D5DB" };

for (const sheet of [dashboard, monthly, breakdowns]) {
  sheet.getUsedRange().format.autofitColumns();
}

dashboard.charts.add("line", {
  title: "Monthly Revenue Trend",
  categories: summary.monthly_revenue.map((row) => row.order_month),
  series: [{ name: "Revenue", values: summary.monthly_revenue.map((row) => currency(row.revenue)) }],
  hasLegend: false,
  from: { row: 18, col: 0 },
  extent: { widthPx: 580, heightPx: 280 },
});

dashboard.charts.add("ColumnClustered", {
  title: "Top Products by Revenue",
  categories: summary.product_revenue.slice(0, 6).map((row) => row.product),
  series: [{ name: "Revenue", values: summary.product_revenue.slice(0, 6).map((row) => currency(row.revenue)) }],
  hasLegend: false,
  from: { row: 18, col: 6 },
  extent: { widthPx: 520, heightPx: 280 },
});

monthly.charts.add("line", {
  title: "Monthly Revenue Trend",
  categories: summary.monthly_revenue.map((row) => row.order_month),
  series: [{ name: "Revenue", values: summary.monthly_revenue.map((row) => currency(row.revenue)) }],
  hasLegend: false,
  from: { row: 1, col: 4 },
  extent: { widthPx: 650, heightPx: 340 },
});

breakdowns.charts.add("ColumnClustered", {
  title: "Revenue by Region",
  categories: summary.region_revenue.map((row) => row.region),
  series: [{ name: "Revenue", values: summary.region_revenue.map((row) => currency(row.revenue)) }],
  hasLegend: false,
  from: { row: 10, col: 0 },
  extent: { widthPx: 520, heightPx: 300 },
});

workbook.recalculate();
const blob = await SpreadsheetFile.exportXlsx(workbook);
await writeFile(outputPath, Buffer.from(blob.data));
console.log(`Wrote ${outputPath.pathname}`);
