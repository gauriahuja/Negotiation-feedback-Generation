Negotiation-Feedback-Generator

This project simulates an AI-powered feedback engine that analyzes negotiation dialogues and generates categorized coaching feedback for skill improvement.

Built using the UF AI API (LLaMA 3.3 70B model), it processes real negotiation transcripts and provides structured feedback in three areas:
- Assessment-Oriented
- Process-Based
- Interaction & Communication

Features

Feedback Categories
Each dialogue receives:
Assessment-Oriented Feedback
Highlights strengths and gaps in decision-making and understanding.

Process-Based Feedback 
Evaluates sequencing, efficiency, pacing, and strategic clarity.

Interaction & Communication Feedback
Covers clarity, responsiveness, empathy, and tone.

Batch Processing
Reads 35 dialogues per run from `train.txt`
Generates clean, professional output in `.csv` and `.xlsx` format

Technologies Used
Python 3.10+
UF AI API (LLaMA 3.3)
`pandas`, `requests`, `python-dotenv`
Clean CSV + Excel feedback generation

Project Structure
.
├── generate.py                  # Main batch processor
├── generate_feedback.py        # Prompt logic & API integration
├── train.txt                   # Dataset with <dialogue> and <eos> markers
├── .env.example                # Template for secure API setup
├── final_api_feedback_output.csv  
├── final_api_feedback_output.xlsx  
└── README.md                   # This file

Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Negotiation-Feedback-Generator.git
cd Negotiation-Feedback-Generator
```

2. Install dependencies:
```bash
pip install pandas requests python-dotenv
```

3. Create a `.env` file and add your API key:
```
UF_AI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
How to Use

Option 1: Batch Feedback Generation

```bash
python generate.py
```

- Reads 35 dialogues at a time
- Generates 3 types of feedback per dialogue
- Outputs to: `final_api_feedback_output.csv` and `.xlsx`

Dialogue Format (`train.txt`)

```xml
<dialogue>
them: I want 4 hats <eos> you: Deal <eos>
</dialogue>

Example Output (Excel Row)

| Dialogue ID | Dialogue Text | Assessment Feedback | Process Feedback | Interaction Feedback |
|-------------|----------------|---------------------|------------------|-----------------------|
| Dialogue 1  | them: ... you: ... | Identified acceptance and lack of questioning | Reactive strategy, no clarification | Missing follow-up to ensure shared understanding |

 Notes

- The script automatically resumes from where it left off
- Output is cleaned of markdown and formatted for professional reporting
- `.env` file is excluded via `.gitignore`

 License

This project is intended for academic and research purposes at the University of Florida.


Author

Gauri Ahuja
M.S. in Computer Science, University of Florida  
[Mail](mailto:ahujagauri@ufl.edu)  
[LinkedIn](https://linkedin.com/in/gauri777)

Acknowledgements

- Built as part of research in AI-driven feedback systems under Professor [Your Professor's Name]
- Uses LLaMA-based AI for real-time negotiation insights

