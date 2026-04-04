from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


BG = "#efefef"
SHAPE = "#d8d8d8"
EDGE = "#666666"
TEXT = "#3f5a74"
CURRENT = "#3f5a74"
VOLTAGE = "#3f5a74"


def _depth_vector(depth: float) -> tuple[float, float]:
    return 0.55 * depth, 0.22 * depth


def draw_run(ax, x0: float, x1: float, y: float, depth: float) -> None:
    dx, dy = _depth_vector(depth)
    pts = [(x0, y), (x1, y), (x1 + dx, y + dy), (x0 + dx, y + dy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=SHAPE, edgecolor=EDGE, linewidth=1.0, zorder=3))


def draw_drop(ax, x: float, y_top: float, y_bottom: float, depth: float) -> None:
    dx, dy = _depth_vector(depth)
    pts = [(x, y_top), (x + dx, y_top + dy), (x + dx, y_bottom + dy), (x, y_bottom)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=SHAPE, edgecolor=EDGE, linewidth=1.0, zorder=4))


def shear_points(points: list[tuple[float, float]], shear: float, origin_y: float) -> list[tuple[float, float]]:
    return [(x + shear * (y - origin_y), y) for x, y in points]


def draw_sheared_polygon(
    ax,
    points: list[tuple[float, float]],
    shear: float,
    origin_y: float,
    **patch_kwargs,
) -> None:
    ax.add_patch(Polygon(shear_points(points, shear, origin_y), closed=True, **patch_kwargs))


def draw_series_plot(output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=180)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    levels = [8.0, 6.7, 3.9]
    x_edges = [0.6, 3.8, 7.0, 10.2]
    depth = 1.0

    draw_run(ax, x_edges[0], x_edges[1], levels[0], depth)
    draw_drop(ax, x_edges[1], levels[0], levels[1], depth)
    draw_run(ax, x_edges[1], x_edges[2], levels[1], depth)
    draw_drop(ax, x_edges[2], levels[1], levels[2], depth)
    draw_run(ax, x_edges[2], x_edges[3], levels[2], depth)

    ax.annotate(
        "",
        xy=(1.35, 8.2775),  # slope: 0.17/.4 = 0.425
        xytext=(1.85, 8.49),
        arrowprops=dict(arrowstyle="<|-|>", linewidth=0.9, color=CURRENT),
    )
    ax.text(2.0, 8.4, "1 A", fontsize=14, color=CURRENT, ha="left", va="center")

    ax.annotate(
        "",
        xy=(5.0, levels[0] + 0.2),
        xytext=(5.0, levels[1] + 0.2),
        arrowprops=dict(arrowstyle="<|-|>", linewidth=0.9, color=VOLTAGE),
    )
    ax.text(5.35, (levels[0] + levels[1] + 0.5) / 2, "1V", fontsize=16, color=VOLTAGE, va="center")

    ax.annotate(
        "",
        xy=(9.0, levels[1] + 0.2),
        xytext=(9.0, levels[2] + 0.2),
        arrowprops=dict(arrowstyle="<|-|>", linewidth=0.9, color=VOLTAGE),
    )
    ax.text(9.35, (levels[1] + levels[2] + 0.5) / 2, "3V", fontsize=16, color=VOLTAGE, va="center")

    ax.set_xlim(0.4, 11.2)
    ax.set_ylim(3.1, 9.0)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def draw_parallel_plot(output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=180)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    shear = 0.34
    origin_y = 3.0

    left_x0, left_x1 = 0.9, 4.0
    junction_x0, junction_x1 = 4.0, 4.28
    branch_x1 = 8.95
    end_bar_x0 = 8.95
    end_bar_x1 = 9.18

    # Main current block and junction
    draw_sheared_polygon(
        ax,
        [(left_x0, 3.0), (left_x1, 3.0), (left_x1, 7.2), (left_x0, 7.2)],
        shear,
        origin_y,
        facecolor="#efc1e6",
        edgecolor="#e077c2",
        linewidth=1.0,
        zorder=2,
    )
    draw_sheared_polygon(
        ax,
        [(junction_x0, 3.0), (junction_x1, 3.0), (junction_x1, 7.2), (junction_x0, 7.2)],
        shear,
        origin_y,
        facecolor="#8e8e8e",
        edgecolor="#7a7a7a",
        linewidth=1.0,
        zorder=3,
    )

    bands = [
        ("A", "1,000", 5.95, 7.2, "#dde08d", "#c2c11f"),
        ("B", "500", 4.45, 5.45, "#8fe0ea", "#16b8c8"),
        ("C", "500", 2.95, 4.05, "#9bc0df", "#2b78be"),
    ]

    for label, value, y0, y1, fill, edge in bands:
        draw_sheared_polygon(
            ax,
            [(junction_x1, y0), (branch_x1, y0), (branch_x1, y1), (junction_x1, y1)],
            shear,
            origin_y,
            facecolor=fill,
            edgecolor=fill,
            linewidth=0.8,
            zorder=1,
        )
        draw_sheared_polygon(
            ax,
            [(end_bar_x0, y0), (end_bar_x1, y0), (end_bar_x1, y1), (end_bar_x0, y1)],
            shear,
            origin_y,
            facecolor=edge,
            edgecolor=edge,
            linewidth=0.8,
            zorder=4,
        )

        ax.text(9.28, (y0 + y1) / 2 + 0.05, label, fontsize=12, color="#222", va="center", ha="left")
        ax.text(9.28, (y0 + y1) / 2 - 0.23, value, fontsize=12, color="#222", va="center", ha="left")

    ax.text(0.45, 8.15, "PARALLEL", fontsize=19, color=TEXT, weight="bold")
    ax.text(0.45, 7.68, "A sheared Sankey-style split: same drop, different branch widths", fontsize=11, color=EDGE)
    ax.text(0.25, 5.25, "Current\n2,000", fontsize=11, color="#222", ha="center", va="center")
    ax.text(4.0, 5.2, "Junction\n2,000", fontsize=11, color="#222", ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#ffffffcc", edgecolor="none"))

    ax.text(0.6, 2.18, "Total current splits: I = I1 + I2 + I3", fontsize=10, color=CURRENT)
    ax.text(0.6, 1.86, "Equal voltage drop across each branch", fontsize=10, color=VOLTAGE)

    ax.set_xlim(0.2, 10.1)
    ax.set_ylim(1.5, 8.7)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    assets_dir = project_root / "src" / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    draw_series_plot(assets_dir / "resistor_series.png")
    draw_parallel_plot(assets_dir / "resistor_parallel.png")

    print(f"Generated plots in {assets_dir}")


if __name__ == "__main__":
    main()
