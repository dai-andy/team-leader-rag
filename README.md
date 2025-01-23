# Team Leader AI Assistant

An AI-powered technical leadership assistant that provides guidance based on your organization's documented practices and policies. Built with RAG (Retrieval Augmented Generation) to ensure responses align with your specific team standards and requirements.

## Features

- Context-aware responses grounded in your team's documentation
- Persistent vector storage for efficient knowledge retrieval
- Streamlit-based chat interface
- Strict adherence to team policies and technical standards
- Comprehensive knowledge base integration

## Technical Stack

- **LangChain**: Framework for RAG implementation
- **OpenAI**: Powers embeddings and chat completion
- **ChromaDB**: Vector store with persistent storage into chroma_db
- **Streamlit**: Interactive web interface
- **Python 3.x**: Core programming language

## Prerequisites

- OpenAI API key
- Python 3.x

## Installation

1. Clone the repository: 

```bash
git clone https://github.com/yourusername/team-leader-rag.git
cd team-leader-rag
```

2. Create and activate a virtual environment:

```bash
conda create --n team-leader-rag
conda activate team-leader-rag
```

3. Install dependencies: 

```bash
pip install -r requirements.txt
```

4. Set up environment variables: 

```bash
# Unix/macOS
export OPENAI_API_KEY='your-api-key'

# Windows
set OPENAI_API_KEY=your-api-key

# Powershell
$env:OPENAI_API_KEY='your-api-key'
```

## Knowledge Base Setup

Place your documentation in the `knowledge_base/` directory as .txt files:

- `team_management.txt`: Team structure and management policies
- `technical_architecture.txt`: System architecture and technical requirements
- `incident_responses.txt`: Incident handling procedures
- `onboarding_guide.txt`: Developer onboarding protocols

## Running the Application

1. Ensure knowledge base files are in place:

```bash
ls knowledge_base/*.txt
```

2. Start the Streamlit interface:

```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

## Architecture

- **RAG Pipeline**: Uses 1000-token chunks with 200-token overlap
- **Vector Store**: ChromaDB with persistent storage in `chroma_db/`
- **LLM**: GPT-3.5-turbo-0125 with temperature 0.65
- **Embeddings**: OpenAI embeddings for document vectorization

# Example Q&A

### Q: What's our policy on test coverage?

Our policy on test coverage is to maintain a minimum of 99.99% test coverage for all codebases. This high level of test coverage ensures that our code is well-tested and helps prevent regressions when making changes. It also promotes code quality and stability across our projects.

Having a robust test suite is essential for catching bugs early in the development process and providing confidence when making changes to the codebase. It's a best practice in software development to have thorough test coverage, and it aligns with our commitment to delivering high-quality software products.

I recommend using tools like code coverage reports to track and monitor test coverage regularly. This helps identify areas of the code that may need additional testing and ensures that new code contributions meet the required standards before merging. Additionally, conducting regular code reviews focused on test coverage can help reinforce the importance of this policy within the team.

---

### Q: What's Andy's favorite food?

I'm here to provide guidance on technical topics related to team leadership, software development, and project management. If you have any questions in those areas, feel free to ask!

---

### Q: I have a use case where I need high observability for an LLM, what should I use?

For high observability in an LLM (Logging, Monitoring, and Metrics) use case, you should leverage Arize's Phoenix, as it is the mandated tool for LLM operations and observability in the current architecture. Arize's Phoenix provides comprehensive monitoring and observability capabilities specifically designed for machine learning models, enabling you to track model performance, data drift, and other key metrics in real-time.

By utilizing Arize's Phoenix, you can gain insights into model behavior, performance, and the impact of changes, which is crucial for maintaining the reliability and effectiveness of your machine learning models. Additionally, integrating Arize's Phoenix with OpenTelemetry will further enhance observability by capturing detailed telemetry data and providing a holistic view of your system's performance.

Therefore, for your LLM use case, I recommend utilizing Arize's Phoenix in conjunction with OpenTelemetry to achieve the high level of observability required for monitoring and optimizing your machine learning models effectively.

---

### Q: What are our team's promotion requirements?

Our team's promotion requirements include:

Maintaining a minimum of 99.99% test coverage to ensure high code quality and reliability.
Writing and publishing at least 5 technical blog posts per year to demonstrate knowledge sharing and thought leadership within the industry.
Responding to production issues within a maximum of 2 hours to ensure timely resolution and minimal impact on users.
Adhering to coding standards with zero tolerance for repeated violations to maintain code consistency and readability.
Making mandatory contributions to internal libraries to foster code reuse and collaboration within the team.
Meeting these promotion requirements showcases a commitment to excellence in software development and continuous improvement, which are essential for career growth within the team.