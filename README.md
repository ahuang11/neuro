# [HoloViz+Bokeh for Neuroscience](https://github.com/holoviz-topics/neuro)

> :warning: This work is in early development and changing rapidly. It is not ready for scientific use. :warning:

### What is this repo?

Our ultimate goal is to facilitate the creation of fully open, reproducible, OS-independent, browser-based workflows for biomedical research. In support of this goal, this repository is the development ground for optimization and demonstration of HoloViz and Bokeh tools within the realm of neuroscience.

<details>
<summary> Urgent objectives: </summary>
  
- **Workflow Development:** Host the development of workflows.
- **Code Sharing:** Promote consistency and facilitate sharing of code across different workflows.
- **Collaboration:** Foster collaborative efforts between the HoloViz+Bokeh development teams and scientific collaborators outside these groups. This cross-collaboration aims to effectively tailor the tools to the specific requirements of the neuroscience community.
- **Issue Identification and Resolution:** As part of ongoing development, identify and address any performance or user interface bottlenecks in the workflows to optimize their usage and effectiveness.
- **Benchmarking and Testing Integration:** Host benchmarking work that involves the use of real and simulated data to assess the performance and functionality of the tools under relevant conditions.

</details> 

<details>
<summary> Slightly less urgent objectives: </summary>

- **Improvement and Refinement:** Over time, enhance, improve, and refine the developed workflows based on user feedback and advancements in the field.
- **Dissemination:** Eventually, share workflows with the broader scientific community. It's unclear yet where these all will be showcased, but at least some will go to examples.holoviz.org.
- **Education and Community Building:** Undertake educational and community-building activities such as providing tutorials, workshops, other educational resources to help researchers effectively utilize the developed tools.
- **Host Domain-Specific Package:** It is possible that not all required code for workflows will be accepted or appropriate for integrations into domain-independent HoloViz/Bokeh packages. Therefore, this repo *might* end up hosting code to be packaged as a domain-specific extension. TBD!

</details>

<details>
<summary> Roadmap: </summary>

- High-level summary: Our current grant period is through 2024, but we want to have a
  first pass of prioritized improvements for generalized workflows to disseminate for
  feedback **within** Q4 2023. The remainder of Q4 2023 and all of 2024 will be for
  iterating on feedback, developing the specialized workflows, demonstrating biomedical
  use-cases, collaborating lab support, educational activities, and as time permits -
  wishlist features and new collaborations.
