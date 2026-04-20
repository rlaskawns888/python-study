# FastAPI Summary API

FastAPI를 사용해 만든 텍스트 요약 API 프로젝트입니다.  
단순히 API를 하나 만드는 것에 그치지 않고, 요청 검증, 응답 모델, 예외 처리, 계층 분리(controller/service/schema), Swagger 문서화를 적용해 실무형 API 구조를 연습하는 것을 목표로 했습니다.

---

## 1. Project Overview

이 프로젝트는 사용자가 입력한 텍스트를 받아 요약 결과를 반환하는 API 서버입니다.

학습 및 구현 목표:
- FastAPI 기본 구조 이해
- POST API 및 Request Body 처리
- Pydantic BaseModel을 통한 검증
- response_model을 통한 응답 표준화
- 커스텀 예외 및 공통 예외 처리
- controller / service / schema 역할 분리
- Swagger 문서 자동화 경험

---

## 2. Main Features

- 텍스트 입력 기반 요약 API 제공
- 요청 데이터 검증
- 응답 구조 표준화
- 공통 에러 응답 처리
- Swagger UI 제공
- 역할별 폴더 구조 분리

---

## 3. Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

추후 확장 가능:
- httpx
- OpenAI API / 외부 LLM API
- Docker
- pytest

---

## 4. Project Structure

```bash
fastapi-summary-api/
├─ app/
│  ├─ main.py
│  ├─ controllers/
│  │  └─ summarize_controller.py
│  ├─ services/
│  │  └─ summarize_service.py
│  ├─ schemas/
│  │  └─ summarize_schema.py
│  ├─ exceptions/
│  │  ├─ custom_exceptions.py
│  │  └─ handlers.py
│  └─ core/
│     └─ config.py
├─ README.md
├─ requirements.txt
├─ .env.example
└─ .gitignore