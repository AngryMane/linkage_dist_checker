#!/usr/bin/env python3
import argparse
from typing import List, Any
from conllu import parse
from conllu.models import Token
from diaparser.utils import Dataset
from diaparser.parsers import Parser


def main(target_sentence: str, language: str) -> None:
    if not target_sentence:
        return

    model_name: str = 'ja_gsd.mbert' if language == 'ja' else 'en_ewt-electra'
    parser: Parser = Parser.load(model_name)
    dataset: Dataset = parser.predict(target_sentence, text=language)
    sentences: List[Any] = parse(str(dataset.sentences[0]))
    sentence: List[Token] = sentences[0]

    id_token_map: Map[int, Token] = {}
    for token in sentence:
        token: Token
        cur_token_id: int = int(token['id'])
        id_token_map[cur_token_id] = token

    total_distance: int = 0
    for token in sentence:
        token: Token
        cur_token_id: int = int(token['id'])
        head_token_id: int = int(token['head'])
        distance: int = 0 if head_token_id == 0 else abs(
            cur_token_id - head_token_id)
        token.distance: int = distance
        total_distance += token.distance

    print(f'total_distance is {total_distance}.')
    sorted_sentence = sorted(sentence, key=lambda x: x.distance, reverse=True)
    for token in sorted_sentence:
        token: Token
        cur_token_str: str = token["form"]
        head_token_id: int = int(token['head'])
        head_token_str: str = 'root' if head_token_id == 0 else id_token_map[
            head_token_id]["form"]
        print(
            f'"{cur_token_str}" linked to "{head_token_str}". distance is {token.distance}.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        'sentence', help='input target sentence', type=str, default='')
    parser.add_argument('-l', help='selecet sentence language("ja" or "en").',
                        type=str, choices=['ja', 'en'], default='ja')
    args = parser.parse_args()
    main(args.sentence, args.l)
