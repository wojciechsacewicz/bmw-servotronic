"""Render the README chart. Requires Matplotlib; reads the published sample data."""

from pathlib import Path
import json
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
samples = json.loads((ROOT / 'data/e84-vs-e92.json').read_text())['samples']
changes = {
    speed: [100 * (row['e84_contribution'] / row['e92_contribution'] - 1)
            for row in samples if row['speed_kmh'] == speed]
    for speed in [0, 15]
}
plt.rcParams.update({'font.family': ['Inter', 'DejaVu Sans'], 'svg.fonttype': 'none',
                     'axes.unicode_minus': False})

BG = '#f6f8f7'
INK = '#142721'
MUTED = '#5c6d66'
GREEN = '#087f63'
GRID = '#dce5df'
fig=plt.figure(figsize=(14.56,5.6),dpi=100,facecolor=BG)
fig.text(.045,.872,'E84 vs E92 steering assistance',fontsize=29,weight='bold',color=INK)
fig.text(.045,.785,"One calculated assist value. Steering effort wasn't measured.",fontsize=18.5,color=MUTED)
ax=fig.add_axes([.35,.285,.47,.40],facecolor=BG)
ax.set_xlim(-35, 105)
ax.set_ylim(-.33, 1.33)
ax.set_xticks([-25,0,25,50,75])
ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'{x:+.0f}%' if x else '0'))
ax.tick_params(axis='x',length=0,labelsize=19,pad=12,colors=MUTED)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(axis='x',color=GRID,lw=.45,alpha=.45)
ax.axvline(0,color=MUTED,lw=2.2,zorder=1)
for y, speed, label in [(1, 0, 'Parked (0 km/h)'), (0, 15, 'Slow (15 km/h)')]:
    data = changes[speed]
    lo, hi = min(data), max(data)
    ax.plot([lo, hi], [y, y], lw=9, color=GREEN, alpha=.14,
            solid_capstyle='round', zorder=2)
    ax.scatter(data, [y] * 4, s=210, color=GREEN, edgecolors=BG,
               linewidths=2.1, zorder=3)
    ax.text(hi + 5 if speed == 0 else lo - 5, y, f'{lo:+.0f}% to {hi:+.0f}%',
            ha='left' if speed == 0 else 'right', va='center',
            fontsize=20, weight='bold', color=GREEN)
    fig.text(.045, .285 + .40 * (y + .33) / 1.66, label, va='center',
             fontsize=20, weight='bold', color=INK)
fig.text(.35,.13,'← Less than E92',ha='left',fontsize=19,color=MUTED)
fig.text(.82,.13,'More than E92 →',ha='right',fontsize=19,color=MUTED)
fig.add_artist(Rectangle((.001,.003),.998,.994,transform=fig.transFigure,fill=False,edgecolor='#e3e8e5',linewidth=.8))
fig.savefig(OUT/'e84-vs-e92.png',facecolor=BG,metadata={'Title':'E84 vs E92 steering assistance','Description':'Change in one isolated calculated assist term. Four matched positive-input samples per speed. Not measured steering effort.'})
plt.close(fig)
print(OUT / 'e84-vs-e92.png')
