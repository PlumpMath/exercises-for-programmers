# 따옴표 출력
# 인용구와 사용자를 담는 자료구조 사용

SPEECH_EXAMPLE = {
    "speaker": "Obi-Wan Kenobi",
    "content": "These aren't the droids you're looking for",
}


def input_speech(container):
    quote = input("What is the quote? ")
    speaker = input("Who said it? ")
    speech = {
        "speaker": speaker,
        "content": quote,
    }
    container.append(speech)


def print_speeches(container):
    for speech in container:
        print(speech['speaker'] + " says, \"" + speech['content'] + ".\"")


speeches = []
input_speech(speeches)
print_speeches(speeches)
