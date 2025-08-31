# RoomPlanner MVP

RoomPlanner is a prototype application that allows users to upload photos of their rooms, browse furniture from multiple sources, visualize how items would fit, and place orders. This repository contains the code for the MVP version.

## Getting Started

The project is split into `backend` (FastAPI) and `frontend` (Streamlit). See `docs/mvp_action_plan.md` for the detailed plan and roadmap.

### Prerequisites

- Python 3.10+
- pip

### Installation

Clone the repository and install dependencies for both backend and frontend.

```
# backend
cd backend
pip install -r requirements.txt

# frontend
cd ../frontend
pip install -r requirements.txt
```

### Running the app

1. Start the backend API:

```
cd backend/app
uvicorn main:app --reload
```

2. Launch the Streamlit frontend:

```
cd ../frontend
streamlit run app.py
```

This will open the UI in your browser.

## License

MIT
