# Academic Planner Agent

An agentic AI academic planner that generates personalized weekly study plans using LLM reasoning, task prioritization, and human approval workflows.

## Features

- Reads structured academic tasks from JSON
- Uses an LLM to generate realistic 7-day plans
- Prioritizes tasks based on urgency and workload
- Breaks large tasks into smaller steps
- Human approval step before saving plans
- Exports plans to markdown

## Tech Stack

- Python
- OpenRouter API
- LLM-based planning
- JSON task storage
- Git/GitHub

## Future Improvements

- Streamlit web interface
- Calendar integration
- File/syllabus parsing
- Research assistant mode
- Sandboxed tool execution inspired by NVIDIA OpenShell

## Run Locally

```bash
pip install -r requirements.txt
python main.py
```

## Example Input

```json
[
  {
    "title": "ML exam",
    "due_date": "2026-05-22",
    "priority": "high",
    "estimated_hours": 8
  }
]
```

## Inspiration

Inspired by NVIDIA’s “Build It Yourself Agentic AI” learning series and concepts from OpenClaw/OpenShell workflows.