- A living task-goal roadmap is visible on [this project board
  view](https://github.com/orgs/holoviz-topics/projects/1/views/3) - currently through Q3
  and early Q4 2023.

</details>
  
### What are workflows?

This repository contains developmental versions of workflows, which can be categorized into two types: **generalized** and **specialized**. Generalized workflows aim to be broadly applicable and primarily utilize domain-independent tools such as Numpy, Pandas, Xarray, and others. These generalized workflows serve as the foundational building blocks for specialized workflows. On the other hand, specialized workflows are designed to cater to specific contexts and have no limitations on the use of domain-specific tools like MNE, Minian, and more.

**Generalized Workflows**:

| Title | Modality | Thumbnail | Info & Links | Description |
| --- | --- | --- | --- | --- |
| EEG Viewer | <span style="color:#9cd4af"><a href="https://github.com/holoviz-topics/neuro/wiki/EEG-notes">eeg</a></span> | <a href="./workflows/eeg-viewer/assets/230524_eeg-viewer.png"><img src="./workflows/eeg-viewer/assets/230524_eeg-viewer.png" alt="EEG Viewer" width="100"></a> | ![Status](https://img.shields.io/badge/status-in%20progress-orange) <br> [readme](./workflows/eeg-viewer/readme_eeg-viewer.md) <br> [workflow](./workflows/eeg-viewer/workflow_eeg-viewer.ipynb) | Synchronized examination of EEG  with stacked time-series, large data handling, scale bar, annotations, minimap , and signal grouping.
| Video Viewer | <span style="color:#ffb3ba"><a href="https://github.com/holoviz-topics/neuro/wiki/Calcium-Imaging-notes">calcium imaging</a></span> | <a href="./workflows/video-viewer/assets/230526_video-viewer.png"><img src="./workflows/video-viewer/assets/230526_video-viewer.png" alt="Video Viewer" width="100"></a> | ![Status](https://img.shields.io/badge/status-in%20progress-orange) <br> [readme](./workflows/video-viewer/readme_video-viewer.md) <br> [workflow](./workflows/video-viewer/workflow_video-viewer.ipynb) | Efficient visualization of large Miniscope calcium imaging movies with, playback controls, 2D annotation, scale bar, intensity histogram, and summary statistics. |
| Ephys Viewer | <span style="color:#a4d7e1"><a href="https://github.com/holoviz-topics/neuro/wiki/Electrophysiology-notes">ephys</a></span> | <a href="./workflows/ephys-viewer/assets/230524_ephys-viewer.png"><img src="./workflows/ephys-viewer/assets/230524_ephys-viewer.png" alt="Ephys Viewer" width="100"></a> | ![Status](https://img.shields.io/badge/status-in%20progress-orange) <br> [readme](./workflows/ephys-viewer/readme_ephys-viewer.md) <br> [workflow](./workflows/ephys-viewer/workflow_ephys-viewer.ipynb) | |
| Waveform | <span style="color:#a4d7e1"><a href="https://github.com/holoviz-topics/neuro/wiki/Electrophysiology-notes">ephys</a></span> | <a href="./workflows/waveform/assets/230524_waveform.png"><img src="./workflows/waveform/assets/230524_waveform.png" alt="Waveform" width="100"></a> | ![Status](https://img.shields.io/badge/status-in%20progress-orange) <br> [readme](./workflows/waveform/readme_waveform.md) <br> [workflow](./workflows/waveform/workflow_waveform.ipynb) | |
| Spike Raster | <span style="color:#a4d7e1"><a href="https://github.com/holoviz-topics/neuro/wiki/Electrophysiology-notes">ephys</a></span> | <a href="./workflows/spike-raster/assets/230524_spike-raster.png"><img src="./workflows/spike-raster/assets/230524_spike-raster.png" alt="Spike Raster" width="100"></a> | ![Status](https://img.shields.io/badge/status-in%20progress-orange) <br> [readme](./spike-raster/readme_spike-raster.md) <br> [workflow](./spike-raster/workflow_spike-raster.ipynb) | |

- Linked eeg-sensor layout [![status: todo](https://img.shields.io/badge/status-todo-purple)]
- Linked ephys-sensor layout [![status: todo](https://img.shields.io/badge/status-todo-purple)]
- Streaming data [![status: todo](https://img.shields.io/badge/status-todo-purple)]

**Specialized Workflows**:

- Spike Motif [![status: todo](https://img.shields.io/badge/status-todo-purple)]
- MNE Raw [![status: todo](https://img.shields.io/badge/status-todo-purple)]
- Minian CNMF [![status: todo](https://img.shields.io/badge/status-todo-purple)]

---
## Contributing

- **Task Management:** As workflows are developed and honed, performance and UI bottlenecks will be identified and addressed. Some improvements for the workflows themselves will be within this repo, but many improvements will be in the appropriate underlying libraries within the [HoloViz](https://github.com/holoviz/), [Bokeh](https://github.com/bokeh), or other GitHub Organizations. We will do our best to track the disparate tasks related to these efforts into this 
[project board](https://github.com/orgs/holoviz-topics/projects/1).
  - Abstracted project board tasks prefixed with 'GOAL:' are for roadmap generation and hours estimation.
- **Meeting minutes:** Logged in the [Wiki](https://github.com/holoviz-topics/neuro/wiki) whenever possible.
- **Specifications:** The [Wiki](https://github.com/holoviz-topics/neuro/wiki) has some data specifications and modality notes (in progress).
- **Data Generation:** To assist the development using real data, some workflows utilize simple data generators to help benchmark across data and parameter space. As the data generators/simulators can be useful to multiple workflows, they are kept as a separate and importable module ([`/src/neurodatagen`](./src/neurodatagen)).
- **Visualization source code:** If there is visualization code or utilities that we want to live separate from the individual workflows, we can store them in [`/src/hvneuro`](./src/hvneuro) for now. However, it's unclear whether this will be released as a new package, incorporated into existing libraries, or live in particular workflows. TBD 
- **Repo Structure and dev patterns:** 
    ```
    /workflows
      /example1
        readme_example1.md
        workflow_example1.ipynb
        environment.yml
        /dev
            date_example-workflow_task.ipynb
    ```
  - Use `readme_<workflow>.md` for any essential workflow-specific info or links.
  - Maintain `workflow_<workflow>.ipynb` as the latest version of the workflow.
  - Each workflow should have an `environment.yml` with which to create a conda env that will install the `neurodatagen` module in dev mode.
  - Use the `dev` dir in each workflow as shared scratch space within the `main` branch. There is no expectation that anything here is maintained.

---
## Who is behind this?

This work is a collaboration between developers and scientists, and some developer-scientists. While some contributions are visible through the GitHub repo, many other contributions are less visible yet equally important.

Funding:
- 2023 - 2024: Chan Zuckerberg Initiative. Learn more in the [grant announcement](https://blog.bokeh.org/announcing-czi-funding-for-bokeh-for-bioscience-5f74426c011a).

---

## Why Neuroscience?

Multiple (probably all) HoloViz+Bokeh developers believe that helping people through the furthering of clinically impactful science is a worthy pursuit and in need of a data visualization boost.

## Why HoloViz+Bokeh?

We hypothesize that the visualization within the process of working always benefits from having the option to suddenly become interactive and shareable - allowing for the poking or plucking, pushing or pulling, drilling in or out, grouping or separating, and sending or receiving of what would otherwise be a static snapshot of the data. The combined use of HoloViz and Bokeh tools provides the interactivity and shareability needed to support research as a collective action rather than a collection of solitary observations.
