from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING

from bokeh.models import Button, ColumnDataSource
from bokeh.plotting import column, figure, row
import numpy as np

from .base import Base

if TYPE_CHECKING:
    from bokeh.document import Document


def bkapp(doc: Document, n: int, output_backend: str):
    cds = ColumnDataSource(data=dict(x=[], y=[]))

    p = figure(width=600, height=400, output_backend=output_backend)
    p.line(source=cds, x="x", y="y")

# Prepare data but do not send it to browser yet.
    x = np.arange(n)
    y = np.random.default_rng(8343).uniform(size=n)

    # Set initial range to 1/10th of the data's total x and y range.
    x_start = x[0]
    x_end = x_start + (x[-1] - x_start) / 10
    y_start = min(y)
    y_end = y_start + (max(y) - y_start) / 10

    # Update the figure's x and y range.
    p.x_range.start = x_start
    p.x_range.end = x_end
    p.y_range.start = y_start
    p.y_range.end = y_end

    def run_callback(event):
        # Latency benchmark times the sending and rendering of this data.
        cds.data = dict(x=x, y=y)

    run_button = Button(label="run")
    run_button.on_click(run_callback)

    def zoom_callback(event):
        # Zoom benchmark times the render caused by this zoom.
        p.x_range.start = x[0]
        p.x_range.end = x[-1]
        p.y_range.start = min(y)
        p.y_range.end = max(y)

    zoom_button = Button(label="zoom")
    zoom_button.on_click(zoom_callback)

    doc.add_root(column(p, row(run_button, zoom_button)))


class BokehExampleBase(Base):
    params: tuple[list[int], list[str]] = (
        [1_000, 10_000, 100_000, 1_000_000],
        ["canvas", "webgl"],
    )
    param_names: tuple[str] = ("n", "output_backend")

    def setup(self, n: int, output_backend: str) -> None:
        bkapp_n = partial(bkapp, n=n, output_backend=output_backend)
        self.playwright_setup(bkapp_n)

        # There is only a single Bokeh figure in each benchmark so store its ID here rather than
        # in the benchmark itself.
        self.figure_id = self.current_figure_id()

    def teardown(self, n: int, output_backend: str) -> None:
        self.figure_id = None
        self.playwright_teardown()


class BokehExampleLatency(BokehExampleBase):
    """Example benchmark using Bokeh only, measuring the latency which is the
    time taken to transfer data to the browser and render it. The browser and
    Bokeh server are already running before the benchmark starts.
    """
    def time_latency(self, n: int, output_backend: str) -> None:
        self.click_button_and_wait_for_render("run", self.figure_id)


class BokehExampleZoom(BokehExampleBase):
    """Example benchmark using Bokeh only, measuring the time taken for an
    interactive render which is achieved here using by zooming the figure.
    """
    def setup(self, n: int, output_backend: str) -> None:
        super().setup(n, output_backend)

        # Render initial data set.
        self.click_button_and_wait_for_render("run", self.figure_id)

    def time_zoom(self, n: int, output_backend: str) -> None:
        self.click_button_and_wait_for_render("zoom", self.figure_id)
