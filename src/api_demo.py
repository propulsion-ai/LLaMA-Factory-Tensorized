import uvicorn

from llmtuner import ChatModel, create_app


def main():
    chat_model = ChatModel()
    app = create_app(chat_model)
    uvicorn.run(app, host="127.0.0.1", port=8080, workers=1)
    print("Visit http://localhost:8080/docs for API documentation.")


if __name__ == "__main__":
    main()
