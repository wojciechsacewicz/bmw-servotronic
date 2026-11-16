# E84 and E92 by the numbers

The README chart compares one calculated part of steering assistance. Higher means a larger value in that part of the calculation. It does not establish how much less effort the driver needs.

## Every plotted sample

| Speed | Steering-wheel input | E92 value | E84 value | Change from E92 |
| --- | --- | --- | --- | --- |
| 0 km/h | 1.00 Nm | 125 | 182 | +45.6% |
| 0 km/h | 1.47 Nm | 197 | 307 | +55.8% |
| 0 km/h | 2.00 Nm | 295 | 448 | +51.9% |
| 0 km/h | 3.04 Nm | 499 | 912 | +82.8% |
| 15 km/h | 1.00 Nm | 60 | 62 | +3.3% |
| 15 km/h | 1.47 Nm | 105 | 104 | -1.0% |
| 15 km/h | 2.00 Nm | 179 | 155 | -13.4% |
| 15 km/h | 3.04 Nm | 435 | 317 | -27.1% |

The values are internal controller counts. Nm measures the turning torque applied at the steering wheel. Each dot represents one of the four positive input samples at that speed. The pale segment spans their minimum and maximum; it is not a continuous test or a confidence interval.

## Calculation and source

The percentage is `(E84 / E92 - 1) * 100`, using the same input and speed for both settings. There is no averaging or selected representative input in the range chart.

These results come from A108, dated 1 November 2026. The original investigation ran 352 combinations across 22 profiles, two speeds, and eight signed inputs. The chart uses the 16 outputs for E92_basis and E84_basis at the four positive inputs, giving eight matched comparisons. Every plotted output was checked against both the retained original graph and its original execution matrix.

The examined functions calculate one contribution later added to requested EPS motor torque. Other composite correction terms and prior states were zero, with mode zero. The selector, full scheduler, final combination, and complete vehicle response were outside those executions. No physical steering-effort measurements or highway-speed calculations are supplied.

The original graph and execution matrix are not bundled. Their SHA-256 hashes and all published inputs are in [the comparison data](../data/e84-vs-e92.json). The reference firmware hash is also recorded there. Reference firmware is not an installed-memory readback.

## Rebuild the chart

The figure uses [render_comparison.py](../scripts/render_comparison.py) and the public JSON data. With Matplotlib installed in your own environment, run:

```sh
python3 scripts/render_comparison.py
```

Inter is used when available, with DejaVu Sans as a fallback. The output is [the README image](../assets/e84-vs-e92.png). Rebuilding the figure reproduces the percentages and layout; it does not rerun the original firmware executions.
