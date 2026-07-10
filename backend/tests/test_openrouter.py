from app.llm.factory import LLMFactory


def main():
    llm = LLMFactory.create()

    response = llm.generate(
        prompt="Reply with only the word SUCCESS."
    )

    print(response)


if __name__ == "__main__":
    main()