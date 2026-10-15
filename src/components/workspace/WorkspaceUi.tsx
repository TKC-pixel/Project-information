import type { ReactNode } from "react";
import { ChevronRight, CircleAlert } from "lucide-react";
import { CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import type { WorkspaceResponse, WorkspaceRow } from "../../services/api";

const tones: Record<string, string> = { red: "text-rose-400", amber: "text-amber-300", blue: "text-blue-400", green: "text-emerald-300", white: "text-slate-100" };
const cls = (...parts: Array<string | false | undefined>) => parts.filter(Boolean).join(" ");

export function Panel({ title, children, className = "" }: { title: string; children: ReactNode; className?: string }) {
  return <section className={cls("min-w-0 border border-[#263342] bg-[#141d28]", className)}><div className="flex min-h-9 items-center justify-between gap-3 border-b border-[#263342] px-3.5"><h2 className="text-[10px] font-semibold text-slate-200">{title}</h2><button type="button" className="text-[8px] text-slate-500 hover:text-blue-300">View all <ChevronRight className="ml-0.5 inline" size={10} /></button></div>{children}</section>;
}

export function Metrics({ data }: { data: WorkspaceResponse }) {
  return <div className="mb-3 grid grid-cols-1 gap-2 sm:grid-cols-2 2xl:grid-cols-4">{data.kpis.map((metric) => <section key={metric.label} className="min-h-[78px] border border-[#263342] bg-[#141d28] px-3.5 py-3"><div className="text-[9px] text-slate-400">{metric.label}</div><div className={cls("mt-2 text-[20px] font-semibold leading-none", tones[metric.tone] ?? "text-slate-100")}>{metric.value}</div><div className="mt-1.5 text-[8px] text-slate-500">{metric.detail}</div></section>)}</div>;
}

export function Trend({ data, className = "" }: { data: WorkspaceResponse; className?: string }) {
  return <Panel title={data.trend_title} className={className}><div className="h-[205px] px-2 pb-2 pt-3"><ResponsiveContainer width="100%" height="100%"><LineChart data={data.trend} margin={{ top: 5, right: 10, left: -18, bottom: 0 }}><CartesianGrid stroke="#263342" strokeDasharray="2 4" vertical={false} /><XAxis dataKey="label" tick={{ fill: "#7f8b9a", fontSize: 8 }} axisLine={{ stroke: "#293644" }} tickLine={false} /><YAxis tick={{ fill: "#7f8b9a", fontSize: 8 }} axisLine={false} tickLine={false} /><Tooltip contentStyle={{ background: "#111a24", border: "1px solid #344253", borderRadius: 2, color: "#e2e8f0", fontSize: 9 }} />{data.series.map((series) => <Line key={series.key} type="monotone" dataKey={series.key} name={series.label} stroke={series.color} strokeWidth={2} dot={false} activeDot={{ r: 3 }} />)}</LineChart></ResponsiveContainer></div><div className="flex flex-wrap gap-x-4 gap-y-1 px-4 pb-3">{data.series.map((series) => <span key={series.key} className="flex items-center gap-1.5 text-[8px] text-slate-400"><i className="h-[2px] w-3" style={{ backgroundColor: series.color }} />{series.label}</span>)}</div></Panel>;
}

export function Records({ data, rows, selected, onSelect, minWidth = "min-w-[640px]" }: { data: WorkspaceResponse; rows: WorkspaceRow[]; selected: string; onSelect: (id: string) => void; minWidth?: string }) {
  return <div className="overflow-x-auto"><table className={cls("w-full border-collapse text-left", minWidth)}><thead><tr className="bg-[#1a2633]">{data.columns.map((column) => <th key={column.key} className="px-3 py-2.5 text-[8px] font-semibold text-slate-400">{column.label}</th>)}</tr></thead><tbody>{rows.map((row, index) => { const id = String(row.id ?? index); return <tr key={id} onClick={() => onSelect(id)} className={cls("cursor-pointer border-t border-[#263342] hover:bg-[#192838]", (selected || String(rows[0]?.id ?? "")) === id && "bg-[#1b3552]")}>{data.columns.map((column) => { const value = String(row[column.key] ?? "—"); const high = /high|overdue|held|expired|candidate|pending/i.test(value); const clear = /verified|clear|complete|no match/i.test(value); return <td key={column.key} className={cls("max-w-[240px] truncate px-3 py-2.5 text-[9px]", high ? "text-rose-300" : clear ? "text-emerald-300" : "text-slate-300")}>{value}</td>; })}</tr>; })}</tbody></table>{rows.length === 0 && <div className="px-4 py-8 text-center text-[10px] text-slate-500">No records match this search.</div>}<div className="border-t border-[#263342] px-3 py-2 text-[8px] text-slate-500">Showing {rows.length} of {data.rows.length} records <span className="float-right">‹ &nbsp; 1 &nbsp; 2 &nbsp; 3 &nbsp; ›</span></div></div>;
}

export function Facts({ items, action = "Review" }: { items: WorkspaceResponse["side_metrics"]; action?: string }) {
  return <div className="divide-y divide-[#263342] px-3.5">{items.map((item) => <div key={item.label} className="flex min-h-[58px] items-center gap-3 py-2"><div className={cls("w-[64px] shrink-0 text-[11px] font-medium", tones[item.tone] ?? "text-slate-300")}>{item.label}</div><div className="min-w-0 flex-1"><div className="text-[9px] font-medium text-slate-200">{item.value}</div><div className="mt-1 text-[8px] leading-relaxed text-slate-500">{item.detail}</div></div><button type="button" className="h-6 border border-[#2b3948] px-2 text-[8px] text-slate-300">{action}</button></div>)}</div>;
}

export function Tabs({ items }: { items: string[] }) {
  return <div className="flex gap-4 overflow-x-auto border-b border-[#263342] px-3.5">{items.map((item, index) => <button key={item} type="button" className={cls("shrink-0 border-b-2 py-2.5 text-[8px]", index === 0 ? "border-blue-400 text-blue-300" : "border-transparent text-slate-500 hover:text-slate-300")}>{item}</button>)}</div>;
}

export function FilterBar({ filters, placeholder, value }: { filters: string[]; placeholder: string; value?: string }) {
  return <div className="my-3 flex flex-wrap gap-1.5"><input placeholder={placeholder} defaultValue={value} className="h-8 w-full max-w-[220px] border border-[#293644] bg-[#141e29] px-2.5 text-[9px] text-slate-300 placeholder:text-slate-500" />{filters.map((filter) => <button key={filter} className="h-8 border border-[#293644] bg-[#141d28] px-2.5 text-[8px] text-slate-300">{filter}</button>)}</div>;
}

export function RiskBreakdown({ data }: { data: WorkspaceResponse }) {
  const risk = data.view.risk;
  const factors = risk?.factors ?? [];
  const maximum = Math.max(...factors.map((item) => item.value), 1);
  return <div className="space-y-3 p-3.5"><div className="flex items-end justify-between"><span className="text-[8px] text-slate-500">Explainable risk score</span><span className="text-[20px] font-semibold text-rose-300">{risk?.score} <small className="text-[8px]">{risk?.level}</small></span></div>{factors.map((item) => <div key={item.label}><div className="flex justify-between gap-2 text-[8px]"><span className="text-slate-300">+{item.value} {item.label}</span><span className="text-right text-slate-500">{item.detail}</span></div><div className="mt-1 h-[3px] bg-[#263342]"><div className="h-full bg-rose-400" style={{ width: `${Math.max(5, item.value / maximum * 100)}%` }} /></div></div>)}<div className="border-l-2 border-amber-400 bg-[#29271f] px-2.5 py-2 text-[8px] leading-relaxed text-amber-100">{risk?.disclaimer}</div><div className="text-[8px] text-slate-500">{risk?.formula}</div></div>;
}

export function RelationshipGraph({ data }: { data: WorkspaceResponse }) {
  const graph = data.view.graph;
  const nodes = graph?.nodes ?? [];
  const nodeById = new Map(nodes.map((item) => [item.id, item]));
  return <div className="relative h-[310px] overflow-hidden bg-[#111a24]"><svg viewBox="0 0 100 100" preserveAspectRatio="none" className="absolute inset-0 h-full w-full" aria-hidden="true">{(graph?.edges ?? []).map((edge) => { const from = nodeById.get(edge.from); const to = nodeById.get(edge.to); return from && to ? <line key={`${edge.from}-${edge.to}`} x1={from.x} y1={from.y} x2={to.x} y2={to.y} stroke="#526172" strokeWidth="0.35" /> : null; })}</svg>{nodes.map((node) => <div key={node.id} className="absolute z-10 -translate-x-1/2 -translate-y-1/2 text-center" style={{ left: `${node.x}%`, top: `${node.y}%` }}><div className={cls("mx-auto flex h-7 w-7 items-center justify-center border", node.type === "selected" ? "rounded-full border-rose-400 bg-[#331f2a] text-rose-200" : node.type === "device" ? "rounded-sm border-blue-400 bg-[#1c3859] text-blue-200" : "rounded-full border-slate-500 bg-[#202c39] text-slate-300")}><span className="text-[8px]">{node.type === "device" ? "D" : node.type === "selected" ? "!" : "C"}</span></div><div className="mt-1 whitespace-nowrap text-[8px] text-slate-200">{node.name}</div><div className="mt-0.5 whitespace-nowrap text-[7px] text-slate-500">{node.label}</div></div>)}<div className="absolute bottom-2 left-3 text-[7px] text-slate-500">{graph?.note}</div></div>;
}

export function AlertIcon({ children }: { children: ReactNode }) {
  return <div className="flex items-center gap-3 p-3.5"><CircleAlert className="shrink-0 text-rose-300" size={17} /><div className="text-[8px] leading-relaxed text-slate-400">{children}</div></div>;
}

export function WorkspaceLoading({ error }: { error: string }) {
  return <main className="min-h-screen bg-[#0b1118] p-8 text-[11px] text-slate-400">{error || "Loading workspace data..."}</main>;
}